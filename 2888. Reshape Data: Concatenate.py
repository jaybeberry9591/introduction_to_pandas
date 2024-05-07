import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    frames = [df1,df2]
    df_keys = pd.concat(frames)
    return df_keys
