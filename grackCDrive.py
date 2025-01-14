from f_get_drive_space import get_drive_space
from datetime import *
import pandas as pd

total, used, free  = get_drive_space('C:/')
timestamp = datetime.now()

data = {
    "FreeSpace": [free],
    "Date": [timestamp]
}
df = pd.DataFrame(data)
try:
    df2 = pd.read_csv("C:/Users/pongpisut.kon/Desktop/track-free-space.csv")
    df_final = pd.concat([df2, df]).drop_duplicates().reset_index(drop=True)
    df_final.to_csv("C:/Users/pongpisut.kon/Desktop/track-free-space.csv", index=False)
except:
    df.to_csv("C:/Users/pongpisut.kon/Desktop/track-free-space.csv", index=False)