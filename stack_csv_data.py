import pandas as pd


def stack_csv_data(csv_path_lst, save_path):
    df_lst = []

    for csv_file in csv_path_lst:
        df = pd.read_csv(csv_file)
        df_lst.append(df)

    result_df = pd.concat(df_lst, ignore_index=True)

    result_df.to_csv(save_path)
    return None


csv_path_lst = [r"data/raw_talkbank_data/language_disorders_scraped_split_1.csv",
                r"data/raw_talkbank_data/language_disorders_scraped_split_2.csv",
                r"data/raw_talkbank_data/language_disorders_scraped_split_3.csv"]
save_path = r"data/raw_talkbank_data/language_disorders.csv"

stack_csv_data(csv_path_lst, save_path)
