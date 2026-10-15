# India Economic Monitor

A Streamlit dashboard for exploring the Indian economy dataset by year, sector,
and quarter. It includes GDP, growth, employment, inflation, trade, and
additional indicators from the supplied CSV.

## Run locally

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The dashboard loads `Indian_Economy.csv` from the project directory.

## Deploy

This repository contains the app source; GitHub does not host Streamlit apps.
To publish a live dashboard, deploy this repository using Streamlit Community
Cloud and set the app entry point to `app.py`.

## Data and emblem

The economic figures come from `Indian_Economy.csv` and have not been
independently validated against official sources.

`static/emblem-of-india.svg` is the Emblem of India image from
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Emblem_of_India.svg),
listed there as public domain. The State Emblem is subject to restrictions on
improper use; this project is an independent data dashboard and is not an
official Government of India publication.
