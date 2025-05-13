# src/data_collection.py

import requests
import pandas as pd
from datetime import datetime
from typing import Optional

def fetch_earthquake_data(start_time: str, end_time: str, min_magnitude: float = 4.5) -> pd.DataFrame:
    """
    Fetch earthquake data from the USGS API within a given time range and minimum magnitude.
    Saves raw data to CSV and returns a DataFrame.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": start_time,
        "endtime": end_time,
        "minmagnitude": min_magnitude,
        "orderby": "time"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        features = data.get("features", [])
        records = []
        for feature in features:
            props = feature["properties"]
            geom = feature["geometry"]
            record = {
                "time": props["time"],
                "place": props["place"],
                "mag": props["mag"],
                "depth": geom["coordinates"][2],
                "longitude": geom["coordinates"][0],
                "latitude": geom["coordinates"][1],
                "type": props["type"],
                "id": feature["id"],
                "url": props["url"]
            }
            records.append(record)

        df = pd.DataFrame(records)
        df["time"] = pd.to_datetime(df["time"], unit='ms')
        df.to_csv("data/raw_data.csv", index=False)
        return df

    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
