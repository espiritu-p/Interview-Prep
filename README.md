<div align="center">

# Interview Prep

Python interview prep + DSA + AI engineering + system design + React — working toward interview-ready by **October 1, 2026** — DSA backlog reset to **November 15, 2026**.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-33%20Solved-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/)
[![Kattis](https://img.shields.io/badge/Kattis-144%20Solved-1F8ACB?style=flat-square)](https://open.kattis.com/)
[![Last Commit](https://img.shields.io/github/last-commit/espiritu-p/Interview-Prep?style=flat-square&color=brightgreen)](https://github.com/espiritu-p/Interview-Prep/commits/master)

</div>

---

## Tracks

Five parallel tracks — **DSA active solo until Nov 15** (backlog reset 2026-10-26); other four tracks paused until the DSA backlog clears.

### DSA — Algorithms & Data Structures

Daily LeetCode and Kattis practice. Solutions in Python with inline explanations, organized by topic following the NeetCode150 progression.

→ [`DSA/`](./DSA/) · Progress: [`DSA/LeetCode/PROGRESS.md`](./DSA/LeetCode/PROGRESS.md) · Plan: [`DSA/COACHING.md`](./DSA/COACHING.md)

### System Design

Six-phase coaching program: foundations → storage → scalability → reliability/ops → AWS/Azure service mapping → mock case studies. Sessions follow real interview format — requirements, estimation, design, deep-dives, tradeoffs.

→ [`System-Design/`](./System-Design/) · Plan: [`System-Design/PLAN.md`](./System-Design/PLAN.md) · Log: [`System-Design/COACHING.md`](./System-Design/COACHING.md)

### AI Engineering

Seven-phase coaching program: LLM internals → RAG → agents → evals → fine-tuning → inference → safety. Each phase ends with a from-scratch coding exercise.

→ [`AI-Engineering/`](./AI-Engineering/) · Plan: [`AI-Engineering/PLAN.md`](./AI-Engineering/PLAN.md) · Log: [`AI-Engineering/COACHING.md`](./AI-Engineering/COACHING.md)

### React

Four-phase frontend interview preparation: React's rendering model → hooks and state → performance → production frontend architecture.

→ [`React/`](./React/) · Plan: [`React/PLAN.md`](./React/PLAN.md) · Log: [`React/COACHING.md`](./React/COACHING.md)

### Python

Four-phase Python interview preparation: language semantics → async/concurrency → interview mechanics → NumPy/pandas.

→ [`Python/`](./Python/) · Plan: [`Python/PLAN.md`](./Python/PLAN.md) · Log: [`Python/COACHING.md`](./Python/COACHING.md)

---

## Structure

```
Interview-Prep/
├── DSA/
│   ├── COACHING.md              session log + September battle plan
│   ├── LeetCode/
│   │   ├── PROGRESS.md          phased checklist with per-problem tick boxes
│   │   └── <Topic>/             solutions grouped by topic
│   ├── Kattis/
│   │   └── <Type>/              solutions grouped by problem type
│   └── Concepts/                paradigm notes + Python interview question bank
│
├── System-Design/
│   ├── PLAN.md                  six-phase curriculum with session map
│   ├── COACHING.md              session log and debrief notes
│   ├── Concepts/                one .md per topic, session-by-session
│   └── Case-Studies/            full mock design write-ups
│
├── AI-Engineering/
    ├── PLAN.md                  seven-phase curriculum with session map
    ├── COACHING.md              session log and debrief notes
    ├── Concepts/                one .md per topic, session-by-session
    └── Exercises/               from-scratch implementations per phase

└── React/
    ├── PLAN.md                  four-phase curriculum with session map
    ├── COACHING.md              session log and pre-session references
    └── Concepts/                one .md per topic, session-by-session

└── Python/
    ├── PLAN.md                  four-phase curriculum with session map
    ├── COACHING.md              session log and pre-session references
    └── Concepts/                one .md per topic, session-by-session

└── CS-ROADMAP.md              ← roadmap.sh CS fundamentals crosswalk + resume backlog
```

---

## Track Status — Oct 26 Reset

DSA runs alone until **Nov 15** ([Backlog Plan](./DSA/COACHING.md)); the other tracks resume after the backlog clears, then get re-dated.

| Track | Scope | Status |
|-------|-------|--------|
| DSA | 48-problem September backlog, re-dated Oct 26 → Nov 15 | 🟡 Resumed Oct 26 |
| System Design | Phases 1–4 + 3 mock case studies | ⏸ Paused — 1.1–1.3 complete |
| AI Engineering | Phases 1–4 + per-phase exercises | ⏸ Paused — 1.1–1.2 complete; `attention_from_scratch.py` in progress since Sept 7 |
| React | Phases 1–4 | ⏸ Paused — not started |
| Python | Phases 1–4 + DSA warm-up drills | ⏸ Paused — Q1.1/Q2.1 pending in drill log |

Detailed battle plans:
- DSA: [`DSA/COACHING.md`](./DSA/COACHING.md)
- System Design: [`System-Design/PLAN.md`](./System-Design/PLAN.md)
- AI Engineering: [`AI-Engineering/PLAN.md`](./AI-Engineering/PLAN.md)
- React: [`React/PLAN.md`](./React/PLAN.md)
- Python: [`Python/PLAN.md`](./Python/PLAN.md)
- CS fundamentals: [`CS-ROADMAP.md`](./CS-ROADMAP.md)

---

## Commands

| Command | Action |
|---------|--------|
| `DSA: next` | Get next DSA problem assignment |
| `SD: Phase X.Y` | Start a System Design concept session |
| `SD: Case 6.X` | Start a mock design interview |
| `AI: Phase X.Y` | Start an AI Engineering concept session |
| `React: Phase X.Y` | Start a React concept session |
| `Python: Phase X.Y` | Start a Python concept session |
