# %%
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine
import plotly.express as px
import streamlit as st

# %%
_ = load_dotenv(find_dotenv())
connection_string = os.getenv("POSTGRESQL_ADDON_URI")
sql_engine = create_engine(connection_string)

# %%
st.set_page_config(page_title="Responses Dashboard",
                    page_icon=":sparkles:",
                   layout="wide")

# %%
df = (pd.read_sql_table("questions_db", sql_engine)
 .sort_values(by="index")
 .reset_index(drop=True)
 )

# %%
df.head()

# %%
df.columns
# %%
