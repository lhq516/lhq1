import requests

import app,logging


class HomeApi:
    """首页API接口方法"""

    def __init__(self):
        # 轮播图
        self.banner_url = app.base_url + "/banner/{}"
        # 专题栏
        self.theme_url = app.base_url + "/theme"
        # 最近新品
        self.recent_product_url = app.base_url + "/product/recent"

    def banner_api(self, num=1):
        """
        请求轮播图
        :param num: 轮播图页面数
        :return: 响应对象
        """
        logging.info("首页-轮播图")
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids="1,2,3"):
        """
        请求专题栏
        :param ids: 专题栏数据
        :return:
        """
        logging.info("首页-专题栏")
        # 查询数据字典
        data={"ids":ids}
        # 请求参数打印
        logging.info("请求参数：{}".format(data))
        return requests.get(self.theme_url, params=data)

    def recent_product_api(self):
        """请求最近新品"""
        logging.info("首页-最近新品")
        return requests.get(self.recent_product_url)
