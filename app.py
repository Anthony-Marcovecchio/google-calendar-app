import streamlit as st
from auth import authenticate_user
from calendar_service import list_events, create_event

st.title("Google Calendar App")

if "service" not in st.session_state:
    st.session_state.service = None

if not st.session_state.service:
    st.write("Authenticate to access your Google Calendar.")
    if st.button("Login"):
        st.session_state.service = authenticate_user()
else:
    st.write("Authenticated! Fetching calendar events...")
    service = st.session_state.service
    events = list_events(service)
    st.write("Upcoming Events:")
    for event in events:
        st.write(f"{event['start']['dateTime']}: {event['summary']}")

    st.write("Add a new event:")
    title = st.text_input("Event Title")
    start = st.text_input("Start Time (YYYY-MM-DDTHH:MM:SS)")
    end = st.text_input("End Time (YYYY-MM-DDTHH:MM:SS)")

    if st.button("Add Event"):
        create_event(service, {"summary": title, "start": start, "end": end})
        st.success("Event added successfully!")
