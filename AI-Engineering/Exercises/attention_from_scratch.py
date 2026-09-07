# AI Engineering — Phase 1 Coding Exercise
# Scaled dot-product attention from scratch (NumPy only — no torch/jax).
#
# Rules of the exercise:
#   - Implement the mechanism, not a copy of a tutorial. If you can't
#     explain one line out loud, you don't own it yet.
#   - Every session drill applies: for each step ask "what problem does
#     this solve, and what breaks without it?" Answer in the STEP NOTES
#     block at the bottom when you finish.
#
# Signature contract:
#   Q: (n_q, d_k)  K: (n_k, d_k)  V: (n_k, d_v)  ->  out: (n_q, d_v)
#   mask: optional (n_q, n_k) array; positions with -inf (or True, if you
#         convert them) are NOT allowed to attend.
#
# Steps to implement (in order):
#   1. scores = Q @ K^T, scaled by 1/sqrt(d_k)      <- why sqrt(d_k)?
#   2. apply mask                                   <- why BEFORE softmax?
#   3. softmax along the KEY axis (rows are queries) <- numerically stable?
#   4. out = weights @ V
#
# Common failure points (found by the tests below):
#   - softmax over the wrong axis
#   - dividing by sqrt(d_v) instead of sqrt(d_k)
#   - naive exp() without subtracting the row max (NaN on large scores)

import numpy as np


def attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
              mask: np.ndarray | None = None) -> np.ndarray:
    """Scaled dot-product attention.

    Returns (n_q, d_v) — each query's convex combination of the value rows.
    """
    # YOUR CODE HERE
    raise NotImplementedError


# --------------------------------------------------------------------------
# Verification — run: python attention_from_scratch.py
# Expected values are hardcoded from hand computation; tolerance 1e-3.
# --------------------------------------------------------------------------

def _tests() -> None:
    # T1: single key — softmax over one value is 1, so output == that V row.
    Q = np.array([[1.0, 2.0]])
    K = np.array([[0.5, -1.0]])
    V = np.array([[3.0, 4.0]])
    out = attention(Q, K, V)
    assert np.allclose(out, V, atol=1e-3), f"T1 single-key: {out}"

    # T2: concrete 2-key case, hand-computed.
    # scores = [1, 0]/sqrt(2) -> softmax -> [0.66976, 0.33024]
    # V = identity -> output IS the weight vector.
    Q = np.array([[1.0, 0.0]])
    K = np.array([[1.0, 0.0], [0.0, 1.0]])
    V = np.eye(2)
    out = attention(Q, K, V)
    assert np.allclose(out, [[0.66976, 0.33024]], atol=1e-3), f"T2 scaling/softmax: {out}"

    # T3: causal mask. Query 0 may only see key 0; query 1 sees both.
    # Row 1 scores = [0, 1]/sqrt(2) -> weights [0.33024, 0.66976].
    Q = np.eye(2)
    K = np.eye(2)
    V = np.eye(2)
    causal = np.array([[0.0, -np.inf], [0.0, 0.0]])
    out = attention(Q, K, V, mask=causal)
    want = np.array([[1.0, 0.0], [0.33024, 0.66976]])
    assert np.allclose(out, want, atol=1e-3), f"T3 causal masking: {out}"

    # T4: numerical stability. Huge dot products must not produce NaN/inf.
    big = np.array([[1e4, 0.0]])
    out = attention(big, big, np.array([[1.0, 7.0]]))
    assert np.all(np.isfinite(out)), f"T4 stability: {out}"
    assert np.allclose(out, [[1.0, 7.0]], atol=1e-3), f"T4 dominance: {out}"

    # T5: weights are a convex combination — rows sum to 1.
    rng = np.random.default_rng(7)
    Q, K, V = rng.normal(size=(4, 8)), rng.normal(size=(6, 8)), rng.normal(size=(6, 3))
    w = attention(Q, K, np.eye(6))
    assert np.allclose(w.sum(axis=1), 1.0, atol=1e-6), "T5 rows must sum to 1"
    assert np.all((w >= 0) & (w <= 1)), "T5 weights must lie in [0, 1]"

    print("All tests passed — scaled dot-product attention is correct.")


if __name__ == "__main__":
    _tests()


# --------------------------------------------------------------------------
# STEP NOTES — fill in when done (this is the interview-relevant part):
#
# 1. Why divide by sqrt(d_k)? What breaks without it?
#    ->
# 2. Why must the mask be applied BEFORE the softmax, not after?
#    ->
# 3. Why subtract the row max before exponentiating?
#    ->
# 4. In a real model this runs as one batched matmul per head. Where does
#    the O(n^2) cost live in your implementation?
#    ->
# --------------------------------------------------------------------------
