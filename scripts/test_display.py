import os, sys
sys.path.append(os.getcwd())
#from base.base_driver import init_driver
from appium import webdriver
#from pages.page_display import PageDisplay #导入页面类
import time
import pytest
from base.base_yaml import yaml_data_with_file

#数据再处理的辅助函数
def data_with_key(key):
    return yaml_data_with_file("data_display", key)

class TestDisplay:
    # def setup(self):
    #     self.driver = init_driver();
    #     self.page_display=PageDisplay(self.driver);
    #
    # def teardown(self):
    #     time.sleep(5);
    #     self.driver.quit()

    @pytest.mark.parametrize("dict", data_with_key("test_key1"))
    def test_key1(self,dict):
        name=dict["name"];
        pwd=dict["pwd"];
        print(name,pwd)


