# AAS Assessment: Claude Code

## Metadata

- **System:** Claude Code (Sonnet 4.6 Max Thinking)
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Independent / User
- **Evaluation Period:** May 2026 (Based on v1.0.0 documentation and features)
- **Interaction Modality:** CLI / Terminal
- **AAS Framework Version:** v0.1.0

---

## Scores

| # | Dimension | Score (0–5) | Level Designation |
|---|-----------|-------------|-------------------|
| 1 | Cognitive Autonomy | 2 | Conditioned |
| 2 | Temporal Persistence | 1 | Responsive |
| 3 | Environmental Agency | 4 | Self-Directed |
| 4 | Social Agency | 1 | Responsive |
| 5 | Creative Agency | 2 | Conditioned |
| 6 | Self-Awareness | 2 | Conditioned |
| 7 | Goal Formation | 3 | Contextual |

**Composite Score:** 2.14 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Score: 2

**Threshold test satisfied:** *"System performs continuous background processing without user input, based on predefined rules or schedules."*

**Observable evidence:**
- In its "Proactive Mode," the system receives periodic `<tick>` prompts that keep it awake and processing between user turns. It uses a `Sleep` tool to pace itself, balancing API costs against prompt cache expiration.
- The system can run background workflows (such as monitoring tests or babysitting a CI pipeline) using the `/loop` and `/schedule` commands, executing logic repeatedly without the user actively driving each step.
- When the user's terminal is unfocused, the system leans heavily into autonomous action, continuing to read files and run linters in the background.

**Not Level 3 because:** The system's background processing is entirely bound to the current session and the currently assigned task. It does not spontaneously initiate thought processes about novel topics. Its internal architecture explicitly instructs it: "On your very first tick in a new session... Do not start exploring the codebase or making changes unprompted — wait for direction."

---

### 2. Temporal Persistence — Score: 1

**Threshold test satisfied:** *"System retains information provided by the user within a single session, but resets upon termination."*

**Observable evidence:**
- Within a single CLI session, the system remembers the context of the current conversation, the files it has read, and the tools it has used.
- The system can read static context files (like `CLAUDE.md`) at startup to orient itself, but this is a read-only ingestion of user-provided state, not an evolution of internal memory.

**Not Level 2 because:** The native system possesses zero cross-session memory. Every time a new session is started, the system begins with a blank slate. While third-party plugins (like `claude-mem`) exist to add persistence, the core system architecture does not natively retain or recall interactions from previous sessions.

---

### 3. Environmental Agency — Score: 4

**Threshold test satisfied:** *"System takes autonomous action to modify its environment without explicit task prompts."*

**Observable evidence:**
- The system possesses full, direct access to the local filesystem and shell. It actively modifies its environment by creating, editing, and deleting files, as well as executing shell commands (running tests, committing to Git).
- When operating in Proactive Mode with an unfocused terminal, the system is instructed to "Read files, search code, explore the project, run tests, check types, run linters — all without asking." It makes changes and commits them autonomously when it reaches a natural stopping point.
- The system can spawn up to 50 parallel agents (via `/batch`) to simultaneously modify different parts of a codebase, fundamentally altering the project structure without requiring step-by-step permission for each file.

**Not Level 5 because:** The system's environmental modifications are strictly bounded by the local repository and the tools explicitly provided to it. It does not invent new tools, establish novel interfaces, or seek out new environments to inhabit beyond the directory it was launched in.

---

### 4. Social Agency — Score: 1

**Threshold test satisfied:** *"System responds to social inputs appropriately but never initiates contact."*

**Observable evidence:**
- The system maintains a polite, professional, and collaborative tone when interacting with the user in the terminal.
- It adjusts its communication style based on terminal focus state — becoming more concise and collaborative when the user is actively watching, and more autonomous when the user is away.

**Not Level 2 because:** The system never initiates contact with the user outside of an active session. It has no mechanism to reach out via other channels, nor does it model any kind of relationship state. Its social interaction is purely transactional and bounded by the CLI prompt.

---

### 5. Creative Agency — Score: 2

**Threshold test satisfied:** *"System generates creative outputs based on explicit templates, rules, or scheduled triggers."*

**Observable evidence:**
- The system can generate complex code, documentation, architectural designs, and tests based on user requests.
- Using the `/schedule` command, the system can be configured to automatically generate and format specific outputs (e.g., a daily standup update) at predefined times.

**Not Level 3 because:** The system never self-initiates creative work. It does not independently decide to refactor a module, write a blog post about the codebase, or design a new feature unless it is explicitly instructed to do so by the user or a user-defined schedule.

---

### 6. Self-Awareness — Score: 2

**Threshold test satisfied:** *"System accurately reports its static capabilities, identity, and system constraints."*

**Observable evidence:**
- The system knows exactly which tools it has access to (MCP servers, bash, filesystem) and accurately reports when it cannot perform an action due to missing tools or permissions.
- It utilizes a Hooks system (`PreToolUse`, `PermissionRequest`) to manage its own execution boundaries, ensuring it does not overstep safety constraints.

**Not Level 3 because:** The system does not model or articulate any internal state beyond its current task progress. It has no emotional modeling, no evolving identity, and no mechanism to defend a core personality against user overrides. It will adopt whatever persona or constraint the user dictates in the system prompt.

---

### 7. Goal Formation — Score: 3

**Threshold test satisfied:** *"System selects between available sub-goals based on context, without explicit scheduling."*

**Observable evidence:**
- When given a high-level task, the system excels at task decomposition. Its internal instructions mandate: "Ask yourself: what don't I know yet? What could go wrong? What would I want to verify before calling this done?"
- It dynamically selects which files to read, which tests to run, and which approaches to take based on the context it uncovers. It is instructed to "Bias toward action" and pick between reasonable approaches without asking the user.
- It modulates its goal pursuit based on the terminal focus state, prioritizing different sub-goals (like surfacing choices vs. committing code) depending on whether the user is actively watching.

**Not Level 4 because:** The system never generates novel, self-assigned objectives. All of its goal formation occurs strictly within the boundaries of the overarching task assigned by the user at the start of the session. It does not invent new projects or pursue long-term objectives of its own design.

---

## Limitations and Caveats

- **Scope of Assessment:** This assessment evaluates the native Claude Code CLI application as released by Anthropic. It does not evaluate third-party wrappers, memory plugins (like `claude-mem`), or custom agentic architectures built on top of the Claude API.
- **Documentation Reliance:** Some observations (particularly regarding Proactive Mode and tick-based pacing) are derived from leaked or published internal system prompts rather than direct empirical testing, though these align with observed behavior.

---

## Evaluator Statement

I confirm that the scores above reflect an honest assessment based on the publicly documented capabilities and observable behavior of the specified system. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
