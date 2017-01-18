# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):

        #点评相关接口
        self.orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
        self.DPverify ='http://www.xiaoshuxiong.com/api/ocoupon/verify'#点评验卷接口
        self.UserOrderListDP_url='http://www.xiaoshuxiong.com/api/order/getUserOrderListDianping' #获取用户订单列表-点评项目
        self.cancelOrder_url='http://www.xiaoshuxiong.com/api/order/cancelOrder'
        self.applyRefund_url='http://order.api.xiaoshuxiong.com/order/applyRefund'
        self.OrderBySnDianping_url='http://www.xiaoshuxiong.com/api/order/getOrderBySnDianping'


        #旅游相关接口
        self.OrderBySnTour_url ="http://www.xiaoshuxiong.com/api/order/getOrderBySnTour"
        self.OrderByGoTime_url='http://www.xiaoshuxiong.com/api/order/getOrderByGoTime'
        self.UserOrderListTour_url='http://www.xiaoshuxiong.com/api/order/getUserOrderListTour'
        self.UserOrderNums_url='http://www.xiaoshuxiong.com/api/order/getUserOrderNums'

        #pms接口
        self.PMSadd_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/add'
        self.PMSoperate_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/operate'
        self.CreateDepositMission_url ='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/createDepositMission'
        self.updateDepositMission_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/updateDepositMission'
        self.PmsUpdatestatus_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/updateStatus'

        #order接口
        self.create_url='http://order.api.xiaoshuxiong.com/order/create'
        self.createOrderXsx_url='http://order.api.xiaoshuxiong.com/Order/createOrderXsx '
        self.UserLimitedSpecialOrderNum_url='http://order.api.xiaoshuxiong.com/order/getUserLimitedSpecialOrderNum'
        self.receiveOrderReturn_url='http://order.api.xiaoshuxiong.com/order/receiveOrderReturn'
        self.OrderGoodsNumTour_url='http://order.api.xiaoshuxiong.com/order/getOrderGoodsNumTour'

        #www域接口
        self.PromotionNums_url='http://www.xiaoshuxiong.com/api/order/getPromotionNums'
        self.updateRemindMsg_url='http://www.xiaoshuxiong.com/api/order/updateRemindMsg'
        self.OrderByProductId_url='http://www.xiaoshuxiong.com/api/order/getOrderByProductId'
        self.updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
        self.RemindMsg_url='http://www.xiaoshuxiong.com/api/order/getRemindMsg'
        self.createOrderTour_url='http://www.xiaoshuxiong.com/api/order/createOrderTour'
        self.OutOrderSn_url='http://www.xiaoshuxiong.com/api/order/setOutOrderSn'
        self.ChildOrderTour_url='http://www.xiaoshuxiong.com/api/order/getChildOrderTour'
        self.shipWithoutCoupon_url='http://www.xiaoshuxiong.com/api/ocoupon/shipWithoutCoupon'










    def tearDown(self):
       # pass

        print(self.code,self.msgs)
