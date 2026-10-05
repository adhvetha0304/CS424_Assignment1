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

I treated one observation as one snapshot of a shared space at a particular date and time. For each observation, I planned to record the space, date and time, number of people present, noise level, main activity, and any useful contextual notes. I planned to repeat this process across the same four spaces so that observations from different sessions could be compared consistently.

For noise level, I used three categories: Quiet, Moderate, and Loud. Quiet meant there was little or no noticeable conversation or background activity, Moderate meant there was noticeable background sound or normal activity, and Loud meant there was substantial conversation, recreation, or other sound. The main activity was based on what people in the space were primarily doing, such as studying/working, exercising, or recreation.

I chose these four spaces because they serve different purposes but are all shared areas available to residents. I planned to collect observations on multiple days and at different times depending on when I was available in the building. I also planned to include observations at different times of day to capture variation in usage. During each observation session, I planned to check the same four spaces so that usage could be compared across locations and times.

Because the observation times depended partly on when I was available in the building, the sample is a convenience sample rather than a balanced sample of all days and times. This could overrepresent the usage patterns that occur during the periods when I was most often available.

I completed the project individually, so I planned and carried out all observations myself.

I did not record names, faces, private conversations, or any other identifying information. I only recorded characteristics of the spaces and general activities. One limitation of this method is that each observation is only a snapshot, so it does not show how long people stayed in a space. The spaces also differ in size, so comparing people counts does not necessarily represent the same level of occupancy in every space. Since I collected the observations by myself, noise level and main activity also depended on my own judgment.

### Initial Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| observation_id | Identifier | Unique number for each observation | 1 |
| date | Temporal | Date of the observation | 2026-09-27 |
| day_of_week | Categorical | Day of the observation | Sunday |
| time | Temporal | Recorded time or time range of the observation | 6-9 PM |
| time_period | Ordinal/Categorical | General period of day: Morning before 12:00 PM; Afternoon 12:00–4:59 PM; Evening 5:00 PM or later | Evening |
| space | Categorical | Shared space being observed | Study Lounge 1 |
| space_type | Categorical | General purpose of the space | Study |
| people_count | Quantitative | Number of people observed | 5 |
| noise_level | Ordinal | Observed noise category | Loud |
| main_activity | Categorical | Main activity occurring in the space | Studying/Working |
| context_notes | Text | Additional relevant details | People playing table tennis |

## Task 2: Pilot Collection and Revision

### Pilot Collection

I used my first two observation sessions, totaling eight observations across the four spaces, as the pilot for the collection process. These early observations helped me see whether the attributes I had chosen were practical to record and what needed to be more consistent. I continued using these observations in the final dataset because they were still compatible with the revised collection method.

One issue I noticed from my first session was the way I recorded time. For the September 27 observations, I only recorded that the observations took place sometime between 6 and 9 PM rather than recording the specific time. After this first session, I realized that a more precise time would be more useful for comparing observations, so I recorded specific observation times in later sessions.

The people count, noise level, and main activity were generally easy to record because they could be observed directly during each visit. However, some spaces could have more than one activity occurring at the same time. For example, the common area could have people working while others were waiting for coffee or doing something recreational. Because of this, I allowed the main activity to be recorded as Mixed when there was not one clear activity representing the space.

Context also became useful during collection. Some observations took place under conditions that could be relevant when interpreting the data, such as heavy rain or an event in the main lobby. I kept these details in `context_notes` rather than assuming that they caused the observed differences.

As the dataset developed, I also refined the domain questions to better match the variation captured by the observations. The initial questions emphasized time of day, while the final questions broaden this focus to comparisons across spaces and sessions, relationships among occupancy, noise and activity, and observations that stand out from typical usage. This made the final questions better match the variation I had actually collected without going beyond what the observations could support.

### Revisions to the Collection Procedure

After the early observations, I made the collection procedure more consistent. I recorded a more specific time whenever possible, continued using the same noise categories across spaces, used None for the main activity when a space was empty, and used Mixed when multiple activities were occurring without one clear dominant activity. I also kept contextual information separate from the main activity so that unusual conditions could be documented without treating them as explanations for the observations.

During collection, I considered whether people counts needed to distinguish between exact and estimated values. In the final dataset, each `people_count` represents the number of people present at the observation snapshot, including the event observation. Because all final counts use the same measurement approach, a separate `count_type` attribute was unnecessary and was not retained in the final schema.

During final dataset cleanup, I compared the structured CSV with my original observation notes and corrected transcription inconsistencies. I only changed an entry when the value was clearly recorded in my notes rather than inferring it afterward. While reviewing the notes, I confirmed that the September 27 Common Area noise level was Moderate, filled in noise values that had been left unresolved in the earlier CSV draft, and verified that the October 1 event observation was an exact snapshot count of 14, even though people were entering and leaving during the event.

The revised procedure still treated one observation as one snapshot of one space. During each observation session, I checked the same four spaces and recorded the people count, noise level, main activity, and any relevant context.

### Revised Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| observation_id | Identifier | Unique number for each observation | 1 |
| date | Temporal | Date of the observation | 2026-09-27 |
| day_of_week | Categorical | Day of the observation | Sunday |
| time | Temporal | Recorded time or approximate time range | 5:50 PM |
| time_period | Ordinal/Categorical | General period of day: Morning before 12:00 PM; Afternoon 12:00–4:59 PM; Evening 5:00 PM or later | Evening |
| space | Categorical | Shared space being observed | Common Area |
| space_type | Categorical | General purpose of the space | Social/Common |
| people_count | Quantitative | Number of people present at the observation time | 14 |
| noise_level | Ordinal | Observed noise level: Quiet, Moderate, or Loud | Moderate |
| main_activity | Categorical | Main activity: Studying/Working, Exercising, Recreation, Reading, Event/Social, Mixed, or None | Mixed |
| context_notes | Text | Additional conditions or details useful for interpreting the observation | Heavy rain outside |

## Task 3: Final Dataset and Domain Questions

### Final Dataset

My final dataset contains 28 observations collected across five dates and seven observation sessions. During each session, I observed the same four spaces: Study Lounge 1, Study Lounge 2, the gym, and the common area. The observations cover morning, afternoon, and evening periods as well as both weekdays and weekends.

The final machine-readable dataset is available in [`shared_spaces.csv`](shared_spaces.csv).
My original observation notes are included as a raw collection artifact: [`initial notes.png`](../raw/initial%20notes.png).

The dataset includes information about the number of people present, noise level, main activity, location, date and time, and relevant context. The observations provide variation across both space and time. Evening observations are more heavily represented in the dataset, so comparisons across time periods should be interpreted within the scope of the collected observations rather than as general usage patterns for the building.

The spaces also differ in size and capacity, but I did not have a reliable, comparable capacity measure for every space, particularly the gym. Because of this, I used the observed number of people rather than occupancy percentages. Comparisons should therefore be interpreted as differences in raw usage counts rather than differences in how full each space was.

The temporal coverage is uneven. Of the 28 observations, 20 were collected during evening sessions, while morning and afternoon are represented by only one session each. Weekend observations account for 8 of the 28 observations across two sessions. The dataset also covers only five dates, so conditions occurring on individual dates, such as the event or heavy rain, can have a noticeable influence on such a small sample. All observations were collected by one observer, and `noise_level` and `main_activity` were based on observational judgment rather than instrument measurements. In addition, each record represents only a snapshot, so the dataset does not show how long people remained in a space or what happened continuously between observation times.

### Reflection on the Data

Turning the observations into structured data required simplifying what was happening in each space. `people_count` was straightforward, while `main_activity` and `noise_level` sometimes required judgment. I used `Mixed` when no single activity clearly represented the space, and kept conditions such as the event and heavy rain in `context_notes` rather than treating them as causes.

Each row represents only one snapshot, so the dataset does not capture how long people stayed, whether they arrived in groups, or how usage changed between observations. Structuring the data helped me see which attributes could be recorded consistently and which involved more interpretation.

### Revised Domain Questions

1. **Which shared spaces have the highest and lowest overall observed usage across all sessions?**  
   This uses `space` and `people_count` to compare the overall distribution and extremes of observed usage across the four spaces.

2. **Within each shared space, how much does `people_count` vary from one observation session to another?**  
   This uses `space`, `date`, `time`, and `people_count` to examine within-space variation across sessions and identify spaces with relatively stable or changing usage.

3. **How are noise level, number of people, and the type of activity related?**  
   This uses `noise_level`, `people_count`, and `main_activity`. For example, similar numbers of people may produce different noise levels depending on what they are doing.

4. **Which shared spaces show more consistent activity patterns, and which are used for a wider variety of activities?**  
   This uses `space` and `main_activity` to compare the distribution and variety of activities observed in each space.

5. **Which individual observations stand out from the usual usage of each space?**  
   This uses `space`, `people_count`, `noise_level`, and `context_notes` to identify unusual observations while keeping contextual conditions separate from causal conclusions.

## Task 4: Abstract Tasks

For each domain question, I translated the question into actions and targets. The actions describe what someone needs to accomplish using the visualization, while the targets describe the aspects of the data that are relevant to that goal.

1. **Which shared spaces have the highest and lowest overall observed usage across all sessions?**
   - **Actions:** Compare and identify.
   - **Target:** Distribution and extremes of `people_count` across `space`.
   - **Reasoning:** This question requires comparing the four spaces using their observed people-count distributions and identifying the highest and lowest overall usage. The target is therefore the distribution and extremes of `people_count` across `space`.

2. **Within each shared space, how much does `people_count` vary from one observation session to another?**
   - **Actions:** Compare and summarize.
   - **Target:** Variation and distribution of `people_count` across `space`, `date`, and `time`.
   - **Reasoning:** This question focuses on variation within each space across repeated observation sessions. Comparing and summarizing `people_count` across session dates and times can show which spaces have relatively stable usage and which vary more substantially.

3. **How are noise level, number of people, and the type of activity related?**
   - **Actions:** Explore and compare.
   - **Target:** Relationships or dependencies among `people_count`, `noise_level`, and `main_activity`.
   - **Reasoning:** The relationship among these attributes is not known in advance, so the task is exploratory. Looking across multiple attributes can reveal whether different combinations of occupancy and activity are associated with different noise levels without assuming that one causes another.

4. **Which shared spaces show more consistent activity patterns, and which are used for a wider variety of activities?**
   - **Actions:** Compare and summarize.
   - **Target:** Distribution and diversity of `main_activity` across `space`.
   - **Reasoning:** This question requires comparing the activity categories observed within each space and summarizing their distributions. This can show whether a space is used primarily for one type of activity or supports a wider variety of activities.

5. **Which individual observations stand out from the usual usage of each space?**
   - **Actions:** Locate and identify.
   - **Target:** Outliers and extremes in `people_count` and `noise_level` within each `space`.
   - **Reasoning:** The particular observations that stand out are not known beforehand, so they first need to be located and then identified. After locating them, `context_notes` can provide additional context for interpreting those observations without assuming that the contextual condition caused the unusual value.

### Reflection on Task Abstraction

Task abstraction helped me separate what I wanted to learn from how I might visualize it. The questions became goals such as comparing distributions, exploring relationships, and locating unusual observations. Q3 was especially exploratory because the relationship among people count, noise, and activity was not known in advance.

## Task 5: Visualization Sketches and Refinement

### Sketch 1: Shared Space Usage Across Observation Sessions

![Sketch 1: Shared Space Usage Across Observation Sessions](../sketches/CS%20424-2.jpg)

I designed this sketch as an overview of how shared-space usage varied across observation sessions, mainly addressing Q1, Q2, and Q5. It represents space, observation session, `people_count`, and `noise_level`. Each cell is a mark representing one observation; horizontal and vertical position encode session and space, luminance encodes people count, shape and color hue distinguish noise level, and text gives the exact count. The combination of shading and exact values made differences in occupancy easy to compare, and unusually high observations such as 10 people in the gym and 14 in the common area stood out clearly. However, the noise symbols were less visually prominent than the occupancy shading, and the design does not represent `main_activity`. Overall, this sketch works well for comparing occupancy patterns and locating unusual observations, but it is more limited for investigating relationships involving activity.

### Sketch 2: Activity, Noise, and Occupancy

![Sketch 2: Activity, Noise, and Occupancy](../sketches/sketch2.jpg)

I designed this sketch to explore Q3, focusing on the relationship among `main_activity`, `noise_level`, and `people_count`. Each observation is represented by a circle positioned according to its activity and noise category. Horizontal position encodes `noise_level`, vertical position encodes `main_activity`, circle size encodes `people_count`, and text gives the exact count. This design made it easy to see which activity and noise combinations occurred in the observations and made larger counts such as 10 and 14 visually prominent. However, comparing similar people counts using circle size was less precise than comparing exact positions, so I included the numerical values with the circles. Cells containing many observations, particularly Studying/Working with Quiet noise and None with Quiet noise, also became more crowded. Unlike Sketch 1, this design removes space and observation session to focus specifically on the relationship among activity, noise, and occupancy.

### Sketch 3: Observed Activity Composition by Shared Space

![Sketch 3: Observed Activity Composition by Shared Space](../sketches/sketch%203.jpg)

I designed this sketch to explore Q4 by comparing activity composition across the four spaces. Each horizontal bar represents one space and contains seven equal rectangular segments, one for each observation. Vertical position encodes `space`, while the number of segments with each label represents the frequency of `main_activity`; `N` represents `None`.

This design makes it easy to compare spaces with relatively consistent activity patterns against spaces with a wider variety of observed activities. Grouping identical activity states together emphasizes composition and frequency across spaces. However, this means the chronological order of the observations is not preserved, so the design is less useful for examining when particular activities occurred. Unlike Sketch 1, which emphasizes occupancy across sessions, and Sketch 2, which focuses on relationships among activity, noise, and people count, this sketch focuses specifically on the distribution and diversity of activities across spaces.


### Comparing the Initial Sketches and Refinement Direction

The three initial sketches focused on different parts of the data. Sketch 1 was strongest for comparing occupancy across spaces and sessions, but its noise encoding was easy to overlook. Sketch 2 showed relationships among activity, noise, and people count, but circle size was less precise and some areas became crowded. Sketch 3 made activity differences across spaces easy to compare, but it removed observation order.

Based on these limitations, I refined Sketches 1 and 2. For Sketch 1, I kept the matrix structure but made noise more noticeable and added context. For Sketch 2, I replaced circle size with position and separated the observations by space.

### Refined Sketch 1: Shared Space Usage with Noise and Context

![Refined Sketch 1: Shared Space Usage with Noise and Context](../sketches/sketch%204.jpg)

I refined Sketch 1 because the matrix worked well for comparing `people_count`, but the noise symbols were not very noticeable and the design did not show context. The refined version still addresses Q1, Q2, and Q5.

Each cell represents one observation. Horizontal position encodes observation session, vertical position encodes `space`, shading encodes `people_count`, and text gives the exact count. `noise_level` is shown using an inner outline: no outline for Quiet, a medium outline for Moderate, and a thicker outline for Loud. The design also includes `context_notes` for the 14-person event observation and the heavy-rain session.

This keeps the occupancy comparison from the original sketch while making noise and unusual observations easier to interpret. The context is included only as additional information and does not imply that it caused the observed values.

### Refined Sketch 2: Activity, Occupancy, and Noise by Space

![Refined Sketch 2: Activity, Occupancy, and Noise by Space](../sketches/sketch%205.jpg)

I refined Sketch 2 because circle size made similar people counts difficult to compare and some activity-noise combinations became crowded. The refined version addresses Q3 and Q4 by using position for `people_count` and separating the observations by space.

Each observation is a point. Horizontal position encodes `people_count`, vertical position encodes `main_activity`, separate panels represent `space`, and point shape represents `noise_level`: circles for Quiet, triangles for Moderate, and stars for Loud. All panels use the same people-count scale. When points would overlap, they are slightly offset only to keep them visible.

Using position makes people-count comparisons more precise than the original bubble design, while the separate panels make activity and noise patterns easier to compare across spaces.

### Additional Sketch 4: Occupancy Distribution by Shared Space

![Sketch 4: Occupancy Distribution by Shared Space](../sketches/sketch%206.jpg)

I added this sketch as another way to explore Q1, Q2, and Q5 without using the session-by-session matrix. Each point represents one observation. Horizontal position encodes `people_count`, vertical position encodes `space`, and shape and color hue encode `noise_level`. Range lines show the minimum and maximum observed count for each space, while annotations identify the heavy-rain and event observations.

Using one common quantitative scale makes differences in spread and extreme values easy to compare. The study lounges have narrow observed ranges, while the gym and common area vary more. Unlike Sketch 1, this design removes session order and focuses on the distribution of occupancy, so it does not show when an observation occurred or what activity was recorded.

## Task 6: Design Comparison and Reflection

The initial sketches explored different parts of the dataset. Sketch 1 gave the clearest overview of occupancy across spaces and sessions, but its noise encoding was less noticeable. Refined Sketch 1 kept the matrix structure while making noise more visible and adding contextual annotations.

Sketch 2 focused on the relationship among `main_activity`, `noise_level`, and `people_count`. It showed several attributes together, but circle size was not very precise and crowded cells were harder to read. Refined Sketch 2 improved this by using horizontal position for `people_count` and separating spaces into panels. Sketch 3 took a simpler approach by showing activity composition, which made differences in activity variety clear but removed chronological order.

I later added the occupancy-distribution sketch to explore Q1, Q2, and Q5 through a different structure. It uses a common quantitative scale, so spread and extreme counts are easier to compare than in the matrix, but it does not preserve session order or activity information.

Overall, the sketches use several different structures: a session-space matrix, an activity-noise relationship view, a segmented composition view, an occupancy-distribution view, and a faceted point view. Trying these alternatives showed me that one visualization does not need to answer every question. Different views are more effective for overview, categorical composition, relationships, or precise quantitative comparison.

The collection process also affected the designs. Each observation is only a snapshot, most observations were collected in the evening, and comparable capacity information was not available for every space. Because of this, I avoided continuous time-series or causal interpretations and used raw `people_count` rather than occupancy percentages. If I collected the data again, I would add more morning, afternoon, and weekend sessions, record exact times from the beginning, and collect reliable capacity and measured-noise information if possible.

With 28 observations, all of the sketches remain readable. With more data, the bubble view would become crowded, the session matrix would require more columns, and the distribution view would require more stacking. The sketching process therefore helped me focus on matching the visual structure to the question rather than trying to put every attribute into one visualization.

## Task 7: Project Process
I completed this assignment individually, so I was responsible for the data collection, organization, sketching, and documentation. During each observation session, I checked the same four shared spaces and recorded the same set of attributes so that the observations would remain as consistent as possible. The pilot stage helped me notice issues such as the lack of a precise time in the first session and the need for clearer rules for `None`, `Mixed`, and contextual notes. I then kept those revised definitions consistent for the remaining observations.

I organized the structured dataset and documentation in GitHub and used separate commits as the project developed. I also uploaded the hand-drawn sketches from GoodNotes and revised the visualization ideas after comparing their strengths and limitations. For example, I changed the noise encoding in the first refined sketch because it was not prominent enough in the original, and I replaced the bubble-size encoding from Sketch 2 with position in the second refinement to make people-count comparisons more precise.

Working alone made it easier to apply one consistent interpretation of the collection rules, but it also meant that judgments such as noise level and main activity came from only one observer. It also required me to manage the full collection and design process myself. Overall, the iterative process helped me improve both the structure of the dataset and the visualization designs as I identified issues during collection and sketching.
