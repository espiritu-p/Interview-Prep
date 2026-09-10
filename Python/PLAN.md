# Python Interview Plan

Target: interview-ready by **October 1, 2026**

## Objective

Predict Python behavior from code, explain the language mechanics behind it,
and work comfortably with common NumPy and pandas operations without relying on
trial-and-error or memorized snippets.

## Phase Map

```
Phase 1 — Language semantics       Expressions, objects, scope, iteration, exceptions
Phase 2 — Async & concurrency      Coroutines, tasks, event loop, timers, threads, processes
Phase 3 — Python in interviews     Built-ins, data model, typing, performance, debugging
Phase 4 — NumPy & pandas           Arrays, broadcasting, indexing, grouping, missing data
```

## Phase 1 — Language Semantics

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 1.1 | Tricky expressions | Truthiness, precedence, short-circuiting, chained comparisons |
| 1.2 | Objects and mutability | Identity vs. equality, aliasing, shallow/deep copies, defaults |
| 1.3 | Scope and execution | LEGB, closures, comprehensions, generators, context managers |
| 1.4 | Iteration and exceptions | Iterators, `yield`, mutation during iteration, exception flow |

## Phase 2 — Async & Concurrency

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 2.1 | Coroutines and the event loop | `async`/`await`, cooperative scheduling, coroutine vs. task |
| 2.2 | Timers and task ordering | `sleep(0)`, `call_later`, task creation order, cancellation |
| 2.3 | Blocking work | Why blocking stalls the loop, executors, threads vs. processes |
| 2.4 | Synchronization | Locks, events, queues, cancellation safety, race conditions |

## Phase 3 — Python in Interviews

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 3.1 | Built-in data structures | Operation costs, hashability, ordering, comprehensions |
| 3.2 | Functions and classes | Decorators, descriptors, `__new__`/`__init__`, protocols |
| 3.3 | Typing and APIs | Iterables, protocols, `dataclass`, generics, validation |
| 3.4 | Performance and debugging | Profiling, memory, GIL, common hidden costs |

## Phase 4 — NumPy & pandas

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 4.1 | NumPy arrays | Shape, dtype, views vs. copies, vectorization |
| 4.2 | Broadcasting and indexing | Broadcasting rules, boolean masks, axis semantics |
| 4.3 | pandas core operations | Series/DataFrame, selection, joins, groupby, aggregation |
| 4.4 | Missing data and debugging | `NaN`/`NA`, alignment, chained assignment, performance |

## Progress Tracker

| Phase | Sessions | Status |
|-------|----------|--------|
| 1 — Language semantics | 1.1 · 1.2 · 1.3 · 1.4 | ⬜ Not started |
| 2 — Async & concurrency | 2.1 · 2.2 · 2.3 · 2.4 | ⬜ Not started |
| 3 — Python in interviews | 3.1 · 3.2 · 3.3 · 3.4 | ⬜ Not started |
| 4 — NumPy & pandas | 4.1 · 4.2 · 4.3 · 4.4 | ⬜ Not started |

Start a session: **`Python: Phase X.Y`** (e.g., `Python: Phase 1.1`)
