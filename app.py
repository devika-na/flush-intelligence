
import streamlit as st
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Flush Intelligence",
    page_icon="🚽",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown(
    """
    <div style="
        text-align:center;
        padding:20px 0 25px 0;
    ">
        <h1 style="font-size:42px; margin-bottom:5px;">
            🚽 FLUSH INTELLIGENCE
        </h1>
        <p style="font-size:18px; opacity:0.65;">
            Smart Acoustic Toilet Monitoring System
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- LOAD PROJECT DATA ----------
history_df = pd.read_csv("flush_history.csv")

stall_names = ["Stall 1", "Stall 2", "Stall 3", "Stall 4"]

flush_counts = history_df["stall"].value_counts().reindex(
    stall_names,
    fill_value=0
).to_dict()

total_flushes = len(history_df)

anomalies = int(
    (history_df["duration"] > 2.0).sum()
)

most_used = max(
    flush_counts,
    key=flush_counts.get
)

# ---------- KPI CARDS ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🚽 Total Flushes",
        total_flushes
    )

with col2:
    st.metric(
        "🟢 Monitored Stalls",
        4
    )

with col3:
    st.metric(
        "⚠️ Anomalies",
        anomalies
    )

with col4:
    st.metric(
        "📊 Most Used Stall",
        most_used
    )

st.divider()

# ---------- BATHROOM OF THE DAY ----------
st.markdown(
    """
    <div style="
        text-align:center;
        padding:22px;
        border-radius:15px;
        border:2px solid rgba(128,128,128,0.25);
        margin:10px 0 25px 0;
    ">
        <div style="font-size:42px;">🏆</div>
        <h2 style="margin:5px;">BATHROOM OF THE DAY</h2>
        <p style="font-size:26px; font-weight:bold; margin:8px;">
            Bathroom B
        </p>
        <p style="font-size:17px; opacity:0.65;">
            67 flushes today
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- STALL MONITORING ----------
st.subheader("🏢 Stall Monitoring")

cols = st.columns(4)

for i, stall in enumerate(stall_names):

    with cols[i]:

        st.markdown(f"### 🚽 {stall}")

        st.metric(
            "Flushes",
            flush_counts[stall]
        )

        st.success("● MONITORING")

st.divider()

# ---------- FLUSH ACTIVITY ----------
st.subheader("📈 Flush Activity")

chart_data = pd.DataFrame({
    "Stall": list(flush_counts.keys()),
    "Flushes": list(flush_counts.values())
})

st.bar_chart(
    chart_data.set_index("Stall")
)

st.divider()

# ---------- RECENT ACTIVITY ----------
st.subheader("🕒 Recent Flush Activity")

display_df = history_df.copy()

display_df = display_df.sort_values(
    "timestamp",
    ascending=False
)

st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
)

st.divider()

# ---------- SYSTEM ALERTS ----------
st.subheader("🚨 System Alerts")

alerts = history_df[
    history_df["duration"] > 2.0
]

if len(alerts) > 0:

    for _, alert in alerts.iterrows():

        st.error(
            f"⚠️ {alert['stall']} — "
            f"Unusual flush duration: "
            f"{alert['duration']:.2f} seconds"
        )

else:

    st.success(
        "✅ No anomalies detected"
    )

# ---------- FOOTER ----------
st.divider()

st.caption(
    "Flush Intelligence • Acoustic Monitoring • "
    "TDOA Localization • Anomaly Detection"
)
