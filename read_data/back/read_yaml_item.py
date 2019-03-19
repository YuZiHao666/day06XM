import os
import yaml


class ReadYaml:
    def __init__(self, filename):
        self.filepath = os.getcwd()+os.sep+"data"+os.sep+filename

    # 以下方法为pytest运行时使用
    def read_yaml(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return yaml.load(f)

    # 以下方法为右键调试使用
    def read_yaml_dug(self):
        with open("../data/data_login.yaml", "r", encoding="utf-8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    datas = ReadYaml("data_login.yaml").read_yaml_dug()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"), data.get("pwd")))
    print(arrs)