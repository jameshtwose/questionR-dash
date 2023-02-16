
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import style_utils as utl

# CONFIG
st.set_page_config(page_title="Responses Dashboard",
                   page_icon=":sparkles:",
                   layout="wide")
# Loading CSS
utl.remote_preconnect_css('https://fonts.googleapis.com')
utl.remote_preconnect_crossorigin_css('https://fonts.gstatic.com')
utl.remote_css('https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap')
utl.local_css("style.css")


# CREATE CACHE DATA FUNCTION
@st.cache_data(ttl=600)
def get_data():
    _ = load_dotenv(find_dotenv())
    connection_string = os.getenv("POSTGRESQL_ADDON_URI")
    sql_engine = create_engine(connection_string)
    return (pd.read_sql_table("questions_db", sql_engine)
            .sort_values(by="index")
            .reset_index(drop=True)
            )

# READ DATA
df = get_data()


# SIDEBAR
st.sidebar.header("Please filter here:")
valence = st.sidebar.multiselect("Select a valence:",
                                 options=df["valence"].unique(),
                                 default=df["valence"].unique()
                                 )
st.sidebar.markdown("---")
st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("""
                    <div style="text-align: center; padding-right: 10px;">
                        <img alt="logo" src="https://services.jms.rocks/img/logo.png" width="100">
                    </div>
                    """,
                    unsafe_allow_html=True)
st.sidebar.markdown("""
                    <div style="text-align: center; color: #E8C003; margin-top: 40px; margin-bottom: 40px;">
                        <a href="https://services.jms.rocks" style="color: #E8C003;">Created by James Twose</a>
                    </div>
                    """, unsafe_allow_html=True)

# Query based on sidebar
df_selection = df.query("valence == @valence")

total_amount_votes = df["votes"].sum()
min_max_amount_votes = df[["narrativeTitle", "votes"]].agg(["min", "max"])
average_vote_amount_per_valence = df.groupby(
    "valence")["votes"].mean().round(2).to_frame().T

# MAINPAGE
st.markdown("<h1>Responses Dashboard</h1>", unsafe_allow_html=True)
left_column, middle_column, right_column = st.columns([1.5, 3, 4.2])
with left_column:
    st.subheader("Total Responses")
    st.subheader(total_amount_votes)
with middle_column:
    st.subheader("Least and Most Important Narratives")
    st.dataframe(min_max_amount_votes)
with right_column:
    st.subheader("Average (mean) Vote Amount Per Valence")
    st.dataframe(average_vote_amount_per_valence, height=50)
st.markdown("---")
st.header("Votes Dataframe")
st.dataframe(df_selection)
st.markdown("---")
st.header("Descriptive Statistics")
st.dataframe(df_selection.drop(columns=["index", "id"]).describe())
st.markdown("---")

# Votes plot
votes_bar = px.bar(df_selection, x="narrativeTitle", y="votes", color="valence",
                   title="<b>Votes per Narrative</b>", height=600, width=1200,
                   color_discrete_sequence=utl.jms_color_list)
votes_bar.add_trace(
        go.Scatter(
            x=df_selection["narrativeTitle"],
            y=df_selection["votes"],
            text=df_selection["votes"],
            mode="text",
            textposition="top center",
            textfont=dict(
                size=16),
            showlegend=False,
        )
    )

st.plotly_chart(votes_bar)


# HIDE STREAMLIT STYLE
hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CUSTOM ELEMENTS
custom_elements = """
                        <style>
                        footer {visibility: show;}
                        </style>
                    <footer class="footer">
                        Created in 2023 by <a href="https://services.jms.rocks">James Twose</a>
                    </footer>
                    """
st.markdown(custom_elements, unsafe_allow_html=True)

