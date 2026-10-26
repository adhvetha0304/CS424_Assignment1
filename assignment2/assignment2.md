
# CS 424 Assignment 2

## Exploring and Building Visualizations

## Task 1: Revisit Data and Questions

For Assignment 2, I continued with the data I collected for Assignment 1: 28 observations of four shared spaces across seven sessions. I reviewed the CSV for missing or inconsistent values and checked how the observations were recorded before starting the visualizations.

The original data uses `None` as the activity when a space is empty, so I kept that value rather than treating it as missing. I also kept the September 27 time as `6-9 PM` because I had not recorded an exact time. To compare observations made during the same visit, I added session IDs and readable session labels.

The questions I focused on were:

1. How does occupancy differ across the four spaces?
2. Which spaces have the most variation between sessions?
3. How do the recorded activities and noise levels relate to occupancy?
4. Which observations stand out, and what was happening during those observations?

Most of my observations were in the evening, so I decided not to make time of day a main question. I used the existing data to explore these questions, without treating the results as typical occupancy patterns for every day or time.

## Task 2: Data Transformation

I used `scripts/prepare_data.py` to prepare the data. It reads `data/shared_spaces.csv` and saves a separate processed file at `data/processed/shared_spaces_processed.csv`.

The script checks observation IDs, dates, people counts, and whether each session includes all four spaces. It also removes extra spaces from category values and preserves `None` in `main_activity`. I added `session_id` (1 through 7) and `session_label` (the session number, date, and recorded time) so that I could organize the observations consistently.

I kept the original CSV unchanged. This way, the processing can be rerun and the processed values can be checked against the data I collected.

## Task 3: Explore the Data

I made three exploratory plots before choosing a visualization design.

### Occupancy Across Shared Spaces

![Occupancy by space](figures/eda/occupancy_by_space.png)

This plot shows the individual counts for each space. Study Lounge 1 had 0–1 people, and Study Lounge 2 had 0–2. The Gym reached 10 people, while the Common Area reached 14. The Gym and Common Area had noticeably more variation than the lounges.

Showing individual points was useful because I could see the range of observations rather than just an average. It was harder to notice small differences in the lounges when all four spaces used the same scale.

### Occupancy Across Observation Sessions

![Occupancy by session](figures/eda/occupancy_by_session.png)

The heatmap showed the counts for all four spaces in each session. Two observations stood out: 10 people in the Gym during the September 29 morning session, and 14 in the Common Area during the October 1 evening event. The Common Area had only 1 person at the later observation that day.

I found this view helpful for comparing individual sessions. It made me want to keep session information in the final design instead of relying only on summary statistics.

### Activity and Noise Level

![Occupancy by activity and noise](figures/eda/occupancy_activity_noise.png)

This plot compares occupancy with the recorded activities and noise levels. Both study lounges were recorded as Quiet, while the Gym and Common Area included Moderate and Loud observations. The highest counts in the Gym and Common Area were both Loud, but the data is too limited to say that more people always means more noise.

My first version had overlapping points and an incorrect vertical range, so I fixed the scale and added small offsets to separate repeated points. I also noticed that activities largely depended on the space itself, which made direct comparisons between activities less useful than I first expected.

### What I Took From the Exploration

The main thing I learned was that I needed both an overview of the counts and a way to look at individual observations. The unusual counts were easier to understand when I could also check when they happened and what I had recorded in the notes.

## Task 4: Exploring Alternative Visualization Designs

I tried three designs that focused on different tasks, rather than making small changes to the same chart.

### Direction A: Occupancy Distribution by Space

![Occupancy distribution](figures/alternatives/alternative_a_distribution.png)

For the first design, I wanted to compare the occupancy ranges of the four spaces. I placed people count on the horizontal axis and space on the vertical axis. Circles show the individual observations, diamonds show medians, and gray lines show the observed ranges.

This made it easy to see that the Common Area and Gym had larger ranges than the lounges. It worked well as a summary, but it did not tell me which sessions the counts came from. I kept it as a useful comparison, rather than choosing it as the main design.

### Direction B: Occupancy Across Observation Sessions

![Session comparison](figures/alternatives/alternative_b_sessions.png)

My second design uses four small line charts, one for each space. The horizontal axis shows session order, and the vertical axis shows people count. I used the same vertical scale so the charts could be compared.

I could follow the counts for each space and quickly spot the Gym's count of 10 and the Common Area's count of 14. I liked having a separate panel for each space. However, the lines connect observations collected at different times, which can make them look like continuous measurements. I wanted to keep the session comparison idea without relying on those connecting lines.

### Direction C: Interactive Observation Explorer

![Initial interactive design](figures/iterations/initial_interactive.png)

[Open the initial interactive visualization](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/alternative_c.html)

For the third design, I tried an interactive scatterplot using Vega-Lite. People count is on the horizontal axis, activity is on the vertical axis, and color shows noise level. I added a dropdown to filter by space and tooltips with the date, time, activity, and context notes.

When I selected the Gym, for example, I could hover over the 10-person observation and see the recorded details. I liked being able to check the context without putting every field on the chart. While testing the All Spaces view, I noticed that some observations had exactly the same activity and people count, so their circles covered one another. That was the main issue I wanted to address in the next version.

### Choosing a Direction

Direction A worked best for comparing ranges, and Direction B was useful for following the sessions. I decided to continue with Direction C because I found the observation details useful, especially for the unusually high counts. My goal was to keep that ability while making it easier to compare all four spaces.

## Task 5: Interaction and Multiple Views

I used interaction where it helped answer a question. The initial dropdown let me focus on one space, and the tooltips showed details without crowding the plot.

In the final version, I used a heatmap linked to a details panel. I can compare the 28 people counts first, then click a cell when I want to check its activity, noise level, time, or notes. I tested this with the Common Area observation of 14 people and the Gym observation of 10 people; the panel updated to the correct record in both cases. I also tested clearing the selection by double-clicking.

I preferred this to showing all the information at once because the main view stayed easy to read, while the extra information was still available when I needed it.

## Task 6: Iterating on the Selected Design

I made two larger changes to Direction C based on what I found while testing it.

### Iteration 1: Separating Overlapping Observations

![Iteration 1](figures/iterations/iteration1.png)

[Open Iteration 1](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration1.html)

**Problem:** In the first interactive plot, several circles overlapped because those observations had the same activity and people count.

**Change:** I changed the vertical axis from activity to observation ID, giving each observation a separate row. People count stayed on the horizontal axis, and I kept the noise colors, space filter, and tooltips.

**Result:** All 28 observations became individually visible and accessible. I tested the space filters and could inspect the records separately. The downside was that a list of observation IDs was not very helpful for comparing spaces or sessions. This led to the next change.

### Iteration 2: Combining an Overview With Observation Details

![Iteration 2](figures/iterations/iteration2.png)

[Open Iteration 2](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration2.html)

**Problem:** Iteration 1 fixed the overlap, but I still had to look through individual rows to compare the observations.

**Change:** I switched to a session-by-space heatmap. Each cell shows one observation using both its people count and color intensity. I linked it to an HTML details panel that updates when a cell is clicked.

**Result:** I could see all 28 counts together and inspect a specific observation without searching through overlapping points. Clicking Common Area in Session 5 showed the 14-person event on October 1 at 6 PM. Clicking Gym in Session 3 showed 10 people exercising on September 29 at 6 AM. I tested both selections and confirmed that the details changed correctly.

I preferred this version because the overview and individual details now worked together. Activity and noise are available in the details panel rather than directly on the heatmap, which is a choice I would like to evaluate with users later.

## Task 7: Current Working Design and Next Steps

My current design is Iteration 2: the occupancy heatmap with a linked details panel.

[Open the current working visualization](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration2.html)

Compared with my first sketches and earlier plots, this version is less focused on showing every attribute at the same time. The heatmap is for comparing counts across the four spaces and seven sessions. When a count stands out, I can click it to check the activity, noise level, date, time, and notes.

I think this works well with my dataset, especially for observations such as the 14-person Common Area event and the 10-person Gym session. It also avoids the overlapping marks from the original interactive plot.

For Assignment 3, I would like to see whether someone else can compare the spaces, find an unusual observation, and get its details without much explanation. I would also check whether the session labels are clear enough, since the sessions are ordered rather than spaced according to elapsed time. With only seven sessions, I would keep any conclusions limited to the observations I collected.
