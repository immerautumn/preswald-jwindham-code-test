from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px
import pandas as pd

connect()
"""
According to documentation, this should work with TOML configured name, and from filename specifically.
It consistently returns None, should for CSV use duckDb, perhaps silent failure? Moving to Pandas instead.  https://docs.preswald.com/data/query
"""
# df = get_df("data/mmp_sample_data.csv", table_name="mmp_sample_data")
# filtered_df = query(sql, 'data/mmp_sample_data.csv')
# text(str(filtered_df))
df = pd.read_csv("data/mmp_sample_data.csv")
df_filtered_event_value = df[df["event_value"].notnull()]
df_grp_country_avg_evt_val = df_filtered_event_value.groupby("country")["event_value"].mean().reset_index()
# text(str(df))
text("# Jwind Data Analysis App")
table(df_grp_country_avg_evt_val, title="Filtered Data")

fig = px.scatter(df, x="country", y="event_value", color="event_type", title="Example MMP Fraud detection")
plotly(fig)