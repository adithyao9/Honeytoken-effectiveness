import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "./decoys_output"
LOG_FILE = "access_log.txt"

class DecoyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.log_event("MODIFIED", event.src_path)

    def on_created(self, event):
        self.log_event("CREATED", event.src_path)

    def on_deleted(self, event):
        self.log_event("DELETED", event.src_path)

    def log_event(self, action, path):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {action}: {path}\n"
        print(line.strip())
        with open(LOG_FILE, "a") as f:
            f.write(line)

def main():
    event_handler = DecoyHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=False)
    observer.start()
    print(f"Watching {WATCH_DIR} for changes... (Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()