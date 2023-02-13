import pandas as pd

def rec_add(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + rec_add(lst[1:])

def split_csv_data(csv_file, num_splits, new_file_path):
    df_tot = pd.read_csv(csv_file, delim_whitespace=True, header=None)
    column_names = df_tot.columns
    num_rows = df_tot.shape[0]
    file_splits_len = []
    if num_rows % num_splits == 0:
        for i in range(num_splits):
            file_splits_len.append(int(num_rows / num_splits))
    else:
        for i in range(num_splits - 1):
            file_splits_len.append(int((num_rows // num_splits)))
        file_splits_len.append(num_rows - sum(file_splits_len))

    splits = []
    splits.append(file_splits_len[0])

    for i in range(num_splits):
        if i == 0:
            continue
        else:
            x = rec_add(file_splits_len[0:i+1])
            splits.append(x)

    pandas_dfs = []
    for i in range(num_splits):
        if i == 0:
            split_df = df_tot.iloc[0:splits[i]]
            split_df.reset_index(inplace=True)
            pandas_dfs.append(split_df)
        else:
            split_df = df_tot.iloc[splits[i-1]:splits[i]]
            split_df.reset_index(inplace=True)
            pandas_dfs.append(split_df)

    for i in range(num_splits):
        pandas_dfs[i].to_csv(new_file_path + "_split_" + str(i+1) + ".csv")


csv_file = r"data/talkbank_transcripts_metadata/language_disorders.csv"
new_file_path = r"data/talkbank_transcripts_metadata/language_disorders"
split_csv_data(csv_file, 3, new_file_path)

