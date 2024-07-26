import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


df = pd.read_csv("data/cases_cumulative_daily.csv",encoding="utf-8")

#df["Cumulative_Iwate"] = df["Iwate"].cumsum()
df["Cumulative_Iwate"] = df["Iwate"].diff().fillna(0)
#print(df["Cumulative_Iwate"])

df["Date"] = pd.to_datetime(df["Date"])

df_iwate = df[["Date","Iwate"]]

fig, ax1 = plt.subplots(figsize=(10,5))

ax1.bar(df_iwate["Date"],df_iwate["Iwate"],label = "岩手の累計感染者数")

ax2 = ax1.twinx()
ax2.plot(df["Date"],df["Cumulative_Iwate"],label="岩手の1日の累計感染者数")

ax1.set_ylabel("岩手の累計感染者数")
ax2.set_ylabel("岩手の新規感染者数")
ax1.set_xlabel("日付")
ax1.set_title("岩手の累計感染者数と１日の累計感染者数")

fig.tight_layout()
fig.legend(loc="upper left",bbox_to_anchor=(0.1,0.9))
plt.show()


