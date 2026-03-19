import pandas as pd


def calculate_conversion_rate(df):
    """
    Calculates the relationship between clicks on sale products vs regular products.

    Sale category = 4
    Regular categories = 1, 2, 3

    Parameters:
        df (pd.DataFrame)

    Returns:
        dict: conversion metrics
    """

    # Count clicks on "sale" products
    sale_clicks = len(df[df["page 1 (main category)"] == 4])

    # Count clicks on regular products
    regular_clicks = len(df[df["page 1 (main category)"].isin([1, 2, 3])])

    # Total clicks
    total_clicks = sale_clicks + regular_clicks

    # Avoid division by zero
    if total_clicks == 0:
        conversion_rate = 0
    else:
        conversion_rate = sale_clicks / total_clicks

    # Print insight (VERY valuable for storytelling)
    print("=== Conversion Analysis ===")
    print(f"Sale clicks: {sale_clicks}")
    print(f"Regular clicks: {regular_clicks}")
    print(f"Conversion rate (sale): {conversion_rate:.2%}")

    return {
        "sale_clicks": sale_clicks,
        "regular_clicks": regular_clicks,
        "conversion_rate": conversion_rate
    }