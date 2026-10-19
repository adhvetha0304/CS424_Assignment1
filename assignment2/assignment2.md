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
