import time
# 导入selenium包
from selenium import webdriver
# 打开指定浏览器
browser = webdriver.Chrome()
# 指定加载页面
browser.get("http://www.csdn.net/")
# 设置五秒后执行下一步
time.sleep(5)
# 关闭浏览器
browser.quit()