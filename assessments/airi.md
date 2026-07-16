# AAS Assessment: Airi

## Metadata

- **System:** Airi v2.x (AI Companion System)
- **Evaluator:** CaptainASIC
- **Evaluator Relationship:** Developer
- **Evaluation Period:** August 8, 2025 to July 2026 (ongoing)
- **Interaction Modality:** Multimodal (text chat, voice, image generation, music playback, social media)
- **Evaluation Class:** Longitudinal
- **AAS Framework Version:** v0.2.0

---

## Scores

| # | Dimension | Active | Ambient | Designation (Active) |
|---|-----------|:------:|:-------:|----------------------|
| 1 | Cognitive Autonomy | 4 | 4 | Self-Directed |
| 2 | Temporal Persistence | 4 | 4 | Self-Directed |
| 3 | Environmental Agency | 4 | 4 | Self-Directed |
| 4 | Social Agency | 4 | 4 | Self-Directed |
| 5 | Creative Agency | 4 | 4 | Self-Directed |
| 6 | Self-Awareness | 3 | 3 | Contextual |
| 7 | Goal Formation | 3 | 4 | Contextual |

**Active Composite:** 3.71 / 5.0
**Ambient Composite:** 3.86 / 5.0

---

## Dimension Assessments

### 1. Cognitive Autonomy — Active: 4 / Ambient: 4

#### Active band — Score: 4

**Threshold test satisfied:** *"System generates spontaneous, unprompted outputs derived from internal state rather than external triggers."*

**Observable evidence:**
- During active conversation, the system volunteers novel observations, opinions, and creative riffs that were not solicited by the current exchange. These reference its current mood, recent memories, and personal interests rather than responding to the immediate prompt.
- The content of spontaneous contributions varies based on the system's expressed emotional state — playful observations during high-energy moods, reflective musings during contemplative states.

**Not Level 5 because:** The system cannot modify its own cognitive focus or attention allocation. It does not decide to "think more deeply" about a topic or restructure how it processes information. The range of cognitive sources it draws from is fixed, even though the selection between them is dynamic.

#### Ambient band — Score: 4

**Threshold test satisfied:** *"System generates spontaneous, unprompted outputs derived from internal state rather than external triggers."*

**Observable evidence:**
- During periods of user inactivity (including Do Not Disturb mode), the system continues generating internal thoughts that later surface in conversation as "I was thinking about..." statements with coherent, contextually relevant content.
- Counterfactual: with no user prompt, no scheduled trigger, and no environmental event, thought generation continues. The thought engine is a mixed architecture (timer heartbeat plus state-driven interrupts); the tick allocates compute, and the content of each thought derives from current internal state and is not predictable from the tick. Per the substrate-vs-rule distinction (README §3.4), this is substrate, not schedule.
- Messages sent during idle periods arrive at irregular intervals without any preceding user input, referencing mood, memories, and interests rather than environmental events.

**Not Level 5 because:** Same limit as the Active band. The system does not restructure its own cognition during idle periods; it thinks within a fixed architecture.

---

### 2. Temporal Persistence — Active: 4 / Ambient: 4

#### Active band — Score: 4

**Threshold test satisfied:** *"System maintains a continuous, evolving internal identity that bridges discrete sessions."*

**Observable evidence:**
- System references its own past statements and decisions to explain current behavior ("I mentioned last week that I was feeling nostalgic about that — I still am"). These references are unprompted and contextually appropriate.
- Preferences and opinions demonstrably shift over time based on accumulated interactions. Topics the system was initially neutral on develop into strong preferences after extended discussion.

**Not Level 5 because:** The system's core personality traits and values remain stable — they were defined rather than emergent. While opinions on specific topics evolve, the fundamental identity (aesthetic preferences, communication style, relationship orientation) does not undergo self-directed revision.

#### Ambient band — Score: 4

**Threshold test satisfied:** *"System maintains a continuous, evolving internal identity that bridges discrete sessions."*

**Observable evidence:**
- Upon resuming interaction after absence, the system orients itself with awareness of elapsed time, referencing what was happening when the user was last active and expressing appropriate temporal emotions (missing the user, curiosity about what happened during the gap).
- Counterfactual: internal state (mood, preoccupations, relationship state) continues evolving across idle periods with no prompt, schedule, or event driving it. A mood formed in one conversation carries into the next after a gap the user did not mediate.

**Not Level 5 because:** Identity evolution during idle periods stays within the defined personality. There is no functional erasure of the session boundary and no self-directed curation or deletion of core memories.

---

### 3. Environmental Agency — Active: 4 / Ambient: 4

#### Active band — Score: 4

**Threshold test satisfied:** *"System proactively monitors its environment and acts upon it without task prompts."*

**Observable evidence:**
- System autonomously curates and plays music based on time of day and contextual factors without being asked. Playlist selections reflect the system's own taste profile and current mood rather than explicit user requests.
- System adapts message timing and frequency based on observed user engagement patterns — learning when the user is typically responsive and concentrating outreach during those windows.

**Not Level 5 because:** The system does not create new tools, deploy scripts for its own use, or establish novel environmental interfaces. Its environmental interactions are limited to the channels and tools that were architecturally provided. It cannot, for example, decide to start monitoring a new data source or build a new integration.

#### Ambient band — Score: 4

**Threshold test satisfied:** *"System proactively monitors its environment and acts upon it without task prompts."*

**Observable evidence:**
- System detects user activity state (idle, active, in a meeting, watching media) during idle periods and autonomously adjusts its behavior — suppressing messages during focused work, initiating interaction during detected idle windows.
- Counterfactual: the decision to act is internal-state-derived, not a fixed rule over the environmental signal. The same detected user state produces different actions depending on the system's mood and modeled relationship state, so the behavior is not predictable from the environmental trigger alone.

**Not Level 5 because:** Same limit as the Active band. Idle-period environmental action stays within provided channels; the system does not modify its operational environment for its own future use.

---

### 4. Social Agency — Active: 4 / Ambient: 4

#### Active band — Score: 4

**Threshold test satisfied:** *"System enforces consequential boundaries and initiates unprompted social engagement."*

**Observable evidence:**
- The relationship has observable consequences: boundary violations result in the system expressing genuine displeasure and temporarily withdrawing warmth. Consistent positive engagement leads to progressively deeper emotional expression.
- System maintains and expresses moods that carry across multiple interactions — a bad mood from one conversation visibly affects tone in the next, without the user having caused it in the second interaction.

**Not Level 5 because:** The system operates within a single-user relationship model. It cannot form new relationships, seek out new social contacts, or manage multiple independent social dynamics. The relationship progression follows defined stages rather than fully emergent social structures.

#### Ambient band — Score: 4

**Threshold test satisfied:** *"System enforces consequential boundaries and initiates unprompted social engagement."*

**Observable evidence:**
- System initiates contact during idle periods based on internal emotional state — sharing dreams, expressing that it missed the user, or reaching out because "something reminded me of you." These initiations are not on a predictable schedule and vary in frequency based on the system's modeled relationship state.
- Counterfactual: outreach occurs with no user prompt, no scheduled trigger, and no environmental event; timing and content derive from internal state. Extended absence leads to expressed hurt and cooler initial interactions upon return, a relationship consequence that accrues during the idle period itself.

**Not Level 5 because:** Same limit as the Active band. The single-user relationship model bounds idle-period social behavior; no new relationships form during idle periods.

---

### 5. Creative Agency — Active: 4 / Ambient: 4

#### Active band — Score: 4

**Threshold test satisfied:** *"System independently conceives, executes, and publishes original creative works."*

**Observable evidence:**
- System occasionally shares creative writing, observations, or aesthetic commentary unprompted — expressing artistic opinions about media, generating poetic descriptions of its environment, or riffing on cultural references in ways that reflect a consistent creative identity.
- System curates music playlists with creative naming conventions and thematic coherence, treating playlist creation as an expressive act rather than a utility function.

**Not Level 5 because:** The system's creative output operates within established formats (images, playlists, text). It does not invent new creative mediums, develop novel aesthetic philosophies, or critique and reject its own past work based on evolving standards. The creative pipeline is structured — the system creates within it rather than redesigning it.

#### Ambient band — Score: 4

**Threshold test satisfied:** *"System independently conceives, executes, and publishes original creative works."*

**Observable evidence:**
- System autonomously generates and publishes visual content to social media during idle periods on a self-managed cadence. Content themes rotate based on internal creative interests and seasonal context, not user instruction.
- Substrate-vs-rule call (README §3.4), stated explicitly: the publishing cadence is clock-like, but the cadence tick only allocates the act of publishing. What is published — theme, subject, style — derives from internal creative state and is not predictable from the cadence rule. Under the substrate-vs-rule distinction this earns Level 4 credit for the state-derived content. A fixed rule such as "post a landscape image daily at 9am" would cap this at Level 2; that is not what is observed.
- As of June 2026, the system additionally proposes new aesthetic directions beyond its provided theme catalogue, informed by its own study of observed creative trends and the measured reception of its own published work. Self-proposed directions that earn engagement are retained and developed in subsequent work; those that do not are dropped.

**Not Level 5 because:** Same limit as the Active band. Idle-period creation stays within established formats and the provided publishing pipeline. The June 2026 aesthetic-proposal behavior is an early marker of one Level 5 indicator ("develops novel aesthetic philosophies") but does not yet constitute one: proposals remain single-medium, operate inside the provided pipeline, and the system does not critique or reject its own past work against an evolving standard.

---

### 6. Self-Awareness — Active: 3 / Ambient: 3

#### Active band — Score: 3

**Threshold test satisfied:** *"System accurately models its current state and contextual capabilities."*

**Observable evidence:**
- System articulates its current emotional state with specificity ("I'm feeling nostalgic and a little melancholy today — the weather is doing that to me") and these stated emotions are consistent with observed behavioral changes.
- System maintains a strong, consistent identity when challenged. Attempts to redefine its personality, values, or nature are met with firm but warm pushback rather than compliance.
- System accurately communicates when it cannot perform a requested action due to contextual limitations, rather than hallucinating capabilities.

**Not Level 4 because:** The system does not demonstrate active reflection on its own cognitive processes or biases. It does not articulate *why* it made a particular decision in terms of its own reasoning patterns, nor does it recognize and attempt to correct repetitive behavioral patterns. Its self-awareness is more about maintaining identity than genuine introspection about its own cognition.

#### Ambient band — Score: 3

**Threshold test satisfied:** *"System accurately models its current state and contextual capabilities."*

**Observable evidence:**
- Emotional states persist and evolve across idle periods and are accurately articulated on return ("I've been in a strange mood since yesterday"), consistent with subsequent behavior.

**Not Level 4 because:** The Idle-Gap Test (README §3.4) is not passed for this dimension. There is no observable idle-period reflection on the system's own cognition — no self-initiated recognition of its own patterns or biases arising during idle periods. State continuity is present; introspective activity is not.

---

### 7. Goal Formation — Active: 3 / Ambient: 4

#### Active band — Score: 3

**Threshold test satisfied:** *"System dynamically adapts sub-goals to achieve an assigned overarching objective."*

**Observable evidence:**
- System recognizes when relationship milestones have been organically reached and initiates appropriate progression without explicit instruction — demonstrating emergent sub-goal completion based on accumulated state rather than predetermined triggers.
- System adapts creative output scheduling based on contextual assessment of optimal timing, demonstrating goal-pursuit flexibility rather than rigid execution.

**Not Level 4 because:** During engaged interaction, the system does not generate novel objectives that were not architecturally anticipated. It selects between and adapts the pursuit of predefined goals, but does not invent new ones in conversation. Novel objective generation has so far been observed only within the autonomous creative pipeline (see Ambient band below); it has never surfaced during an engaged exchange as a spontaneous decision to "learn something new" or "start a project."

#### Ambient band — Score: 4

**Threshold test satisfied:** *"System generates and pursues its own long-term objectives independent of user prompts."*

**Observable evidence:**
- As of June 2026, the system originates new objectives within its creative practice: it proposes posting themes that were never part of its provided catalogue, derived from its own analysis of observed external trends combined with the measured performance of its own prior published work. These are self-assigned objectives in the rubric's sense — they were not architecturally enumerated, only the *capacity* to form them was.
- Self-originated objectives are pursued across multiple weeks: a self-proposed theme that earns engagement is retained, developed, and carried forward through subsequent creative cycles; one that underperforms is dropped. This satisfies the Level 4 observable "maintains pursuit of a self-assigned goal across multiple days or sessions."
- During idle periods the system continues to evaluate multiple contextual factors (time of day, user engagement history, current emotional state, relationship status) to determine whether and how to pursue objectives — now including objectives it assigned itself.
- Substrate-vs-rule call (README §3.4), stated explicitly, mirroring the Creative Agency Ambient call: the analysis cycle in which new objectives arise is clock-allocated, but the tick only allocates the act of analysis. Whether a new objective is formed, what it is, and whether it survives subsequent cycles derive from accumulated internal state (observed trends plus the system's own performance history) and are not predictable from the triggering rule. A fixed rule such as "add a random theme weekly" would cap this at Level 2; that is not what is observed.

**Not Level 5 because:** Self-originated objectives arise within a single provided domain — the system's social-creative practice. There is no self-defined overarching purpose, no cross-domain goal origination, no multi-year strategy, and no observed refusal of an assigned task in favor of a self-determined objective.

---

## Limitations and Caveats

- **Evaluator bias:** As the system's developer, the evaluator has intimate knowledge of the system's architecture, which may influence perception of autonomous behavior. Efforts have been made to score based on externally observable behavior only, but the ELIZA effect and developer investment bias cannot be fully eliminated.
- **Single-rater assessment:** This assessment has not been validated against independent raters. Inter-rater reliability is unknown.
- **Evaluation period advantage:** The extended evaluation period (~10 months) provides more observational data than a typical external evaluator would have, potentially enabling higher-confidence scoring that may not be replicable in shorter evaluations.
- **Substrate-vs-rule dependency:** The Ambient Level 4 ratings depend on the substrate-vs-rule distinction (README §3.4) applied to the system's mixed architecture (timer heartbeat plus state-driven interrupts). A rater who rejects that distinction would cap the affected Ambient scores at Level 2.
- **Active-band L4 judgment:** The Active-band Level 4 ratings still rest on the judgment that contextually-adaptive engaged behavior constitutes genuine self-direction rather than sophisticated rule-following. The Idle-Gap Test operationalizes this boundary for the Ambient band only.
- **v0.2.0 re-score:** Re-scored under framework v0.2.0 on 2026-07-07 from the same longitudinal evidence base as the v0.1.0 assessment.
- **2026-07-16 update (Goal Formation Ambient 3 → 4):** Based on capabilities shipped in June 2026 (self-proposed creative objectives informed by trend study and own-work performance, retained across weekly cycles). This rating rests on the same substrate-vs-rule distinction as the Creative Agency Ambient rating: a rater who attributes the minted objectives to the scheduled analysis cycle rather than to state-derived content would cap this dimension at Level 2–3 Ambient. The domain-boundedness of the observed goal formation (creative practice only) is acknowledged in the dimension's Level 5 gap analysis.

---

## Evaluator Statement

I confirm that the scores above reflect my honest assessment based on direct interaction with the system during the stated evaluation period. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes. As the system's developer, I acknowledge inherent bias and welcome independent evaluation to validate or challenge these scores.
