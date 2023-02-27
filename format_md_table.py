import pandas as pd

def emojify_links(df) -> pd.DataFrame:
    """
    Converts a cell to a linked emoji corresponding to the column type, ie, "emojifying" it
    """
    emoji_dict = {"Contact": "[:mail:]",
                  "RequestForm": "[:memo:]",
                  "PrivacyPolicy": "[:blue_book:]"}

    for k in emoji_dict.keys():
        i = 0
        for r in df[k]:
            if type(r) == str:
                r = "{emoji}(".format(emoji=emoji_dict[k]) + r.strip() + ")"
                df.at[i, k] = r
            else:
                df.at[i, k] = ""
            i += 1
    return df


def emojify_frameworks(df) -> pd.DataFrame:
    """
    Adds a checkmark to any cell marked True in any of the privacy framework columns
    """
    for col in ["CCPA", "CPA", "CTDPA", "CDPA", "UCPA"]:
        i = 0
        for r in df[col]:
            if type(r) is bool and r:  # cell is True
                df.at[i, col] = ":heavy_check_mark:"
            else:  # cell is False or empty
                df.at[i, col] = ""
            i += 1

    return df


def cleanse_request_type(df) -> pd.DataFrame:
    """
    Prepares the request type column for parsing for stats
    """
    i = 0
    for r in df["RequestType"]:
        if type(r) is not str:
            df.at[i, r] = ""
        else:  # cell is False or empty
            df.at[i, r] = r.strip()
        i += 1

    return df