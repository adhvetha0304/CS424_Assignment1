# CS 424: Shared Spaces Visualization

This repository contains my work for CS 424 Assignments 1, 2, and 3. I collected 28 observations across seven sessions in four shared spaces and used the data to explore differences in occupancy, activity, and noise levels.

For Assignment 2, I explored different visualization approaches and developed an interactive visualization to compare occupancy across spaces and sessions while allowing individual observations to be examined in more detail.

## Assignment Write-ups

- [Assignment 1](data/assignment.md)
- [Assignment 2](assignment2/assignment2.md)
- [Assignment 3](assignment3/assignment3.md)

## Dataset

- `data/shared_spaces.csv` — Original observations collected for Assignment 1.
- `data/processed/shared_spaces_processed.csv` — Processed dataset containing additional session identifiers and labels.

## Tools Used

- Python
- Pandas
- Matplotlib
- Vega-Lite
- JavaScript
- HTML

## Setup and Reproduction

Python dependencies are listed in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
```

The following scripts are run from the repository root, in order:

```bash
python scripts/prepare_data.py
python scripts/eda.py
python scripts/visualization_alternatives.py
python scripts/build_interactive.py
python scripts/build_iteration1.py
python scripts/build_iteration2.py
```

These scripts prepare the dataset and generate the exploratory plots, visualization alternatives, and interactive HTML files.

## Visualizations

The exploratory plots are available in `assignment2/figures/eda/`, while the static visualization alternatives are in `assignment2/figures/alternatives/`.

The interactive versions are:

- [Initial interactive design](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/alternative_c.html)
- [Iteration 1 — Individual observations](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration1.html)
- [Iteration 2 — Coordinated overview and details](https://adhvetha0304.github.io/CS424_Assignment1/assignment2/visualization/iteration2.html)
  
**Current working design:** Iteration 2

The final design includes a heatmap of occupancy across the four spaces and seven observation sessions. Selecting a cell displays the corresponding observation's date, time, occupancy, activity, noise level, and context notes.

### Viewing the Interactive Visualization

A local server can be started from the repository root using:

```bash
python -m http.server 8000
```

The current visualization is then available at:

`http://localhost:8000/assignment2/visualization/iteration2.html`



## Assignment 3: Interaction and Evaluation

Assignment 3 compares static and interactive versions of the shared-spaces heatmap using a study with 10 participants. See the [Assignment 3 report](assignment3/assignment3.md) for the study design and results.

### Reproducing Assignment 3

Install the Python dependencies using the command in Setup and Reproduction above. From the repository root, run:

    python assignment3/build_static.py
    python assignment3/build_interactive.py
    python assignment3/build_practice.py
    python assignment3/analysis/analyze_results.py

To view the visualizations locally, start a server with `python -m http.server 8000` and open:

- [Static visualization](http://localhost:8000/assignment3/visualization/static.html)
- [Interactive visualization](http://localhost:8000/assignment3/visualization/interactive.html)

## Limitations

The dataset contains 28 observations collected across seven sessions, with uneven coverage across dates and times. The visualizations describe these recorded observations rather than general occupancy patterns across all days or times.

The exploration, alternative designs, and changes made during the two iterations are documented in the Assignment 2 write-up.
