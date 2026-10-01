from datetime import datetime,timedelta

event = input("Enter Event Name: ")
event_datetime = input("Enter Event Date & Time (YYYY-MM-DD HH:MM): ")

try:
    event_date_time = datetime.strptime(event_datetime, "%Y-%m-%d %H:%M")
    current_date_time = datetime.now()
    time_remaining = event_date_time-current_date_time

    
    if time_remaining>=timedelta(0):
        
        total_seconds = int(time_remaining.total_seconds())

        days = total_seconds // (24 * 60 * 60)
        hours = (total_seconds % (24 * 60 * 60)) // (60 * 60)
        minutes = (total_seconds % (60 * 60)) // 60

        print()
        print(f"Countdown to {event}:")
        print()
        print(f"{days} Days, {hours} Hours, and {minutes} Minutes remaining! ")


    else:
        print(f"Event {event} has already passed!")

except ValueError:
    print("Invalid Date format!")
    print("Please use: YYYY-MM-DD HH:MM")