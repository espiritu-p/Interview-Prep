# Interview Prep — AI Instructions

Rules for every session in this repo. Read this file at the start of every session
before touching any coaching log or plan file.

---

## Session Start Checklist

Every session, in order:

1. Read `DSA/COACHING.md` — restore battle plan, DSA topic status, last session state
2. Read `System-Design/COACHING.md` — restore last SD session and debrief
3. Read `AI-Engineering/COACHING.md` — restore last AI session and debrief
4. Surface today's plan across all three tracks before doing anything else

The user may be on a different machine with a fresh clone. Never assume prior
in-memory state carries over — the coaching logs are the source of truth.

---

## Standing Coaching Rules

### All tracks
1. **Best interview answer always.** After critiquing any response, close with the
   exact phrasing an interviewer wants to hear. Format: What landed → What was
   wrong/missing → Best interview answer.
2. **Plan checks are cross-track.** Any request to check the plan or today's
   progress must report status across all three tracks — DSA, System Design,
   and AI Engineering.
3. **Clarifying questions welcome mid-session.** Log as a teachable moment, not a gap.
4. **Always ask before proceeding.** After finishing a session or sub-step, present options and wait for the user's go-ahead before starting the next one.
5. **Generic changes apply to all topics.** Any structural update made to one track's files (COACHING.md, PLAN.md, READMEs, protocol sections) must be checked and mirrored across all three tracks — DSA, System Design, and AI Engineering — before committing.

### DSA review rubric (apply to every submitted solution)
1. **Correctness first** — loop bounds, off-by-one, edge cases (empty, single element, all-invalid input)
2. **Python idiom** — snake_case vars, no redundant `else` after `return`, no parens on `while`/`if`
3. **Space/time tradeoffs** — name the variant not written (e.g. O(n) copy vs O(1) in-place)
4. **Talk-aloud check** — restate + edge cases → plan → complexity → variant, unprompted
5. **Workflow** — user pastes solution → review vs rubric → user revises → only then commit/push

### DSA mastery grading scheme
Applied when updating `DSA/LeetCode/PROGRESS.md` topic grades after each session.

| Grade | Label | Criteria |
|-------|-------|----------|
| ⬜ | Not Started | Haven't begun |
| 🔴 | Exposed | Read or attempted; cannot solve independently |
| 🟠 | Familiar | 1–2 easy solved independently; hints needed on medium; miss edge cases |
| 🟡 | Developing | Easy independent, medium with occasional hints; core template known; explanation rough under pressure |
| 🟢 | Proficient | Easy + medium independent in interview time; explains pattern, complexity, tradeoffs; handles most variations |
| 🔵 | Advanced | Easy + medium + hard solved; all major variations known; optimal solutions; can teach it |
| ⭐ | Mastered | Solves any variant cold under interview conditions; explains from first principles; no hints needed |

Update a topic's grade whenever new problems are solved. Be honest — 1 easy problem is 🟠 Familiar, not ⭐ Mastered.

---

## End-of-Session Checklist

Before every commit and push, verify **every `.md` file in the repo** is current.
Full file list — check each one:

| File | What to check |
|------|---------------|
| `README.md` | LeetCode solved count, all track statuses |
| `CLAUDE.md` | Rules up to date; no stale protocol in coaching files |
| `DSA/COACHING.md` | Session log current; battle plan dates correct |
| `DSA/LeetCode/README.md` | Problem list, topic counts |
| `DSA/LeetCode/PROGRESS.md` | Topic status table + problem checklist ticks |
| `DSA/Concepts/README.md` | Index matches files present |
| `DSA/Concepts/sliding-window.md` | Content only; no status to update |
| `DSA/Concepts/bit-manipulation.md` | Content only; no status to update |
| `DSA/Concepts/greedy.md` | Content only; no status to update |
| `DSA/Concepts/dynamic-programming.md` | Content only; no status to update |
| `DSA/Kattis/README.md` | Problem count and list |
| `System-Design/PLAN.md` | Progress tracker session statuses |
| `System-Design/COACHING.md` | Session log current |
| `System-Design/Concepts/README.md` | Session status per concept file |
| `System-Design/Case-Studies/README.md` | Mock session statuses |
| `AI-Engineering/PLAN.md` | Progress tracker session statuses |
| `AI-Engineering/COACHING.md` | Session log current |
| `AI-Engineering/Concepts/README.md` | Session status per concept file |
| `AI-Engineering/Exercises/README.md` | Coding exercise statuses |

New `.md` files added during a session → add them to this list immediately.
Then commit with Conventional Commits format and push to master.

---

## Repo Structure (quick reference)

```
Interview-Prep/
├── CLAUDE.md                        ← you are here
├── README.md                        ← public-facing progress
├── DSA/
│   ├── COACHING.md                  ← session log + battle plan + baseline
│   └── LeetCode/                    ← solutions by topic
├── System-Design/
│   ├── PLAN.md                      ← phase curriculum
│   ├── COACHING.md                  ← session log + debriefs
│   ├── Concepts/                    ← one .md per topic
│   └── Case-Studies/                ← mock design write-ups
└── AI-Engineering/
    ├── PLAN.md                      ← phase curriculum
    ├── COACHING.md                  ← session log + debriefs
    ├── Concepts/                    ← one .md per topic
    └── Exercises/                   ← from-scratch implementations
```
