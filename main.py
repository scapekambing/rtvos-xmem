## ctrl +c to stop process

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import find 
import GUI

class ImageHandler(FileSystemEventHandler):

    def __init__(self, boundary):
        super().__init__()
        self.boundary = boundary

    def process_image(self, image_path):
        # This method contains the logic to process an image.
        # You can modify this method to include the actual processing logic.
        print(f"Processing image: {image_path}")
        find.detect_objects_out_of_bounds(image_path, self.boundary)
        
    def on_created(self, event):
        # This method is called when a new file is created.
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg')):
            self.process_image(event.src_path)

    def on_modified(self, event):
        # This method is called when a file is modified.
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg')):
            self.process_image(event.src_path)

def main():

    ## Set the first frame here
    # first_frame = os.path.join(os.getcwd(), "mask")
    # first_frame = os.path.join(first_frame, "00000.png")
    # print("first frame: " + first_frame)

    ## Select the frames by GUI

    first_frame_path = GUI.select_first_frame()
    
    if not first_frame_path:
        print("No file selected.")
        return
    
    boundary = GUI.select_points(first_frame_path)
    handler = ImageHandler(boundary)
    directory_to_watch = os.path.dirname(first_frame_path)

    # First, process all existing images in the directory
    for filename in os.listdir(directory_to_watch):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            handler.process_image(os.path.join(directory_to_watch, filename))

    # Start monitoring the directory for new or modified images
    observer = Observer()
    observer.schedule(handler, directory_to_watch, recursive=False)
    observer.start()

    print(f"Starting to monitor {directory_to_watch} for new or modified images...")
    try:
        while True:
            # os.execute('mv file1 to your working directory')
            # Keep the script running until interrupted
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop monitoring when interrupted
        observer.stop()
        print("Stopped monitoring.")
        
    observer.join()

if __name__ == "__main__":
    main()
