import re
import os
import logging
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
LUA_FILE_NAME = 'version_info.lua'      #Lua版本文件
WHITELIST_FILE_NAME = 'whitelist.txt'   #白名单文件
ROOT_PATH = 'D:\\'                      #监控文件路径
 
class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, **kwargs):
        super(FileMonitorHandler, self).__init__(**kwargs)
        # 监控目录 目录下面以device_id为目录存放各自的图片
        self._watch_path = game_path
 
    # 重写文件改变函数，文件改变都会触发文件夹变化
    def on_modified(self, event):
        if not event.is_directory:  # 文件改变都会触发文件夹变化
            file_path = event.src_path
            logging.info("file changed: %s " % file_path)
            file_name = os.path.split(file_path)[-1]
            # 白名单或者配置文件修改，则触发事件
            if file_name == LUA_FILE_NAME:  # lua文件发生变化
                # 验证该目录下是否存在白名单文件
                whitelist_file, is_exists = check_file_exists(file_path, WHITELIST_FILE_NAME)
                if not is_exists:  # 不存在白名单，则不进行修改操作
                    logging.info(f'{whitelist_file} not exists')
                else:
                    # 读取文件进行替换操作
                    whitelist_handler(file_path, whitelist_file)
            elif file_name == WHITELIST_FILE_NAME:  # 白名单文件发生变化
                # 验证配置文件是否存在
                lua_file, is_exists = check_file_exists(file_path, LUA_FILE_NAME)
                if not is_exists:  # 不存在Lua文件
                    logging.info(f'{lua_file} not exists')
                else:
                    whitelist_handler(lua_file, file_path)
        else:
            logging.info('Director changed')
 
    def on_created(self, event):
        pass
 
 
def check_file_exists(path, file_name):
    """
    验证文件的存在性
    """
    file_path = os.path.join(os.path.dirname(path), file_name)
    is_exists = os.path.isfile(file_path)
    return file_path, is_exists
 
def replace_content(lua_file, new_str):
    with open(lua_file, 'r', encoding='utf-8') as f1, open("%s.bak" % lua_file, "w", encoding='utf-8') as f2:
        old_content = f1.read()
        if 'testId' in old_content:
            # 进行正则匹配
            pattern = re.compile(r'testId = "(.*?)"', re.M | re.S)
            new_content = re.sub(pattern, f'testId = "{new_str}"', old_content)
            logging.info('Old content:%s' % old_content)
            logging.info('New content:%s' % new_content)
            f2.write(new_content)
 
    os.remove(lua_file)
    os.rename("%s.bak" % lua_file, lua_file)
 
 
def whitelist_handler(lua_file, whitelist_file):
    """
    白名单处理
    """
    with open(whitelist_file, 'r', encoding='utf-8') as f:
        whitelist_content = f.read().replace("\n", "")
    logging.info(f'Replace content: lua_file->{lua_file} whitelist content->{whitelist_content}')
    replace_content(lua_file, whitelist_content)
 
def main():
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=game_path, recursive=True)  # recursive递归的
    observer.start()
    observer.join()
 
 
if __name__ == '__main__':
    global game_path
    game_path = ROOT_PATH
    main()