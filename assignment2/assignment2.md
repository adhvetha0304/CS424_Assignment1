
# CS 424 Assignment 2

## Exploring and Building Visualizations

## Task 1: Revisit Data and Questions

For Assignment 2, I continued working with the dataset I collected for Assignment 1. It contains 28 observations of four shared spaces across seven observation sessions. I reviewed the data again before creating the visualizations, checking for missing values, duplicate observations, and inconsistencies in how the information was recorded.

I kept `None` as the activity for observations where a space was empty rather than treating it as missing data. I also kept the September 27 time as `6-9 PM` because I had not recorded a more exact time.

My original Assignment 1 questions included comparing occupancy by time of day. However, five of my seven sessions were in the evening, with only one morning and one afternoon session. I decided to focus more on differences between spaces and individual observation sessions, since the available data would not support a meaningful comparison of typical morning, afternoon, and evening occupancy.

The questions I focused on were:

1. How does occupancy differ across the four spaces?
2. Which spaces have the most variation between observation sessions?
3. How do the recorded activities and noise levels relate to occupancy?
4. Which observations stand out, and what was happening during those observations?

I kept the existing dataset because I had observations of all four spaces during each session, with enough variation to compare different visualization designs. The results are still limited to the observations I collected, rather than representing how these spaces are used at all times.

## Task 2: Data Transformation

I used `scripts/prepare_data.py` to prepare the dataset. The script reads the original data from `data/shared_spaces.csv` and saves the processed version to `data/processed/shared_spaces_processed.csv`.

The script checks for duplicate observation IDs, valid dates, nonnegative people counts, and whether every session includes all four spaces. It also removes extra whitespace from categorical values and preserves `None` in `main_activity`.

I added two columns:

- `session_id` assigns a number from 1 to 7 to each observation session.
- `session_label` includes the session number, date, and recorded time.

These columns made it easier to group observations from the same session and compare the spaces. The sessions are arranged chronologically rather than by observation ID, because the original observation IDs do not follow the exact chronological order of the sessions.

I kept the original CSV unchanged so the data processing can be rerun and the results checked against the original observations.

## Task 3: Explore the Data

I created three exploratory plots before deciding which visualization approaches to develop further.

### Occupancy Across Shared Spaces

![Occupancy by space](figures/eda/occupancy_by_space.png)

The first plot shows the individual people counts for each space. Study Lounge 1 had between 0 and 1 people, while Study Lounge 2 had between 0 and 2. The Gym reached 10 people, and the Common Area reached 14. The Gym and Common Area also showed more variation than either study lounge.

I found it useful to see the individual observations instead of just comparing averages. However, the shared scale made the smaller differences in the lounges harder to notice. The spaces also differ in size and purpose, so comparing their counts does not necessarily tell us how full they were relative to their capacity.

### Occupancy Across Observation Sessions

![Occupancy by session](figures/eda/occupancy_by_session.png)

The second plot uses a heatmap to compare the four spaces across the seven observation sessions.

Two counts stood out: 10 people in the Gym during the September 29 morning observation and 14 people in the Common Area during the October 1 evening event. The Common Area had only 1 person during the later observation that same day.

I liked this view because it made comparing the sessions straightforward. It also showed differences that would be less noticeable if I only looked at average occupancy. The observations were collected at separate times, so the heatmap represents the recorded sessions rather than continuous changes in occupancy.

### Activity and Noise Level

![Occupancy by activity and noise](figures/eda/occupancy_activity_noise.png)

For the third plot, I compared people counts with the recorded activity and noise level.

Both study lounges were recorded as Quiet, while the Gym and Common Area included Moderate and Loud observations. The highest counts in the Gym and Common Area were both labeled Loud, although the dataset is too small to establish a general relationship between occupancy and noise.

My first version of this plot had overlapping points, and the vertical axis did not show the full range of people counts. I corrected the scale and added small offsets to make repeated observations easier to see.

I also noticed that activity was closely related to the type of space. For example, exercise-related activities were recorded in the Gym. This made comparisons between activities less straightforward without also considering where they took place.

### What I Learned From the Exploration

The exploratory plots showed me that I needed both an overview of occupancy and a way to examine individual observations. The heatmap was especially useful for comparing counts, while the activity and noise plot showed why the context behind an observation was worth keeping.

## Task 4: Exploring Alternative Visualization Designs

I implemented three visualization directions to explore different ways of presenting the data. Each focused on a different question rather than just changing the appearance of the same chart.

### Direction A: Occupancy Distribution by Space

![Occupancy distribution](figures/alternatives/alternative_a_distribution.png)

For the first design, I wanted to compare the occupancy distributions of the four spaces.

I used horizontal position for people count and vertical position to separate the spaces. The circles show individual observations, the diamonds show medians, and the gray lines show the observed ranges.

This design made it easy to compare the counts and see that the Common Area and Gym had larger ranges than the lounges. I liked it as a summary of the observations, but it did not show which sessions the counts came from or what activities were happening.

### Direction B: Occupancy Across Observation Sessions

![Session comparison](figures/alternatives/alternative_b_sessions.png)

My second design uses four small line charts, one for each space. The horizontal axis shows the observation sessions, and the vertical axis shows people count. I kept the same vertical scale so the spaces could be compared.

I liked having a separate chart for each space because I could follow its counts across the seven sessions. The Gym's count of 10 and the Common Area's count of 14 were easy to spot.

One concern was that the lines connected observations collected at different times. This could make the counts appear to represent continuous changes, which I had not measured. I wanted to keep the session comparison without relying on connecting lines.

### Direction C: Interactive Observation Explorer

![Initial interactive design](figures/iterations/initial_interactive.png)

[Open the initial interactive visualization](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/alternative_c.html)

For the third design, I tried an interactive scatterplot using Vega-Lite.

People count is shown on the horizontal axis, main activity on the vertical axis, and noise level through color. I added a dropdown to filter by space and tooltips showing the observation's date, time, activity, noise level, and context notes.

I liked being able to hover over a point and see more information without displaying every detail on the chart. For example, filtering to the Gym allowed me to examine the observation with 10 people and its recorded context.

While testing the All Spaces view, I noticed that some observations had the same people count and activity. Their circles appeared in the same position, making some records difficult to inspect separately.

### Choosing a Direction

Direction A was useful for comparing distributions, while Direction B worked well for comparing sessions. Direction C gave me more information about individual observations through filtering and tooltips.

I decided to develop Direction C further because I wanted to keep those observation details. My first goal was to solve the overlapping-points problem and then improve how the observations could be compared.

## Task 5: Interaction and Multiple Views

I explored interaction because I wanted users to be able to check the context behind a count rather than only view the numbers.

In Direction C, I used a dropdown to focus on one space and tooltips to show the recorded details. These interactions made it possible to examine observations without putting all the information directly on the chart.

In my final design, I used a heatmap linked to a separate HTML details panel. Users can compare the occupancy counts first and click a cell to see its date, time, activity, noise level, and context notes.

I tested this interaction with the Common Area observation of 14 people and the Gym observation of 10 people. The details panel showed the corresponding record in both cases. I also tested clearing the selection by double-clicking.

I found the linked panel more useful for this dataset because it kept the overview focused on comparing counts while still making the recorded details accessible.

## Task 6: Iterating on the Selected Design

I made two main changes after testing Direction C. The first addressed overlapping observations, and the second changed how the information was organized.

### Iteration 1: Separating Overlapping Observations

![Iteration 1](figures/iterations/iteration1.png)

[Open Iteration 1](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration1.html)

**Problem:** In the initial interactive scatterplot, several observations had the same activity and people count, so their circles overlapped.

**Change:** I replaced activity on the vertical axis with observation ID. Each observation now has its own row, while people count remains on the horizontal axis. I kept the noise colors, space filter, and tooltips.

**Result:** All 28 observations became individually visible, and I could inspect records separately without overlapping points covering one another.

Although this solved the original problem, organizing everything by observation ID made comparisons across spaces and sessions less convenient. I could find individual records, but it was harder to see the overall occupancy patterns. This made me reconsider whether the scatterplot was the best layout to continue with.

### Iteration 2: Combining an Overview With Observation Details

![Iteration 2](figures/iterations/iteration2.png)

[Open Iteration 2](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration2.html)

**Problem:** Iteration 1 separated the observations successfully, but I still wanted an easier way to compare occupancy across spaces and sessions.

**Change:** I returned to the session-by-space heatmap approach I had explored earlier. The heatmap shows the four spaces across seven observation sessions, with each cell displaying its people count through a number and color intensity. I also used session labels that include the recorded dates and times.

I added a linked details panel so that clicking a cell displays the corresponding observation's date, time, count, activity, noise level, and context notes. This allowed me to combine the session comparison with the observation details I had liked in Direction C.

**Result:** I could compare all 28 counts in one view and inspect individual observations without searching through overlapping points.

For example, clicking the Common Area cell in Session 5 showed the 14-person event on October 1 at 6 PM. Clicking the Gym cell in Session 3 showed 10 people during an exercise-related observation on September 29 at 6 AM.

I tested these selections and confirmed that the details panel updated correctly. I also adjusted the text colors to make the numbers easier to read against the heatmap colors.

The main improvement was that I no longer had to choose between comparing occupancy and examining individual observations. Both were possible in the same interface.

## Task 7: Current Working Design and Next Steps

My current working design is the heatmap with a linked details panel from Iteration 2.

[Open the current working visualization](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration2.html)

The heatmap shows occupancy across the four spaces and seven sessions. Each cell includes the recorded people count, and selecting a cell displays the observation's additional information below the chart.

This design is based on the heatmap idea from my Assignment 1 sketches, but I made changes after testing the other visualization approaches. My original sketch used color and shape to include noise information, while the final heatmap uses color mainly for occupancy. I removed noise from the overview to keep the counts easier to compare, but the recorded noise level is still available in the details panel.

The final design also includes clickable observations and a separate details panel, which were not part of the original static sketch. The session labels now show dates and recorded times instead of only session numbers.

I think this version works best for comparing spaces, identifying differences between sessions, and checking unusual observations. The question about activity and noise is less immediate because those attributes are not visible together in the overview. Users need to select observations to examine them.

For Assignment 3, I would like to test whether someone else can compare the spaces, identify an unusual observation, and retrieve its context without much explanation. I would also consider whether a separate view for activity and noise would be helpful without making the main heatmap too crowded.

The dataset contains only seven sessions with uneven coverage across dates and times, so I would keep any conclusions limited to the observations I collected.
