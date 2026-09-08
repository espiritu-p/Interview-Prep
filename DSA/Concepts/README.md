# DSA Concepts

Concept notes with problem-grounded examples. Each file covers one paradigm: what it is, when to reach for it, the general template, and a worked example.

## Index

| Concept | Core idea | When to use |
|---|---|---|
| [Bit Manipulation](./bit-manipulation.md) | Operate directly on binary bits using AND, OR, XOR, shifts | Powers of two, XOR tricks, subarray OR/AND problems, bitmask DP |
| [Dynamic Programming](./dynamic-programming.md) | Break into overlapping subproblems; cache results | Optimization over choices with repeated substructure |
| [Greedy](./greedy.md) | Always take the locally best option | Optimization where local best = global best |
| [Sliding Window](./sliding-window.md) | Two pointers defining a window that expands right and shrinks left | Longest/shortest contiguous subarray satisfying a constraint |
| [Python Interview Questions](./python-interview.md) | Language semantics, built-in costs, closures, GIL — asked alongside DSA rounds | Warm-up drill at the start of every DSA session |

## How to read these

1. Read the **Core idea** section first — resist jumping to code.
2. Trace through the **worked example by hand** before reading the code.
3. Look at the **template** last — it should feel obvious by then.
