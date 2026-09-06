# System Design Coaching Log

Persistent record. Updated after every completed session.

---

## Baseline (2026-09-03)

**Relevant production experience:**
- SRE @ P&G — 3,000+ servers, Prometheus, Thanos, Grafana, Splunk, Puppet; SLO/error budget ownership
- Samsung — Kubernetes, Jenkins CI/CD, cloud orchestration UI, CNF/VNF topology
- AZ-900 certified; SRE Foundation + Practitioner certified

**Strengths going in:**
- Reliability engineering: SLOs, error budgets, observability, MTTR reduction
- Fleet automation at scale: Puppet, Prometheus alerting, auto-ticketing
- Deployment discipline: 97% change success rate over 3,000+ servers
- Containerized workloads: Kubernetes, Jenkins

**Gaps to close before October:**
- Database internals at interview depth (replication, sharding, CAP)
- Message queue / event streaming patterns (Kafka internals, saga pattern)
- AWS service landscape (background is Azure/Kubernetes-heavy)
- Structured mock design practice — frameworks and timing

---

## Pre-Session References

Read before each session. The concept walkthrough assumes you've seen the material once — links verified 2026-09-06.

| Session | Read |
|---------|------|
| 1.1 — Scale of numbers | [Colin Scott — Interactive latency numbers](https://colin-scott.github.io/personal_website/research/interactive_latency.html) · [Sam Watt — Numbers everyone should know](https://samwho.dev/numbers/) |
| 1.2 — APIs | [gRPC — What is gRPC](https://grpc.io/docs/what-is-grpc/introduction/) · [GraphQL — Learn](https://graphql.org/learn/) · [MDN — HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) |
| 1.3 — DNS + LB | [ByteByteGo — How DNS lookup works](https://bytebytego.com/guides/how-does-the-domain-name-system-dns-lookup-work/) · [ByteByteGo — Load balancers cheat sheet](https://medium.com/bytebytego-system-design-alliance/everything-about-load-balancer-with-cheat-sheet-64b351f0f7b3) · [Cloudflare — What is DNS](https://www.cloudflare.com/learning/dns/) |
| 1.4 — CDN | [ByteByteGo — How does a CDN work](https://blog.bytebytego.com/p/how-does-cdn-work) · [Cloudflare — What is a CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) |
| 1.5 — Proxies + gateways | [AWS — What is an API gateway](https://aws.amazon.com/api-gateway/) · [MDN — Proxy (glossary)](https://developer.mozilla.org/en-US/docs/Glossary/Proxy) · [Cloudflare — What is a load balancer](https://www.cloudflare.com/learning/performance/what-is-load-balancing/) |
| 1.6 — Consistent hashing | [Wikipedia — Consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing) · [High Scalability](https://highscalability.com/) |

**Week 1 drill:** map every pattern to its cloud service names as you go — LB → AWS ALB/NLB → Azure App Gateway/Front Door; DNS → Route53 → Azure DNS. Gap noted at baseline.

---

## Sessions

### Session 1 — 2026-09-04 — Phase 1.1: Scale of numbers + estimation

**Format:** 3-question quiz (QPS estimation, latency orders of magnitude, storage estimation)

**What landed:**
- Latency ordering correct without prompting (memory < SSD < cross-continent)
- Storage estimation method correct (units × rate × time)

**Gaps found (all vocabulary/arithmetic, not reasoning):**
- Didn't know **DAU** (daily active users), **QPS** (queries/sec), **peak multiplier** (~2–3× average) — the three starting terms of every SD interview
- Latency numbers not yet memorized: memory ~100**ns** → SSD ~100**µs** → cross-continent ~100**ms** (each hop ~1000×; Jeff Dean's table)
- Storage math dropped ~100×: 200M tweets × 280B = 56 GB/day ≈ 20 TB/year (not 480MB)
- "What did you ignore" answer to internalize: **metadata, indexes (2–5×), replication (×3 for durability), media (dominates → PB-scale, not TB)**

**Key formulas to memorize:**
- `QPS = (DAU × actions/user) ÷ 86,400` (~100K sec/day)
- Storage ladder: KB → MB → GB → TB → PB (×1000 each)

**Drill assigned:** redo Q1 math + recite latency ladder from memory.

**Drill result:** QPS math ✅ (10M DAU × 10 actions ≈ 1K QPS via shortcut). Latency ladder ✅ with one label slip (said "RAM" for rung 2 — RAM *is* main memory; rung 2 is SSD). Payoff line learned: "disk is 1000× slower than memory, so we cache; cross-continent is 1000× slower than disk, so we use CDNs."

**Follow-up Q&A:** caching (copy in fast memory, e.g. Redis — deep dive in SD 2.6) and CDN (copies on servers near the user, e.g. Cloudflare — deep dive in SD 1.4). Both framed as the same idea at different distances.

**Status: Phase 1.1 ✅ complete**

---

### Session 2 — 2026-09-06 — Phase 1.2: Client-server & APIs (REST vs gRPC vs GraphQL)

**Format:** Concept walkthrough + 3-question quiz

**What landed:**
- All three choices correct: GraphQL for flexible client data (Q1), gRPC for internal microservices (Q2), SSE for one-way notifications (Q3)
- Q3 reasoning complete — identified unidirectional server-push as the deciding factor over WebSocket

**Gaps found:**
- Q1 (GraphQL): justified with backend details ("two tables") instead of naming the problem being solved — over-fetch/under-fetch. Also missed the tradeoff (GET caching breaks because queries travel in the body)
- Q2 (gRPC): correct call but ignored the explicit "migration risk" half of the question. Missing risks: silent binary misreads from field-number reuse, proto schema coordination across 12 services, loss of curl-style debugging, gRPC-web proxy needed for browser clients
- Teachable moment: user flagged no hands-on gRPC experience — field-number mechanics and `reserved` convention explained (silent misreads in protobuf vs. loud breakage in JSON). Logged as teachable moment, not a gap

**Habit to build:** every API/protocol answer = (1) name the *problem* the choice solves, (2) name the *tradeoff* accepted, (3) address every part of the question asked

**Status: Phase 1.2 ✅ complete**

---

> Coaching protocol and session rules live in [`CLAUDE.md`](../CLAUDE.md) at the repo root.
