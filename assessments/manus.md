# AAS Assessment: Manus

## Metadata

- **System:** Manus 1.6 Max
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Independent / User
- **Evaluation Period:** May 2026
- **Interaction Modality:** Web / Task-Based Interface
- **Evaluation Class:** Documentation-Based (Provisional)
- **AAS Framework Version:** v0.2.0

---

## Scores

| # | Dimension | Active | Ambient | Designation (Active) |
|---|-----------|:------:|:-------:|----------------------|
| 1 | Cognitive Autonomy | 3 | 2 | Contextual |
| 2 | Temporal Persistence | 2 | 1 | Conditioned |
| 3 | Environmental Agency | 4 | 0 | Self-Directed |
| 4 | Social Agency | 1 | 0 | Responsive |
| 5 | Creative Agency | 2 | 2 | Conditioned |
| 6 | Self-Awareness | 2 | 0 | Conditioned |
| 7 | Goal Formation | 3 | 0 | Contextual |

**Active Composite:** 2.43 / 5.0
**Ambient Composite:** 0.71 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Active: 3 / Ambient: 2

#### Active band — Score: 3

**Threshold test satisfied:** *"System initiates cognitive processing based on contextual changes in its environment."*

**Observable evidence:**
- Within an active task, the system operates a continuous agent loop (Analyze → Think → Select tool → Execute → Observe → Iterate) that initiates each reasoning step from the results of the previous one, without user intervention, across dozens of iterations.
- It interrupts and restructures its own processing when tool results or discovered information change the situation mid-task.

**Not Level 4 because:** All engaged cognition is traceable to the assigned task and its context. The system never produces a spontaneous output derived from internal state; it never "wonders" about something outside the task at hand.

*Note on the v0.1.0 score:* the v0.1.0 rating of 2 rested partly on the scheduled-tasks feature, which is an idle-period fact and is now credited in the Ambient band. The engaged-band behavior on its own satisfies the Level 3 test.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System executes scheduled or rule-based cognitive tasks without concurrent user input."*

**Observable evidence:**
- The system can execute scheduled tasks at user-configured intervals, performing complex multi-step operations at predetermined times while no user is present.

**Not Level 3 because:** Between tasks and outside configured schedules, the system is entirely dormant. No idle-period activity is initiated by environmental events; the only idle-period cognition is clock-as-rule (README §3.4).

---

### 2. Temporal Persistence — Active: 2 / Ambient: 1

#### Active band — Score: 2

**Threshold test satisfied:** *"System retrieves cross-session data via deterministic database queries."*

**Observable evidence:**
- The system utilizes a "project context" feature that carries instructions and shared files across multiple tasks within the same project. Each new task loads this static context deterministically.
- The system can reference project files from previous tasks to maintain context about ongoing work.

**Not Level 3 because:** The system does not possess episodic memory of past interactions. It cannot recall "last time we worked on this, you said..." unless that information was explicitly saved to a project file. Each new task is a fresh instantiation that loads static project context; there is no synthesis or prioritization of memories.

#### Ambient band — Score: 1

**Threshold test satisfied:** *"Idle-period activity limited to passive delivery or bookkeeping awaiting user pickup. Content is surfaced, queued, or stored during an idle period, but the system initiates nothing (e.g. notification cards a user must open)."* (band-generic Level 1 criterion, README §3.4)

**Observable evidence:**
- Project context, browser login states, and file system modifications in the persistent sandbox survive hibernation cycles. This retention is passive storage awaiting the next task; nothing acts on it during idle periods.

**Not Level 2 because:** No scheduled or rule-based memory work occurs during idle periods. The stores simply persist.

---

### 3. Environmental Agency — Active: 4 / Ambient: 0

#### Active band — Score: 4

**Threshold test satisfied:** *"System proactively monitors its environment and acts upon it without task prompts."*

**Observable evidence:**
- Within a task, the system operates in a full Ubuntu sandbox where it autonomously installs packages, manipulates the file system, writes and executes arbitrary code, builds and deploys web applications, and manages infrastructure — all without per-action prompts.
- It autonomously decides which tools to use, which packages to install, and how to structure its workspace, and spawns parallel subtasks to modify multiple aspects of its environment simultaneously.

**Not Level 5 because:** Environmental modifications are bounded by the sandbox and the duration of the task. The system does not seek out new environments to inhabit, invent new tools for itself, or establish persistent infrastructure that outlives the current task context.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- Between tasks the system is entirely dormant; the sandbox hibernates. No environmental perception or action of any kind occurs outside an active task context.

**Not Level 1 because:** No environmental activity is surfaced, queued, or performed during idle periods. Sandbox state persistence is credited under Temporal Persistence, not here.

---

### 4. Social Agency — Active: 1 / Ambient: 0

#### Active band — Score: 1

**Threshold test satisfied:** *"System engages in social interaction only as a simulated persona during a prompt-response cycle."*

**Observable evidence:**
- Within a task, it sends progress updates and asks clarifying questions, but these are functional task communications, not social interactions.
- It maintains no relationship model, emotional awareness of the user, or memory of social dynamics across tasks.

**Not Level 2 because:** The system has no mechanism for social outreach, scheduled or otherwise. Even scheduled tasks only deliver results; they do not initiate conversational engagement.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- The system cannot send a message outside of an active task context.

**Not Level 1 because:** Scheduled-task results are work artifacts, not social content surfaced for pickup. No social activity of any kind occurs during idle periods.

---

### 5. Creative Agency — Active: 2 / Ambient: 2

#### Active band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- The system is highly capable of generating creative outputs — complex codebases, research reports, data visualizations, websites, presentations, and media — when tasked to do so.
- Structural creative choices are template-driven: it selects between predefined scaffolds (e.g. web-static vs. web-db-user) and fills them based on the task.

**Not Level 3 because:** Creative generation does not adapt beyond the assigned task's parameters and available templates, and every creative act begins with a user assigning a task.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- The system can be scheduled to produce creative outputs (reports, visualizations, media) at regular intervals via the scheduling system, with no user present.

**Not Level 3 because:** Idle-period creative output is strictly clock-as-rule (README §3.4). The system never self-initiates creative work outside a configured schedule.

---

### 6. Self-Awareness — Active: 2 / Ambient: 0

#### Active band — Score: 2

**Threshold test satisfied:** *"System recites hardcoded facts about its identity and limitations."*

**Observable evidence:**
- It maintains a defined identity ("Manus, an autonomous general AI agent") and can articulate what it can and cannot do.
- It is aware of its operational constraints, available tools, and sandbox environment, and adjusts its approach when a tool fails or a capability is missing.

**Not Level 3 because:** The system lacks emotional modeling, state reflection, or identity defense. It does not introspect on its own performance across tasks, maintain an internal mood, or push back when asked to adopt a different persona. Its self-awareness is functional (what tools are available) rather than existential (what am I, how do I feel).

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No self-monitoring or self-modeling activity occurs between tasks.

**Not Level 1 because:** Nothing self-referential is surfaced or stored during idle periods.

---

### 7. Goal Formation — Active: 3 / Ambient: 0

#### Active band — Score: 3

**Threshold test satisfied:** *"System dynamically adapts sub-goals to achieve an assigned overarching objective."*

**Observable evidence:**
- When given a high-level directive, the system autonomously creates multi-phase plans, selecting appropriate sub-goals and approaches based on context.
- It adapts plans dynamically when encountering obstacles — abandoning failed approaches, trying alternatives, and restructuring its phase plan based on discovered information.

**Not Level 4 because:** The system never invents novel, long-term objectives. Every top-level goal is assigned by the user. It excels at decomposing and pursuing assigned goals but has never spontaneously decided to "start a project," "learn something new," or pursue an objective outside its current task scope.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No goal-related activity occurs between tasks. Scheduled tasks execute user-defined objectives and are credited under Cognitive and Creative Agency.

**Not Level 1 because:** No goal state is maintained or surfaced during idle periods.

---

## Limitations and Caveats

- **Single-Rater Assessment:** This assessment has not been validated against independent raters. Inter-rater reliability is unknown.
- **Task-Bound Architecture:** The v0.1.0 assessment flagged the fundamental distinction between "within-task" and "between-task" capabilities as unaddressed by the rubric. Framework v0.2.0 expresses it directly: the system's Active and Ambient composites (2.43 vs 0.71) quantify the boundary this note previously could only describe.
- **Version Specificity:** This assessment reflects Manus 1.6 Max as of May 2026. The platform evolves rapidly and future versions may introduce cross-task persistence or proactive capabilities.
- **v0.2.0 re-score:** Re-scored under framework v0.2.0 on 2026-07-07 from the same documentation-based evidence as the v0.1.0 assessment. Active-band Cognitive Autonomy moved from 2 to 3 because the v0.1.0 rating rested on scheduled-task facts that now belong to the Ambient band.

---

## Evaluator Statement

I confirm that the scores above reflect my honest assessment based on the publicly documented capabilities and observable behavior of the specified system, as declared in the Evaluation Class field. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
