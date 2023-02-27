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
            if r == "TRUE":
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


def rename_columns(df) -> pd.DataFrame:
    """ Adds a space between columns for readability """
    # Credit to user @lexual on Stack Overflow: https://stackoverflow.com/a/11354850
    return df.rename(columns={'PrivacyPolicy': 'Privacy Policy',
                              'RequestForm': 'Request Form',
                              'RequestType': 'Request Type'
                              })


def convert_bools(df) -> pd.DataFrame:
    """ Converts all bools in the table to string for processing """

    mask = df.applymap(type) != bool
    d = {True: 'TRUE', False: 'FALSE'}
    return df.where(mask, df.replace(d))


if __name__ == '__main__':
    input_file_path = 'master_test.csv'
    output_file_path = 'master_test_md.csv'

    print("Beginning program.")

    try:
        df = pd.read_csv(input_file_path)
    except:
        print("Couldn't read .CSV file. Check formatting and try again.")
        quit()

    print("File opened:", input_file_path, "|", "Writing to:", output_file_path)

    print("Markdown-ifying...")
    df = convert_bools(df)
    df = emojify_frameworks(df)
    df = emojify_links(df)
    df = rename_columns(df)

    df.to_csv(output_file_path, index=False) # Saves the result to CSV in output path

    print("Complete!")