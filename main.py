# Importing required libraries
import streamlit as st
from datetime import datetime, time
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Title of the app
st.title("Time Zone Converter")

# App description 
st.write("Convert your local time to any other time zone.")

# Display current time in selected time zones
selected_time_zone = st.multiselect("Select Time Zone", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Current Time in Selected Time Zones")
for tz in selected_time_zone:
    current_time = datetime.now(ZoneInfo(tz))
    st.write(f"Time in **{tz}** is {current_time.strftime('%Y-%m-%d %I:%M %p')}")

# Convert time to selected time zone
st.subheader("Convert Time Between Time Zones")
current_time = st.time_input("Current Time", value=datetime.now().time())  # FIXED
from_tz = st.selectbox("From Time Zone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Time Zone", TIME_ZONES, index=1)

# Convert time to selected time zone
if st.button("Convert Time"):
    # Correct way to set timezone
    dt = datetime.combine(datetime.today(), current_time).replace(tzinfo=ZoneInfo(from_tz))  # FIXED
    converted_time = dt.astimezone(ZoneInfo(to_tz))
    
    st.success(f"Time & Date in **{to_tz}** is {converted_time.strftime('%Y-%m-%d %I:%M %p')}")
