# System Design Interview Plan

Target: interview-ready by **October 1, 2026**  
Background: SRE @ P&G (3,000+ servers, Prometheus/Grafana/Splunk, Puppet, Kubernetes), Samsung (cloud orchestration UI, telecom CNF/VNF topology)

---

## Your Edge

Most candidates learn system design from theory. You've **operated** production systems at scale:
- Engineered monitoring across 3,000+ servers → you know what breaks at scale
- Owned change deployments across 100+ global sites → you know rollout strategies
- Built SLO/error budget discipline → you can reason about reliability quantitatively
- Kubernetes + Jenkins CI/CD at Samsung → you understand container orchestration

Frame your answers from the operator's perspective. That's differentiating.

---

## How System Design Interviews Work

You'll be given an open-ended prompt: *"Design Twitter"* or *"Design a URL shortener"*. The interviewer wants to see:

1. **Requirements gathering** — ask before designing; scope clarifies the whole problem
2. **Capacity estimation** — rough math: QPS, storage, bandwidth
3. **High-level architecture** — components, data flow, interfaces between them
4. **Deep-dives** — the interviewer will pick 1–2 areas to go deep: DB schema, caching strategy, consistency model, failure handling
5. **Tradeoffs** — every design decision is a tradeoff; name them explicitly

You will never be judged on "correct answer" — you're judged on structured thinking and tradeoff awareness.

---

## Phase Map

```
Phase 1 — Foundations          (Week 1)     Core primitives every design uses
Phase 2 — Storage & Databases  (Week 1–2)   SQL, NoSQL, caching, search
Phase 3 — Scalability Patterns (Week 2–3)   Load balancing, sharding, CDN, queues
Phase 4 — Reliability & Ops    (Week 3)     SLOs, circuit breakers, observability
Phase 5 — Cloud (AWS/Azure)    (Week 3–4)   Managed services mapped to design patterns
Phase 6 — Case Studies         (Week 4)     6 full mock designs end-to-end
```

---

## Phase 1 — Foundations

The primitives. Every single design question touches these.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| ~~1.1~~ ✅ | Scale of numbers | Latency numbers every engineer should know; QPS estimation; storage units |
| ~~1.2~~ ✅ | Client-server & APIs | REST vs. GraphQL vs. gRPC; HTTP/2; long-polling vs. SSE vs. WebSocket |
| 1.3 | DNS & load balancing | DNS resolution, L4 vs. L7 load balancers, health checks, sticky sessions |
| 1.4 | CDN | Edge caching, push vs. pull CDN, cache invalidation, origin shield |
| 1.5 | Proxies & gateways | Forward/reverse proxy, API gateway, rate limiting, auth at the edge |
| 1.6 | Hashing & consistent hashing | Mod-N hashing failure, consistent hashing ring, virtual nodes |

---

## Phase 2 — Storage & Databases

The most-probed area in system design. You need to know *when to use what* and *why*.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 2.1 | Relational DBs | ACID, indexes, query planning, connection pooling, read replicas |
| 2.2 | NoSQL types | Key-value, document, wide-column, graph — use cases, tradeoffs |
| 2.3 | CAP theorem | Consistency vs. availability under partition; CP vs. AP systems |
| 2.4 | Replication | Leader-follower, multi-leader, leaderless; replication lag |
| 2.5 | Sharding | Horizontal sharding, shard key selection, hotspot problem, resharding |
| 2.6 | Caching | Cache-aside, write-through, write-behind; eviction policies; Redis vs. Memcached |
| 2.7 | Search & time-series | Elasticsearch internals, inverted index; InfluxDB / Prometheus for metrics |

**AWS map:** RDS, DynamoDB, ElastiCache, OpenSearch, Timestream  
**Azure map:** Azure SQL, Cosmos DB, Azure Cache for Redis, Azure AI Search

---

## Phase 3 — Scalability Patterns

How systems stay fast and available as load grows.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 3.1 | Message queues | Async decoupling, at-least-once vs. exactly-once, backpressure, DLQ |
| 3.2 | Event streaming | Kafka architecture — topics, partitions, consumer groups, offset management |
| 3.3 | Rate limiting | Token bucket, leaky bucket, sliding window log; Redis-backed distributed limiting |
| 3.4 | Idempotency | Why it matters, idempotency keys, deduplication at the storage layer |
| 3.5 | Distributed transactions | Two-phase commit, saga pattern, outbox pattern |
| 3.6 | Service discovery & coordination | Consul, ZooKeeper, etcd; leader election; distributed locks |

**AWS map:** SQS, SNS, MSK (Kafka), EventBridge  
**Azure map:** Service Bus, Event Hub, Event Grid

---

## Phase 4 — Reliability & Ops

Your SRE background makes this your strongest phase — articulate it clearly.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 4.1 | SLOs & error budgets | SLI → SLO → SLA hierarchy; error budget math; burn rate alerts |
| 4.2 | Circuit breakers & bulkheads | Closed/open/half-open states; failure isolation; Hystrix / Resilience4j |
| 4.3 | Retries & timeouts | Exponential backoff, jitter, timeout budgets, cascading failure |
| 4.4 | Observability | Metrics, logs, traces — the three pillars; OpenTelemetry; structured logging |
| 4.5 | Deployment strategies | Blue-green, canary, feature flags, rolling; rollback triggers |
| 4.6 | Disaster recovery | RTO vs. RPO; active-active vs. active-passive; chaos engineering |

**AWS map:** CloudWatch, X-Ray, CloudTrail, Route53 health checks  
**Azure map:** Azure Monitor, Application Insights, Azure Service Health

---

## Phase 5 — Cloud (AWS / Azure)

Pattern-to-service mapping. Interviews rarely ask "name an AWS service" — they ask you to design something; you use your cloud knowledge to justify choices.

| Session | Topic | AWS | Azure |
|---------|-------|-----|-------|
| 5.1 | Compute | EC2, ECS, EKS, Lambda | VMs, AKS, Azure Functions |
| 5.2 | Storage | S3, EBS, EFS, Glacier | Blob Storage, Azure Files, Archive |
| 5.3 | Networking | VPC, Route53, CloudFront, ALB/NLB | VNet, Azure DNS, Front Door, App Gateway |
| 5.4 | Data & analytics | Redshift, Athena, Glue, Kinesis | Synapse, Data Factory, Stream Analytics |
| 5.5 | AI/ML services | Bedrock, SageMaker, Rekognition | Azure OpenAI, Azure ML, Cognitive Services |
| 5.6 | Security & IAM | IAM, KMS, Secrets Manager, WAF | Entra ID, Key Vault, Defender, Azure WAF |
| 5.7 | Well-Architected | Operational excellence, security, reliability, performance, cost | Azure Well-Architected Framework |

---

## Phase 6 — Case Studies (Mock Designs)

Full end-to-end mock design sessions. Each one: requirements → estimation → design → deep-dive → tradeoffs. ~45 minutes each, same format as a real interview.

| # | Problem | Core Challenges |
|---|---------|----------------|
| 6.1 | URL Shortener | Hash collision, redirect latency, analytics |
| 6.2 | Rate Limiter | Distributed state, sliding window, Redis coordination |
| 6.3 | Notification Service | Fan-out at scale, delivery guarantees, multi-channel |
| 6.4 | Web Crawler | Politeness, deduplication, distributed frontier |
| 6.5 | Design YouTube | Video encoding pipeline, CDN strategy, view count at scale |
| 6.6 | Design an AI Inference Service | Model serving, autoscaling, latency SLOs, cost-per-token |

Case Study 6.6 is specifically designed for your AI engineering angle — ties both tracks together.

---

## Progress Tracker

| Phase | Sessions | Status |
|-------|----------|--------|
| 1 — Foundations | ✅ 1.1 · 1.2 · 🔜 1.3 · 1.4 · 1.5 · 1.6 | 🟡 In progress |
| 2 — Storage & Databases | 2.1 · 2.2 · 2.3 · 2.4 · 2.5 · 2.6 · 2.7 | ⬜ Not started |
| 3 — Scalability Patterns | 3.1 · 3.2 · 3.3 · 3.4 · 3.5 · 3.6 | ⬜ Not started |
| 4 — Reliability & Ops | 4.1 · 4.2 · 4.3 · 4.4 · 4.5 · 4.6 | ⬜ Not started |
| 5 — Cloud (AWS/Azure) | 5.1 · 5.2 · 5.3 · 5.4 · 5.5 · 5.6 · 5.7 | ⬜ Not started |
| 6 — Case Studies | 6.1 · 6.2 · 6.3 · 6.4 · 6.5 · 6.6 | ⬜ Not started |

---

## How Sessions Work

1. I explain the concept or give you the design prompt.
2. For concepts: I ask probing questions as an interviewer would.
3. For case studies: you drive — I interrupt with real interviewer follow-ups.
4. Debrief: what you nailed, what was vague, what was missing.

Start a session: **`SD: Phase X.Y`** (e.g., `SD: Phase 1.1`)  
Start a mock design: **`SD: Case 6.1`**
