import os
import pandas as pd
from tqdm import tqdm as td


def IngestInputs(path):
    data = []
    for filename in td(os.listdir(path), ascii=True):
        if filename.endswith(".txt"):
            filepath = os.path.join(path, filename)
            with open(filepath, "r") as file:
                for line in file:
                    row = line.strip().split()
                    row.append(filename[:11])
                    row = [
                        str(row[0]),
                        int(row[1]),
                        int(row[2]),
                        int(row[3]),
                        str(row[4]),
                    ]
                    row.append(row[0][:4])
                    data.append(row)

    df = pd.DataFrame(
        data, columns=["Date", "Max_Temp", "Min_Temp", "PPT", "Station_ID", "Year"]
    )
    df = df[(df["Max_Temp"] != -9999) & (df["Min_Temp"] != -9999) & (df["PPT"] != -9999)]
    return df


def WeatherMetrics(df):
    groupby_cols = ["Year", "Station_ID"]
    agg_funcs = {"Max_Temp": "mean", "Min_Temp": "mean", "PPT": "sum"}
    result = (
        df.groupby(groupby_cols)
        .agg(agg_funcs)
        .rename(
            columns={"Max_Temp": "Avg_Max_Temp", "Min_Temp": "Avg_Min_Temp", "PPT": "AccPPT"}
        )
        .reset_index()
    )
    return result
