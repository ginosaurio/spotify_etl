import pandas as pd

def transform(raw_data, date):
    data = []
    for r in raw_data["items"]:
        data.append(
            {
                "played_at": r["played_at"],
                "artist": r["track"]["artists"][0]["name"],
                "track": r["track"]["name"]
            }
        )
    df = pd.DataFrame(data)
    

    # Remove dates different from what we want
    clean_df = df[pd.to_datetime(df["played_at"]).dt.date == date.date()]

    # Data validation FTW
    if not df["played_at"].is_unique:
        raise Exception("A value from played_at is not unique")

    if df.isnull().values.any():
        raise Exception("A value in df is null")

    return df