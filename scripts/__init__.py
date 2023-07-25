"""放在这个__init__.py中后，执行scripts下的所有.py文件时都会加载下面这段代码"""
import sys
import os
sys.path.append(os.getcwd())   # 用于使用pytest.ini文件运行