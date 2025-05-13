# src/analysis.py

import pandas as pd
from scipy.stats import pearsonr, ttest_ind

def perform_analysis(df: pd.DataFrame) -> dict:
    """
    Perform statistical analysis on earthquake data:
    - Pearson correlation between depth and magnitude
    - T-test on magnitude between top 2 most frequent regions
    Returns a dictionary of results.
    """
    results = {}

    # Correlation: depth vs. magnitude
    corr_coef, corr_p = pearsonr(df["depth"], df["mag"])
    results["correlation"] = {
        "coefficient": corr_coef,
        "p_value": corr_p
    }

    # T-test: magnitude between top 2 regions
    top_regions = df["region"].value_counts().index[:2]
    if len(top_regions) == 2:
        group1 = df[df["region"] == top_regions[0]]["mag"]
        group2 = df[df["region"] == top_regions[1]]["mag"]
        t_stat, t_p = ttest_ind(group1, group2, equal_var=False)
        results["t_test"] = {
            "region_1": top_regions[0],
            "region_2": top_regions[1],
            "t_statistic": t_stat,
            "p_value": t_p
        }
    else:
        results["t_test"] = "Not enough regions to compare."

    return results
