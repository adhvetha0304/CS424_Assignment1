# CS 424 Assignment 1

## Occupancy and Usage Patterns Across Shared Apartment Spaces

## Task 1: Data Collection Plan
### Project Description

I chose to observe shared spaces in my apartment building because I spend a lot of time in the building and regularly use or pass through these areas. I had noticed that some spaces seemed much busier at certain times than others, which made me curious about how their usage changes throughout the day.

I focused on four shared spaces: Study Lounge 1, Study Lounge 2, the gym, and the common area. I wanted to observe how the number of people and the way these spaces are used vary depending on the location and time of day. Since the spaces have different purposes, I was also interested in comparing their noise levels and the main activities taking place in them.

### Initial Domain Questions

1. How does the number of people using each shared space vary by time of day?
2. Which shared spaces are used the most and least during the observed periods?
3. How does noise level vary across the different shared spaces?
4. What types of activities occur in each space, and how do they change across observation periods?

### Initial Collection Plan

I treated one observation as one snapshot of a shared space at a particular date and time. For each observation, I planned to record the space, date and time, number of people present, noise level, main activity, and any useful contextual notes. I observed the same four spaces repeatedly so that I could compare different locations and different times.

For noise level, I used three categories: Quiet, Moderate, and Loud. Quiet meant there was little or no noticeable conversation or background activity, Moderate meant there was noticeable background sound or normal activity, and Loud meant there was substantial conversation, recreation, or other sound. The main activity was based on what people in the space were primarily doing, such as studying/working, exercising, or recreation.

I chose these four spaces because they serve different purposes but are all shared areas available to residents. I collected observations on multiple days and at different times depending on when I was available in the building. I also intentionally included observations at different times of day to get more variation in the dataset. During each observation session, I checked the same four spaces so that I could compare their usage across locations and times.

I did not record names, faces, private conversations, or any other identifying information. I only recorded characteristics of the spaces and general activities. One limitation of this method is that each observation is only a snapshot, so it does not show how long people stayed in a space. The spaces also differ in size, so comparing people counts does not necessarily represent the same level of occupancy in every space. Since I collected the observations by myself, noise level and main activity also depended on my own judgment.

### Initial Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| observation_id | Identifier | Unique number for each observation | 1 |
| date | Temporal | Date of the observation | 2026-09-27 |
| day_of_week | Categorical | Day of the observation | Sunday |
| time | Temporal | Recorded time or time range of the observation | 6-9 PM |
| time_period | Ordinal/Categorical | General period of the day | Evening |
| space | Categorical | Shared space being observed | Study Lounge 1 |
| space_type | Categorical | General purpose of the space | Study |
| people_count | Quantitative | Number of people observed | 5 |
| noise_level | Ordinal | Observed noise category | Loud |
| main_activity | Categorical | Main activity occurring in the space | Studying/Working |
| context_notes | Text | Additional relevant details | People playing table tennis |

## Task 2: Pilot Collection and Revision

### Pilot Collection

I used my first few observation sessions as a pilot for the collection process. These early observations helped me see whether the attributes I had chosen were practical to record and what needed to be more consistent. I continued using these observations in the final dataset because they were still compatible with the revised collection method.

One issue I noticed from my first session was the way I recorded time. For the September 27 observations, I only recorded that the observations took place sometime between 6 and 9 PM rather than recording the specific time. After this first session, I realized that a more precise time would be more useful for comparing observations, so I recorded specific observation times in later sessions.

The people count, noise level, and main activity were generally easy to record because they could be observed directly during each visit. However, some spaces could have more than one activity occurring at the same time. For example, the common area could have people working while others were waiting for coffee or doing something recreational. Because of this, I allowed the main activity to be recorded as Mixed when there was not one clear activity representing the space.

Context also became useful during collection. Some observations took place under conditions that could be relevant when interpreting the data, such as heavy rain or an event in the main lobby. I kept these details in `context_notes` rather than assuming that they caused the observed differences.

### Revisions to the Collection Procedure

After the early observations, I made the collection procedure more consistent. I recorded a more specific time whenever possible, continued using the same noise categories across spaces, used None for the main activity when a space was empty, and used Mixed when multiple activities were occurring without one clear dominant activity. I also kept contextual information separate from the main activity so that unusual conditions could be documented without treating them as explanations for the observations.

The revised procedure still treated one observation as one snapshot of one space. During each observation session, I checked the same four spaces and recorded the people count, noise level, main activity, and any relevant context.

### Revised Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| observation_id | Identifier | Unique number for each observation | 1 |
| date | Temporal | Date of the observation | 2026-09-27 |
| day_of_week | Categorical | Day of the observation | Sunday |
| time | Temporal | Recorded time or approximate time range | 5:50 PM |
| time_period | Ordinal/Categorical | General period of the day | Evening |
| space | Categorical | Shared space being observed | Common Area |
| space_type | Categorical | General purpose of the space | Social/Common |
| people_count | Quantitative | Number of people present at the observation time | 14 |
| count_type | Categorical | Whether the recorded count was exact or estimated | Exact |
| noise_level | Ordinal | Quiet, Moderate, or Loud | Moderate |
| main_activity | Categorical | Main activity in the space, including None or Mixed when appropriate | Mixed |
| context_notes | Text | Additional conditions or details useful for interpreting the observation | Heavy rain outside |

## Task 3: Final Dataset and Domain Questions

## Task 4: Abstract Tasks

## Task 5: Visualization Sketches and Refinement

## Task 6: Design Comparison and Reflection

## Task 7: Project Process
