import tkinter as tk
import pygame
import datetime
import threading

def set_alarm():
    alarm_time = entry.get()
    interval = int(interval_entry.get())  # Get the interval between alarms in minutes
    maxtime = duration_entry.get()  # Get the duration of the alarm in seconds

    # Format the alarm time to HH:MM
    formatted_time = alarm_time[:2] + ":" + alarm_time[2:]
    maxtime = maxtime[:2] + ":" + maxtime[2:]
    label.config(text="Alarm set for: " + formatted_time)

    # Start the timer loop in a background thread
    t = threading.Thread(target=check_alarm, args=(formatted_time, interval, maxtime))
    t.start()

def check_alarm(alarm_time, interval, maxtime):
    while True:
        # Get the current time in HH:MM format
        current_time = datetime.datetime.now().strftime('%H:%M')

        # Check if it's time for the alarm
        if current_time == alarm_time:
            play_alarm()
        if current_time == maxtime:
            break

        # Wait for the specified interval before checking again
        datetime.datetime.now() + datetime.timedelta(minutes=interval)

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/varun/Downloads/alarm.mp3")  # Replace "alarm.mp3" with your MP3 file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if paused:
            pygame.mixer.music.stop()
            break

def pause_alarm():
    global paused
    paused = True

def resume_alarm():
    global paused
    paused = False

# Create the GUI window
window = tk.Tk()
window.title("Alarm Clock")

# Create and place the widgets
label = tk.Label(window, text="Enter alarm time (HHMM):")
label.pack()

entry = tk.Entry(window)
entry.pack()

interval_label = tk.Label(window, text="Enter interval between alarms (minutes):")
interval_label.pack()

interval_entry = tk.Entry(window)
interval_entry.pack()

duration_label = tk.Label(window, text="Enter max alarm time:")
duration_label.pack()

duration_entry = tk.Entry(window)
duration_entry.pack()

button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

pause_button = tk.Button(window, text="Pause Alarm", command=pause_alarm)
pause_button.pack()

resume_button = tk.Button(window, text="Resume Alarm", command=resume_alarm)
resume_button.pack()

# Global variable to track if the alarm is paused or not
paused = False

# Start the GUI event loop
window.mainloop()
