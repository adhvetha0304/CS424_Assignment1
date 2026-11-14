# CS 424 Assignment 3 — Evaluation Protocol

## Evaluation Goal

**Evaluation question:** Does an interactive heatmap with noise highlighting and observation details help people answer comparison questions faster or more accurately than a static heatmap with a reference table?

In Assignment 2, my final heatmap showed occupancy counts but left noise and activity in a details panel, and I wasn't sure that made my third question (how noise relates to occupancy) easy to answer. Task A below tests that directly. Task B only asks about counts the heatmap already shows, so it works as a comparison point.

**H1:** Participants will complete the noise-and-occupancy questions (Task A) faster with the interactive version, because highlighting narrows the sessions they need to check.

**H2:** Completion times for the occupancy-change questions (Task B) will be similar in both versions, since the counts are visible in the heatmap either way.

I'll measure accuracy and completion time. The results may not support these hypotheses, and that is fine.

## Conditions

Both versions use the same 28 observations, four spaces, seven sessions, and occupancy color scale.

**Static version:** A non-interactive heatmap plus a reference table with the session, space, people count, noise level, activity, date, time, and context for all 28 observations. The table is grouped by space, with sessions 1–7 in order inside each space.

**Interactive version:** The same heatmap with two interactions:

- **Noise highlighting:** Pick any of the four spaces and a noise level, and the sessions where that space matches the noise level are highlighted. The other sessions stay visible but dimmed. The highlight can be cleared.
- **Details-on-demand:** Clicking a cell shows its date, time, people count, activity, noise level, and notes in a separate panel. Double-clicking clears the selection.

Both versions contain everything needed to answer every question. The goal is to compare how people reach the information, not to make one version easier.

## Analytical Questions

Each participant answers four questions: one Task A variant and one Task B variant with each visualization.

### Task A: Noise and Occupancy

These questions need three steps: check noise levels, add the counts from two spaces, and compare sessions.

**A1:** Among sessions where the Gym was recorded as Quiet, which session had the highest combined occupancy of the Gym and Common Area, and what was that count?

**Correct answer:** Session 2, 11 people.

- Session 2: 3 + 8 = 11
- Session 4: 2 + 4 = 6
- Session 6: 0 + 1 = 1

**A2:** Among sessions where the Common Area was recorded as Quiet, which session had the highest combined occupancy of the Gym and Common Area, and what was that count?

**Correct answer:** Session 4, 6 people.

- Session 4: 2 + 4 = 6
- Session 6: 0 + 1 = 1
- Session 7: 2 + 2 = 4

Both variants have three qualifying sessions. The noise condition matters because the session with the highest combined occupancy overall (Session 5) doesn't qualify in either question, so the answer can't be found just by spotting the darkest cell.

### Task B: Occupancy Changes

These questions ask for the largest absolute change in occupancy across all four spaces between two sessions. An absolute change is the difference between two counts, ignoring whether it went up or down.

**B1:** Between Sessions 1 and 3, which space had the largest absolute change in occupancy, and what was the change?

**Correct answer:** Gym, 6 people.

- Study Lounge 1: 1
- Study Lounge 2: 2
- Gym: 6
- Common Area: 0

**B2:** Between Sessions 2 and 5, which space had the largest absolute change in occupancy, and what was the change?

**Correct answer:** Common Area, 6 people.

- Study Lounge 1: 0
- Study Lounge 2: 2
- Gym: 2
- Common Area: 6

In both variants the largest change is 6 and the next-largest is 2, so they should be about equally hard. The pilot will help check that.

## Study Design

This is a within-subject study with at least 10 participants, and everyone uses both versions. One or two extra people do a pilot first, and their results are not included in the main analysis.

Five participants start with Static and five start with Interactive. Question variants are spread evenly across the two conditions, as the schedule shows.

### Participant Assignment Schedule

| Participant | First condition | Questions | Second condition | Questions |
|---|---|---|---|---|
| P01 | Static | A1, B1 | Interactive | A2, B2 |
| P02 | Static | A2, B2 | Interactive | A1, B1 |
| P03 | Static | A1, B2 | Interactive | A2, B1 |
| P04 | Static | A2, B1 | Interactive | A1, B2 |
| P05 | Static | A1, B1 | Interactive | A2, B2 |
| P06 | Interactive | A1, B2 | Static | A2, B1 |
| P07 | Interactive | A2, B1 | Static | A1, B2 |
| P08 | Interactive | A1, B1 | Static | A2, B2 |
| P09 | Interactive | A2, B2 | Static | A1, B1 |
| P10 | Interactive | A1, B1 | Static | A2, B2 |

Each question variant appears five times in each condition. Within each condition, Task A comes first, then Task B. IDs are assigned in recruitment order following this schedule.

If a participant withdraws, I'll recruit a replacement for the same schedule slot so the balance holds. The withdrawn participant's data is kept separately and left out of the 10-participant analysis. I won't fill in values for tasks they didn't complete.

## Participant Instructions

Every participant hears the same script:

"You will use two versions of a visualization showing observations of four shared spaces. Both contain the same data.

You will answer four questions about occupancy and noise levels. Some questions will require comparing several spaces or sessions.

One version has a reference table. The other lets you highlight sessions based on noise level and click cells for more details.

Please answer independently and as accurately as possible. You will have up to two minutes for each question.

I will record your answers and how long you take, using an anonymous participant ID. You will not receive feedback about whether your answers are correct during the study.

Participation is voluntary, and you can stop at any time."

Before the timed questions, I demonstrate how to read the heatmap, use the reference table, and use the interactive controls. The demonstration uses a separate practice example with different data, so it doesn't reveal any study answers.

## Study Procedure

1. Ask for the participant's agreement and assign an anonymous ID.
2. Record their familiarity with charts: Beginner, Intermediate, or Advanced.
3. Read the instructions and give the practice demonstration.
4. Open the first assigned visualization with no selections or highlights.
5. Show Task A. The stopwatch starts when the question and visualization are both visible.
6. Timing stops at the participant's final answer or at 120 seconds.
7. Record the answer, time, and correctness.
8. Reset the visualization and repeat for Task B.
9. Switch to the second condition and repeat with the assigned variants.
10. Note any difficulties or comments, without identifying the participant.

No hints or correctness feedback are given between questions.

I'll use the same laptop, browser, screen size, and 100% zoom for everyone when possible, and time with a stopwatch. Any difference in device or setting gets recorded.

## Measurements and Scoring

Results go in `assignment3/study/results.csv`, with one row per participant per question. Ten participants with four questions each gives 40 task records.

| Column | Description |
|---|---|
| `participant_id` | Anonymous ID, P01–P10 |
| `visualization_familiarity` | Beginner, Intermediate, Advanced |
| `condition_order` | Static-first or Interactive-first |
| `condition` | Static or Interactive |
| `task_type` | A or B |
| `variant` | A1, A2, B1, or B2 |
| `task_order` | Position from 1 to 4 |
| `response` | Participant's final answer |
| `accuracy` | 1 = correct, 0 = incorrect |
| `time_seconds` | Completion time in seconds |
| `timed_out` | 1 = timed out, 0 = completed |
| `device` | Device and testing setup used |
| `notes` | Relevant difficulties or observations |

**Scoring**

- Task A is correct only if the participant gives both the right session and the right combined count.
- Task B is correct only if the participant gives both the right space and the right absolute change.
- Wrong or incomplete answers get accuracy 0.
- Each question has a 120-second limit. If time runs out, I record 120 seconds, accuracy 0, and `timed_out = 1`.
- If the participant answers within the limit, I record the actual time and `timed_out = 0`, whether or not the answer is right.

## Pilot Study

Before the main study, I'll try the procedure with one or two people who won't be among the 10 main participants. I'll check whether:

- Both versions give all the information needed to answer the questions.
- The reference table is easy to navigate.
- The highlighting and cell selection make sense to a new user.
- The question variants are about equally hard.
- The instructions and practice example are clear.
- Two minutes is the right time limit.
- Answers and times can be recorded consistently.

Problems and changes go in `assignment3/study/pilot_notes.md`. The visualizations, practice materials, questions, and scoring are drafted before the pilot and revised afterward if needed. Once the main study begins, nothing changes.

## Analysis Plan

I'll use Python, Pandas, and Matplotlib to compare accuracy and completion time between Static and Interactive. The analysis will include:

- Overall accuracy for each condition.
- Mean and median completion time for each condition.
- Accuracy and time for Task A and Task B separately.
- Differences between individual participants.
- One chart comparing accuracy and one comparing completion time.

I'll compare the results with H1 and H2 and discuss whether interaction helped, made little difference, or made some questions harder. I'll also consider participants' chart experience, the small sample, learning effects, and anything I notice during testing. Task A always comes before Task B inside each condition, so question position could affect results, and I'll mention that as a limitation.

I'm not planning significance tests, since they aren't required. Conclusions will rest on the measurements, not on an assumption that the interactive version is better.