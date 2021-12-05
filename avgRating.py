import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv("data.csv")
data = df["Avg Rating"].tolist()
print(data)
fig = ff.create_distplot([data],["rating"],show_hist=False)
fig.show()