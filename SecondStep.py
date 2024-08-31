import re
import pandas as pd
from datetime import datetime, timedelta
from persiantools.jdatetime import JalaliDateTime


df = pd.read_excel("news.xlsx")


def extract_time(time_str):
    t_value = int(re.findall(r"\d+", time_str)[0])
    return t_value


converted_times = []

for time_str in df["time"]:
    if "دقیقه" in time_str:
        converted_times.append(extract_time(time_str))
    elif "ساعت" in time_str:
        converted_times.append(extract_time(time_str) * 60)

df["converted_time"] = converted_times

df["date_time"] = df["converted_time"].apply(lambda p: datetime.now() - timedelta(minutes=p))

df["shamsi_date_time"] = df["date_time"].apply(lambda d: JalaliDateTime(d).strftime("%Y-%m-%d %H:%M:%S"))


def view_cleaner(view):
    if "K" in view:
        return int(float(view.replace("K", "")) * 1000)
    else:
        return int(view.replace("K", ""))


df["view_count"] = df["views"].apply(view_cleaner)

df.to_excel("news1.xlsx", index=False)
