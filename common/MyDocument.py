import csv
import json
import os
import yaml

from configparser import ConfigParser
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义数据文件路径
DOC_PATH = os.path.join(BASE_PATH, "data")
if not os.path.exists(DOC_PATH):
    os.mkdir(DOC_PATH)


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class Document:
    """json、yaml、csv、ini等文件读写操作"""

    def __init__(self):
        pass

    @staticmethod
    def make_csv(file_path):
        try:
            with open(file_path, 'w', encoding='utf8') as file:
                file.write('英语姓名,汉字姓名,生年月日,身高\n'
                           'Tom,汤姆,1994/2/1,180\n'
                           'Jack,杰克,1995/3/15,170\n'
                           'Kai,凯莉,1996/03/09,168\n')
        except FileNotFoundError:
            print('无此文件!!')
        else:
            print('创建成功。。')

    @staticmethod
    def make_json(file_path):
        try:
            with open(file_path, 'w', encoding='utf8') as file:
                file.write(
                    '{"affinityOrganization":"test","drivers":[{"age":30,"birthday":"1990-01-01","gender":"MALE",'
                    '"idNumber":"S59379985I","idType":"OTHER","maritalStatus":"UNMARRIED","name":"Peppa HXFEP",'
                    '"occupation":"G001"}],"effectiveDate":"2021-10-21 00:00:00","excess":"100","plan":"PC_RDC",'
                    '"policyHolder":{"birthday":"1990-01-01","countryCode":"+65","email":"dongyan.HXFEP@zatech.com",'
                    '"gender":"FMAIL","idNumber":"S59379985I","idType":"OTHER","mobileNo":"13102522381","name":"Peppa '
                    'HXFEP","nationality":"SINGAPORE"}}')
        except FileNotFoundError:
            print('无此文件!!')
        else:
            print('创建成功。。')

    @staticmethod
    def load_yaml(file_path):
        try:
            logger.info("加载 {} 文件......".format(file_path))
            with open(file_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
            logger.info("读到数据 ==>>  {} ".format(data))
            return data
        except FileNotFoundError:
            print('无此文件!!')

    @staticmethod
    def load_json(file_path):
        """读取json文件"""
        try:
            logger.info("加载 {} 文件......".format(file_path))
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)
            logger.info("读到数据 ==>>  {} ".format(data))
            return data
        except FileNotFoundError:
            print('无此文件!!')

    @staticmethod
    def load_ini(file_path):
        """读取ini文件"""
        try:
            logger.info("加载 {} 文件......".format(file_path))
            config = MyConfigParser()
            config.read(file_path, encoding="UTF-8")
            data = dict(config._sections)
            # print("读到数据 ==>>  {} ".format(data))
            return data
        except FileNotFoundError:
            print('无此文件!!')

    @staticmethod
    def load_csv(file_path):
        """读取csv文件，返回字典"""
        try:
            logger.info("加载 {} 文件......".format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                content = csv.reader(f)
                header_row = next(content)
                li_content = []
                for row in content:
                    row_content = dict(zip(header_row, row))
                    li_content.append(row_content)
                logger.info("读到数据 ==>>  {} ".format(li_content))
                return li_content
        except FileNotFoundError:
            print('无此文件!!')


if __name__ == '__main__':
    filepath = os.path.join(DOC_PATH, "demo.csv")
    doc = Document()
    doc.make_csv(filepath)
    cs = doc.load_csv(filepath)
    # doc.make_json()
    # js = doc.json_reader()
    # print(js['drivers'][0]['birthday'])
