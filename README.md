# Hantavirus Outbreak Tracker — MV Hondius / Andes Virus

A public-facing Streamlit dashboard tracking the 2026 Andes hantavirus outbreak linked to MV Hondius cruise ship travel.

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## Features

- **How It Started** — narrative timeline of the outbreak from departure to disembarkation
- **Global Spread** — case distribution map (ESRI World Street Map) and country breakdown
- **Outbreak Data** — epidemic curve, cumulative case chart, full case linelist, WHO/ECDC case definitions
- **Clinical Guide** — symptoms by phase, when to seek emergency care, diagnosis & treatment for clinicians, rodent exposure prevention
- **Updates** — full chronological situation log with official sources

## Data Sources

WHO Disease Outbreak News (DON-600/601), ECDC Rapid Risk Assessment, CDC HAN-528, Global.health Hondius hantavirus dataset.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Disclaimer

This dashboard is for public information and educational purposes. It is not a substitute for guidance from public health agencies or clinical authorities. If you believe you have been exposed to hantavirus, contact your local public health department immediately.
