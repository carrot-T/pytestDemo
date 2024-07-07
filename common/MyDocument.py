'''
1、csv文件读取，返回列表
2、json文件读取，返回字典

'''
import csv
import json


class Document:
    def __init__(self, filepath):
        self.path = filepath

    def make_csv(self):
        try:
            with open(self.path, 'w', encoding='utf8') as file:
                file.write('英语姓名,汉字姓名,生年月日,身高\n'
                           'Tom,汤姆,1994/2/1,180\n'
                           'Jack,杰克,1995/3/15,170\n'
                           'Kai,凯莉,1996/03/09,168\n')
        except FileNotFoundError:
            print('无此文件!!')
        else:
            print('创建成功。。')

    def make_json(self):
        try:
            with open(self.path, 'w', encoding='utf8') as file:
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

    def csv_reader(self):
        try:
            with open(self.path, 'r', encoding='utf8') as f:
                content = csv.reader(f)
                header_row = next(content)
                li_content = []
                for row in content:
                    row_content = dict(zip(header_row, row))
                    li_content.append(row_content)

                print(li_content)
                return li_content
        except FileNotFoundError:
            print('无此文件!!')

    def json_reader(self):
        try:
            with open(self.path, 'r', encoding='utf8') as file:
                con = json.load(file)
                print(con)
                return con
        except FileNotFoundError:
            print('无此文件!!')


if __name__ == '__main__':
    filepath = 'D:/PycharmProjects/document/test.txt'
    doc = Document(filepath)
    doc.make_csv()
    cs = doc.csv_reader()
    # doc.make_json()
    # js = doc.json_reader()
    # print(js['drivers'][0]['birthday'])
