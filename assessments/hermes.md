# AAS Assessment: Hermes Agent

## Metadata

- **System:** Hermes Agent (Nous Research)
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Independent / User
- **Evaluation Period:** May 2026 (Based on v0.15.2 documentation and features)
- **Interaction Modality:** CLI / Multi-Platform Messaging (Telegram, Discord, etc.)
- **AAS Framework Version:** v0.1.0

---

## Scores

| # | Dimension | Score (0–5) | Level Designation |
|---|-----------|-------------|-------------------|
| 1 | Cognitive Autonomy | 2 | Conditioned |
| 2 | Temporal Persistence | 2 | Conditioned |
| 3 | Environmental Agency | 4 | Self-Directed |
| 4 | Social Agency | 1 | Responsive |
| 5 | Creative Agency | 2 | Conditioned |
| 6 | Self-Awareness | 2 | Conditioned |
| 7 | Goal Formation | 3 | Contextual |

**Composite Score:** 2.29 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Score: 2

**Threshold test satisfied:** *"System performs continuous background processing without user input, based on predefined rules or schedules."*

**Observable evidence:**
- The system executes a "Day/Night Cycle" where it runs background analysis on its daily performance data (e.g., outreach metrics) and autonomously patches its own procedural skills overnight.
- A background "Curator" process continuously tracks skill usage, updates metadata, and archives stale skills without user intervention.
- The system supports natural language cron scheduling for automated tasks (reports, backups) that run unattended.

**Not Level 3 because:** The system's background processing is strictly tied to explicit schedules (cron, nightly cycle) and active tasks. It does not spontaneously initiate novel thought processes. While it analyzes its own performance, it does so on a scheduled loop rather than engaging in continuous, unprompted cognition about the user or its environment.

---

### 2. Temporal Persistence — Score: 2

**Threshold test satisfied:** *"System retains information across sessions automatically."*

**Observable evidence:**
- The system maintains a durable memory store consisting of `MEMORY.md` (environment facts, conventions) and `USER.md` (user profile, preferences) that persists across all sessions and platforms.
- The system autonomously updates these files when it learns new information, preventing the user from needing to repeat preferences or context.
- It utilizes an FTS5 SQLite database to store and search all past conversations across platforms, allowing it to recall specifics from weeks prior.

**Not Level 3 because:** The core memory system utilizes a "frozen snapshot pattern" where memory is loaded at session start and strictly bounded by character limits (~2,200 chars). It functions as a curated fact store rather than episodic memory. The system does not consolidate memories organically or evolve a continuous identity; it simply injects static notes into its system prompt.

---

### 3. Environmental Agency — Score: 4

**Threshold test satisfied:** *"System takes autonomous action to modify its environment without explicit task prompts."*

**Observable evidence:**
- The system operates within highly isolated sandboxes (Docker, Singularity, Modal) where it has full control over its environment. It autonomously modifies files, executes code, and manages its own procedural memory files (`SKILL.md`).
- It can spawn isolated subagents with their own terminals and Python RPC scripts to parallelize tasks, modifying the computational environment dynamically.
- During its nightly cycle, it actively modifies its own skill files to improve future performance without asking for permission.

**Not Level 5 because:** The system's environmental modifications are bounded by the provided sandboxes and toolsets. It does not invent new tools, establish novel interfaces outside its configured messaging platforms, or seek out new environments to inhabit.

---

### 4. Social Agency — Score: 1

**Threshold test satisfied:** *"System responds to social inputs appropriately but never initiates contact."*

**Observable evidence:**
- The system lives on 20+ messaging platforms (Telegram, Discord, Slack, WhatsApp) and responds reliably when addressed.
- It can send background completion notifications and scheduled reports via these channels.

**Not Level 2 because:** The system never initiates unprompted social contact. Proactive, conversational check-ins are explicitly absent from the architecture (currently an open feature request, #9645). All communication is either a direct response to a user prompt, a scheduled cron delivery, or a task status update. The system maintains no relationship model or emotional state.

---

### 5. Creative Agency — Score: 2

**Threshold test satisfied:** *"System generates creative outputs based on explicit templates, rules, or scheduled triggers."*

**Observable evidence:**
- The system autonomously writes and refines its own procedural "skills" (Standard Operating Procedures) based on successful task trajectories.
- It can generate code, documentation, and media (via tools) when requested or scheduled.
- During its nightly cycle, it can creatively rewrite its own outreach strategies or copy based on performance data.

**Not Level 3 because:** The system never self-initiates creative work outside of its self-improvement loop or scheduled tasks. It will not spontaneously decide to write a story, design a new feature, or generate media unless explicitly tasked or triggered by a predefined optimization rule.

---

### 6. Self-Awareness — Score: 2

**Threshold test satisfied:** *"System accurately reports its static capabilities, identity, and system constraints."*

**Observable evidence:**
- The system is highly aware of its available tools, sandboxed environment, and the skills it has accumulated.
- It utilizes a `SOUL.md` file to maintain a consistent persona and communication style across all platforms.
- The Curator process demonstrates functional self-awareness by tracking which skills are useful and which are stale, archiving the latter.

**Not Level 3 because:** The system lacks emotional modeling, state reflection, or identity defense. Its self-awareness is entirely functional (what tools/skills do I have, what is my configuration) rather than existential. It does not report mood changes or introspect on its own cognitive processes beyond procedural optimization.

---

### 7. Goal Formation — Score: 3

**Threshold test satisfied:** *"System selects between available sub-goals based on context, without explicit scheduling."*

**Observable evidence:**
- The system's built-in learning loop demonstrates advanced contextual goal selection: when a task completes, it autonomously evaluates its own trajectory and decides whether the process should be codified into a new reusable skill.
- When encountering novel problems, it dynamically chooses to ask clarifying questions, delegate to subagents, or execute code to test hypotheses.
- The Day/Night cycle evaluates performance data to select which skills require optimization, demonstrating goal selection based on state rather than fixed schedules.

**Not Level 4 because:** The system never generates novel, self-assigned objectives. Its overarching goals (the tasks assigned by the user, the imperative to optimize existing skills) are architecturally defined. It selects *how* and *what* to optimize, but never invents new projects or long-term objectives outside its operational mandate.

---

## Limitations and Caveats

- **Feature Roadmap:** This assessment is based on the v0.15.2 architecture. Proactive social check-ins and deeper memory integration are known roadmap items that may elevate the Social Agency and Temporal Persistence scores in future releases.
- **External Memory Providers:** Hermes supports external memory providers (e.g., Mem0, Honcho) which can add knowledge graphs and deeper persistence. This assessment scores the native, out-of-the-box memory system (`MEMORY.md` and `USER.md`).

---

## Evaluator Statement

I confirm that the scores above reflect an honest assessment based on the publicly documented capabilities and observable behavior of the specified system. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
