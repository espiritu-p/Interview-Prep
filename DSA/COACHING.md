# Interview Prep — Master Coaching Log

Persistent record across all three tracks. Updated after every session.  
**Goal: Interview-ready by October 1, 2026.**

> Coaching protocol and session rules live in [`CLAUDE.md`](../CLAUDE.md) at the repo root.

---


## Baseline (2026-09-03)

| Track | Starting point |
|-------|---------------|
| DSA | LeetCode: 27 solved · Kattis: 144 solved |
| System Design | SRE background in prod — strong ops instincts, needs interview framing |
| AI Engineering | LangGraph/LangChain/MCP in prod, 2× NLP publications — needs conceptual depth |

---

## DSA Topic Status

### Phase 1 — Foundations

| Topic | Status | Remaining |
|---|---|---|
| Arrays and Hashing | ✅ Partial | Majority Element, Two Sum, Group Anagrams, Product of Array Except Self, Valid Sudoku, Encode and Decode Strings, Find the Duplicate Number, Sort an Array, Longest Consecutive Sequence |
| Math and String | ✅ Partial | (covered well enough, not blocking) |
| Bit Manipulation | 🔁 Needs redo | Problems solved but concepts need re-learning from scratch |
| Sliding Window | 🔁 Needs redo | Best Time to Buy and Sell Stock, Max Vowels in Substring, Min Size Subarray Sum, Longest Substring Without Repeating Characters, Longest Repeating Character Replacement, Permutation in String, Min Window Substring, Sliding Window Maximum |
| **Two Pointers** | ⬜ NOT STARTED | Valid Palindrome, Move Zeroes, Two Sum II, 3Sum, Sort Colors, Container With Most Water, Trapping Rain Water |
| **Stack** | ⬜ NOT STARTED | Valid Parentheses, Decode String, Asteroid Collision, Min Stack, Evaluate Reverse Polish Notation, Generate Parentheses, Daily Temperatures, Car Fleet, Largest Rectangle in Histogram |
| **Binary Search** | ⬜ NOT STARTED | Binary Search, Find Peak Element, Search a 2D Matrix, Koko Eating Bananas, Find Min in Rotated Sorted Array, Search in Rotated Sorted Array, Time Based Key-Value Store, Median of Two Sorted Arrays |

### Phase 2 — Core Data Structures

| Topic | Status |
|---|---|
| Linked List | ⬜ NOT STARTED |
| Trees (BFS/DFS) | ⬜ NOT STARTED |
| Tries | ⬜ NOT STARTED |
| Heap / Priority Queue | ⬜ NOT STARTED |

### Phase 3 — Algorithms

| Topic | Status |
|---|---|
| Backtracking | ⬜ NOT STARTED |
| Graphs (BFS/DFS) | ⬜ NOT STARTED |
| Advanced Graphs | ⬜ NOT STARTED |

### Phase 4 — Optimization Paradigms

| Topic | Status | Remaining |
|---|---|---|
| Greedy | ✅ Partial | Maximum Subarray, Jump Game, Jump Game II, Gas Station, Hand of Straights, Merge Triplets to Form Target Triplet, Partition Labels, Valid Parenthesis String, Non-overlapping Intervals, Min Arrows to Burst Balloons |
| DP 1D | ⬜ NOT STARTED | Climbing Stairs, Min Cost Climbing Stairs, House Robber, House Robber II, Longest Palindromic Substring, Palindromic Substrings, Decode Ways, Coin Change, Maximum Product Subarray, Word Break, Longest Increasing Subsequence, Partition Equal Subset Sum |
| DP 2D | ⬜ Barely started | (skipped until October — not worth the time) |
| Intervals | ⬜ NOT STARTED | (skipped until October — not worth the time) |

### Phase 5 — Advanced

| Topic | Status |
|---|---|
| Segment Tree / Sorted Container | 🔁 Needs redo |
| Math and Geometry | ⬜ NOT STARTED |

Topics skipped intentionally (not worth the time before October):  
Tries, DP 2D, Advanced Graphs, Intervals, Segment Trees, Math & Geometry

---

## Daily Schedule

**Three tracks, one day.** Each track has a distinct activity type so they don't blur together.

| Block | Track | Activity | Time |
|-------|-------|----------|------|
| Morning (before work or commute) | AI Engineering | Read one concept note or session | 20–30 min |
| Evening block 1 | DSA | 1–2 LeetCode problems | 30–45 min |
| Evening block 2 | System Design | One concept session OR a mock design | 30–45 min |

**Total: ~90 min/day.** Sustainable alongside a full-time SRE role.

**Rotation logic:**
- DSA is daily — pattern recognition requires daily repetition
- AI Engineering and System Design alternate: concept sessions on weekdays, mock/deep-dives on weekends
- Weekends: one longer System Design mock (~45 min) replaces the two concept sessions

---

## September Battle Plan

**27 days. Target: DSA Phases 1–3 + DP 1D + Graphs · SD Phases 1–4 · AI Phases 1–3**

### Week 1 — Sept 4–10
**DSA focus:** Two Pointers + Stack + Binary Search  
**SD focus:** Phase 1 — Foundations (scale, APIs, DNS, CDN, proxies, hashing)  
**AI focus:** Phase 1 — LLM Internals (Transformer, attention, positional encoding)

| Day | DSA | System Design | AI Engineering |
|-----|-----|---------------|----------------|
| Sept 4 ✅ | Valid Palindrome · Valid Parentheses · Binary Search | `SD: Phase 1.1` — Scale of numbers + estimation | `AI: Phase 1.1` — Transformer architecture |
| Sept 5 ✅ | Move Zeroes · Min Stack | `SD: Phase 1.2` — APIs (REST vs gRPC vs GraphQL) | `AI: Phase 1.2` — Attention deep-dive |
| Sept 6 | Two Sum II · Evaluate Reverse Polish Notation | `SD: Phase 1.3` — DNS + load balancing | `AI: Phase 1.3` — Positional encoding |
| Sept 7 | 3Sum · Daily Temperatures | `SD: Phase 1.4` — CDN | `AI: Phase 1.4` — KV cache |
| Sept 8 | Find Min in Rotated Sorted Array · Generate Parentheses | `SD: Phase 1.5` — Proxies + API gateways | `AI: Phase 1.5` — Scaling laws |
| Sept 9 | Search in Rotated Sorted Array · Koko Eating Bananas | `SD: Phase 1.6` — Consistent hashing | `AI: Phase 1.6` — Tokenization |
| Sept 10 | Container With Most Water — review/catch-up | **Weekend:** `SD: Case 6.1` mock — URL Shortener | Review AI Phase 1 — explain each concept from memory |

### Week 2 — Sept 11–17
**DSA focus:** Sliding Window redo + Arrays & Hashing gaps + Linked List  
**SD focus:** Phase 2 — Storage & Databases  
**AI focus:** Phase 2 — Retrieval & RAG

| Day | DSA | System Design | AI Engineering |
|-----|-----|---------------|----------------|
| Sept 11 | Best Time to Buy and Sell Stock · Longest Substring Without Repeating Characters | `SD: Phase 2.1` — Relational DBs + indexes | `AI: Phase 2.1` — RAG fundamentals |
| Sept 12 | Longest Repeating Character Replacement · Permutation in String | `SD: Phase 2.2` — NoSQL types | `AI: Phase 2.2` — Chunking strategies |
| Sept 13 | Two Sum · Group Anagrams | `SD: Phase 2.3` — CAP theorem | `AI: Phase 2.3` — Embedding models |
| Sept 14 | Product of Array Except Self · Longest Consecutive Sequence | `SD: Phase 2.4` — Replication | `AI: Phase 2.4` — Vector search (HNSW, IVF) |
| Sept 15 | Reverse Linked List · Merge Two Sorted Lists | `SD: Phase 2.5` — Sharding | `AI: Phase 2.5` — Reranking |
| Sept 16 | Linked List Cycle · Reorder List | `SD: Phase 2.6` — Caching | `AI: Phase 2.6` — Hybrid search |
| Sept 17 | Remove Nth Node From End of List — review/catch-up | **Weekend:** `SD: Case 6.2` mock — Rate Limiter | Review AI Phase 2 — walk through a RAG pipeline from memory |

### Week 3 — Sept 18–24
**DSA focus:** Trees (BFS/DFS) + Heap  
**SD focus:** Phase 3 — Scalability Patterns  
**AI focus:** Phase 3 — Agents & Tool Use

| Day | DSA | System Design | AI Engineering |
|-----|-----|---------------|----------------|
| Sept 18 | Invert Binary Tree · Maximum Depth of Binary Tree | `SD: Phase 3.1` — Message queues | `AI: Phase 3.1` — ReAct pattern |
| Sept 19 | Same Tree · Diameter of Binary Tree | `SD: Phase 3.2` — Kafka internals | `AI: Phase 3.2` — Tool use + function calling |
| Sept 20 | Binary Tree Level Order Traversal · Binary Tree Right Side View | `SD: Phase 3.3` — Rate limiting | `AI: Phase 3.3` — Memory types |
| Sept 21 | Validate Binary Search Tree · Kth Smallest Element in a BST | `SD: Phase 3.4` — Idempotency | `AI: Phase 3.4` — Multi-agent coordination |
| Sept 22 | Lowest Common Ancestor of a BST · Count Good Nodes | `SD: Phase 3.5` — Distributed transactions | `AI: Phase 3.5` — LangGraph internals |
| Sept 23 | Kth Largest Element in a Stream · K Closest Points to Origin | `SD: Phase 3.6` — Service discovery | `AI: Phase 3.6` — MCP architecture |
| Sept 24 | Kth Largest Element in an Array — review/catch-up | **Weekend:** `SD: Case 6.3` mock — Notification Service | **Weekend:** AI Phase 3 coding exercise — ReAct agent from scratch |

### Week 4 — Sept 25–Oct 1
**DSA focus:** DP 1D + Bit Manipulation redo + Graphs intro + Greedy gaps  
**SD focus:** Phase 4 — Reliability & Ops (your strongest — lean into SRE experience)  
**AI focus:** Phase 4 — Evaluation & Evals

| Day | DSA | System Design | AI Engineering |
|-----|-----|---------------|----------------|
| Sept 25 | Climbing Stairs · House Robber | `SD: Phase 4.1` — SLOs + error budgets | `AI: Phase 4.1` — Why evals are hard |
| Sept 26 | House Robber II · Coin Change | `SD: Phase 4.2` — Circuit breakers + bulkheads | `AI: Phase 4.2` — Automated metrics (BLEU, BERTScore, G-Eval) |
| Sept 27 | Longest Increasing Subsequence · Maximum Product Subarray | `SD: Phase 4.3` — Retries + timeouts | `AI: Phase 4.3` — Eval dataset design |
| Sept 28 | Power of Two · Number of 1 Bits · Single Number | `SD: Phase 4.4` — Observability (metrics/logs/traces) | `AI: Phase 4.4` — LLM-as-judge |
| Sept 29 | Number of Islands · Clone Graph | `SD: Phase 4.5` — Deployment strategies | `AI: Phase 4.5` — RAG-specific evals (RAGAS) |
| Sept 30 | Max Area of Island · Rotting Oranges | `SD: Phase 4.6` — Disaster recovery (RTO/RPO) | `AI: Phase 4.6` — Agent evals |
| Oct 1 | Maximum Subarray · Jump Game — final review | **Final mock:** `SD: Case 6.6` — AI Inference Service (bridges both tracks) | **Final:** AI Phase 4 coding exercise — LLM-as-judge eval harness |

---

## DSA Review Rubric

> Rubric lives in [`CLAUDE.md`](../CLAUDE.md) — DSA review rubric section.

---

## Coaching Sessions

### Session 1 — 2026-09-03

**Assigned challenges (Session 1):**

| # | Problem | Topic | Difficulty | Status |
|---|---|---|---|---|
| 1 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | Easy | ✅ Done (Sept 4) |
| 2 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | Easy | ✅ Done (Sept 4) |
| 3 | [Binary Search](https://leetcode.com/problems/binary-search/) | Binary Search | Easy | ✅ Done (Sept 4) |

**Completed:**

**Valid Palindrome (Sept 4)** — committed as `solved(LeetCode): #125`
- Correct two-pointer pattern, correct `<` loop condition, early return
- Coach notes: camelCase vars (`startIdx`) → use `left`/`right`; redundant `else` after `return`; built O(n)-space `clean_s` without naming the O(1)-space variant — in interviews, acknowledge the tradeoff in one sentence
- Drill: restate edge cases → plan → complexity → variant, out loud, every problem

**Valid Parentheses (Sept 4)** — committed as `solved(LeetCode): #20`
- Correct on all edge cases (empty-stack closer, leftover openers, mismatch)
- Coach notes: leftover debug `print` committed (biggest red flag); `for i in range(len(s))` → `for char in s`; triple-`or` mismatch chain → `pairs` dict lookup; tail `if/return` → `return not stack`
- Drill: before submitting, scan for `print` and `range(len(` — both are tells

**Binary Search (Sept 4)** — committed as `solved(LeetCode): #704`
- Textbook-correct: `<=` condition, ±1 bound updates, `-1` fallback; all edge cases fine
- Coach notes: parens on `while` again (2nd occurrence — C/Java habit, actively unlearn); comment typo
- Interview line to memorize: `(high + low) // 2` overflows in Java/C++ (`low + (high - low) // 2`), Python ints are unbounded so it's fine — say it unprompted
- Session 1 complete: 3/3 in one day

---

### Session 2 — 2026-09-05/06

**Assigned challenges (Session 2):**

| # | Problem | Topic | Difficulty | Status |
|---|---|---|---|---|
| 4 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Two Pointers | Easy | ✅ Done (Sept 5) |
| 5 | [Min Stack](https://leetcode.com/problems/min-stack/) | Stack | Medium | ✅ Done (Sept 5) |
| 6 | [Two Sum II — Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Medium | 🔜 In progress (Sept 6) |
| 7 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack | Medium | 🔜 In progress (Sept 6) |

**Move Zeroes (Sept 5)** — committed as `solved(LeetCode): #283`
- Correct write-pointer + backfill approach, O(n)/O(1) stated upfront
- Coach notes: `range(len(nums))` → `enumerate` where index isn't the point; docstring plan block is good interview behavior — keep narrating before coding

**Min Stack (Sept 5)** — committed as `solved(LeetCode): #155`
- Two-stack design correct including duplicate handling (`<=` on push, match-check on pop) — the duplicate case is where most candidates fail
- Coach notes: name the space tradeoff unprompted (`min_list` can be O(n); alternate = store `(value, current_min)` pairs, same worst case but one stack); `getMin` capitalization is LeetCode's, not yours — leave it

---

## How to Update This File

**After a DSA problem:** tell me the name, whether you solved independently or needed hints, and what tripped you up. I'll log it and assign the next one.

**After a System Design session:** tell me which session, what you answered well vs. struggled on. I'll log the debrief.

**After an AI Engineering session:** same — which phase, what landed vs. felt shaky. I'll update the AI COACHING.md.
