import pandas as pd
import torch
from transformers import pipeline
from src.data_cleaning import clean_earthquake_data

device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline(
    "summarization",
    model="google/flan-t5-small",
    device=device
)

def summarize_trends() -> str:
    df = clean_earthquake_data()
    df['time'] = pd.to_datetime(df['time'])
    week_ago = pd.Timestamp.now() - pd.Timedelta(days=7)
    recent = df[df['time'] >= week_ago].sort_values('time', ascending=False)

    if recent.empty:
        recent = df.sort_values('time', ascending=False).head(10)
        intro = (
            "Hallo! In den letzten 7 Tagen gab es keine größeren Erdbeben über Mag 4. "
            "Hier dennoch ein kurzer Überblick:\n\n"
        )
    else:
        intro = "Hallo! Hier die auffälligsten Erdbeben der letzten 7 Tage:\n\n"

    records = recent[['place','mag','time']].head(20).to_dict(orient='records')
    data_text = "\n".join(
        f"{r['time'].strftime('%Y-%m-%d')}: {r['place']} (Mag {r['mag']})"
        for r in records
    )

    prompt = (
            intro
            + data_text
            + "\n\nBitte fasse in 2–3 Sätzen flüssig und freundlich zusammen und schließe mit „Bleib sicher!“.  "
    )

    out = summarizer(prompt, max_length=150, min_length=50, do_sample=False)
    summary = out[0].get('summary_text', '').strip()

    if not summary:
        summary = (
            "In den letzten 7 Tagen gab es keine auffälligen Erdbeben über Mag 4. Bleib sicher!"
        )

    return summary
