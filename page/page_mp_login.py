from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()
class PageMpLogin(WebBase):  # 继承base
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类输入方法
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 调用父类中点击方法
        self.base_click(page.mp_login_btn)

    # 获取昵称封装  ->测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法  ->发布文章依赖使用
    def page_mp_login(self, username="13812345678", code="246810"):
        """提示：调用相同页面操作步骤，跨页面操作暂不考虑"""
        log.info("正在调用自媒体业务方法，用户名：{} 密码：{}".format(username, code))
        self.page_input_username(username)
        self.page_input_code(code)
        sleep(1)
        self.page_click_login_btn()

