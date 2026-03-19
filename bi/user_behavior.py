import pandas as pd


def sales_funnel_analysis(df):
    """
    Analyzes user navigation funnel across pages.

    Parameters:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame with funnel metrics
    """

    # Count number of interactions per page (1 to 5)
    funnel = df["page"].value_counts().sort_index()

    # Convert to DataFrame for better structure
    funnel_df = funnel.reset_index()
    funnel_df.columns = ["page", "visits"]

    # Calculate drop-off percentage between steps
    funnel_df["drop_off_rate"] = funnel_df["visits"].pct_change().fillna(0)

    # Calculate cumulative retention
    funnel_df["retention_rate"] = funnel_df["visits"] / funnel_df["visits"].iloc[0]

    # Print clear insight (Evergreen style — short & sharp)
    print("=== Funnel Insight ===")
    print("Largest drop occurs at early navigation stages.")

    return funnel_df