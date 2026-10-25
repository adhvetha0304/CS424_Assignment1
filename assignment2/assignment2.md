# CS 424 Assignment 2

## Exploring and Building Visualizations

## Task 1: Revisit Data and Questions
I revisited the Assignment 1 dataset before starting the visualization work. The dataset contains 28 observations collected across seven observation sessions and four shared spaces. I checked the data for duplicate observations, blank or inconsistent values, and other issues that could affect the analysis.

The original dataset already used `None` for `main_activity` when a space was empty, so I preserved those values during processing. I also validated the dates and kept them in a consistent `YYYY-MM-DD` format. I added `session_id` and `session_label` so that observations collected during the same session could be grouped consistently. I kept the September 27 time as `6-9 PM` because a more exact observation time was not recorded.

For this assignment, I will focus on these questions:

1. How does observed occupancy differ across the four shared spaces?
2. Which spaces show the most variation in occupancy across observation sessions?
3. How are activity type and noise level associated with observed occupancy?
4. Which observations stand out from the usual pattern for their space, and what context was recorded for them?

I am not using time of day as a main question because the temporal coverage is uneven, with most observations collected in the evening. The dataset still contains repeated observations of the same four spaces across seven sessions, so I am keeping the existing data for the initial exploration rather than collecting additional observations at this stage.

## Task 2: Data Transformation
I created a reproducible data preparation script in `scripts/prepare_data.py`. The script reads the original Assignment 1 data from `data/shared_spaces.csv` and produces `data/processed/shared_spaces_processed.csv`.

The processing preserves `None` as an existing activity value instead of treating it as missing data. It also checks that observation IDs are unique, converts the numeric fields to the correct types, removes accidental surrounding whitespace from categorical values, validates the dates, and checks that people counts are not negative.

I added two derived attributes for working with the repeated observations. `session_id` assigns each collection session a number from 1 to 7, and `session_label` provides a readable label containing the session number, date, and recorded time. The script also checks that every session contains four observations representing all four shared spaces.

I did not change the original Assignment 1 CSV. All processed data is written to a separate file so the original observations, transformation code, and visualization-ready data remain clearly separated.

## Task 3: Explore the Data

I created three exploratory visualizations using the processed dataset to look at differences in occupancy across spaces, changes between observation sessions, and how activity and noise level were related to the number of people observed.

### Occupancy Across Shared Spaces

![Occupancy by space](figures/eda/occupancy_by_space.png)

The first plot shows all seven observations for each space instead of just comparing averages. Study Lounge 1 had counts between 0 and 1, while Study Lounge 2 had counts between 0 and 2. The Gym and Common Area showed more variation, with maximum counts of 10 and 14 respectively. However, using the same vertical scale for all four spaces made smaller differences between the study lounges harder to see. This made me realize that comparing all the spaces in one view might not be enough to understand the patterns within each space.

### Occupancy Across Observation Sessions

![Occupancy by session](figures/eda/occupancy_by_session.png)

The heatmap helped me compare the four spaces within each observation session. The Gym had 10 people during the September 29 morning observation, while the Common Area had 14 people during the October 1 evening event. Later that same day, the Common Area had only 1 person. Looking at the individual sessions made it clear that averages alone could hide some of these differences. It also showed why keeping the session information was useful.

### Activity and Noise Level

![Occupancy by activity and noise](figures/eda/occupancy_activity_noise.png)

The third plot explored occupancy along with the recorded activity and noise level. All observations in the study lounges were labeled Quiet, while the Gym and Common Area included Moderate and Loud observations. The highest recorded counts in the Gym (10) and Common Area (14) were both labeled Loud, although the limited dataset does not establish a general relationship between noise and occupancy.

My initial plot had overlapping points, and the vertical axis did not show the full range of people counts. I corrected the scale and added small horizontal offsets to make repeated observations visible. Even after these changes, the shared scale made differences in the study lounges less noticeable. I also noticed that activity type was closely related to the purpose of each space, making comparisons across activities less straightforward. Some activities appeared only once or twice, which further limited what I could conclude.

### What I Learned

Overall, these plots showed me that individual observations and the context of each session are important, especially when looking at unusual counts. I also noticed a trade-off between comparing all four spaces using the same scale and being able to see smaller changes within spaces that usually had fewer people. For the next task, I want to explore different visualization designs that make it easier to compare occupancy across spaces while still allowing individual sessions and unusual observations to be examined.

## Task 4: Exploring Alternative Visualization Designs

I implemented three visualization approaches to explore different aspects of the shared-space observations. Each design focuses on a different analytical task, allowing me to compare what information it communicates effectively and what limitations remain.

### Direction A: Occupancy Distribution by Space

![Occupancy distribution](figures/alternatives/alternative_a_distribution.png)

This design focuses on comparing the occupancy distributions of the four shared spaces. It uses the space and people-count attributes, with horizontal position representing occupancy and vertical position separating the spaces. Individual observations are shown as circles, medians as diamonds, and observed ranges as horizontal lines.

The chart makes it easy to compare typical occupancy and identify differences in the observed ranges. For example, the Common Area reaches 14 people, while the two study lounges have much lower counts. However, the shared scale makes differences between smaller occupancy values harder to see, and the chart does not show when observations occurred or provide their recorded context.

I would keep this approach as a useful summary view, but it is not sufficient as the main visualization.

### Direction B: Occupancy Across Observation Sessions

![Session comparison](figures/alternatives/alternative_b_sessions.png)

This design focuses on comparing how the recorded occupancy differs across seven observation sessions. It uses small-multiple line charts, with one panel for each space. Horizontal position represents session order, and vertical position represents the number of people observed.

The shared vertical scale supports comparisons between spaces. It also makes unusual observations visible, including the Gym's count of 10 people in Session 3 and the Common Area's count of 14 in Session 5.

However, the sessions were collected at irregular intervals. Connecting the points may suggest continuous occupancy changes even though the dataset contains separate observations. The design also does not explain the activities or circumstances behind the counts.

I would retain the session comparison as a possible complementary overview, while reconsidering the connecting lines.

### Direction C: Interactive Observation Explorer

The third approach is an interactive Vega-Lite scatterplot that explores the relationship between occupancy, activity, and noise level.

[Open the interactive observation explorer](visualization/alternative_c.html)

Horizontal position represents people count, vertical position represents the recorded main activity, and color represents noise level. A dropdown filters the observations by space, while hovering over a point reveals its date, time, activity, noise level, and context notes.

This approach supports more detailed investigation than the first two designs. For example, selecting the Gym and hovering over the observation with 10 people reveals that it occurred on September 29 at 6 AM, with loud noise and exercise-related activity recorded.

The main limitation is overlapping marks. Some observations have the same people count and activity, causing multiple records to occupy the same position. As a result, not every observation can be inspected individually in the current implementation.

I would develop this direction further because its filtering and details-on-demand support the goal of investigating individual observations and understanding unusual counts in context.

### Comparison and Design Decision

The three approaches offer different strengths. Direction A is effective for summarizing distributions, Direction B supports comparisons across observation sessions, and Direction C allows users to explore individual observations and retrieve contextual information.

I selected Direction C as the starting point for further development because it addresses more of the original research questions through filtering and observation-level details. In the next iterations, I plan to address overlapping marks and investigate whether a complementary overview could improve comparisons across spaces and sessions.

These visualizations describe the 28 observations collected rather than establishing typical usage patterns for all days or times.

## Task 6: Iterating on the Selected Design

I selected the interactive observation explorer for further development because it allows users to examine individual observations and their recorded context. I focused on addressing problems identified while testing the initial design.

### Iteration 1: Making Individual Observations Accessible

**Problem:** In the original interactive scatterplot, people count was mapped to horizontal position and main activity to vertical position. Several observations had identical values for these attributes, causing their marks to overlap. This made some observations difficult or impossible to inspect individually.

**Change:** I changed the vertical encoding from main activity to observation ID. Each observation now occupies a separate row, while horizontal position continues to represent people count and color represents noise level. I preserved the space filter and hover tooltips.

[Open Iteration 1](visualization/iteration1.html)

**Result:** The revised design displays all 28 observations in separate rows. Testing confirmed that the space filters work and individual observations can be examined without marks completely covering one another. The original people counts remain unchanged.

**Trade-off:** Although this improves access to individual records, it makes activity patterns less immediately visible because activity is no longer represented directly on an axis. This suggests a need for a complementary overview that supports broader comparisons while retaining observation-level details.

