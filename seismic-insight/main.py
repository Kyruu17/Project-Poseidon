# main.py

from src import (
    fetch_earthquake_data,
    clean_earthquake_data,
    perform_analysis,
    generate_summary_from_data,
    map_epicenters,
)

def main():
 
    raw_df = fetch_earthquake_data("2025-03-01", "2025-04-01")

    cleaned_df = clean_earthquake_data()

    results = perform_analysis(cleaned_df)
    print("Analysis Results:", results)

    summary = generate_summary_from_data(cleaned_df)
    print("Summary:\n", summary)

    map_epicenters(cleaned_df)
    print("Earthquake map saved.")

if __name__ == "__main__":
    main()
