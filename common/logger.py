import logging
import os
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:

    def __init__(self):
        # 设置日志路径
        self.log_file_path = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        # 创建日志对象
        self.logger = logging.getLogger("log")
        # 设置全局的日志级别
        self.logger.setLevel(logging.DEBUG)
        # 定义日志格式
        self.formater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        # 创建文件日志的控制器
        self.filelogger = logging.FileHandler(self.log_file_path, mode='a', encoding="UTF-8")
        # 设置文件日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 设置文件日志格式
        self.filelogger.setFormatter(self.formater)

        # 创建控制台日志的控制器
        self.console = logging.StreamHandler()
        # 设置控制台日志的级别
        self.console.setLevel(logging.DEBUG)
        # 设置控制台日志的格式
        self.console.setFormatter(self.formater)

        # 控制器加入日志对象
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")
