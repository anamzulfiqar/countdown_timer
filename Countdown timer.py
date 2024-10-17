import streamlit as st
from datetime import datetime, timedelta
import time

# Function to calculate remaining time for each event
def calculate_time_remaining(event_date):
    now = datetime.now()
    time_remaining = event_date - now
    return time_remaining

# Function to create progress bar animation
def show_countdown_animation(days_left):
    progress = (365 - days_left) / 365
    st.progress(progress)

# Main app interface
def main():
    st.title("🎉 Event Countdown Timer for Siblings 🎉")
    st.write("Create countdowns for your special events like birthdays, holidays, or trips!")

    # Initialize session state to store events
    if 'events' not in st.session_state:
        st.session_state['events'] = []

    # Add a new event
    st.subheader("Add a New Event")
    event_name = st.text_input("Event Name", placeholder="e.g., Birthday, Holiday")
    event_date = st.date_input("Event Date", min_value=datetime.now().date())

    if st.button("Add Event"):
        event_date_time = datetime.combine(event_date, datetime.min.time())
        st.session_state['events'].append({
            'name': event_name,
            'date': event_date_time
        })
        st.success(f"Event '{event_name}' added successfully!")

    # Display existing countdowns
    if st.session_state['events']:
        st.subheader("Upcoming Events")
        for event in st.session_state['events']:
            days_left = (event['date'] - datetime.now()).days

            if days_left >= 0:
                st.write(f"**{event['name']}**: {days_left} days left! 🎉")
                show_countdown_animation(days_left)
            else:
                st.write(f"**{event['name']}** has already passed. 🥳")

    # Notifications or reminders (not fully supported in Streamlit directly)
    st.info("You will receive a notification when an event is approaching (in the real app).")

if __name__ == "__main__":
    main()
