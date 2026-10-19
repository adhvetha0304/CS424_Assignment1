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
