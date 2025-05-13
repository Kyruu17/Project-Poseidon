# src/visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import folium
import os
os.makedirs("outputs", exist_ok=True)


def plot_magnitude_over_time(df: pd.DataFrame, output_path: str = "outputs/magnitude_over_time.png"):
    plt.figure(figsize=(10, 5))
    df_sorted = df.sort_values("time")
    plt.plot(pd.to_datetime(df_sorted["time"]), df_sorted["mag"], marker='o')
    plt.title("Earthquake Magnitude Over Time")
    plt.xlabel("Date")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return output_path

def map_epicenters(df: pd.DataFrame, output_path: str = "outputs/earthquake_map.html"):
    m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=2)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=row["mag"] * 1.5,
            popup=f"{row['place']} (Mag: {row['mag']})",
            color="red", fill=True, fill_opacity=0.7
        ).add_to(m)
    m.save(output_path)
    return output_path
