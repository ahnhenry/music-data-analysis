# 🎧 What Makes Ahn Press Play?
### Exploratory Data Analysis of Ahn's Music Taste to Identify Factors Influencing Listening Probability
 
---
 
## Overview
 
**Hypothesis:** Is Ahn's likelihood of listening to a song influenced by a specific characteristic of that song?
 
**Purpose:** Move beyond surface-level observations like *"Ahn listens to K-Pop"* and uncover the underlying audio features — tempo, energy, valence, danceability, key, acousticness — that actually drive listening behavior.
 
**Approach:** Ahn's most-played playlist was exported from Apple Music and enriched with musical metadata (BPM, key, mode, energy, danceability, valence, acousticness, time signature) to build a queryable dataset. The data was then analyzed and visualized interactively to surface patterns and test the hypothesis.
 
---
 
## Dataset
 
The dataset (`ahndata.csv`) contains **552 songs** sourced from 5 of Ahn's Apple Music playlists, composed of the following fields:
 
| Column | Description |
|---|---|
| `title` | Song title |
| `artist` | Artist name |
| `album` | Album name |
| `genre` | Genre tag |
| `year` | Release year |
| `duration` | Track length (mm:ss) |
| `plays` | Number of plays (listening probability proxy) |
| `bpm` | Tempo in beats per minute |
| `key` | Musical key (e.g. F# minor) |
| `time_signature` | Time signature (e.g. 4/4) |
| `mode` | Major or minor |
| `energy` | Intensity level (0.0 – 1.0) |
| `danceability` | How suitable for dancing (0.0 – 1.0) |
| `valence` | Musical positivity / happiness (0.0 – 1.0) |
| `acousticness` | Acoustic vs. electronic character (0.0 – 1.0) |
 
---
 
## Stack
 
| Layer | Technology |
|---|---|
| Data preparation | Excel, Python |
| Backend / API | Python Flask |
| Database | SQLite3 |
| Frontend | HTML, CSS |
| Querying | SQL (SQLite3) |
 
---

## Findings
 
> *Coming soon — analysis in progress.*
 
Key questions being explored:

- What experimental factors may have influenced these findings?
- How would a larger dataset change these findings ?
- Does higher BPM correlate with more plays?
- Are major-key songs played more than minor-key songs?
- Which genre has the highest average play count?
- Does energy or danceability predict listening frequency?
- Are there release year trends in Ahn's listening habits?

---
 
## Project Structure
 
```
├── ahndata.csv   
├── app.py                 
├── templates/
│   └── data.html          
├── static/
│   ├── style.css
│   └── ...
└── README.md
```
 
---
 
## Contact
 
- 💼 [LinkedIn — Ahn Laurie Henry](https://www.linkedin.com/in/ahnlauriehenry/)
- 🐙 [GitHub](https://github.com/ahnhenry)