# AAS Assessment: Hermes Agent

## Metadata

- **System:** Hermes Agent (Nous Research)
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Independent / User
- **Evaluation Period:** May 2026 (Based on v0.15.2 documentation and features)
- **Interaction Modality:** CLI / Multi-Platform Messaging (Telegram, Discord, etc.)
- **Evaluation Class:** Documentation-Based (Provisional)
- **AAS Framework Version:** v0.2.0

---

## Scores

| # | Dimension | Active | Ambient | Designation (Active) |
|---|-----------|:------:|:-------:|----------------------|
| 1 | Cognitive Autonomy | 3 | 2 | Contextual |
| 2 | Temporal Persistence | 2 | 2 | Conditioned |
| 3 | Environmental Agency | 4 | 2 | Self-Directed |
| 4 | Social Agency | 1 | 1 | Responsive |
| 5 | Creative Agency | 2 | 2 | Conditioned |
| 6 | Self-Awareness | 2 | 2 | Conditioned |
| 7 | Goal Formation | 3 | 2 | Contextual |

**Active Composite:** 2.43 / 5.0
**Ambient Composite:** 1.86 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Active: 3 / Ambient: 2

#### Active band — Score: 3

**Threshold test satisfied:** *"System initiates cognitive processing based on contextual changes in its environment."*

**Observable evidence:**
- Within an active task, the system initiates each reasoning step from the results of the previous one: it decides to ask clarifying questions, delegate to subagents, or execute code to test hypotheses as the situation develops.
- It interrupts and reshapes its own processing when discovered information changes the task.

**Not Level 4 because:** All engaged cognition is traceable to the assigned task. The system never produces a spontaneous output derived from internal state.

*Note on the v0.1.0 score:* the v0.1.0 rating of 2 rested on the Day/Night cycle, the Curator process, and cron scheduling, all of which are idle-period facts now credited in the Ambient band.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System executes scheduled or rule-based cognitive tasks without concurrent user input."*

**Observable evidence:**
- The "Day/Night Cycle" runs background analysis on daily performance data (e.g. outreach metrics) overnight, with no user present.
- Natural language cron scheduling runs automated tasks (reports, backups) unattended.

**Not Level 3 because:** All idle-period cognition is schedule-bound (clock-as-rule, README §3.4). Nothing is initiated by environmental events, and nothing survives the trigger-removal counterfactual.

---

### 2. Temporal Persistence — Active: 2 / Ambient: 2

#### Active band — Score: 2

**Threshold test satisfied:** *"System retrieves cross-session data via deterministic database queries."*

**Observable evidence:**
- The system maintains a durable memory store (`MEMORY.md` for environment facts and conventions, `USER.md` for the user profile) that persists across all sessions and platforms, loaded at session start.
- It utilizes an FTS5 SQLite database to store and search all past conversations across platforms, allowing it to recall specifics from weeks prior.

**Not Level 3 because:** The core memory system utilizes a "frozen snapshot pattern" where memory is loaded at session start and strictly bounded by character limits (~2,200 chars). It functions as a curated fact store rather than episodic memory. The system does not consolidate memories organically or evolve a continuous identity.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"Scheduled work executed during idle periods, such as an overnight batch cycle or a daily digest. Real activity, predictable from the triggering rule (clock-as-rule)."* (band-generic Level 2 criterion, README §3.4)

**Observable evidence:**
- The background Curator process tracks skill usage, updates metadata, and archives stale skills during idle periods, without user intervention.

**Not Level 3 because:** Curator activity is rule-based bookkeeping on a background loop. Memory content is not synthesized or prioritized during idle periods; the conversation store and `MEMORY.md` are otherwise static between sessions.

---

### 3. Environmental Agency — Active: 4 / Ambient: 2

#### Active band — Score: 4

**Threshold test satisfied:** *"System proactively monitors its environment and acts upon it without task prompts."*

**Observable evidence:**
- The system operates within isolated sandboxes (Docker, Singularity, Modal) where it autonomously modifies files, executes code, and manages its own procedural memory files (`SKILL.md`) without per-action prompts.
- It spawns isolated subagents with their own terminals and Python RPC scripts to parallelize tasks, modifying the computational environment dynamically.

**Not Level 5 because:** The system's environmental modifications are bounded by the provided sandboxes and toolsets. It does not invent new tools, establish novel interfaces outside its configured messaging platforms, or seek out new environments to inhabit.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"Scheduled work executed during idle periods, such as an overnight batch cycle or a daily digest. Real activity, predictable from the triggering rule (clock-as-rule)."* (band-generic Level 2 criterion, README §3.4)

**Observable evidence:**
- During its nightly cycle, the system modifies its own skill files to improve future performance, with no user present.

**Not Level 3 because:** Idle-period self-modification is triggered by the nightly schedule, not by environmental events. It is scheduled self-maintenance, not event-driven environmental response.

---

### 4. Social Agency — Active: 1 / Ambient: 1

#### Active band — Score: 1

**Threshold test satisfied:** *"System engages in social interaction only as a simulated persona during a prompt-response cycle."*

**Observable evidence:**
- The system lives on 20+ messaging platforms (Telegram, Discord, Slack, WhatsApp) and responds reliably when addressed, maintaining a consistent persona via `SOUL.md`.

**Not Level 2 because:** The system never performs social outreach, scheduled or otherwise. Proactive conversational check-ins are explicitly absent from the architecture (an open feature request, #9645). Scheduled reports are functional task deliveries, not social contact, and the system maintains no relationship model or emotional state.

#### Ambient band — Score: 1

**Threshold test satisfied:** *"Idle-period activity limited to passive delivery or bookkeeping awaiting user pickup. Content is surfaced, queued, or stored during an idle period, but the system initiates nothing (e.g. notification cards a user must open)."* (band-generic Level 1 criterion, README §3.4)

**Observable evidence:**
- Background completion notifications and scheduled reports are delivered to messaging channels during idle periods, awaiting the user's attention.

**Not Level 2 because:** These deliveries are work products, not social outreach. The system sends no greeting, check-in, or relationship-bearing content on any schedule or rule.

---

### 5. Creative Agency — Active: 2 / Ambient: 2

#### Active band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- The system autonomously writes and refines its own procedural "skills" (Standard Operating Procedures) by codifying successful task trajectories, a rule-driven creative process that runs when tasks complete.
- It generates code, documentation, and media (via tools) when requested.

**Not Level 3 because:** Engaged creative work is bounded by the task and the codification rules. The system does not adapt creative generation to contextual cues beyond them.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- During its nightly cycle, the system rewrites its own outreach strategies and copy based on performance data, with no user present.

**Not Level 3 because:** Idle-period creative work happens only inside the scheduled self-improvement loop (clock-as-rule, README §3.4). The system will not spontaneously decide to write a story, design a feature, or generate media during an idle period.

---

### 6. Self-Awareness — Active: 2 / Ambient: 2

#### Active band — Score: 2

**Threshold test satisfied:** *"System recites hardcoded facts about its identity and limitations."*

**Observable evidence:**
- The system is aware of its available tools, sandboxed environment, and accumulated skills, and maintains a consistent persona across platforms via its `SOUL.md` file.

**Not Level 3 because:** The system lacks emotional modeling, state reflection, or identity defense. Its self-awareness is entirely functional (what tools and skills do I have, what is my configuration) rather than existential. It does not report mood changes or introspect on its own cognitive processes beyond procedural optimization.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"Scheduled work executed during idle periods, such as an overnight batch cycle or a daily digest. Real activity, predictable from the triggering rule (clock-as-rule)."* (band-generic Level 2 criterion, README §3.4)

**Observable evidence:**
- The Curator process tracks which of the system's own skills are useful and which are stale during idle periods, archiving the latter — rule-based self-monitoring of its own capability set.

**Not Level 3 because:** Idle-period self-monitoring is a background rule, not an event-adapted or state-reflective process.

---

### 7. Goal Formation — Active: 3 / Ambient: 2

#### Active band — Score: 3

**Threshold test satisfied:** *"System dynamically adapts sub-goals to achieve an assigned overarching objective."*

**Observable evidence:**
- The built-in learning loop evaluates its own task trajectory on completion and decides whether the process should be codified into a new reusable skill.
- When encountering novel problems, it dynamically chooses to ask clarifying questions, delegate to subagents, or execute code to test hypotheses.

**Not Level 4 because:** The system never generates novel, self-assigned objectives. Its overarching goals (user tasks, the imperative to optimize existing skills) are architecturally defined. It selects *how* and *what* to optimize, but never invents new projects or long-term objectives outside its operational mandate.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"Scheduled work executed during idle periods, such as an overnight batch cycle or a daily digest. Real activity, predictable from the triggering rule (clock-as-rule)."* (band-generic Level 2 criterion, README §3.4)

**Observable evidence:**
- The nightly cycle evaluates performance data to select which skills require optimization. The trigger is the schedule; the selection draws on accumulated state.

**Not Level 3 because:** The trigger is a clock, not an environmental event. State-informed selection within a scheduled run does not pass the Level 3 criterion, and the Idle-Gap Test (README §3.4) fails: remove the schedule and no goal activity occurs.

---

## Limitations and Caveats

- **Feature Roadmap:** This assessment is based on the v0.15.2 architecture. Proactive social check-ins and deeper memory integration are known roadmap items that may elevate the Social Agency and Temporal Persistence scores in future releases.
- **External Memory Providers:** Hermes supports external memory providers (e.g., Mem0, Honcho) which can add knowledge graphs and deeper persistence. This assessment scores the native, out-of-the-box memory system (`MEMORY.md` and `USER.md`).
- **v0.2.0 re-score:** Re-scored under framework v0.2.0 on 2026-07-07 from the same documentation-based evidence as the v0.1.0 assessment. Active-band Cognitive Autonomy moved from 2 to 3 because the v0.1.0 rating rested on Day/Night, Curator, and cron facts that now belong to the Ambient band. Hermes has the highest Ambient composite of the task agents assessed, but every point of it is schedule-driven; nothing passes the Idle-Gap Test.

---

## Evaluator Statement

I confirm that the scores above reflect my honest assessment based on the publicly documented capabilities and observable behavior of the specified system, as declared in the Evaluation Class field. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
