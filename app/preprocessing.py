import pandas as pd

def prepare_series(df):

    df = df.dropna()
    df = df.sort_values("ds")
    df = df.drop_duplicates(subset="ds")

    df = df.set_index("ds")

    freq = pd.infer_freq(df.index)

    if freq:
        df = df.asfreq(freq)
    else:
        df = df.asfreq("D")

    df["y"] = df["y"].interpolate()

    return df["y"]