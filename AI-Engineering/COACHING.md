# AI Engineering Coaching Log

Persistent record for cross-session coaching. Updated after every completed session.

> Coaching protocol and session rules live in [`CLAUDE.md`](../CLAUDE.md) at the repo root.

---


## Baseline (2026-09-03)

**Background:**
- SRE @ Procter & Gamble — autonomous agents in prod (LangGraph, LangChain, MCP)
- Authored Agent Skills as incident copilot across Claude, Copilot, Gemini
- 2× peer-reviewed NLP publications (Seq2Seq, multi-label classification)
- MS CS @ DLSU, 3.9 GPA

**Strengths going in:**
- Agentic patterns (LangGraph, MCP) from real production work
- NLP research background (sequence modeling, low-resource settings)
- SRE observability — can instrument and measure AI systems in prod

**Gaps to close before October:**
- LLM internals (attention, KV cache, scaling laws) — from-scratch explanation
- RAG pipeline design — chunking, reranking, hybrid search
- Eval methodology — metrics, LLM-as-judge, RAGAS
- PEFT stack — LoRA, QLoRA, DPO (classic DL background, not modern PEFT)
- Inference & serving — quantization, vLLM, speculative decoding
- Safety & alignment — RLHF, RLAIF, red-teaming

---

## Sessions

### Session 1 — 2026-09-04 — Phase 1.1: Transformer architecture ✅ Complete

**Reading:** Jay Alammar — *The Illustrated Transformer* (jalammar.github.io/illustrated-transformer/). Completed prior to session.

**Debrief:**

| Question | Performance | Notes |
|----------|-------------|-------|
| Q1 — Encoder vs decoder / GPT decoder-only | ⚠️ Weak | Correct direction; missed bidirectional vs causal attention distinction; GPT decoder-only rationale entirely absent |
| Q2 — Why residual connections exist | ⚠️ Weak | Described WHERE (add+norm), not WHY (gradient flow); conflated residual connections with layer norm; missed 2 per block |
| Gradient flow clarification | ✅ Good instinct | Asked before moving on — correct behavior; concept now understood |
| Q3 — What layer norm does | ❌ Wrong | Said 0–1 scaling (that's sigmoid/softmax); correct answer: zero mean, unit variance per token |
| Q4 — FFN role | ❌ Wrong | Said "next RNN" — no RNNs in transformers; missed per-token independence and parameter dominance |
| Q5 — Attention vs FFN | ⚠️ Partial | Correct that attention evaluates word-to-word relevance; missed the key contrast: attention=cross-token mixing, FFN=per-token transformation |

**Overall:** Directionally aware but precision not yet at interview level. Expected — these are LLM internals gaps identified at baseline. Right instincts, wrong mechanics. Needs one more pass on transformer block structure before 1.2.

**Concepts to re-read before Phase 1.2:**
- Residual connections: WHY (gradient flow) not just WHERE
- Layer norm: zero mean + unit variance (not 0–1 scaling)
- FFN: per-token, independent, ~2/3 of parameters, no RNNs

**Coding exercise:** Not yet attempted (Phase 1 exercise: implement scaled dot-product attention in NumPy — due after Phase 1.2).

---

### Session 2 — 2026-09-06 — Phase 1.2: Attention deep-dive (Q/K/V) ✅ Complete

**Format:** Concept walkthrough (Q/K/V, scaled dot-product, multi-head, causal masking) + 3-question quiz

| Question | Performance | Notes |
|----------|-------------|-------|
| Q1 — Why divide by √(dₖ) | ⚠️ Partial | Got the outcome (dot products too big → near-zero gradients); missed the mechanism — softmax saturation into near one-hot + variance of dot product scales with dₖ, so √(dₖ) normalizes variance back to 1 |
| Q2 — Computational bottleneck | ⚠️ Partial | Correctly named the n×n attention matrix; answer stayed at "more space and time" — missing O(n²·d) time / O(n²) space, quadratic consequence (2× context = 4× cost), and the existence of FlashAttention/sparse/sliding-window attention as responses |
| Q3 — Why multi-head beats single-head | ⚠️ Partial | Correct core idea (heads attend to different aspects: syntax, coreference); missed that each head has its own learned W_Q/W_K/W_V projections, and that d_k = d_model/h keeps total parameter count identical — diversity for free |

**Pattern across session:** instincts consistently right, answers stop at the outcome instead of the mechanism. Interview differentiator is the *why* behind design choices — drill stating mechanism before consequence.

**Drill for 1.3 (positional encoding):** for every architectural choice encountered, answer "what problem does this solve, and what breaks without it?" in one sentence before moving on.

**Status: Phase 1.2 ✅ complete**

---

## How to Update This File

After each session, tell me:
- What phase/session we covered
- Which probing questions you answered well vs. struggled with
- Whether you completed the coding exercise

I'll log the debrief and update PLAN.md progress tracker.
