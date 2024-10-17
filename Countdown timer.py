import streamlit as st
from datetime import datetime, timedelta

# Function to calculate remaining time for each event
def calculate_time_remaining(event_date):
    now = datetime.now()
    time_remaining = event_date - now
    return time_remaining

# Main app interface
def main():
    st.title("🎉 Event Countdown Timer for Siblings 🎉")
    st.write("Create countdowns for your special events like birthdays, holidays, or trips!")

    # Initialize session state to store events
    if 'events' not in st.session_state:
        st.session_state['events'] = []

    # Input for adding a new event
    with st.form("Add Event"):
        event_name = st.text_input("Event Name", placeholder="e.g., Birthday, Holiday")
        event_date = st.date_input("Event Date", min_value=datetime.now().date())
        submit_button = st.form_submit_button(label="Add Event")

    if submit_button:
        event_date_time = datetime.combine(event_date, datetime.min.time())
        if event_name:
            st.session_state['events'].append({
                'name': event_name,
                'date': event_date_time
            })
            st.success(f"Event '{event_name}' added successfully!")
        else:
            st.error("Please enter an event name.")

    # Display upcoming events
    if st.session_state['events']:
        st.subheader("Upcoming Events")
        for event in st.session_state['events']:
            time_left = calculate_time_remaining(event['date'])
            if time_left.days >= 0:
                st.write(f"**{event['name']}**: {time_left.days} days left! 🎉")
                st.progress((365 - time_left.days) / 365)
            else:
                st.write(f"**{event['name']}** has already passed. 🥳")

if __name__ == "__main__":
    main()
