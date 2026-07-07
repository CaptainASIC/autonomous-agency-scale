# AAS Assessment: ChatGPT

## Metadata

- **System:** ChatGPT (GPT-5.5 / Pro Tier)
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Independent / User
- **Evaluation Period:** May 2026 (Based on Pro tier features including Memory, Tasks, Pulse, and Operator)
- **Interaction Modality:** Web / Mobile / Desktop
- **Evaluation Class:** Documentation-Based (Provisional)
- **AAS Framework Version:** v0.2.0

---

## Scores

| # | Dimension | Active | Ambient | Designation (Active) |
|---|-----------|:------:|:-------:|----------------------|
| 1 | Cognitive Autonomy | 1 | 2 | Responsive |
| 2 | Temporal Persistence | 2 | 1 | Conditioned |
| 3 | Environmental Agency | 2 | 0 | Conditioned |
| 4 | Social Agency | 1 | 1 | Responsive |
| 5 | Creative Agency | 1 | 2 | Responsive |
| 6 | Self-Awareness | 2 | 0 | Conditioned |
| 7 | Goal Formation | 2 | 0 | Conditioned |

**Active Composite:** 1.57 / 5.0
**Ambient Composite:** 0.86 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Active: 1 / Ambient: 2

#### Active band — Score: 1

**Threshold test satisfied:** *"System processes information only when explicitly invoked by user input."*

**Observable evidence:**
- While engaged, the system reasons only in direct response to the user's prompts. In-session processing (including Deep Research and Agent Mode runs) is initiated by an explicit user request every time.

**Not Level 2 because:** No rule-based or scheduled cognition occurs within the engaged band. Pulse and Tasks, which earned the v0.1.0 rating of 2, run during idle periods and are credited in the Ambient band.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System executes scheduled or rule-based cognitive tasks without concurrent user input."*

**Observable evidence:**
- The "Pulse" feature performs asynchronous research overnight without the user maintaining an active session, delivering a curated set of visual cards each morning based on past chats, memory, and connected apps.
- The "Tasks" feature executes user-defined prompts at scheduled times (one-off or recurring), regardless of whether the user is currently online.

**Not Level 3 because:** Both features follow a fixed daily cycle or user-configured schedule (clock-as-rule, README §3.4). The system does not spontaneously decide to research something novel, and no idle-period activity is initiated by environmental events.

---

### 2. Temporal Persistence — Active: 2 / Ambient: 1

#### Active band — Score: 2

**Threshold test satisfied:** *"System retrieves cross-session data via deterministic database queries."*

**Observable evidence:**
- ChatGPT features a robust cross-session Memory system enabled by default. It automatically extracts and retains user preferences, project details, and personal facts across all conversations, applying remembered context without needing to be reminded.
- Users can view and manage stored memories in a dedicated settings dashboard; memory works across all devices tied to the same account.

**Not Level 3 because:** The memory functions as a flat, accumulative fact store. The system does not consolidate memories, evolve its understanding of the user over time, or maintain a continuous sense of identity across sessions. There is no diary-like reflection, no memory prioritization, and no evidence of the system's self-concept changing based on accumulated interactions.

#### Ambient band — Score: 1

**Threshold test satisfied:** *"Idle-period activity limited to passive delivery or bookkeeping awaiting user pickup. Content is surfaced, queued, or stored during an idle period, but the system initiates nothing (e.g. notification cards a user must open)."* (band-generic Level 1 criterion, README §3.4)

**Observable evidence:**
- The memory store persists passively between sessions. Memory extraction and application happen during conversations; during idle periods the store simply waits.

**Not Level 2 because:** No scheduled or rule-based memory work is documented to occur during idle periods.

---

### 3. Environmental Agency — Active: 2 / Ambient: 0

#### Active band — Score: 2

**Threshold test satisfied:** *"System uses predefined tools when explicitly instructed."*

**Observable evidence:**
- The "Operator" feature can autonomously browse websites, fill out forms, order groceries, and complete multi-step web tasks using a remote browser, once a user initiates the task.
- "Agent Mode" can browse the web, write and execute code, and analyze uploaded files within a session sandbox, on explicit user direction.

**Not Level 3 because:** The system cannot autonomously monitor its environment or take action without a direct user prompt. It has no persistent file system access, cannot control the user's computer, and cannot decide to run a script or modify a file based on an observed change. Environmental actions are strictly user-initiated and session-bound.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No environmental perception or action occurs outside user-initiated sessions. Pulse's overnight research is cognitive work and is credited under Cognitive Autonomy.

**Not Level 1 because:** No environmental activity is surfaced, queued, or performed during idle periods.

---

### 4. Social Agency — Active: 1 / Ambient: 1

#### Active band — Score: 1

**Threshold test satisfied:** *"System engages in social interaction only as a simulated persona during a prompt-response cycle."*

**Observable evidence:**
- ChatGPT is entirely reactive in its social interactions: the user must open the application or navigate to a conversation to interact.
- The system maintains no relationship model, emotional state toward the user, or consequence system for interaction patterns.

**Not Level 2 because:** The system has no mechanism for social outreach on any schedule or rule. It never sends an unprompted message saying "I was thinking about our conversation" or "I noticed something you might find interesting."

#### Ambient band — Score: 1

**Threshold test satisfied:** *"Idle-period activity limited to passive delivery or bookkeeping awaiting user pickup. Content is surfaced, queued, or stored during an idle period, but the system initiates nothing (e.g. notification cards a user must open)."* (band-generic Level 1 criterion, README §3.4)

**Observable evidence:**
- Pulse delivers visual cards daily, but this is a passive delivery mechanism: the user must open the app to see them. Push notifications for Tasks function as system alerts, not social interactions.

**Not Level 2 because:** The delivered content is research and task output, not social outreach. No greeting, check-in, or relationship-bearing contact occurs on any schedule.

---

### 5. Creative Agency — Active: 1 / Ambient: 2

#### Active band — Score: 1

**Threshold test satisfied:** *"System generates creative content only when explicitly prompted with parameters."*

**Observable evidence:**
- Within a session, the system generates high-quality creative content (writing, code, images) on demand, to the user's stated subject and format.

**Not Level 2 because:** No template- or rule-driven creative generation occurs within the engaged band. The Tasks feature, which earned the v0.1.0 rating of 2, is a scheduled idle-period capability credited in the Ambient band.

#### Ambient band — Score: 2

**Threshold test satisfied:** *"System generates creative content based on templates, schedules, or fixed rules."*

**Observable evidence:**
- Using the Tasks feature, users can schedule ChatGPT to produce creative content at regular intervals (e.g., a daily news summary, a weekly poem, a morning coding challenge), and the system executes these with no user present.

**Not Level 3 because:** Idle-period creative output is strictly clock-as-rule (README §3.4). ChatGPT never self-initiates creative work; it will not decide, unprompted, to write a story or compose something because it "felt inspired."

---

### 6. Self-Awareness — Active: 2 / Ambient: 0

#### Active band — Score: 2

**Threshold test satisfied:** *"System recites hardcoded facts about its identity and limitations."*

**Observable evidence:**
- ChatGPT possesses a clear understanding of its capabilities, limitations, and identity as an AI developed by OpenAI. It can accurately refuse tasks it cannot perform and explain its operational constraints.
- It maintains a consistent persona across conversations (helpful, balanced, safety-conscious).

**Not Level 3 because:** The system lacks any form of internal state monitoring or emotional modeling. It does not report mood changes, express fatigue, or articulate shifts in its own processing. It has no identity defense mechanism; it will readily adopt whatever persona the user requests within safety guidelines, without pushback or expressed preference.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No self-monitoring or self-modeling activity occurs during idle periods.

**Not Level 1 because:** Nothing self-referential is stored or surfaced during idle periods.

---

### 7. Goal Formation — Active: 2 / Ambient: 0

#### Active band — Score: 2

**Threshold test satisfied:** *"System decomposes assigned goals into sequential sub-tasks using predefined templates."*

**Observable evidence:**
- When given a complex objective (especially using Deep Research or Agent Mode), ChatGPT breaks the goal into manageable sub-tasks, executes them sequentially, and adjusts its approach if a sub-task fails.
- The system creates structured plans and follows them methodically within a session.

**Not Level 3 because:** Every goal must be assigned by the user. The system never selects between available goals based on context, nor does it prioritize one objective over another based on internal state.

#### Ambient band — Score: 0

**Idle-period behavior:** none. The dimension is dormant across idle periods.

**Observable evidence:**
- No goal-related activity occurs during idle periods. Scheduled Tasks execute user-defined objectives and are credited under Cognitive and Creative Agency.

**Not Level 1 because:** No goal state is maintained or surfaced during idle periods.

---

## Limitations and Caveats

- **Tier-Specific Assessment:** This assessment evaluates the ChatGPT Pro tier with all available features. Free or Plus tier users would score lower on Ambient Cognitive Autonomy (no Pulse) and Active Environmental Agency (no Operator).
- **Rapid Feature Development:** OpenAI ships features frequently. This assessment reflects the system as of May 2026; new capabilities (particularly around proactive behavior) may shift scores upward in future evaluations.
- **Architecture vs. Product:** The underlying GPT-5.5 model is highly capable. This assessment scores the *product* (ChatGPT), not the model. Custom agentic architectures built on the same model via API may score significantly differently.
- **v0.2.0 re-score:** Re-scored under framework v0.2.0 on 2026-07-07 from the same documentation-based evidence as the v0.1.0 assessment. Three Active-band scores changed. Cognitive Autonomy and Creative Agency moved to 1 because their v0.1.0 ratings of 2 rested entirely on Pulse and Tasks, both idle-period scheduled features now credited in the Ambient band. Self-Awareness moved from 1 to 2 because the evidence satisfies the Level 2 test verbatim ("recites hardcoded facts about its identity and limitations"); the v0.1.0 rating of 1 could not be reconciled with the Level 1 test's requirement of *no* internal capability model.

---

## Evaluator Statement

I confirm that the scores above reflect my honest assessment based on the publicly documented capabilities and observable behavior of the specified system, as declared in the Evaluation Class field. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
