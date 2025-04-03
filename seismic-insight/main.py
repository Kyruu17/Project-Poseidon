# main.py

from src import (
    fetch_earthquake_data,
    clean_earthquake_data,
    perform_analysis,
    generate_summary_from_data,
    map_epicenters,
)

def main():
    # Step 1: Get data
    raw_df = fetch_earthquake_data("2025-03-01", "2025-04-01")

    # Step 2: Clean it
    cleaned_df = clean_earthquake_data()

    # Step 3: Analyze
    results = perform_analysis(cleaned_df)
    print("📊 Analysis Results:", results)

    # Step 4: Summary (simulated LLM)
    summary = generate_summary_from_data(cleaned_df)
    print("🧠 Summary:\n", summary)

    # Step 5: Visuals
    map_epicenters(cleaned_df)
    print("🗺️ Earthquake map saved.")

if __name__ == "__main__":
    main()
