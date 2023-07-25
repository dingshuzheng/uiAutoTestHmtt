# 根据用例执行业务步骤进行分析页面公共方法进行抽取
import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver: {}".format(driver))
        """解决driver问题"""
        self.driver = driver

    # 查找方法封装  #元素的8种定位/元素三种等待方法/ctrl+p提示
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc:格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认30s
        :param poll: 查找元素频率 默认0.5
        :return:
        """
        log.info("正在查找元素: {}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入方法封装
    def base_input(self, loc, value):
        """
        :param loc: 元素定位信息
        :param value: 要输入的值
        """
        # 1.获取元素
        el = self.base_find(loc)
        # 2.清空操作
        log.info("正在对：{}元素执行清空操作！".format(loc))
        el.clear()
        # 3.输入操作
        log.info("正在对：{}元素执行输入: {} 操作!".format(loc, value))
        el.send_keys(value)

    # 点击方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        log.info("正在对：{}元素执行点击操作！".format(loc))
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回元素文本值
        """
        log.info("正在对：{}元素获取文本操作！, 获取文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error("断言出错,正在执行截图操作!")
        # 1.调用截图方法
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错,正在将错误图片写入allure报告!")
        # 2. 调用图片写入报告方法
        self.__base_write_img()

    # 将图片写入报告方法(私有)
    def __base_write_img(self):
        # 1.获取图片文件流
        with open("./image/err,png", "rb") as f:
            allure.attach("错误原因: ", f.read(), allure.attach.type.PNG)
