# Python Technical Interview Questions

High-frequency Python language questions asked alongside (or instead of) DSA rounds.
Each entry: **Q** → **A** in interview-ready phrasing. ★ = asked at ≥50% of Python
interviews; ★★ = near-certain.

**Protocol:** 1–2 questions from this file open every DSA session (warm-up drill).
Missed questions get logged in `DSA/COACHING.md → Python Drill Log` and re-asked
until answered cold. If a solution review catches a Python-semantics bug, its
matching question enters the rotation immediately.

---

## 1. Semantics and Objects

### Q1.1 ★★ `is` vs `==` — what's the difference, and when is `is` correct?
`==` compares **values** (calls `__eq__`); `is` compares **identity** (same object
in memory, `id()` equality). Use `is` only for singletons: `x is None`, `x is True`,
sentinel objects. Never for ints/strings — CPython caches small ints (−5..256) and
interns some strings, so `a is b` can be True or False for equal values depending on
history. `1000 is 1000` may be False at the REPL.

### Q1.2 ★★ Mutable default argument — what does this do and why?
```python
def append_to(item, target=[]):
    target.append(item)
    return target
```
The default is evaluated **once at function definition**, not per call. All calls
without an explicit `target` share one list: `append_to(1)` → `[1]`,
`append_to(2)` → `[1, 2]`. Fix: default `None`, then `target = target if target is not None else []`
inside the body.

### Q1.3 ★ Are integers immutable? What does that cost, and what follows from it?
Yes — `x += 1` rebinds `x` to a **new** int object; it never mutates the old one.
Consequences: shared references can't be changed under you (`is`-safe reasoning),
big-int arithmetic is O(bits) not O(1) word ops, and building a string by repeated
`+=` over characters is O(n²) — each `+=` copies. Use `''.join(parts)`.

### Q1.4 ★ What is truthiness? Which values are falsy?
`if x` calls `bool(x)`: `__bool__`, else `__len__` (0 → False), else True.
Falsy: `False`, `None`, `0` (all numeric types), `''`, `[]`, `{}`, `set()`, `()` —
i.e., empty containers and zero. Everything else is truthy — including `0.1`, `"0"`,
`[None]`. Prefer `if items:` over `if len(items) > 0:`; it's O(1) on generators-safe.

### Q1.5 ★ Shallow vs deep copy?
`copy.copy` / `list(b)` / `b[:]` copy the top container only — nested objects are
**shared references**. `copy.deepcopy` recurses into everything. In DSA:
`grid = [[0]*m]*n` is a classic bug — one row object aliased n times; mutating
`grid[0][0]` changes every row. Correct: `[[0]*m for _ in range(n)]`.

---

## 2. Built-in Types and Their Costs

*(Directly load-bearing for every complexity claim you make in a DSA round.)*

### Q2.1 ★★ What are `list` and `dict` implemented as, and what does each core operation cost?
`list` = dynamic array of pointers: index O(1), `append` amortized O(1) (geometric
over-allocation ~12.5% + realloc), `insert(0, x)` / `pop(0)` O(n) (memmove).
`dict` = open-addressed hash table: average O(1) get/set, worst-case O(n); ordered by
insertion since 3.7 (guaranteed by the language spec, not just CPython).
`set` = hash table of keys, same costs.

### Q2.2 ★★ Why is `x in some_list` dangerous in an interview, and what do you use instead?
`in` on a list is O(n) linear scan. On a `set`/`dict` it's average O(1) hash lookup.
In the 3Sum-adjacent problems this is the difference between O(n²) and O(n³).
Related trap already burned in review (RPN, Sept 7): `token not in "+-/*"` is a
**substring** check on a string — O(k) scan, and semantically wrong for multi-char
tokens. Use a `set`/`frozenset`: membership, O(1), correct semantics.

### Q2.3 ★ Why can't you use a float / list / dict as a dict key? What CAN be a key?
Keys must be **hashable**: immutable with a stable `__hash__` for the object's
lifetime (equal objects must hash equal). Lists/dicts/sets are mutable → unhashable.
Allowed: int, float, str, tuple (only if all elements hashable — `(1, [2])` fails),
`frozenset`, any frozen dataclass. Custom classes are hashable by identity unless
you define `__eq__` without `__hash__` (then Python sets `__hash__ = None`).

### Q2.4 ★ When do you reach for each of: `deque`, `heapq`, `Counter`, `defaultdict`, `bisect`?
- `deque` — O(1) `append` **and** `appendleft`/`popleft` (list pop(0) is O(n)): BFS queues, sliding-window deques (Monotonic Queue).
- `heapq` — min-heap over a plain list; `heappush`/`heappop` O(log n); negate for max-heap. Top-K, Dijkstra.
- `Counter` — dict subclass; `counts[c]` returns 0 for missing keys; `most_common(k)`.
- `defaultdict(list)` — auto-creates missing keys; group-anagrams pattern without `if k not in d` noise.
- `bisect` — binary search in sorted lists: `bisect_left` insertion point; `insort` keeps order (insert is still O(n) memmove — heap or balanced structure if hot).

### Q2.5 Why is `str` immutable, and how does Python still make `''.join` fast?
Immutability lets strings be hashable dict keys, cached/interned, and safely shared
between references. `join` pre-scans the parts to compute total length and fills one
pre-allocated buffer in a single pass — O(n) total. Repeated `s += ch` allocates a
new string per step → O(n²).

---

## 3. Functions, Scope, Closures

### Q3.1 ★★ Explain LEGB and `global` vs `nonlocal`.
Name lookup order: **L**ocal (function) → **E**nclosing (function, for nested defs) →
**G**lobal (module) → **B**uiltins. Assignment inside a function makes the name local
for the whole function (hence `UnboundLocalError` on read-then-assign). `global`
binds to module scope; `nonlocal` binds to the nearest enclosing **function** scope —
required to mutate a closure variable (e.g., counter in a decorator).

### Q3.2 ★★ The closure-in-a-loop trap. What prints?
```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
```
`[2, 2, 2]`. Lambdas capture the **variable** `i`, not its value; by call time the
loop finished and `i == 2`. Fix: bind at definition — `lambda i=i: i` (default-arg
trick) or `functools.partial`. This bites in generated tool callbacks and async task
lists, not just interviews.

### Q3.3 ★ Write a decorator from memory. What's `functools.wraps` for?
```python
import functools, time

def timed(fn):
    @functools.wraps(fn)          # copies __name__, __doc__, __module__
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            print(f"{fn.__name__} {time.perf_counter() - t0:.4f}s")
    return wrapper
```
Without `@wraps`, the decorated function's metadata is `wrapper`'s — breaks
`help()`, doctests, pickling, and any introspection. With arguments
(`@retry(times=3)`) add one more layer: `def retry(times): def deco(fn): ... return deco`.

### Q3.4 What are `*args` and `**kwargs`? Where does `/` and `*` go in a signature?
`*args` collects extra positionals into a tuple; `**kwargs` collects keyword args
into a dict (last). In a definition: parameters before `*args`, keyword-only params
after `*` (`def f(a, *, b)` — `b` must be passed by name), and `/` forces
positional-only before it (`def f(a, /, b)`). Order: positional-only `/`, normal,
`*args`/keyword-only, `**kwargs`.

### Q3.5 How does Python evaluate default arguments, and in what order?
Defaults are evaluated left-to-right **at def time** (once), which is the mechanism
behind Q1.2. Annotations are evaluated at def time too (without
`from __future__ import annotations`). Argument *expressions* at **call** time are
evaluated left-to-right before the function body runs.

---

## 4. Iterators and Generators

### Q4.1 ★★ Difference between iterable and iterator? The protocol?
**Iterable**: has `__iter__()` returning an iterator (list, str, dict, file).
**Iterator**: has both `__iter__()` (returns self) and `__next__()` raising
`StopIteration` when exhausted. Iterators are consumed once; iterables can be looped
repeatedly. `for x in ys` is sugar for: `it = iter(ys)` → loop `next(it)` → catch
`StopIteration`. Gotcha: zip/filter/map results are iterators — single-pass; a list
comprehension is eagerly evaluated and re-usable.

### Q4.2 ★★ What does `yield` do? Why would you use a generator in an interview?
A function containing `yield` returns a **generator** — code runs lazily, suspending
at each `yield` with full local state, resuming on `next()`. Memory: O(1) vs O(n) —
stream a 10GB file line-by-line instead of `readlines()`. Interview use: permutations/
subsets when the caller only needs early termination or streaming; all-pairs without
nested lists; `yield from` to delegate to a sub-generator (flattening recursion).
Tradeoff to name: generators are single-pass and have no `len()`.

### Q4.3 Which of these are generators, and what prints?
```python
x = [i for i in range(3)]
y = (i for i in range(3))
z = map(int, "123")
```
`x` is a list (materialized). `y` is a generator — lazy, one pass. `z` is a map
object — **lazy iterator** in Python 3 (eager in Python 2, common stale-answer tell).
`list(y)` twice: second returns `[]`.

### Q4.4 Name itertools primitives you'd use to replace hand-written loops.
`pairwise` (sliding window of 2), `accumulate` (prefix sums / running max),
`combinations` / `permutations` / `product`, `chain.from_iterable` (flatten one
level), `groupby` (needs sorted input), `islice` (slice an iterator), `cycle`.
Saying "I'd use `itertools.accumulate` for prefix sums" is a fluency signal.

---

## 5. Classes and Dunder

### Q5.1 ★ `@classmethod` vs `@staticmethod` vs plain method?
Instance method: receives `self`; full object access. `@classmethod`: receives `cls`
— used for **alternative constructors** (`Date.fromisoformat`) and subclass-safe
factories. `@staticmethod`: no implicit receiver — namespaced utility with no
access to class or instance; reach for a module-level function instead unless the
grouping genuinely helps. Order of preference in interviews: plain, classmethod
factory, staticmethod last.

### Q5.2 ★ Which dunder methods make a class usable in a dict/set, printable, comparable, iterable?
`__repr__` (debug-facing; `__str__` falls back to it, not vice versa), `__eq__` +
`__hash__` (define both or neither — defining `__eq__` alone nulls `__hash__`),
rich comparisons `__lt__`/`__le__`/... (or `@functools.total_ordering`), `__len__`
(also gives truthiness for free — Q1.4), `__iter__`/`__next__`, `__contains__`
(falls back to `__iter__`), `__getitem__` (also enables slicing and iteration
fallback), `__call__` (instance as function).

### Q5.3 What is the MRO and how is it computed?
Method Resolution Order — the linearized lookup path for attributes on a subclass
with multiple parents, computed by **C3 linearization** (monotonic: a class precedes
its parents; local order preserved). Inspect with `Cls.__mro__` / `cls.mro()`.
`super().__init__()` follows the MRO, calling the **next** class, not "the parent" —
this is what makes diamond inheritance cooperate. Name-dropping C3 is optional;
demonstrating `super()` is cooperative, not parental, is the point.

### Q5.4 ★ What do `@dataclass` and `__slots__` each buy you?
`@dataclass` generates `__init__`, `__repr__`, `__eq__` (order by default:
`frozen=True` adds `__hash__`, `slots=True` adds slots). `__slots__` fixes the
attribute set per instance — no per-object `__dict__`, saves memory and speeds
attribute access (useful for millions of small objects, e.g. tree nodes in a
contested interview). Tradeoff: no dynamic attributes, inheritance caveats.

### Q5.5 Interface question: how do you get polymorphism without ABCs in Python?
Duck typing — call the method, handle `AttributeError`/`TypeError`, or use
`typing.Protocol` (structural subtyping, static-only) instead of `abc.ABC`
(nominal, runtime-enforced). Interview phrasing: "Protocol gives me interface
checks at type-check time without forcing an inheritance relationship."

---

## 6. Memory, Performance, GIL, Concurrency

### Q6.1 ★★ How does CPython manage memory?
Reference counting primary: every object keeps a count; reaching 0 frees immediately
and deterministically (why `__del__`/context managers behave predictably). Cycles
(A ↔ B) leak from refcounts alone — a **generational** (three generations, older
collected less often) **mark-and-sweep** cyclic GC collects them periodically;
`gc.disable()` exists for latency-critical loops. Ints are unbounded (variable-size),
so `mid = (lo + hi) // 2` never overflows — the Java/C++ fix `lo + (hi - lo) // 2`
is unnecessary in Python (already drilled Sept 4 — say it unprompted).

### Q6.2 ★★ What is the GIL, and what does it actually block?
A mutex around CPython interpreter state: **one thread executes Python bytecode at a
time**. It does NOT slow single-threaded code, and it is released during most
blocking C calls — I/O waits, and C-extension compute like NumPy — so threading
still wins for **I/O-bound** work and for C-heavy libraries. It DOES block
**CPU-bound parallelism** across Python threads → use `multiprocessing`
/`ProcessPoolExecutor` (separate interpreters, pickled args — beware large-data
transfer cost) or push hot loops to NumPy/Cython. Modern note (bonus points): PEP 703
adds **free-threaded** (no-GIL) builds in 3.13+ experimental; production default is still GIL.

### Q6.3 When do you choose threading vs multiprocessing vs asyncio?
Decision rule: I/O-bound + many concurrent + cheap callbacks → `asyncio` (one thread,
event loop, cooperative — await points are the only preemption); I/O-bound + blocking
libs you can't rewrite → `threading`/ThreadPoolExecutor (preemptive, GIL released
during I/O); CPU-bound Python → `ProcessPoolExecutor` (true parallel, heavier startup,
data crossing process boundary is a copy). SRE angle: "for Prometheus scrape-style
fan-out I'd use asyncio — tens of thousands of sockets, one thread."

### Q6.4 Are Python's data structures thread-safe?
`dict`/`list`/`set` **element** operations are effectively atomic (GIL), but
check-then-act sequences are NOT (`if k not in d: d[k] = v` races). Iterating a
dict while another thread mutates → `RuntimeError`. Use `queue.Queue` (locks +
conditions built in) for producer/consumer, `threading.Lock` for shared state,
`multiprocessing` primitives across processes. Atomic ≠ safe composition.

### Q6.5 How do you actually find a performance problem before optimizing?
`time.perf_counter()` around regions; `cProfile` (function-level, low overhead) →
`snakemake`-style call charts (`snakeviz`); `line_profiler` (`@profile`) for
per-line hotspots; `memory_profiler` / `tracemalloc` for allocations. Optimize in
order: algorithm → data structure → vectorization (NumPy) → cache (`functools.lru_cache`)
→ C extension/Cython. Never guess: profile first. In an interview this answer beats
any micro-optimization trivia.

---

## 7. Correctness Traps Interviewers Probe

### Q7.1 ★★ What does this print?
```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
```
`[99, 2, 3]` — assignment copies the **reference**, not the list; `a is b`.
`b = a[:]` or `list(a)` copies one level (still shares nested objects — Q1.5).
Same aliasing applies to ints inside containers only for cached values; the list
container itself is what's shared.

### Q7.2 What's wrong with `try: ... except: ...`, and what's the Pythonic form?
Bare `except:` swallows `KeyboardInterrupt`, `SystemExit`, and every unrelated bug.
Catch the **narrowest specific exception** you can handle; `except Exception as e:`
at worst (covers everything user-code raises; `BaseException` for cleanup-and-reraise);
`raise` (bare) inside a handler preserves the original traceback; `raise NewError() from e`
for exception chaining. `else:` = run when no exception (better than widening the try);
`finally:` = always, and a `return` in `finally` silently overrides the try's value —
know this before using finally in an interview.

### Q7.3 Why does `for x in lst: lst.remove(x)` skip elements, and what are three fixes?
Mutation during iteration shifts indices while the iterator advances by position —
removing the current element skips the next one. Fixes: iterate a **copy**
(`lst[:]`), build a new list with a comprehension (`[x for x in lst if keep(x)]`),
or reverse-in-place by index. Same trap: `del d[k]` while `for k in d` →
`RuntimeError`; iterate `list(d.items())`.

### Q7.4 What does `dict.get(k, default)` vs `dict[k]` vs `defaultdict` vs `setdefault` — when each?
`d[k]` raises `KeyError` (the honest signal when absence is a bug).
`d.get(k, 0)` for a read that tolerates absence. `defaultdict(list)` when *every*
access should create — beware: `dd[k]` in a **read** inserts the key (surprise
population; use `.get` on a defaultdict to avoid). `d.setdefault(k, []).append(v)`
creates-or-fetches but re-evaluates the default object every call — `defaultdict` is
cleaner in loops.

### Q7.5 `==` between int and bool? `"5" == 5`? What does `sum([True, False, True])` return?
`True == 1` is True (bool subclasses int — hence `sum` over a list of bools counts
truthy values: returns 2). `"5" == 5` is False (no coercion across types).
`[1, 2] == (1, 2)` is False — list ≠ tuple by type equality. These matter for
`in` on mixed-type containers and for set dedup: `{1, True}` has length **1**.

### Q7.6 What is `None` really, and what are the idioms around it?
A singleton instance of `NoneType` — the explicit "no value". Always compare with
`is None` / `is not None` (identity; `== None` can be overridden by `__eq__` in
custom classes). Function with no return statement returns `None`. `x = x or []`
triggers on **any** falsy (0, "", []) — bug if 0 is valid; use `x if x is not None else []`.

---

## 8. Rapid-Fire (know cold; one line each)

| Question | One-line answer |
|---|---|
| Python 3 `//` vs `/` | `//` floor-divides toward −∞ (`-7 // 2 == -4`), `/` always float; LeetCode division trap → `int(a/b)` truncates toward 0 (RPN, Sept 7) |
| `x, y = y, x` mechanism | RHS tuple built first, then unpacked — safe swap without temp |
| list comprehension vs generator expression | `[...]` eager list in memory; `(...)` lazy one-pass — pass generator to `sum`/`max`/`any` |
| `all`/`any` short-circuit? | Yes — stop at first False/True; `all(x > 0 for x in xs)` never builds a list |
| f-string vs `format` vs `%` | f-string evaluated at source location (supports `=` debug specifier), fastest, use it; `.format` when template is data |
| `__init__` vs `__new__` | `__new__` creates the instance (override for immutable subclassing/singletons), `__init` configures it |
| Why `type` vs `isinstance`? | `isinstance` honors inheritance (and ABC/Protocol); `type(x) == T` rejects subclasses — almost always want `isinstance` |
| `del x` | Unbinds the name; frees object only when refcount hits 0 — not a destructor call guarantee |
| `sorted(lst, key=..., reverse=...)` vs `lst.sort()` | Same Timsort (stable, O(n log n)); `sort` in-place returns None — mutation visible to aliases (Q7.1) |
| What is Timsort's stability worth? | Equal elements keep relative order → sort by secondary key first, then primary, without a composite comparator |
| `zip` truncates? | Yes, to shortest; 3.10+ `strict=True` raises on mismatch (off-by-one detector); `itertools.zip_longest` pads |
| `enumerate(iterable, start=1)` | Default start 0 — pass `start=1` for LeetCode 1-indexed answers instead of `i + 1` everywhere (Two Sum II, Sept 7) |
| `reversed(lst)` vs `lst[::-1]` | Iterator, O(1) memory vs copy, O(n) memory |
| Is `range(10**18)` expensive? | No — lazy, O(1) memory, Python 3 range is not a list |
| `a += b` vs `a = a + b` for lists | `+=` calls `extend` (in-place, aliases see it); `a + b` builds new list (aliases don't). Same operator, different semantics — aliasing bug generator |
| `frozenset` | Immutable + hashable set — set as dict key / element of a set |
| `id()` reuse trap | CPython reuses memory addresses after free; two live objects have distinct ids |
| Dict insertion order | Guaranteed since 3.7; JSON responses stay key-ordered without `OrderedDict` |
| `str.split` vs `str.split(sep)` | No-arg splits on runs of any whitespace (strips edges); explicit sep preserves empty fields — `split(",")` on `"a,,b"` → `['a', '', 'b']`. Affects every Decode/Encode Strings problem |
| `collections` you'd name unprompted | `deque`, `Counter`, `defaultdict`, `OrderedDict`, `namedtuple`, `chainmap`, `heapq` (module), `bisect` (module) |

---

## How to Study

1. Cover the A lines, quiz yourself on the Q lines.
2. For ★★ questions, deliver the answer out loud in ≤30 seconds — interview length.
3. Anything you miss gets added to the drill log in `DSA/COACHING.md`; it returns to
   warm-up rotation until answered cold twice in a row.
