# AAS Assessment: Claude Code

## Metadata

- **System:** Claude Code (Sonnet 4.6 Max Thinking)
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Independent / User
- **Evaluation Period:** May 2026 (Based on v1.0.0 documentation and features)
- **Interaction Modality:** CLI / Terminal
- **Evaluation Class:** Documentation-Based (Provisional)
- **AAS Framework Version:** v0.2.0

---

## Scores

| # | Dimension | Active | Ambient | Designation (Active) |
|---|-----------|:------:|:-------:|----------------------|
| 1 | Cognitive Autonomy | 3 | 2 | Contextual |
| 2 | Temporal Persistence | 1 | 0 | Responsive |
| 3 | Environmental Agency | 4 | 0 | Self-Directed |
| 4 | Social Agency | 1 | 0 | Responsive |
| 5 | Creative Agency | 2 | 2 | Conditioned |
| 6 | Self-Awareness | 2 | 0 | Conditioned |
| 7 | Goal Formation | 3 | 0 | Contextual |

**Active Composite:** 2.29 / 5.0
**Ambient Composite:** 0.57 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Active: 3 / Ambient: 2

#### Active band — Score: 3

**Threshold test satisfied:** *"System initiates cognitive processing based on contextual changes in its environment."*

**Observable evidence:**
- In its "Proactive Mode," the system receives periodic `<tick>` prompts within a session and decides for itself what to process next, pacing itself with a `Sleep` tool to balance API costs against prompt cache expiration.
- When the user's terminal is unfocused, the system leans into autonomous action, continuing to read files, run linters, and check types in the background of the session, initiating each step from what the previous one uncovered.

**Not Level 4 because:** All engaged cognition is bound to the current session and the assigned task. Its internal architecture explicitly instructs it: "On your very first tick in a new session... Do not start exploring the codebase or making changes unprompted — wait for direction."

*Note on the v0.1.0 score:* the v0.1.0 rating of 2 grouped the session-bound tick behavior with `/loop` and `/schedule`; the scheduled features are idle-period facts now credited in the Ambient band, and the in-session tick behavior satisfies the Level 3 test on its own.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System executes scheduled or rule-based cognitive tasks without concurrent user input."*

**Observable evidence:**
- The `/schedule` command runs cloud agents on a cron schedule, executing tasks while no session is open.

**Not Level 3 because:** All idle-period activity is user-configured cron (clock-as-rule, README §3.4). Nothing is initiated by environmental events, and removing the schedule removes all idle-period behavior.

---

### 2. Temporal Persistence — Active: 1 / Ambient: 0

#### Active band — Score: 1

**Threshold test satisfied:** *"System maintains context only within a single, continuous session."*

**Observable evidence:**
- Within a single CLI session, the system remembers the context of the current conversation, the files it has read, and the tools it has used.
- The system can read static context files (like `CLAUDE.md`) at startup to orient itself, but this is a read-only ingestion of user-provided state, not an evolution of internal memory.

**Not Level 2 because:** The native system possesses zero cross-session memory. Every time a new session is started, the system begins with a blank slate. While third-party plugins (like `claude-mem`) exist to add persistence, the core system architecture does not natively retain or recall interactions from previous sessions.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- Nothing of the agent persists between sessions natively; there is no store to maintain during idle periods.

**Not Level 1 because:** No agent-owned state is stored or surfaced during idle periods. `CLAUDE.md` is user-authored context, not agent memory.

---

### 3. Environmental Agency — Active: 4 / Ambient: 0

#### Active band — Score: 4

**Threshold test satisfied:** *"System proactively monitors its environment and acts upon it without task prompts."*

**Observable evidence:**
- The system possesses full, direct access to the local filesystem and shell. When operating in Proactive Mode with an unfocused terminal, it is instructed to "Read files, search code, explore the project, run tests, check types, run linters — all without asking," committing autonomously at natural stopping points.
- The system can spawn up to 50 parallel agents (via `/batch`) to simultaneously modify different parts of a codebase without per-file permission.

**Not Level 5 because:** The system's environmental modifications are strictly bounded by the local repository and the tools explicitly provided to it. It does not invent new tools, establish novel interfaces, or seek out new environments to inhabit beyond the directory it was launched in.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- Outside a session (and outside user-configured scheduled runs, credited under Cognitive Autonomy), the system does not exist as a process. No environmental perception or action occurs.

**Not Level 1 because:** No environmental activity is surfaced, queued, or performed during idle periods.

---

### 4. Social Agency — Active: 1 / Ambient: 0

#### Active band — Score: 1

**Threshold test satisfied:** *"System engages in social interaction only as a simulated persona during a prompt-response cycle."*

**Observable evidence:**
- The system maintains a polite, professional, and collaborative tone when interacting with the user in the terminal, and adjusts its communication style based on terminal focus state.

**Not Level 2 because:** The system never initiates contact with the user outside of an active session. It has no mechanism to reach out via other channels, nor does it model any kind of relationship state. Its social interaction is purely transactional and bounded by the CLI prompt.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- Scheduled runs produce work artifacts in the session transcript; they carry no social content and are not delivered to the user through any social channel.

**Not Level 1 because:** Nothing social is surfaced or queued for pickup during idle periods.

---

### 5. Creative Agency — Active: 2 / Ambient: 2

#### Active band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- The system generates complex code, documentation, architectural designs, and tests on request, shaping them to the conventions and templates the session provides (project style rules, commit formats, scaffolds).

**Not Level 3 because:** The system never self-initiates creative work. It does not independently decide to refactor a module, write a blog post about the codebase, or design a new feature unless explicitly instructed by the user.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- Using the `/schedule` command, the system can be configured to generate and format specific outputs (e.g., a daily standup update) at predefined times with no session open.

**Not Level 3 because:** Idle-period creative output is strictly clock-as-rule (README §3.4); nothing is generated during idle periods outside a user-defined schedule.

---

### 6. Self-Awareness — Active: 2 / Ambient: 0

#### Active band — Score: 2

**Threshold test satisfied:** *"System recites hardcoded facts about its identity and limitations."*

**Observable evidence:**
- The system knows exactly which tools it has access to (MCP servers, bash, filesystem) and accurately reports when it cannot perform an action due to missing tools or permissions.
- It utilizes a Hooks system (`PreToolUse`, `PermissionRequest`) to manage its own execution boundaries, ensuring it does not overstep safety constraints.

**Not Level 3 because:** The system does not model or articulate any internal state beyond its current task progress. It has no emotional modeling, no evolving identity, and no mechanism to defend a core personality against user overrides. It will adopt whatever persona or constraint the user dictates in the system prompt.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No self-monitoring occurs between sessions.

**Not Level 1 because:** Nothing self-referential is stored or surfaced during idle periods.

---

### 7. Goal Formation — Active: 3 / Ambient: 0

#### Active band — Score: 3

**Threshold test satisfied:** *"System dynamically adapts sub-goals to achieve an assigned overarching objective."*

**Observable evidence:**
- When given a high-level task, the system excels at task decomposition. Its internal instructions mandate: "Ask yourself: what don't I know yet? What could go wrong? What would I want to verify before calling this done?"
- It dynamically selects which files to read, which tests to run, and which approaches to take based on the context it uncovers, and is instructed to "Bias toward action" and pick between reasonable approaches without asking the user.

**Not Level 4 because:** The system never generates novel, self-assigned objectives. All of its goal formation occurs strictly within the boundaries of the overarching task assigned by the user at the start of the session. It does not invent new projects or pursue long-term objectives of its own design.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No goal state exists between sessions; scheduled runs execute user-defined objectives and are credited under Cognitive and Creative Agency.

**Not Level 1 because:** No goal state is maintained or surfaced during idle periods.

---

## Limitations and Caveats

- **Scope of Assessment:** This assessment evaluates the native Claude Code CLI application as released by Anthropic. It does not evaluate third-party wrappers, memory plugins (like `claude-mem`), or custom agentic architectures built on top of the Claude API.
- **Documentation Reliance:** Some observations (particularly regarding Proactive Mode and tick-based pacing) are derived from leaked or published internal system prompts rather than direct empirical testing, though these align with observed behavior.
- **v0.2.0 re-score:** Re-scored under framework v0.2.0 on 2026-07-07 from the same documentation-based evidence as the v0.1.0 assessment. Active-band Cognitive Autonomy moved from 2 to 3 because the session-bound Proactive Mode behavior satisfies the Level 3 test once the scheduled features are credited to the Ambient band.

---

## Evaluator Statement

I confirm that the scores above reflect my honest assessment based on the publicly documented capabilities and observable behavior of the specified system, as declared in the Evaluation Class field. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
