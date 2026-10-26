# CS Fundamentals Crosswalk — roadmap.sh/computer-science ↔ this repo

Source: [Computer Science roadmap](https://roadmap.sh/computer-science) (topic tree inventoried 2026-10-26).
Purpose: check the five interview tracks against a full CS curriculum, list real gaps, and queue them
**after the Nov 15 DSA backlog clears** — nothing here runs during the DSA-only window.

Coverage grades: ✅ covered by a track · 🟡 partial · ⬜ gap · ⏸ intentionally cut.

## Area-by-area mapping

| Roadmap area | Repo home | Grade | Gap detail |
|---|---|---|---|
| Pick a language (Python, C, Java, Go, Rust…) | Python track | ✅ | Python chosen; C/Java never needed for these loops |
| Basic math, combinatorics, probability, floating point | SD 1.1 estimation + AI internals | 🟡 | **Floating-point arithmetic** (IEEE 754, precision, NaN/inf) — pairs with Python Phase 4 NumPy work |
| Data structures: arrays, strings, linked lists, stacks, queues, heaps, hash tables, binary trees, BST | DSA track, Oct 26 → Nov 15 plan | ✅ | The hands-on core is exactly the plan |
| Advanced DS: AVL, red-black, B/B+/2-3/2-3-4, skip lists, tries, k-d, suffix arrays | — | 🟡 | Never asked to *implement* in these interviews; asked to *explain what problem each solves*. One theory flash-pass (30 min), never a problem set |
| Algorithms: sorting, searching, BFS/DFS, MST, shortest path, DP, greedy | DSA track | ✅ | Dijkstra/MST theory rides with Advanced Graphs cut — revisit only if a graph role appears |
| String matching (KMP, Rabin-Karp, Boyer-Moore), max-flow | — | ⏸ | Cut — not worth time before interviews |
| Complexity classes: P, NP, NP-complete, NP-hard, reductions | — | ⬜ | Asked in senior/applied-science loops ("is this problem tractable?"). Half-day: definitions, classic NP-complete set, how to recognize + argue in an answer |
| OS / process models: CPU execution, processes vs threads, scheduling algorithms, process forking, memory management, virtual memory, CPU caches, endianness, interrupts | Python Phase 2 touches concurrency; nothing systematic | ⬜ | **Biggest real gap.** Classic SRE + backend interview territory — scheduling, fork/exec, virtual memory/OOM, deadlock conditions, context-switch cost |
| Concurrency: locks/mutexes/semaphores, multi-core, GIL | Python Phase 2.4 + Phase 3.4 | 🟡 | Python-specific angle covered; OS-level theory missing (same sessions fix it) |
| Networking: OSI vs TCP/IP models, sockets, TCP internals, HTTP, DNS, TLS/HTTPS, WebSocket/SSE | SD 1.2–1.3 | 🟡 | HTTP/DNS/SSE covered. Missing: layer models, TCP handshake/state machine/congestion, sockets API, TLS handshake |
| Databases: ACID, transactions, indexes, NoSQL, CAP, replication, sharding | SD Phase 2 | ✅ | Core covered |
| DB modeling: normalization, ER model, views, stored procedures, federation | — | 🟡 | **1NF–3NF + ER diagram fluency** helps mock schema design (URL shortener, notification service); rest is admin trivia, skip |
| System design: scaling, CDN, proxies, LB, caching, consistent hashing, rate limiting, queues, service discovery | SD Phases 1–3 | ✅ | Roadmap adds nothing beyond the track |
| Design patterns (GoF, dependency injection) + UML diagrams | — | ⬜ | LLD/implementation-loop material. Low priority unless a role's interview mentions "design a parking lot": 5 patterns (strategy, observer, factory, decorator, singleton) + sequence/class diagram literacy |
| Security: hashing vs encoding vs encryption, public-key crypto, TLS, OWASP Top 10 | — | ⬜ | One session post-restart. **AI crossover:** OWASP **LLM Top 10** (prompt injection ↔ SSRF analogy) is directly on-topic for AI Engineering interviews |
| Cloud services | SRE day job | ✅ | Original SD Phase 5 cut stands |

## Resume-window backlog (queue after Nov 15, before mock rounds)

| # | Session | Track home | Closes gap |
|---|---|---|---|
| 1 | OS fundamentals: processes/threads, scheduling, virtual memory, deadlock, context switches | New SD Phase 0 *or* Python Phase 2 prelude | OS ⬜, concurrency theory |
| 2 | Networking deep dive: OSI vs TCP/IP, TCP handshake + congestion, sockets, TLS | SD Phase 1 (extends 1.3) | Networking 🟡 |
| 3 | Complexity classes + NP-completeness recognition | New AI/DSA crossover note | NP ⬜ |
| 4 | Data modeling: 1NF–3NF, ER diagrams, then redo mock schemas | SD Phase 2 (extends 2.1) | DB modeling 🟡 |
| 5 | Security: TLS + OWASP Top 10 + OWASP LLM Top 10 map | SD + AI joint session | Security ⬜ |
| 6 | Floating point: IEEE 754, catastrophic cancellation, why `int(a/b)` in RPN went wrong-side | Python Phase 4 prelude | Math 🟡 |
| 7 | Advanced DS theory flash: one sentence per tree — problem it solves, where it lives (Postgres=B-tree, Redis=skip list, etcd=B+… ) | 30-min pass | Adv DS 🟡 |
| 8 | GoF five patterns + UML literacy (only if an LLD interview is on the calendar) | Deferred trigger | Patterns ⬜ |

**Protocol for the next planning session:** anything scheduled from this backlog must get verified
video-first links into the owning track's COACHING.md Pre-Session References before its session date
(standing rules 6–7), and each session is added to that track's PLAN.md tracker.
