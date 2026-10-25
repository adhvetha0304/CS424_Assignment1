# CS 424 Assignment 2

## Exploring and Building Visualizations

## Task 1: Revisit Data and Questions

For this assignment, I continued working with the dataset I collected for Assignment 1. It contains 28 observations of four shared spaces, collected across seven observation sessions. Before creating the visualizations, I reviewed the data again to check for duplicate observations, missing values, and anything else that might affect the analysis.

The original dataset already used `None` for `main_activity` when a space was empty, so I kept those values. I also checked the dates and kept them in a consistent `YYYY-MM-DD` format. Since each session included observations from all four spaces, I added `session_id` and `session_label` to make it easier to compare the spaces within the same session. For September 27, I kept the recorded time as `6-9 PM` rather than assigning an exact time that was not recorded.

The questions I wanted to explore were:

1. How does occupancy differ across the four shared spaces?
2. Which spaces show the most variation across observation sessions?
3. How are activity type and noise level related to the number of people observed?
4. Which observations are unusual compared with the other observations of the same space, and what was happening at those times?

I decided not to focus mainly on time of day because most of my observations were collected in the evening. The dataset is also fairly small, so the results can describe what I observed, but they cannot establish how these spaces are generally used at all times.

I kept the same dataset for this assignment because it was sufficient to explore the initial visualization designs, while keeping these limitations in mind.

## Task 2: Data Transformation

I wrote a Python script, `scripts/prepare_data.py`, to prepare the dataset for visualization. It reads the original file from `data/shared_spaces.csv` and saves the processed version as `data/processed/shared_spaces_processed.csv`.

The script checks that observation IDs are unique, people counts are nonnegative, dates are valid, and each session contains one observation for each of the four spaces. It also converts numeric fields to the correct types and removes extra whitespace from categorical values.

One thing I had to be careful about was the `None` activity value. This was already present in the original data for empty spaces, so I made sure Python preserved it rather than treating it as a missing value.

I added two columns:

- `session_id`, which numbers the seven observation sessions from 1 to 7.
- `session_label`, which provides a readable label with the session number, date, and recorded time.

I did not modify the original CSV. Keeping the raw and processed files separate makes it easier to check the transformations and reproduce the visualizations.

## Task 3: Explore the Data

I started with three exploratory plots to better understand the occupancy counts and see which types of visualizations might work for the final design.

### Occupancy Across Shared Spaces

![Occupancy by space](figures/eda/occupancy_by_space.png)

This plot shows the individual people counts for each shared space.

Study Lounge 1 had between 0 and 1 people, and Study Lounge 2 had between 0 and 2. The Gym reached 10 people, while the Common Area reached 14. These two spaces also showed much more variation than the study lounges.

I found it useful to see individual observations instead of just an average. However, because all four spaces shared the same scale, smaller differences in the study lounges were not very noticeable. This made me think more carefully about how to compare spaces with different occupancy ranges.

### Occupancy Across Observation Sessions

![Occupancy by session](figures/eda/occupancy_by_session.png)

I then created a heatmap to compare occupancy across the seven observation sessions.

The Gym had 10 people during the September 29 morning session, while the Common Area had 14 during the October 1 evening event. The Common Area had only 1 person during the later session that same day.

This plot helped me see how much the counts could differ between observations. It also showed that using only average occupancy would hide some interesting differences. The session information was therefore important to keep in the later designs.

One limitation is that the sessions are shown at equal distances even though the actual time intervals between them were different.

### Activity and Noise Level

![Occupancy by activity and noise](figures/eda/occupancy_activity_noise.png)

For the third plot, I looked at the recorded activity and noise level alongside occupancy.

All observations of the two study lounges were labeled Quiet, while the Gym and Common Area included Moderate and Loud observations. The highest counts in the Gym and Common Area were both labeled Loud, but there are too few observations to conclude that higher occupancy always leads to more noise.

My first version had overlapping points, and the vertical scale did not show the full range of counts. I corrected the scale and added small offsets to make repeated observations easier to see.

I also noticed that activities were closely related to the spaces where they occurred. For example, exercise-related activity was mainly associated with the Gym. Because of this, comparing activities without considering the space could be misleading. Some activities were also recorded only once or twice.

### What I Learned From the Exploration

The exploratory plots showed me that the individual observations matter, especially when a count is unusually high or low. I also realized that there was a trade-off between comparing all four spaces on the same scale and making the smaller differences within each space visible.

For the next task, I wanted to try designs that could compare occupancy across spaces while still making it possible to examine individual sessions and the context behind unusual observations.

## Task 4: Exploring Alternative Visualization Designs

I created three different visualization designs. Rather than changing only the colors or appearance, I tried to make each one answer a different question.

### Direction A: Occupancy Distribution by Space

![Occupancy distribution](figures/alternatives/alternative_a_distribution.png)

My first design focused on comparing the occupancy distributions of the four spaces.

I used horizontal position for the number of people and vertical position to separate the spaces. The circles represent individual observations, the orange diamonds show the medians, and the horizontal lines show the observed ranges.

This design makes it fairly easy to compare the usual occupancy levels and see which spaces have larger ranges. For example, the Common Area has a much wider range than either study lounge.

The main problem is that the shared scale makes differences between small counts harder to see. It also does not show which session an observation belongs to or what activity was happening.

I would keep this design as a summary of occupancy distributions, but I would not use it by itself as the final visualization.

### Direction B: Occupancy Across Observation Sessions

![Session comparison](figures/alternatives/alternative_b_sessions.png)

For the second design, I used small-multiple line charts, with a separate chart for each space.

The horizontal position represents the observation session, and the vertical position represents the number of people observed. I used the same vertical scale across all four charts so their counts could be compared.

This version made it easier to follow the recorded counts for each space across the seven sessions. The Gym's count of 10 in Session 3 and the Common Area's count of 14 in Session 5 stood out clearly.

However, I realized that the connecting lines could be misleading. Since I did not observe the spaces continuously, the lines might suggest that I measured occupancy changes between sessions. The actual observations were also collected at irregular time intervals.

I liked the session-based comparison, but I would reconsider the connecting lines and use this mainly as an overview.

### Direction C: Interactive Observation Explorer

[Open the interactive observation explorer](visualization/alternative_c.html)

My third design was an interactive Vega-Lite scatterplot. I wanted to see whether interaction would make it easier to explore the recorded activity, noise level, and context.

The horizontal position represents people count, the vertical position represents main activity, and color represents noise level. I also added a dropdown to filter by space and tooltips to show the details of individual observations.

For example, when I filtered the chart to the Gym and hovered over the observation with 10 people, I could see its date, time, activity, noise level, and context notes.

I liked that I could explore individual observations without putting all the information directly on the chart.

However, I noticed a problem when looking at all four spaces together. Several observations had the same activity and people count, so their circles appeared in exactly the same position. This meant I could not easily access every observation.

I decided to continue with this design because the filtering and observation details were useful, but I needed to fix the overlapping points.

### Comparing the Three Designs

Each design worked better for a different task. Direction A was useful for comparing distributions, Direction B made session differences easier to follow, and Direction C was better for examining individual observations and their context.

I chose Direction C for further development because I wanted the final visualization to support both comparisons and a closer look at unusual observations.

My plan was to first fix the overlapping points and then find a better way to combine occupancy comparisons with individual observation details.

All three designs use the 28 observations I collected, so the patterns should be interpreted as results from this dataset rather than general conclusions about how the spaces are always used.

## Task 5: Interaction and Multiple Views

I explored interaction because I wanted users to do more than just look at a static chart. In particular, I wanted them to compare occupancy across spaces and sessions, then examine the context behind an individual observation.

In Direction C, I first added a dropdown to filter observations by space and tooltips to show more information when hovering over a point. The filter reduced the number of observations shown, while the tooltips provided details without making the chart too crowded.

After testing this version, I found that overlapping points made some observations difficult to inspect. I addressed this in the first iteration by giving every observation its own row.

In the second iteration, I introduced a session-by-space heatmap together with a separate details panel. The heatmap provides an overview of all 28 occupancy counts, and clicking a cell displays the selected observation's information below it.

I tested the selection using the Common Area observation with 14 people and the Gym observation with 10 people. In both cases, the details panel updated to show the corresponding record.

I found this interaction more useful than displaying every attribute at once. It allows the overview to remain relatively simple while still providing the activity, noise level, date, time, and context when needed.

The main limitation is that activity and noise patterns are not immediately visible in the overview, since those attributes are shown only after selecting an observation.

## Task 6: Iterating on the Selected Design

I continued developing Direction C because it was the most useful starting point for examining individual observations. I made two main changes based on the problems I noticed while testing the visualizations.

### Iteration 1: Making Individual Observations Accessible

**Problem:** In the original interactive scatterplot, multiple observations had the same people count and main activity. Their circles overlapped, so some records were difficult to inspect separately.

**Change:** I replaced main activity on the vertical axis with observation ID. Every observation now has its own row, while horizontal position still represents people count and color represents noise level. I kept the space filter and hover tooltips.

[Open Iteration 1](visualization/iteration1.html)

**Result:** This version shows all 28 observations separately. I tested the filters for all four spaces and checked that individual observations could still be inspected. The actual people counts were not changed.

**What did not work as well:** Although the overlapping-point problem was fixed, the observation IDs were not very useful for seeing patterns across activities or sessions. I could examine individual records, but it was harder to compare the spaces at a glance.

This led me to reconsider how the information should be organized.

### Iteration 2: Adding an Overview and Details Panel

**Problem:** Iteration 1 made every record accessible, but arranging the observations by ID did not make comparisons between spaces and sessions very easy.

**Change:** I created a heatmap showing the four spaces across seven observation sessions. Each cell represents one observation, with color intensity and a number showing its people count.

I also added a details panel below the heatmap. Clicking a cell displays the selected observation's date, time, people count, activity, noise level, and context notes.

[Open Iteration 2](visualization/iteration2.html)

**Result:** This version makes it easier to compare all 28 counts while still looking at individual observations.

For example, clicking the Common Area cell in Session 5 shows 14 people during an event on October 1 at 6 PM. Clicking the Gym cell in Session 3 shows 10 people during an exercise-related observation on September 29 at 6 AM.

I tested both selections and confirmed that the details panel displayed the corresponding information.

**What could still be improved:** Although the heatmap works well for comparing people counts, it does not directly show activity or noise level. Users need to click individual cells to see those details.

Also, the sessions are equally spaced on the horizontal axis even though the observations were collected at irregular intervals. The axis represents the order of the sessions, not continuous time.

Overall, I preferred this version because it made comparing occupancy and examining individual observations part of the same process.

## Task 7: Current Working Design and Next Steps

My current working design is the coordinated heatmap and details panel from Iteration 2.

[Open the current working visualization](visualization/iteration2.html)

The design has two main parts. The heatmap shows occupancy across the four spaces and seven sessions, while the details panel displays information about whichever observation is selected.

This version is different from my earlier designs because I no longer try to show all the attributes using one set of marks. Instead, I use the heatmap for comparing occupancy and the details panel for examining the activity, noise level, and context.

I think this works better for my dataset because users can quickly notice observations such as the Common Area count of 14 or the Gym count of 10 and then check what was recorded during those observations.

The main interactions are also straightforward: clicking a cell selects an observation and updates the details panel. This avoids the overlapping-point problem I had in the earlier scatterplot.

There are still limitations I would like to address in Assignment 3. The dataset contains only seven observation sessions, with uneven coverage across dates and times, so I cannot make broader claims about typical occupancy. The heatmap also does not show how much actual time passed between observations.

For the next assignment, I would like to evaluate whether users can identify unusual observations, compare spaces, and retrieve the relevant context without confusion. I would also look at whether adding a simple way to compare activity or noise patterns would help, or whether that would make the interface too complicated.

For now, I think the coordinated view is the strongest of the designs I tested because it provides both a useful overview and a way to examine individual records in more detail.