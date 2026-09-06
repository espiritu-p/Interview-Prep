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

## Pre-Session References

Read/watch before each session — concept walkthrough + quiz assumes one pass through the material. Links verified 2026-09-06.

| Session | Read | Watch |
|---------|------|-------|
| 1.1 — Transformer architecture | [Jay Alammar — The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) (ch.1 covers the same ground) | [3Blue1Brown — Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc) |
| 1.2 — Attention deep-dive | [HF blog — Attention is all you need walkthrough](https://huggingface.co/blog/Esmail-AGumaan/attention-is-all-you-need) | [3Blue1Brown video above](https://www.youtube.com/watch?v=eMlx5fFNoYc) (best single explainer) · [Alammar video companion](https://www.youtube.com/watch?v=hVEo76eZmpo) |
| 1.3 — Positional encoding | [HF blog — Designing Positional Encoding for Transformers](https://huggingface.co/blog/designing-positional-encoding) · [EleutherAI — Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) · [Raschka — Positional info FAQ](https://sebastianraschka.com/faq/docs/positional-information-transformer.html) | [Transformer Explainer (interactive)](https://poloclub.github.io/transformer-explainer/) |
| 1.4 — KV cache | [Lilian Weng — LLM Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) (KV cache section) · [KV caching explained](https://medium.com/@joaolages/kv-caching-explained-276520203249) | — |
| 1.5 — Scaling laws | [Kaplan et al. — Scaling Laws for Neural LMs](https://arxiv.org/abs/2001.08361) (skim abstract + ch.2) · [Hoffmann et al. — Chinchilla](https://arxiv.org/abs/2203.15556) (read blog summary first) | — |
| 1.6 — Tokenization | [HF — How tokenizers work (course ch.2)](https://huggingface.co/learn/llm-course/en/chapter2/2) · [minbpe (Karpathy's reference BPE)](https://github.com/karpathy/minbpe) · [Tiktokenizer (live playground)](https://tiktokenizer.vercel.app/) | [Karpathy — Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) (~2h; watch at 1.5×, skip the coding if time-pressed — the first hour is the concept) |

**Supplement (any session):** [Lilian Weng — The Transformer Family v2](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — dense but it's the reference map for everything in Phase 1.

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
