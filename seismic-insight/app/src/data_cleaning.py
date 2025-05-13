# src/data_cleaning.py

import os
import pandas as pd
import re

def clean_earthquake_data(filepath: str = None) -> pd.DataFrame:
    """
    Cleans the earthquake data.

    If filepath is provided, it will be used. Otherwise, the function
    will look for cleaned_data.csv or raw_data.csv in the project's data folder.

    Cleaning steps:
    - Parses time strings into datetime
    - Converts numeric fields to floats
    - Extracts region name from 'place'
    - Drops rows with missing/invalid data
    - Saves cleaned output to cleaned_data.csv
    """

    #    __file__ kann in app/src/ liegen oder in seismic-insight/src/
    src_dir = os.path.dirname(__file__)
    # Wir springen bis zum Ordner, der data/ enthält
    project_root = os.path.abspath(
        os.path.join(src_dir, os.pardir, os.pardir)
    )
    data_dir = os.path.join(project_root, 'data')

    if filepath:
        raw_path = os.path.join(project_root, filepath)
    else:
        cleaned_file = os.path.join(data_dir, 'cleaned_data.csv')
        raw_file     = os.path.join(data_dir, 'raw_data.csv')
        if os.path.exists(cleaned_file):
            raw_path = cleaned_file
        elif os.path.exists(raw_file):
            raw_path = raw_file
        else:
            raise FileNotFoundError(
                f"None of cleaned_data.csv or raw_data.csv found in {data_dir}"
            )

    df = pd.read_csv(raw_path)

    # 4) Zeit-Spalte konvertieren
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'], errors='coerce')

    for col in ['mag', 'depth', 'longitude', 'latitude']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'place' in df.columns:
        df['region'] = df['place'].astype(str).apply(
            lambda x: re.sub(r'^.* of ', '', x)
        )

    key_cols = ['time', 'mag', 'depth', 'longitude', 'latitude', 'region']
    existing_keys = [c for c in key_cols if c in df.columns]
    df = df.dropna(subset=existing_keys)

    out_path = os.path.join(data_dir, 'cleaned_data.csv')
    df.to_csv(out_path, index=False)

    return df
