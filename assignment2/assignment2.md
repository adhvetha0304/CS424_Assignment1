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
