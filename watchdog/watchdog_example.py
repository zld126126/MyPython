import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#设置打印级别
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
#设置观察目录
ROOT_PATH = 'D:\\'

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info("文件被修改了 %s" % event.src_path)

    def on_created(self, event):
        logging.info("文件被创建了 %s" % event.src_path)

if __name__ == "__main__":
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = ROOT_PATH
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()