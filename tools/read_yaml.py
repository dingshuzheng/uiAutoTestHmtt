import os
import yaml
from config import BASE_PATH



# 定义函数
def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表
    arr = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8") as f:
        # 便利 调用yaml.safe.load(f).values()方法
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))  # 列表嵌套元组
    # 返回结果
    return arr

if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))