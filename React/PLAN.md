# React Interview Plan

Target: interview-ready by **October 1, 2026**

## Objective

Explain React's rendering model, state and effects, performance tradeoffs, and
frontend architecture clearly in interviews. Sessions use concept walkthroughs,
interviewer probes, and small implementation exercises only when they add value.

## Phase Map

```
Phase 1 — Core model                 Components, JSX, props, state, rendering
Phase 2 — Hooks & state              Effects, refs, context, reducers, custom hooks
Phase 3 — Performance                Reconciliation, memoization, lists, profiling
Phase 4 — Production frontend       Data fetching, testing, accessibility, architecture
```

## Phase 1 — Core Model

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 1.1 | Components and JSX | Component boundaries, props, composition, keys |
| 1.2 | State and rendering | Render cycle, immutability, batching, controlled inputs |
| 1.3 | Reconciliation | Element identity, keys, mount vs. update, Strict Mode |

## Phase 2 — Hooks & State

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 2.1 | `useEffect` | Synchronization, dependencies, cleanup, stale closures |
| 2.2 | `useRef` and custom hooks | Mutable values, DOM references, reusable behavior |
| 2.3 | Context and reducers | Prop drilling, provider boundaries, state ownership |

## Phase 3 — Performance

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 3.1 | Memoization | `memo`, `useMemo`, `useCallback`, when they hurt |
| 3.2 | Lists and large UIs | Stable keys, virtualization, derived state |
| 3.3 | Debugging performance | Profiler, render waterfalls, code splitting |

## Phase 4 — Production Frontend

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 4.1 | Data fetching | Loading/error states, caching, race conditions, aborting |
| 4.2 | Testing | Component tests, user behavior, mocking boundaries |
| 4.3 | Accessibility and architecture | Semantic HTML, keyboard access, feature boundaries |

## Progress Tracker

| Phase | Sessions | Status |
|-------|----------|--------|
| 1 — Core model | 1.1 · 1.2 · 1.3 | ⬜ Not started |
| 2 — Hooks & state | 2.1 · 2.2 · 2.3 | ⬜ Not started |
| 3 — Performance | 3.1 · 3.2 · 3.3 | ⬜ Not started |
| 4 — Production frontend | 4.1 · 4.2 · 4.3 | ⬜ Not started |

Start a session: **`React: Phase X.Y`** (e.g., `React: Phase 1.1`)
