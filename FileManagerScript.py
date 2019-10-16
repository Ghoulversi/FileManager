from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_created(self, event):
        print("opa changed")
    
    def on_modified(self, event):
        print("Join func")
        new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            print(filename.title)
            file_exist = os.path.isfile(folder_destination + "/" + new_name)
            while file_exist:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exist = os.path.isfile(folder_destination + "/" + new_name)
                
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)
            
folder_to_track = "Folder Path - where to track"
folder_destination = "Folder path - where to move"
print(os.getcwd())
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start

print("here?")

try:
    while True:
        time.sleep(10)
        print("lel")
except KeyboardInterrupt:
    observer.stop()
observer.join()

