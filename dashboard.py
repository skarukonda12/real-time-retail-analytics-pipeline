import streamlit as st
import pandas as pd
import psycopg2
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000)

conn = psycopg2.connect(
    host="localhost",
    database="retail_db",
    user="shivaprasadreddy"
)

query = "SELECT * FROM detections"
df = pd.read_sql(query, conn)

st.title("Retail Dashboard")

if df.empty:
    st.warning("No detections found.")
else:
    df["date"] = pd.to_datetime(df["detected_at"]).dt.date

    st.sidebar.title("Filters")

    objects = df["label"].unique()

    selected_object = st.sidebar.selectbox(
        "Select Object",
        objects
    )

    selected_date = st.sidebar.date_input(
        "Select Date"
    )

    filtered_df = df[df["date"] == selected_date]

    if selected_object != "All":
        filtered_df = filtered_df[
            filtered_df["label"] == selected_object
        ]


    st.subheader("Filtered Detections")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Detections", len(filtered_df))

    with col2:
        st.metric(
            "Avg Confidence",
            round(filtered_df["confidence"].mean(), 2)
            if len(filtered_df) > 0 else 0
        )

    st.dataframe(filtered_df)
    
    csv = filtered_df.to_csv(index=False)

    st.download_button(
        "Download CSV",
        csv,
        "detections.csv",
        "text/csv"
    )
    st.subheader("All Detections")
    st.dataframe(df)


    

    st.subheader("Latest Images")

    for _, row in filtered_df.tail(5).iterrows():
        st.write(f"{row['label']} ({row['confidence']:.2f})")
        st.image(row["img_path"], width=250)

    st.subheader("Search Object")

    search_text = st.text_input("Enter object name")

    search_df = filtered_df[
        filtered_df["label"].str.contains(
            search_text,
            case=False,
            na=False
        )
    ]

    st.dataframe(search_df)

    st.subheader("Object Count Chart")

    if len(filtered_df) > 0:
        st.bar_chart(filtered_df["label"].value_counts())
    else:
        st.info("No data for selected filters.")