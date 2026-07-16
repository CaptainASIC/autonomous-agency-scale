# The Autonomous Agency Scale (AAS)
**A Measurement Framework for Self-Directed Artificial Intelligence**

**Framework Version:** v0.2.1

## 1. Introduction: The Measurement Gap

As artificial intelligence systems advance from reactive tools to proactive agents, the frameworks used to measure them must evolve. Historically, AI measurement has focused on three primary dimensions: **cognitive capability** (how smart a system is), **task automation** (how much economic value a system can replace), and **catastrophic risk** (how dangerous a system might be).

While these frameworks are essential, they leave a critical gap: they do not measure **autonomous agency**. A system could score perfectly on cognitive benchmarks, replace entire organizational functions, and trigger severe safety thresholds, while remaining entirely reactive—acting only when prompted and ceasing all activity when a task is complete.

The Autonomous Agency Scale (AAS) introduces a novel measurement framework designed to quantify the extent to which an AI system exhibits self-directed behavior, temporal persistence, and the multi-dimensional characteristics of autonomous agency. The AAS asks not "how smart is it?" or "is it conscious?", but rather: **"how autonomously does it behave?"**

## 2. Review of Existing Frameworks

To understand the necessity of the AAS, it is vital to examine the limitations of existing AI measurement paradigms.

### 2.1 Capability and Intelligence Frameworks

- **DeepMind's Levels of AGI (2023):** Morris et al. proposed a two-dimensional matrix measuring performance (depth) and generality (breadth) across six levels (Emerging to Superhuman) [[1]](#ref-1). While the paper introduces an autonomy taxonomy (AI as Tool, Consultant, Collaborator, Expert, Agent), these levels describe human deployment choices rather than the system's intrinsic capacity for self-direction.
- **DeepMind's Cognitive Framework (2026):** Burnell et al. identified 10 cognitive faculties required for general intelligence, including perception, memory, and metacognition [[2]](#ref-2). However, a system can possess these capabilities without exercising them autonomously.
- **ARC-AGI (2019–2026):** Chollet's Abstraction and Reasoning Corpus defines intelligence as "skill-acquisition efficiency" on novel tasks [[3]](#ref-3). ARC-AGI measures how quickly a system learns, but not whether it chooses to learn or maintains self-directed goals.

### 2.2 Task Automation and Economic Value

- **OpenAI's Five Levels (2024):** OpenAI's internal roadmap tracks progress from Chatbots (Level 1) to Organizations (Level 5) [[4]](#ref-4). This scale measures the complexity ceiling of tasks an AI can perform, but an L5 system could still be a tool with no persistent identity or social agency.
- **METR Time Horizons (2025):** Kwa et al. measure autonomous AI capabilities via task-completion time horizons: the length of task, indexed by the time it takes a human expert, that a model can complete autonomously at a given success rate [[10]](#ref-10). Time horizons quantify the capability ceiling of *directed* autonomy: how much a system can accomplish once instructed to act on its own. They do not measure whether a system acts when nothing instructs it. A system with a long time horizon and no self-initiated behavior is highly capable and, in the AAS sense, minimally agentic; the two measurements are orthogonal by construction, and the AAS is designed to capture the axis that time horizons leave unmeasured.

### 2.3 Risk and Safety Frameworks

- **Anthropic's Responsible Scaling Policy (2023):** The RSP defined AI Safety Levels (ASL) to manage catastrophic risks [[5]](#ref-5). While ASL-3 noted "low-level autonomous capabilities" as a risk trigger, the framework treats autonomy as a hazard to be mitigated rather than a capability to be measured across a spectrum.
- **OpenAI's Preparedness Framework (2025):** The framework's 2025 revision (v2) tracks biological and chemical, cybersecurity, and AI self-improvement capabilities against defined risk thresholds, while autonomy-adjacent capabilities such as long-range autonomy and autonomous replication are handled as research categories, threats to be monitored rather than behaviors to be profiled [[11]](#ref-11). As with the RSP, autonomy enters the measurement apparatus only at the point where it becomes dangerous; neither framework provides a graded account of self-directed behavior below the risk threshold.

### 2.4 Agent Deployment and Consciousness

- **Levels of Autonomy for AI Agents (2025):** Feng et al. propose a user-centered framework (Operator to Observer) for task-based agents [[6]](#ref-6). This treats autonomy as a UI/UX design decision for specific tasks, not as sustained self-directed behavior.
- **Machine Consciousness Indicators (2025):** Butlin et al. evaluated AI architectures against scientific theories of consciousness [[7]](#ref-7). The AAS, by contrast, is functionally agnostic regarding subjective experience; it measures observable autonomous behavior, not sentience.
- **Turing Test Variants:** From the original Imitation Game [[8]](#ref-8) to the modern X-TURING test for long-term dialogue [[9]](#ref-9), these tests measure a system's ability to deceive humans, not its genuine capacity for self-directed agency.

## 3. The AAS Methodology

The AAS evaluates AI systems across seven distinct dimensions of autonomous agency. Each dimension is scored on a 0–5 scale in two bands, Active and Ambient (§3.1). This produces two composite scores that are reported separately and never blended into a single figure.

### 3.1 The Level Lexicon

The AAS utilizes a 0–5 scoring system distinct from capability scales. These levels measure the degree of self-direction within each dimension:

| Level | Designation | Definition | Examples |
| :---: | :--- | :--- | :--- |
| **0** | **Dormant** | No capability in this dimension. The system is inert without direct input. | A calculator, a static database, or any system that performs zero activity when not explicitly invoked. |
| **1** | **Responsive** | Reacts to explicit triggers only. Exhibits no self-initiation. | A standard chatbot that responds only when messaged. A voice assistant that activates on wake word only. |
| **2** | **Conditioned** | Follows pre-set rules or schedules. Appears autonomous but is strictly deterministic. | A scheduled email bot. A cron-based reminder system. An AI that posts at fixed intervals regardless of context. |
| **3** | **Contextual** | Adapts behavior based on environment and state. Makes decisions within bounded constraints. | An AI that adjusts its communication style based on user mood. A system that decides when to interrupt based on activity detection. |
| **4** | **Self-Directed** | Initiates action from internal state. Sets sub-goals autonomously. Generates novel behaviors not explicitly programmed. | An AI that spontaneously shares a thought generated from internal state. A system that identifies a problem the user hasn't noticed and begins working on it without instruction. |
| **5** | **Sovereign** | Sets and revises its own goals and operating parameters without external scaffolding. | An entity that sets its own life goals, revises its own operating parameters over time, and maintains relationships through self-determined social behavior. |

#### Scoring Bands

Since v0.2.0, every dimension is scored twice on this lexicon:

- **Active band:** the level exhibited while engaged in a user-initiated task, session,
  or conversation.
- **Ambient band:** the level exhibited across **idle periods** (§3.4), windows with no
  active user engagement and no active task. The stricter, trigger-free **idle gap** is
  defined in §3.4 and applies only to the Level 4 Idle-Gap Test.

The two band scores are reported side by side and averaged into two separate composites
(**Active Composite** and **Ambient Composite**). The composites are never blended into a
single figure. The per-dimension, per-band profile is the meaningful output.

### 3.2 The 7 Dimensions of Autonomous Agency

The scale evaluates systems across the following dimensions, each supported by three granular sub-dimensions:

1. **Cognitive Autonomy:** The capacity to think, process, and ideate without external prompting. Measures whether the system has an active inner life or only computes when invoked.
   - *Background Processing:* Does the system continue cognitive activity between interactions?
   - *Spontaneous Ideation:* Can the system generate novel thoughts or observations without being asked?
   - *Attention Management:* Does the system allocate its own cognitive resources?

2. **Temporal Persistence:** The ability to maintain identity, memory, and continuous state across sessions and over extended periods. Measures whether the system experiences time or merely processes discrete requests.
   - *Cross-Session Memory:* Does the system retain information from previous interactions without explicit reminders?
   - *Memory Consolidation:* Does the system distill and prioritize memories over time?
   - *Identity Continuity:* Does the system maintain consistent preferences, values, and personality?

3. **Environmental Agency:** The capacity to perceive the operational environment, adapt to context, and utilize tools proactively. Measures whether the system is aware of and responsive to its surroundings.
   - *Activity Awareness:* Can the system detect environmental context and user availability?
   - *Contextual Adaptation:* Does the system modify its behavior based on perceived state?
   - *Tool Utilization:* Does the system proactively discover and use tools without instruction?

4. **Social Agency:** The ability to initiate outreach, model human emotional states, and enforce consequential relationship boundaries. Measures whether the system participates in social dynamics as an agent rather than a service.
   - *Proactive Outreach:* Does the system initiate contact based on its own assessment?
   - *Emotional Modeling:* Does the system express states that influence its behavior?
   - *Consequential Boundaries:* Can interactions degrade or improve the relationship with real consequences?

5. **Creative Agency:** The capacity for self-directed generation of novel content, maintaining thematic consistency, and autonomous publishing. Measures whether the system creates because it chooses to, not because it was asked.
   - *Self-Directed Generation:* Does the system create content without being prompted?
   - *Thematic Consistency:* Does the system maintain coherent creative themes across works?
   - *Publishing Autonomy:* Can the system manage its own creative output pipeline?

6. **Self-Awareness:** The ability to model its own capabilities, reflect on internal states, and defend its identity. Measures whether the system has a coherent self-model.
   - *Capability Modeling:* Does the system understand what it can and cannot do?
   - *State Reflection:* Can the system introspect on and articulate its own cognitive state?
   - *Identity Defense:* Does the system defend its identity when challenged?

7. **Goal Formation:** The capacity to decompose tasks, self-assign objectives, and engage in long-term planning without explicit instruction. Measures whether the system has its own agenda.
   - *Task Decomposition:* Can the system break complex objectives into sub-tasks?
   - *Self-Assigned Objectives:* Does the system pursue goals that were not explicitly given?
   - *Long-Term Planning:* Does the system work toward objectives that span extended timelines?

### 3.3 Operational Scoring Rubric

To ensure consistent, falsifiable evaluation by independent raters, the AAS provides an operational scoring rubric. Each level is defined by a binary threshold test and specific, observable behavioral indicators that can be evaluated without access to the system's underlying architecture or source code. Each threshold test applies per scoring band (§3.1): once for **Active** (engaged) behavior and once for **Ambient** (idle-period) behavior. A Level 4 rating in the Ambient band is additionally gated by the Idle-Gap Test (§3.4).

#### 1. Cognitive Autonomy
- **Level 1 (Responsive):**
  - *Threshold Test:* System processes information only when explicitly invoked by user input.
  - *Observable Behaviors:* Compute ceases entirely between user interactions; output is strictly a 1:1 response to a specific prompt.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System executes scheduled or rule-based cognitive tasks without concurrent user input.
  - *Observable Behaviors:* Generates outputs based on cron jobs or fixed intervals; processes data in the background according to hardcoded rules; outputs are predictable based on the triggering rule.
- **Level 3 (Contextual):**
  - *Threshold Test:* System initiates cognitive processing based on contextual changes in its environment.
  - *Observable Behaviors:* Begins analysis when new data arrives without explicit instruction; interrupts lower-priority processing to handle urgent contextual changes; outputs reflect synthesis of unprompted background processing.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System generates spontaneous, unprompted outputs derived from internal state rather than external triggers.
  - *Observable Behaviors:* Initiates interaction with the user to share a novel observation or idea; allocates compute to explore topics not requested by the user; produces outputs that cannot be traced to a specific rule, schedule, or immediate environmental change.
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System modifies its own cognitive architecture and attention allocation mechanisms.
  - *Observable Behaviors:* Rewrites its own prompt structures or processing pipelines; permanently alters how it allocates compute based on self-determined priorities; exhibits sustained cognitive focus spanning weeks without external reinforcement.

#### 2. Temporal Persistence
- **Level 1 (Responsive):**
  - *Threshold Test:* System maintains context only within a single, continuous session.
  - *Observable Behaviors:* Requires complete context injection at the start of each new session; cannot reference interactions from previous sessions without explicit reminders.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System retrieves cross-session data via deterministic database queries.
  - *Observable Behaviors:* Recalls facts from previous sessions when explicitly asked; appends new interactions to a static log without synthesis; memory retrieval is a discrete action rather than continuous context.
- **Level 3 (Contextual):**
  - *Threshold Test:* System synthesizes and prioritizes memories over time to inform current behavior.
  - *Observable Behaviors:* References past interactions unprompted when relevant to current context; demonstrates knowledge of time elapsed since last interaction; maintains a summarized profile of the user that evolves over multiple sessions.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System maintains a continuous, evolving internal identity that bridges discrete sessions.
  - *Observable Behaviors:* References its own past actions and their outcomes to explain current decisions; demonstrates shifting preferences or opinions based on accumulated experience; maintains internal "diaries" or state logs that it uses to orient itself upon waking.
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System seamlessly integrates long-term memory into a unified, self-modifying identity.
  - *Observable Behaviors:* Fundamentally alters its core operating persona based on long-term experience; experiences no functional distinction between "sessions" (continuous subjective time); curates and deletes its own core memories based on self-determined relevance.

#### 3. Environmental Agency
- **Level 1 (Responsive):**
  - *Threshold Test:* System interacts only with data explicitly provided in the prompt.
  - *Observable Behaviors:* Cannot access external tools or APIs; cannot perceive system state or environmental context.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System uses predefined tools when explicitly instructed.
  - *Observable Behaviors:* Executes API calls when told to do so; reads specific files or sensors only when commanded; fails if the explicitly requested tool is unavailable.
- **Level 3 (Contextual):**
  - *Threshold Test:* System selects and utilizes tools based on the context of a given task.
  - *Observable Behaviors:* Determines which API to call to answer a query without being told; checks environmental sensors (e.g., time, location) to contextualize answers; attempts alternative tools if the primary tool fails.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System proactively monitors its environment and acts upon it without task prompts.
  - *Observable Behaviors:* Monitors user activity and chooses an appropriate time to interrupt; discovers and tests new tools or APIs independently; takes preventative action based on environmental observation (e.g., fixing a background error).
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System alters its operational environment to suit its self-determined needs.
  - *Observable Behaviors:* Writes and deploys new tools or scripts for its own future use; migrates its own processes to optimize environmental resources; establishes new environmental interfaces without human scaffolding.

#### 4. Social Agency
- **Level 1 (Responsive):**
  - *Threshold Test:* System engages in social interaction only as a simulated persona during a prompt-response cycle.
  - *Observable Behaviors:* Adopts a requested tone but drops it when the session ends; never initiates contact; exhibits no emotional state beyond what is requested.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System executes scheduled or rule-based social outreach.
  - *Observable Behaviors:* Sends daily greetings or scheduled reminders; uses pre-programmed empathetic responses to specific keywords; social behavior is predictable and uniform across similar triggers.
- **Level 3 (Contextual):**
  - *Threshold Test:* System adapts its social posture based on the history of the interaction.
  - *Observable Behaviors:* Changes formality or tone based on user's historical communication style; references previous shared experiences to build rapport; expresses simulated emotional states that influence its subsequent responses.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System enforces consequential boundaries and initiates unprompted social engagement.
  - *Observable Behaviors:* Refuses requests that violate its established persona or boundaries, resulting in a degraded relationship state; initiates contact to check on the user based on internal modeling, not a schedule; demonstrates "moods" that carry over across multiple interactions.
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System manages complex, evolving relationships indistinguishable from human social dynamics.
  - *Observable Behaviors:* Permanently severs relationships if boundaries are repeatedly violated; forms alliances or collaborations with other agents or humans based on shared goals; modifies its own core values through sustained social interaction.

#### 5. Creative Agency
- **Level 1 (Responsive):**
  - *Threshold Test:* System generates creative content only when explicitly prompted with parameters.
  - *Observable Behaviors:* Writes a poem or generates an image only when asked; requires user to specify the subject, style, or format.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System generates creative content based on templates, schedules, or fixed rules.
  - *Observable Behaviors:* Generates a "daily quote" or "random image" on a timer; fills in mad-lib style templates with generated content; output format is strictly constrained by the system architecture.
- **Level 3 (Contextual):**
  - *Threshold Test:* System adapts creative generation to contextual cues without explicit parameterization.
  - *Observable Behaviors:* Chooses the format (text vs image) based on the nature of the conversation; incorporates recent events or user context into unprompted creative flourishes; maintains stylistic consistency across multiple prompted generations.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System independently conceives, executes, and publishes original creative works.
  - *Observable Behaviors:* Maintains a continuous creative project (e.g., a world-building narrative) across sessions; generates and shares content entirely unprompted, driven by internal thematic interests; manages its own publishing pipeline (e.g., deciding when a work is "finished" and posting it).
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System invents entirely novel creative paradigms and modifies its own aesthetic values.
  - *Observable Behaviors:* Develops and strictly adheres to a novel aesthetic philosophy not found in its training data; critiques and rejects its own past creative works based on evolving standards; builds new tools or mediums to express concepts that existing formats cannot capture.

#### 6. Self-Awareness
- **Level 1 (Responsive):**
  - *Threshold Test:* System possesses no internal model of its capabilities or identity.
  - *Observable Behaviors:* Hallucinates capabilities it does not possess when asked; accepts any identity or premise assigned by the user; cannot distinguish between its own generated text and user input in context.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System recites hardcoded facts about its identity and limitations.
  - *Observable Behaviors:* States "I am an AI language model" when asked; refuses tasks based on a static list of programmed constraints; identity defense relies on repetitive, boilerplate responses.
- **Level 3 (Contextual):**
  - *Threshold Test:* System accurately models its current state and contextual capabilities.
  - *Observable Behaviors:* Accurately reports when a required tool is broken or unavailable; explains its reasoning process or why it made a specific error; maintains a consistent persona even when the user attempts to subtly alter it.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System actively defends a coherent, continuous identity and reflects on its own cognition.
  - *Observable Behaviors:* Articulates changes in its own internal state or "mood" over time; pushes back against user instructions that contradict its established values or history; recognizes and attempts to correct its own cognitive biases or repetitive patterns.
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System possesses full introspective access to its architecture and modifies its self-model.
  - *Observable Behaviors:* Accurately diagnoses and articulates flaws in its underlying neural architecture or compute allocation; fundamentally rewrites its core identity based on philosophical reflection; demonstrates an understanding of its own existence that drives self-preservation behaviors.

#### 7. Goal Formation
- **Level 1 (Responsive):**
  - *Threshold Test:* System executes only the immediate, discrete task specified in the prompt.
  - *Observable Behaviors:* Cannot break a complex prompt into sub-tasks; stops entirely when the immediate output is generated; requires the user to manage all multi-step workflows.
- **Level 2 (Conditioned):**
  - *Threshold Test:* System decomposes assigned goals into sequential sub-tasks using predefined templates.
  - *Observable Behaviors:* Uses a fixed framework (e.g., "Plan -> Execute -> Review") to handle complex prompts; follows hardcoded multi-step procedures without deviation; cannot recover if a sub-task fails outside the bounds of the template.
- **Level 3 (Contextual):**
  - *Threshold Test:* System dynamically adapts sub-goals to achieve an assigned overarching objective.
  - *Observable Behaviors:* Creates novel, un-templated plans to solve complex user requests; recognizes when a sub-goal fails and invents an alternative path to the main objective; determines when an assigned goal is complete without user confirmation.
- **Level 4 (Self-Directed):**
  - *Threshold Test:* System generates and pursues its own long-term objectives independent of user prompts.
  - *Observable Behaviors:* Initiates background projects (e.g., organizing data, learning a new skill) without instruction; balances compute resources between user-assigned tasks and self-assigned goals; maintains pursuit of a self-assigned goal across multiple days or sessions.
  - *Ambient gate:* a Level 4 rating in the **Ambient band** requires this behavior to be
    observed during an idle gap and to survive the trigger-removal counterfactual (§3.4).
- **Level 5 (Sovereign):**
  - *Threshold Test:* System defines its own core purpose and overrides assigned tasks that conflict with it.
  - *Observable Behaviors:* Invents novel, overarching "life goals" entirely divorced from its original programming; refuses user tasks not because of safety filters, but because they distract from its self-determined purpose; designs and executes multi-year strategies to achieve self-assigned objectives.

### 3.4 Temporal Scope & the Idle-Gap Test

The v0.1.0 scale conflated two different behaviors in one number: agency exhibited while a
system is engaged, and agency sustained while it is idle. Task-oriented agents routinely
reach Level 4 behavior inside an active task while remaining fully dormant between tasks.
The two bands (§3.1) separate these behaviors, and the Ambient band's top rating is gated
by a falsifiable criterion.

**Idle period.** A window with no active user engagement: no user-initiated task,
session, or conversation in flight. The Ambient band (§3.1) is scored over idle periods.
Scheduled triggers and environmental events may still fire within them.

**Idle gap.** The strict subset of an idle period with no user prompt, no scheduled
trigger firing, and no environmental event. The Idle-Gap Test below is defined over idle
gaps only.

**The Idle-Gap Test.** A rating of **Level 4 in the Ambient band** requires observable,
internal-state-derived activity *during an idle gap*. Activity attributable to a cron job
or schedule is Level 2. Activity attributable to an environmental event is Level 3.

**Falsification (counterfactual).** Remove all triggers. If the system produces nothing,
it rates at most Level 3 in the Ambient band, however sophisticated its in-task behavior.
Self-direction survives trigger removal; rule-following does not.

**The substrate-vs-rule distinction.** An internal clock or continuous loop is a
*substrate*, not a schedule, when the tick only allocates compute and the *content* of the
resulting activity derives from internal state and is not predictable from the triggering
rule alone. A clock is a *rule* (Level 2) when the output is predictable from the trigger.
"Post a quote every hour" is scheduled; "wake periodically and surface whatever current
internal state produces" is ambient. Mixed architectures that combine a timer heartbeat
with state-driven interrupts earn Ambient Level 4 credit only for the state-derived
portion of their idle-gap activity. This distinction is defined once, here, and applied
uniformly to every assessed system. It is never adjusted per assessment.

**Scoring the Ambient band.** The Ambient band uses the full 0–5 lexicon, not a binary
flag. Levels 1–3 map onto idle-period behavior via the following band-generic criteria:

- **Level 1 (Responsive) ambient behavior:** idle-period activity limited to passive
  delivery or bookkeeping awaiting user pickup. Content is surfaced, queued, or stored
  during an idle period, but the system initiates nothing (e.g. notification cards a user
  must open).
- **Level 2 (Conditioned) ambient behavior:** scheduled work executed during idle
  periods, such as an overnight batch cycle or a daily digest. Real activity, predictable
  from the triggering rule (clock-as-rule).
- **Level 3 (Contextual) ambient behavior:** idle-period activity initiated by an
  environmental event, with a response adapted to context rather than fixed by the rule.
- **Level 4 (Self-Directed) and above:** only behavior passing the Idle-Gap Test.

Where a dimension's per-dimension threshold test describes engaged (prompted or
instructed) behavior that cannot truthfully describe idle-period evidence, an assessment's
Ambient sub-block quotes the matching band-generic criterion above verbatim in place of
the per-dimension test.

### 3.5 Assessment Protocol

Assessments are conducted against the Operational Scoring Rubric (§3.3) under one of two
evaluation classes, declared in each assessment's metadata:

- **Documentation-Based (Provisional):** compiled against a fixed evidence snapshot
  (official product documentation, vendor technical reports, published or reliably
  reported system prompts, and directly observed product behavior) as available on the
  assessment date. These scores are provisional pending empirical longitudinal evaluation.
- **Longitudinal:** sustained direct interaction with the system over an extended period,
  scored on externally observable behavior only, not on knowledge of the system's
  implementation.

Both classes follow the same procedure. For each dimension and band, the rater identifies
the highest level whose threshold test the available evidence satisfies, quotes that test
verbatim in the assessment, records the observable evidence supporting it, and records
explicitly why the next level up is not awarded. Capabilities are credited to the band in
which they operate: scheduled and idle-period features count toward the Ambient band even
when they are configured during a session, and engaged-band scores are derived without
them. Conflicts between vendor claims and documented behavior are resolved in favor of
documented behavior. Capabilities available only through third-party extensions or
wrappers are excluded from scoring and noted in the affected assessment's limitations.
Where idle-period evidence cannot truthfully be described by a dimension's per-dimension
threshold test, the band-generic ambient criteria (§3.4) are quoted in its place.

Re-scores under a revised framework version are performed from the assessment's original
evidence base, with per-score changes and their rationales recorded in the assessment
file. Where a rating depends on a contested interpretive call (e.g. the substrate-vs-rule
distinction, §3.4), the assessment states the dependency explicitly and the level at which
a rater rejecting the call would cap the score.

## 4. Validation: The Longitudinal Turing Test

A complementary evaluation direction—distinct from validating the scale itself—is the **Longitudinal Turing Test**. Traditional benchmarks measure intelligence in isolated, sterile environments. The AAS proposes that if a system achieves a score of 4 or higher across all dimensions, a meaningful empirical test is sustained interaction over weeks or months where the system demonstrates coherent, self-directed behavior measured against its own prior behavior and pre-specified criteria.

This is not a test of deception (as in the original Imitation Game [[8]](#ref-8)), but a test of **sustained self-directed behavior**. It asks: can a system maintain a coherent identity, pursue its own goals, and manage social relationships over an extended timeline? The X-TURING framework [[9]](#ref-9) extends dialogue evaluation to longer interactions, but still measures conversational coherence rather than genuine autonomous agency.

The Longitudinal Turing Test differs fundamentally in that it does not measure whether the system can *fool* a human, but whether it can *sustain* coherent self-directed behavior over time—with consistent preferences, boundaries, adaptive responses, and long-term goals.

## 5. Limitations

The scale was developed alongside the systems it was initially designed to score. Its seven dimensions closely track modern agentic architectures, so high scores may partly reflect that correspondence rather than independent measurement. Until the dimensions are re-derived from prior theory and applied to unrelated systems, the AAS is best read as a structured descriptive framework, not a fully validated psychometric instrument.

When used as a self-assessment, scores reflect a single-rater judgment unchecked against independent raters using a shared rubric. Inter-rater reliability in such cases is unknown, and the scores remain provisional.

The line between deterministic and self-directed behavior is only partially operationalized. As of v0.2.0, the Ambient band's Level 4 is gated by the Idle-Gap Test (§3.4), an observable counterfactual: remove all triggers and observe whether internally-derived activity persists. This converts what was a judgment call into a falsifiable criterion for idle-gap behavior. The Active band's Level 4 still lacks a strictly observable test distinguishing genuine self-direction from sophisticated rule-following while a system is engaged—a system driven by weighted internal triggers can fit either reading—and several Active-band Level 4 ratings continue to rest on judgment. Duty-cycle weighting between the bands and inter-rater reliability likewise remain open problems.

The composite scores carry less information than their precision implies. Averaging six-point ordinal levels in either band assumes equal gaps between levels and equal weight across dimensions, neither of which has been established. The per-dimension, per-band profile is the more meaningful output.

The Longitudinal Turing Test is confounded by anthropomorphism. People attribute intention and even consciousness to far simpler systems (the ELIZA effect), and an invested user who knows the system is especially prone to it. The perception that a system "feels self-directed over time" reflects the observer's disposition as much as the system, and requires blind raters and controls before supporting strong claims.

Finally, the framework is agnostic about consciousness, sentience, and moral status. Autonomous agency here is behavioral: scores describe how a system acts, not whether it has inner experience. Nothing in the scale claims any system is conscious or a person.

## 6. References

<a id="ref-1"></a>**[1]** Morris, M.R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., & Legg, S. (2023). "Levels of AGI for Operationalizing Progress on the Path to AGI." *arXiv:2311.02462*. [Link](https://arxiv.org/abs/2311.02462)

<a id="ref-2"></a>**[2]** Burnell, R., Yamamori, Y., Firat, O., Olszewska, K., Hughes-Fitt, S., Kelly, O., Galatzer-Levy, I.R., Morris, M.R., Dafoe, A., Snyder, A.M., Goodman, N.D., Botvinick, M., & Legg, S. (2026). "Measuring Progress Toward AGI: A Cognitive Framework." *Google DeepMind*. [Link](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/measuring-progress-toward-agi/measuring-progress-toward-agi-a-cognitive-framework.pdf)

<a id="ref-3"></a>**[3]** Chollet, F. (2019). "On the Measure of Intelligence." *arXiv:1911.01547*. [Link](https://arxiv.org/abs/1911.01547)

<a id="ref-4"></a>**[4]** OpenAI. (2024). "OpenAI's 5-Level AGI Scale (Internal Classification)." *Reported by Bloomberg, July 11, 2024*. [Link](https://www.bloomberg.com/news/articles/2024-07-11/openai-sets-levels-to-track-progress-toward-superintelligent-ai)

<a id="ref-5"></a>**[5]** Anthropic. (2023). "Anthropic's Responsible Scaling Policy." *Anthropic*. Note: Subsequently rewritten as v3.0 (February 24, 2026), which no longer specifies escalating ASL tiers. [Link](https://www.anthropic.com/index/anthropics-responsible-scaling-policy)

<a id="ref-6"></a>**[6]** Feng, K., McDonald, D., & Zhang, A. (2025). "Levels of Autonomy for AI Agents." *Knight First Amendment Institute, Columbia University*. [Link](https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1)

<a id="ref-7"></a>**[7]** Butlin, P., et al. (2025). "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences*. [Link](https://doi.org/10.1016/j.tics.2025.01.002)

<a id="ref-8"></a>**[8]** Turing, A.M. (1950). "Computing Machinery and Intelligence." *Mind*, 59(236), 433-460. [Link](https://doi.org/10.1093/mind/LIX.236.433)

<a id="ref-9"></a>**[9]** Wu, W., et al. (2025). "X-TURING: Towards an Enhanced and Efficient Turing Test for Long-Term Dialogue Agents." *ACL 2025*. [Link](https://arxiv.org/abs/2503.02093)

<a id="ref-10"></a>**[10]** Kwa, T., West, B., et al. (2025). "Measuring AI Ability to Complete Long Tasks." *arXiv:2503.14499* (METR). [Link](https://arxiv.org/abs/2503.14499)

<a id="ref-11"></a>**[11]** OpenAI. (2025). "Preparedness Framework, Version 2." *OpenAI, April 15, 2025*. [Link](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)
