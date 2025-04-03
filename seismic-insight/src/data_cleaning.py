# src/data_cleaning.py

import pandas as pd
import re

def clean_earthquake_data(filepath: str = "data/raw_data.csv") -> pd.DataFrame:
    """
    Cleans the raw earthquake data:
    - Parses time strings into datetime
    - Converts numeric fields to floats
    - Extracts region name from 'place'
    - Drops rows with missing/invalid data
    """
    df = pd.read_csv(filepath)

    # Convert time to datetime
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # Convert strings to numeric
    for col in ["mag", "depth", "longitude", "latitude"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Extract region name from place string
    df["region"] = df["place"].apply(lambda x: re.sub(r".* of ", "", x))

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Save cleaned version
    df.to_csv("data/cleaned_data.csv", index=False)

    return df
