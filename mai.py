import datetime
import time

# Define your daily routine schedule (24-hour format "HH:MM")
DAILY_ROUTINE = {
    "07:00": "Wake up and stretch! 🌅",
    "08:30": "Time for breakfast and coffee. ☕",
    "09:00": "Start working / studying. 💻",
    "13:00": "Lunch break! Take a walk. 🚶‍♂️",
    "18:00": "Exercise or gym time. 💪",
    "22:30": "Wind down and get ready for sleep. 🛌",
}

print("📅 Daily Routine Reminder is running... Press Ctrl+C to stop.")

try:
    while True:
        # Get the current time in HH:MM format
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Check if the current time matches any routine item
        if current_time in DAILY_ROUTINE:
            print(f"\n⏰ REMINDER [{current_time}]: {DAILY_ROUTINE[current_time]}")
            # Sleep for 61 seconds to avoid triggering the same reminder twice in the same minute
            time.sleep(61)

        # Check the time every 30 seconds
        time.sleep(30)

except KeyboardInterrupt:
    print("\n👋 Reminder system stopped.")
