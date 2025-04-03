# src/llm_helper.py

import pandas as pd

def generate_summary_from_data(df: pd.DataFrame) -> str:
    """
    Simulates an LLM-generated summary of earthquake statistics.
    In a real setup, you would call an LLM API here (e.g., OpenAI).
    """
    summary = []

    summary.append(f"📊 Total earthquakes: {len(df)}")
    summary.append(f"🔍 Max magnitude: {df['mag'].max()}")
    summary.append(f"🌍 Regions affected: {df['region'].nunique()}")
    summary.append(f"📈 Average depth: {df['depth'].mean():.2f} km")
    summary.append(f"📅 Time range: {pd.to_datetime(df['time']).min().date()} to {pd.to_datetime(df['time']).max().date()}")
    summary.append(f"📌 Most frequent region: {df['region'].value_counts().idxmax()}")

    return "\n".join(summary)
