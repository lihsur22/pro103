import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")

e = px.scatter(df, x="date", y="cases", color="country", title="Covid Cases", height= 900, width= 1800)

e.show()