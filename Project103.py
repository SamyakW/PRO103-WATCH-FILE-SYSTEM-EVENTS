import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/user/Downloads/Sample"

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"{event.src_path} has been created.")

    def on_deleted(self, event):
        print (f"{event.src_path} is deleted!")
    
    def on_modified(self,event):
        print (f"{event.src_path} has been modified.")
    
    def on_moved(self,event):
        print(f"{event.src_path} is moved to {event.dest_path}.")
    
    def on_rename(self,event):
        print(f"{event.src_path} is renamed.")

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Working...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()
