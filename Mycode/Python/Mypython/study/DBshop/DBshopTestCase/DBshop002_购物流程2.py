'''
编写时间：2022-08-06
编写人：xuguo

1.在首页搜索"小米",点击搜索按钮
2.选择小米mix3,加入到购物车,点击购物车按钮
3.点击"去结算"按钮
4.默认地址已经别选择,点击下一步按钮
5.支付方式选择"余额支付",点击确认订单
6.点击马上支付，支付成功。
7.登录后台管理系统,地址是"http://localhost/dbshop/admin",
8.点击商品管理订单管理，找到刚才前台提交的订单，点击“编辑查看”。
9.点击发货操作按钮，编辑快递单号“1000000000” 发货说明“保证正品”，点击“点击发货”按钮。
10.点击完成订单按钮,操作说明填写"已签收",点击完成订单按钮
11.进入前台我的订单—已发货，点击“确认收货”按钮，完成订单。
'''
from DBshop.public.tools import *
from DBshop.public.business import *
from DBshop.public.action import *
from DBshop.public.testData import *
import time

# 打开网页
dr = openWeb(url)
# 登录
DBdenglu(dr,'cyy')
# 首页搜索小米，并添加至购物车
search(dr,'小米')
# 查看购物车
dr.find_element_by_xpath('//a[contains(.,"购物车")]').click()
time.sleep(2)
dr.refresh()
# 去结算
dr.find_element_by_link_text('去结算').click()

# 下一步
dr.find_element_by_xpath('//input[@value="下一步"]').click()
# 选择‘余额支付’
dr.find_element_by_xpath('//input[@value="yezf"]').click()
# 点击‘确认订单’
dr.find_element_by_xpath('//input[@value="确认订单"]').click()
# 提取订单号
orderID=dr.find_element_by_xpath('(//font)[2]').text
# 点击‘马上去支付’
dr.find_element_by_xpath('//input[@value="马上去支付"]').click()

# 打开后台网页
dr.get(urlhou)
# 登录后台
DBhouLogin(dr)
# 点击‘销售管理’下的‘订单管理’
DBshopEnterMenu2(dr,'销售管理','订单管理')
# 在搜索框输入订单号
dr.find_element_by_xpath('//input[@name="order_sn"]').send_keys(orderID)
# 点击‘搜索’
dr.find_element_by_xpath('//button').click()
time.sleep(3)
# 点击‘编辑查看’
dr.find_element_by_link_text('编辑查看').click()

# 点击‘发货操作’
dr.find_element_by_link_text('发货操作').click()
# 输入快递单号"1000000000"
dr.find_element_by_id('express_number').send_keys('1000000000')
# 输入操作说明"保证正品"
dr.find_element_by_xpath('//textarea').send_keys('保证正品')
# 点击‘点击发货’
dr.find_element_by_xpath('//button').click()
# 点击‘完成订单’
dr.find_element_by_link_text('完成订单').click()
# 操作说明填写"已签收"
dr.find_element_by_xpath('//textarea').send_keys('已签收')
# 点击‘订单完成’
dr.find_element_by_xpath('//button').click()

# 打开前台网页
dr.get(url)
# 点击‘我的订单’
dr.find_element_by_link_text('我的订单').click()
# 点击‘交易完成’
dr.find_element_by_partial_link_text('交易完成').click()
# 在搜索框输入订单号
dr.find_element_by_xpath('//input[@type="text" and @name="search_order_sn"]').send_keys(orderID)
dr.find_element_by_xpath('//button[text()="搜索"]').click()

# 判断订单是否存在
try:
    dr.find_element_by_link_text(orderID).is_displayed()
    writeLog('购物流程2 测试通过')
except:
    writeLog('购物流程2 测试未通过')
    getPhoto(dr)

#点击‘确认收货’
# dr.find_element_by_xpath('//button[text()="确认收货"]').click()

dr.quit()



