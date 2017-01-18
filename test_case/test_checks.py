# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,json,time
from test_data.check_data import check_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
from Interface.check import interface_check
times= int(time.time())

class Test(interface_check.MyTest):

    '''点评接口'''
    def test_post_orderDP_sucess(self):
        '''创建点评订单接口检查'''
        api_key=setting.DBConns.Api_secret(**check_data.data_OrderDPSuces)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.data_OrderDPSuces
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.orderDP_url, params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_UserOrderListDP_sucess(self):
        '''获取用户订单列表-点评项目'''
        api_key=setting.DBConns.Api_secret(**check_data.data_UserOrderListDP)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.data_UserOrderListDP
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderListDP_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_cancelOrder_sucess(self):
        '''取消订单-点评'''
        api_key=setting.DBConns.Api_secret(**check_data.cancelOrder_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.cancelOrder_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.cancelOrder_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_applyRefund_sucess(self):#现在还调不通
        '''取用户申请退款-点评项目'''
        api_key=setting.DBConns.Api_secret(**check_data.applyRefund_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.applyRefund_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.applyRefund_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_OrderBySnDianping_sucess(self):#现在还调不通
        '''取用订单详情-点评项目'''
        api_key=setting.DBConns.Api_secret(**check_data.OrderBySnDianping_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.OrderBySnDianping_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderBySnDianping_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    '''旅游接口'''
    def test_OrderBySnTour_sucess(self):
        '''旅游获取用户所有的订单列表接口检查'''
        api_key=setting.DBConns.Api_secret(**check_data.test_OrderBySnTour)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.test_OrderBySnTour
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderBySnTour_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_OrderByGoTime_sucess(self):
        '''旅游通过出行日期查询已支付的订单接口检查'''
        api_key=setting.DBConns.Api_secret(**check_data.test_OrderByGoTime)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.test_OrderByGoTime
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderByGoTime_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_UserOrderListTour_success(self):
        '''旅游获取用户所有的订单列表接口检查'''
        api_key=setting.DBConns.Api_secret(**check_data.test_UserOrderListTour)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.test_UserOrderListTour
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderListTour_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)

                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'

            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_UserOrderNums_sucess(self):
        '''旅游根据订单分类获取分类订单总数接口检查'''
        api_key=setting.DBConns.Api_secret(**check_data.test_UserOrderNums)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.test_UserOrderNums
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderNums_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    '''www接口'''
    def test_PromotionNums_sucess(self):
        '''获取秒杀订单实际秒杀购买数'''
        api_key=setting.DBConns.Api_secret(**check_data.PromotionNums_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.PromotionNums_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PromotionNums_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_updateRemindMsg_sucess(self):
        '''更新订单客服留言接口'''
        api_key=setting.DBConns.Api_secret(**check_data.updateRemindMsg_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.updateRemindMsg_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.updateRemindMsg_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_UserLimitedSpecialOrderNum_sucess(self):
        '''获取用户商品下单商品数量'''
        api_key=setting.DBConns.Api_secret(**check_data.UserLimitedSpecialOrderNum_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.UserLimitedSpecialOrderNum_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserLimitedSpecialOrderNum_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_RemindMsg_sucess(self):
        '''获取订单客服留言接口'''
        api_key=setting.DBConns.Api_secret(**check_data.RemindMsg_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.RemindMsg_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.RemindMsg_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_createOrderTour_sucess(self):
        '''旅游创建订单'''
        api_key=setting.DBConns.Api_secret(**check_data.createOrderTour_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.createOrderTour_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.createOrderTour_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_OutOrderSn_sucess(self):
        '''对接要出发回调设置外部订单号'''
        api_key=setting.DBConns.Api_secret(**check_data.OutOrderSn_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.OutOrderSn_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OutOrderSn_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_ChildOrderTour_sucess(self):
        '''根据订单号获取订单列表'''
        api_key=setting.DBConns.Api_secret(**check_data.ChildOrderTour_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.ChildOrderTour_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.ChildOrderTour_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_OrderGoodsNumTour_sucess(self):
        '''获取用户购买的商品数量'''
        api_key=setting.DBConns.Api_secret(**check_data.OrderGoodsNumTour_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.OrderGoodsNumTour_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderGoodsNumTour_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")




    def test_query_sucess(self):
        '''获取用户购买的商品数量'''
        api_key=setting.DBConns.Api_secret(**check_data.query_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.query_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.query_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_CouponCode_sucess(self):
        '''获取用户购买的商品数量'''
        api_key=setting.DBConns.Api_secret(**check_data.CouponCode_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.CouponCode_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.ByCouponCode_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_receiveOrderReturn_sucess(self):#现在这个没有调通
        '''接收open域回推要出发订单信息'''
        api_key=setting.DBConns.Api_secret(**check_data.receiveOrderReturn_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.receiveOrderReturn_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.receiveOrderReturn_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    '''PMS接口'''
    def test_Pmsadd_sucess(self):
        '''Pms添加优惠劵'''
        api_key=setting.DBConns.Api_secret(**check_data.test_Addpms)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.test_Addpms
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PMSadd_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_Pmsoperate_sucess(self):
        '''Pms操作优惠活动（开启、关闭）接口'''
        api_key=setting.DBConns.Api_secret(**check_data.test_Pmsoperate)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.test_Pmsoperate
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PMSoperate_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_createDepositMission_sucess(self):
        '''添加定金团活动'''
        api_key=setting.DBConns.Api_secret(**check_data.CreateDepositMission_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload=check_data.CreateDepositMission_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.CreateDepositMission_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")



    def test_updateDepositMission_sucess(self):
        '''修改定金团活动'''
        api_key=setting.DBConns.Api_secret(**check_data.updateDepositMission_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload=check_data.updateDepositMission_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.updateDepositMission_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_Pmsupdate_sucess(self):
        '''修改优惠劵状态'''
        api_key=setting.DBConns.Api_secret(**check_data.Pms_updateStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload=check_data.Pms_updateStatus
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PmsUpdatestatus_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    '''订单接口'''
    def test_updatePayStatus_sucess(self):
        '''更新订单支付状态'''
        api_key=setting.DBConns.Api_secret(**check_data.data_updatePayStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.data_updatePayStatus
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.updatePayStatus_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_OrderByProductId_sucess(self):
        '''通过商品id获取订单列表'''
        api_key=setting.DBConns.Api_secret(**check_data.data_OrderByProductId)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.data_OrderByProductId
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderByProductId_url, params=payload)
                print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_hipWithoutCoupon_sucess(self):
        '''不输入消费券直接发货'''
        api_key=setting.DBConns.Api_secret(**check_data.shipWithoutCoupon_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=check_data.shipWithoutCoupon_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.shipWithoutCoupon_url, params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_createOrderXsx_sucess(self):
        '''小树熊下单接口'''
        payload=check_data.data_createOrderXsx
        r=requests.post(self.createOrderXsx_url,params=payload)
        #print payload
        self.code=r.status_code
        self.result=r.text
        js=setting.result_jsons.result_json(self.result)
        if js.has_key('msg')==True:
            self.msgs=js.get('msg')
            self.assertEquals(self.code,200)
            self.assertEqual(self.msgs, 'SUCCESS')
        else:
            print 'NO msg'




if __name__=='__main__':
    unittest.main()



