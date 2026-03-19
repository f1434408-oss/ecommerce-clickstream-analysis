# Import pandas for data manipulation
import pandas as pd


def get_country_name(df):
    """
    Maps numeric country codes to country names based on dataset documentation.

    Parameters:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: DataFrame with new column 'COUNTRY_NAME'
    """

    # Complete mapping dictionary (important for real analysis)
    country_mapping = {
        1: "Australia", 2: "Austria", 3: "Belgium",
        4: "British Virgin Islands", 5: "Cayman Islands",
        6: "Christmas Island", 7: "Croatia", 8: "Cyprus",
        9: "Czech Republic", 10: "Denmark", 11: "Estonia",
        12: "Unidentified", 13: "Faroe Islands", 14: "Finland",
        15: "France", 16: "Germany", 17: "Greece",
        18: "Hungary", 19: "Iceland", 20: "India",
        21: "Ireland", 22: "Italy", 23: "Latvia",
        24: "Lithuania", 25: "Luxembourg", 26: "Mexico",
        27: "Netherlands", 28: "Norway", 29: "Poland",
        30: "Portugal", 31: "Romania", 32: "Russia",
        33: "San Marino", 34: "Slovakia", 35: "Slovenia",
        36: "Spain", 37: "Sweden", 38: "Switzerland",
        39: "Ukraine", 40: "United Arab Emirates",
        41: "United Kingdom", 42: "USA",
        43: "biz", 44: "com", 45: "int", 46: "net", 47: "org"
    }

    # Map numeric country codes to names
    df["country_name"] = df["country"].map(country_mapping)

    return df

def clean_currency_data(df):
    """
    Cleans and validates the PRICE column.

    - Removes null values
    - Removes non-positive prices (<= 0)
    - Logs number of affected rows

    Parameters:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    # Store initial row count for comparison
    initial_rows = len(df)

    # Count null values before cleaning
    null_count = df["price"].isnull().sum()

    # Remove null values
    df = df.dropna(subset=["price"])

    # Count non-positive values
    non_positive_count = (df["price"] <= 0).sum()

    # Keep only valid prices (> 0)
    df = df[df["price"] > 0]

    # Store final row count
    final_rows = len(df)

    # Print summary (data quality check)
    print("=== Data Cleaning Summary ===")
    print(f"Initial rows: {initial_rows}")
    print(f"Null values removed: {null_count}")
    print(f"Non-positive values removed: {non_positive_count}")
    print(f"Final rows: {final_rows}")

    return df