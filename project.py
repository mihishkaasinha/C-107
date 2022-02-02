from statistics import mean
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
df_main = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

fig = px.scatter(df_main, x = "student_id", y = "level", color = "attempt", size = "attempt")
fig.show()