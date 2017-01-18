# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import time
import datetime
times= int(time.time())
dtime=datetime.datetime.now()
def addHTime():#当前时间戳增加1小时
    dtime=datetime.datetime.now()
    dtime2= dtime + datetime.timedelta(hours=1)
    timestamp=int(time.mktime(dtime2.timetuple()))
    return timestamp


def addTime():#当前时间戳增加15分钟
    dtime=datetime.datetime.now()
    dtime2= dtime + datetime.timedelta(hours=0.25)
    timestamp=int(time.mktime(dtime2.timetuple()))
    return timestamp



add_time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))# 获取当前时间。
promotionNames=str(add_time) + 'Test_AddPms'

Title=str(add_time)+'Test_AddPms'
dingjintuanTitle = str(add_time)+'Test_DJTuan'


#点评相关接口

#成功创建订单
data_OrderDPSuces={
         'uid':'43507844',
        'timestamp':times,
        'consignee':'么么22',
        'shop_id':'38021',
        'pay_expire':'7200',
        'mobile':'13728142737',
        'source':'wap',
        'shop_city':'289',
        'version':'2.0',
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'products':'[{"product_id":"10852",'
                   '"goods_id":"846",'
                   '"product_sn":"product2016101010852",'
                   '"goods_name":"扣点商品001（xsx勿动）",'
                   '"shop_price":"10.00",'
                   '"goods_thumb":"//cdn-dianping.mama.cn/upload/201610/20161010/b02077e9907e75c58d15b8c6245bb175.jpg",'
                   '"supplier_id":"121",'
                   '"without_return":"0",'
                   '"goods_number":"1",'
                   '"use_coupon":"3",'
                   '"end_return_time":"0",'
                   '"return_anytime":"1",'
                   '"goods_attr_id":"3030",'
                   '"goods_attr":"默认属性:均码"}]'
}


'''点评验卷接口'''
data_DPverif={
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'data':'{"supplierId":1,"couponIds":[2447]}'
}
'''获取用户订单列表-点评项目'''
data_UserOrderListDP={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'uid':'43507844',
     'order_cate_id':'[2001,2006]'
}
'''点评取消订单'''
cancelOrder_data={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'timestamp':times,
     'order_sn':'DP48414730126849',
     'uid':'43507844',

}
'''用户申请退款-点评项目'''
applyRefund_data={
    'timestamp':times,
    'uid':'43507844',
    'order_sn':'DP48414731026869',
    'suggest_reason':'122',
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',

}
'''订单详情-点评项目'''
OrderBySnDianping_data={
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',
    'order_sn':'DP48414731026869',
}





#旅游相关接口

'''test:获取用户所有的订单列表'''
test_UserOrderListTour={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'uid':'43507844',
        'page_num':'1',
        'page_size':'20',
        'status':'100',
        'order_cate_id':'[2001,2002,2003,2004]'
    }
'''test:根据订单分类获取分类订单总数'''
test_UserOrderNums={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'uid':43507844,
        'order_cate_id':'[2001,2002,2003,2004,2006]'
    }
'''旅游通过出行日期查询已支付的订单'''
test_OrderByGoTime={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'time':time,
     'go_time':'2016-10-26',
     'extra_fields':'["refund","delivery"]'

}
'''旅游根据订单编号获取订单信息'''
test_OrderBySnTour={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':time,
    'order_sn':'LY67414946235558'

}


#PMS相关接口

'''增加优惠劵 '''
test_Addpms={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{'
           '"promotionName":"' + str(promotionNames) + '",'
           '"sendNumLimit":2,'
           '"sendNum":0,"startDateLimit":2,'
           '"dateExpireNum":1,'
           '"getNumLimit":0,'
           '"adminId":1,"suppliersId":0,'
           '"promotionTitle":"' + str(Title) + '",'
           '"promotionDetail":"",'
           '"receiveLimit":1,'
           '"type":0,'
           '"rangeType":0,'
           '"chargePer":0.9,'
           '"supplierChargePer":0.1,'
           '"promotionRange":[],'
           '"supportMsGoods":1,'
           '"linkUrl":"",'
           '"selfType":"1",'
           '"supportDistributeGoods":1,'
           '"promotionType":1,'
           '"discountMoney":10,'
           '"useMinMoney":20,'
           '"goodsNumber":0'
           '}'

}
'''操作优惠活动（开启、关闭）接口 '''
test_Pmsoperate = {
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,

    'data':'{'
           '"promotionId": 454,'
           '"adminId": 1,'
           '"status": 2'
           ' }'
}



'''定金团4个时间处理机制：'''

'''1：定金支付时间直接使用当前时间戳'''
startAt=times

'''2.定金结束时间等于开始时间+15分钟'''
endAt=addTime()

'''3.尾款开始时间为定金结束时间+15分钟'''
fromAt=str(int(endAt)+600)

'''4.尾款结束时间为定金结束时间+15分钟'''
toAt=str(int(fromAt)+600)

'''新增定金团接口'''
CreateDepositMission_data={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
     'data':'{'
            '"photo":"images\/ms\/1484566379924518021.jpg",'
            '"goodsId":777,'
             '"title":"' + str(dingjintuanTitle) + '",'
             '"startAt":"'+ str(startAt) +'",'
             '"endAt":"'+ str(endAt) + '",'
             '"fromAt":"'+ str(fromAt) + '",'
             '"toAt":"'+ str(toAt) + '",'
             '"virtualHit":0,'
             '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0}'



}
'''修改定金团接口'''
updateDepositMission_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
    'data':'{'
        '"photo":"images\/ms\/1484566379924518021.jpg",'
        '"goodsId":777,"title":"2017-01-17 17:54:59Test_DJTuan",'
        '"startAt":1484646899,'
        '"endAt":1484647799,'
        '"fromAt":1484648399,'
        '"toAt":1484648999,'
        '"virtualHit":0,'
        '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0,"id":327}'
}
'''更新优惠劵状态'''
Pms_updateStatus={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionCode":"79241216","status":2,"orderId":"24594"}'


}

#order域

'''更新订单支付状态'''
data_updatePayStatus = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_sn':'DP08414562386338',
    'order_amount':'10',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}
'''创建订单'''
data_create = {
     'api_key':'b47d4503ce201db6df525911812dd089',
     'timestamp':times,
     'uid':'43507844',
     'consignee':'leo_peng',
     'mobile':13728142737,
     'products':'[{"product_id":10750 ,'
                '"goods_id":777,'
                '"goods_name":"test001",'
                '"shop_price":0.1,'
                '"goods_number":1,'
                '"supplier_id":128,'
                '"goods_own_type":1,'
                '"delivery_method":1'
                '}]'
}
'''通过商品id获取订单列表'''
data_OrderByProductId={
    'api_key':'d81b8598bc36a686cc8cbbd26599bd92',
    'uid':'43507844',
    'product_id':'10750',
    'goods_id':'777',
}
'''获取用户商品下单商品数量'''
UserLimitedSpecialOrderNum_data={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'timestamp':times,
     'uid':'43507844',
     'promotion_id':'158',
     'goods_id':'714',
     'order_cate':'1101'

}
'''旅游创建订单'''
createOrderTour_data={
    "uid": "43507844",
    "consignee": "刘德华",
    "postscript": "",
    "source_type": "1",
    "version": "2.0",
    "passenger": "[{\"contact_type\":2,\"email\":\"\",\"identit_card\":\"\",\"passenger_name\":\"刘德华\",\"passenger_type\":1,\"phone\":\"13728142737\"}]",
    "timestamp": times,
    "track_param": "{}",
    "source": "pc",
    "products": "[{\"base_day\":1,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"主套餐1 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1798,\"item_name\":\"主套餐1\",\"item_num\":1,\"item_timestamp\":1484553897,\"item_type\":1,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131608,\"product_sn\":\"tour_131608\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":10.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1},{\"base_day\":0,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"N选1 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1799,\"item_name\":\"N选1\",\"item_num\":1,\"item_timestamp\":1484553924,\"item_type\":1,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131624,\"product_sn\":\"tour_131624\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":1.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1},{\"base_day\":0,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"包含 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1800,\"item_name\":\"包含\",\"item_num\":1,\"item_timestamp\":1484553929,\"item_type\":0,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131628,\"product_sn\":\"tour_131628\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":0.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1}]",
    "sms_param": "{\"delivery\":{\"1251\":{\"enabled\":0,\"supplier_phone\":\"111111\",\"destination\":\"深圳市南山区深南大道华侨城欢乐谷\"}}}",
    "mobile": "13728142737",
    "api_key": "9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o",

}


#www域接口

'''获取秒杀订单实际秒杀购买数'''
PromotionNums_data={
      'api_key':'b47d4503ce201db6df525911812dd089',
      'timestamp':times,
      'data':'{"promotion_type":2,"promotion_id":62}'
}
'''更新订单客服留言接口'''
updateRemindMsg_data={
      'api_key':'b47d4503ce201db6df525911812dd089',
      'timestamp':times,
      'order_sn':'XS48414708726629 ',
      'msg_ids':'[1,2,3]'
}
'''获取订单客服留言'''
RemindMsg_data={
     'api_key':'b47d4503ce201db6df525911812dd089',
     'timestamp':times,
     'order_sn':'XS48414708726629'

}
'''对接要出发回调设置外部订单号'''
OutOrderSn_data={
    'api_key': '9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    't':times,
    'out_order_sn':'1382089191274',
    'order_sn':'LY48414722526789'


}

'''接收open域回推要出发订单信息'''
receiveOrderReturn_data={
    'order_sn':'LY48414722526789',
    't':'1484722585',
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'type':'0',
    'status':'1'
}
'''根据订单号获取订单列表'''
ChildOrderTour_data={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'order_sn':'LY48414726526809 '
}
'''获取用户购买的商品数量'''
OrderGoodsNumTour_data={
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',
    'timestamp':times,
    'goods_id':743,
    'uid':43507844,
    'passenger':'[{"phone":"13728142737","type":1}]'

}
'''不输入消费券直接发货'''
shipWithoutCoupon_data={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'data':'{"supplierId":110,"orderId":24610}'


}
'''查询发货单列表'''
query_data={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':times,
    'supplierId':'13'

}
CouponCode_data={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':times,


}
















































'''小树熊下单'''
data_createOrderXsx1 ={
    "_url": "/Order/createOrderXsx",
    "order_info": "{"
                  "order:{serial_no:14841953352617914717,"
                         "user_id:1160,"
                         "uid:43507844,"
                         "source:wap,"
                         "referer:windows|wap|192.168.14.61,"
                         "source_type:1,"
                        "pid:c73400f06fe6f3c9796003c08a0f5a6d,"
                        "trade_pwd:\"\","
                        "surplus:40.00},"
                  "address:{address_id:1724,"
                            "\"customs_id\":\"3474\","
                            "\"address_type\":\"0\","
                            "\"consignee\":\"\\u674e\\u56db\","
                            "\"mobile\":\"13728142737\","
                            "\"province\":\"1\","
                            "\"city\":\"37\","
                            "\"district\":\"0\","
                            "\"country\":\"0\","
                            "\"address\":\"\\u81ea\\u8d2d\\u8fd4\\u73b0\","
                            "\"is_default\":\"0\"},"
              "\"customs\":{\"is_customs\":\"2\",\"customs_info\":{\"card_id\":\"440921199201184218\",\"customs_id\":\"3474\"},"
              "\"customs_pic\":{\"id\":\"3474\",\"identit_card\":\"440921199201184218\",\"img_front_original\":\"identit_card\\/original_10dba1499d2e72e1c5e0c7345dcb7e3f.jpg\",\"img_front_max\":\"identit_card\\/max_1bdaf04b61d9cdc5ecd4deb1ba1e28ac.jpg\",\"img_front_thumb\":\"identit_card\\/thumb_abf6163039e3f3b035546f81c565f0fb.jpg\",\"img_back_original\":\"identit_card\\/original_945a264a54944207f124ee62a20fbaf2.jpg\",\"img_back_max\":\"identit_card\\/max_0ef88ad15a28f791e632c04925258a9d.jpg\",\"img_back_thumb\":\"identit_card\\/thumb_7cd66cb9b1033ba540ef72c3d72fc6b7.jpg\"}}}",
"goods_list": "{\"10750\":{\"goods_id\":\"777\",\"product_id\":\"10750\",\"product_sn\":\"cp0000001234\",\"goods_name\":\"\\u3010\\u666e\\u3011\\u63a5\\u53e3\\u6d4b\\u8bd5\\u5546\\u54c1_\\u52ff\\u52a8\\u52ff\\u6539\",\"goods_sn\":\"XSX000777\",\"goods_own_type\":\"1\",\"shop_price\":40,\"market_price\":\"52.00\",\"is_on_sale\":\"1\",\"is_delete\":\"0\",\"is_customs\":\"2\",\"product_number\":\"129\",\"ext_price\":\"0.00\",\"delivery_method\":\"19\",\"goods_weight\":\"1.000\",\"cdn_status\":\"1\",\"goods_thumb\":\"https:\\/\\/cdn.xiaoshuxiong.com\\/images\\/201604\\/thumb_img\\/777_thumb_P_1461658613884.jpg\",\"order_quota\":\"100\",\"is_real\":\"1\",\"supplier_id\":\"128\",\"without_return\":\"0\",\"erp_goods_id\":\"0\",\"app_id\":\"0\",\"cat_id\":\"25\",\"shelf_life\":\"0\",\"shelf_life_start\":\"0\",\"sms_delivery\":\"0\",\"coupons\":\"0\",\"coupons_verificat\":\"0\",\"return_anytime\":\"0\",\"brand_id\":\"3\",\"goods_attr\":[\"\\u9ed8\\u8ba4\\u5c5e\\u6027\\uff1a\\u5747\\u7801\",\" \\n\"],\"goods_attr_id\":\"2777\",\"isDistribution\":0,\"order_type\":2,\"goods_number\":1,\"is_gift\":0,\"gift_code\":\"\",\"code\":\"\",\"code_id\":0,\"code_name\":\"\",\"reduce_price\":0,\"is_seckill\":0,\"is_pinhuo\":0,\"is_zhuanxiang\":0,\"promotion_dimension_id\":0,\"pinhuo_code\":\"\",\"is_groupon\":0,\"promotion_id\":null}}",
"shipping_rules": "{\"shipFeeList\":[{\"id\":105,\"gapToFree\":0,\"amountToFree\":0,\"shipFee\":0,\"products\":[{\"isGift\":0,\"cartId\":0,\"productId\":10750}],\"isFree\":1,\"ruleName\":\"\\u6ee188\\u5305\\u90ae\"}],\"totalFee\":0}",
"tracking_data": "{\"26\":\"c73400f06fe6f3c9796003c08a0f5a6d\"}",
"timestamp": "1484195335",
"api_key": "xsx",
"api_sign": "27DBBE360E67E638B6836B7FFBCBE061"
}




data_createOrderXsx ={
    "_url": "/Order/createOrderXsx",
    "order_info": "{\"order\":"
                  "{\"serial_no\":\"14841953352617914717\","
                  "\"user_id\":1160,\"uid\":43507844,"
                  "\"source\":\"wap\","
                  "\"referer\":\"windows|wap|192.168.14.61\","
                  "\"source_type\":1,"
                  "\"pid\":\"c73400f06fe6f3c9796003c08a0f5a6d\","
                  "\"trade_pwd\":\"\","
                  "\"surplus\":\"40.00\"},"
                  "\"address\":{\"address_id\":\"1724\","
                  "\"customs_id\":\"3474\","
                  "\"address_type\":\"0\","
                  "\"consignee\":\"\\u674e\\u56db\","
                  "\"mobile\":\"13728142737\","
                  "\"province\":\"1\",\"city\":\"37\",\"district\":\"0\",\"country\":\"0\","
                  "\"address\":\"\\u81ea\\u8d2d\\u8fd4\\u73b0\",\"is_default\":\"0\"},"
                  "\"customs\":{\"is_customs\":\"2\","
                  "\"customs_info\":{\"card_id\":\"440921199201184218\",\"customs_id\":\"3474\"},"
                  "\"customs_pic\":{\"id\":\"3474\",\"identit_card\":\"440921199201184218\","
                  "\"img_front_original\":\"identit_card\\/original_10dba1499d2e72e1c5e0c7345dcb7e3f.jpg\","
                  "\"img_front_max\":\"identit_card\\/max_1bdaf04b61d9cdc5ecd4deb1ba1e28ac.jpg\","
                  "\"img_front_thumb\":\"identit_card\\/thumb_abf6163039e3f3b035546f81c565f0fb.jpg\","
                  "\"img_back_original\":\"identit_card\\/original_945a264a54944207f124ee62a20fbaf2.jpg\","
                  "\"img_back_max\":\"identit_card\\/max_0ef88ad15a28f791e632c04925258a9d.jpg\","
                  "\"img_back_thumb\":\"identit_card\\/thumb_7cd66cb9b1033ba540ef72c3d72fc6b7.jpg\"}}}",
    "goods_list": "{\"10750\":{\"goods_id\":\"777\","
                  "\"product_id\":\"10750\",\"product_sn\":\"cp0000001234\","
                  "\"goods_name\":\"\\u3010\\u666e\\u3011\\u63a5\\u53e3\\u6d4b\\u8bd5\\u5546\\u54c1_\\u52ff\\u52a8\\u52ff\\u6539\","
                  "\"goods_sn\":\"XSX000777\",\"goods_own_type\":\"1\",\"shop_price\":40,\"market_price\":\"52.00\","
                  "\"is_on_sale\":\"1\",\"is_delete\":\"0\",\"is_customs\":\"2\",\"product_number\":\"129\","
                  "\"ext_price\":\"0.00\",\"delivery_method\":\"19\",\"goods_weight\":\"1.000\","
                  "\"cdn_status\":\"1\","
                  "\"goods_thumb\":\"https:\\/\\/cdn.xiaoshuxiong.com\\/images\\/201604\\/thumb_img\\/777_thumb_P_1461658613884.jpg\",\"order_quota\":\"100\",\"is_real\":\"1\","
                  "\"supplier_id\":\"128\",\"without_return\":\"0\",\"erp_goods_id\":\"0\",\"app_id\":\"0\","
                  "\"cat_id\":\"25\",\"shelf_life\":\"0\",\"shelf_life_start\":\"0\",\"sms_delivery\":\"0\","
                  "\"coupons\":\"0\",\"coupons_verificat\":\"0\",\"return_anytime\":\"0\",\"brand_id\":\"3\","
                  "\"goods_attr\":[\"\\u9ed8\\u8ba4\\u5c5e\\u6027\\uff1a\\u5747\\u7801\",\" \\n\"],"
                  "\"goods_attr_id\":\"2777\",\"isDistribution\":0,\"order_type\":2,\"goods_number\":1,\"is_gift\":0,\"gift_code\":\"\",\"code\":\"\","
                  "\"code_id\":0,\"code_name\":\"\",\"reduce_price\":0,\"is_seckill\":0,\"is_pinhuo\":0,\"is_zhuanxiang\":0,"
                  "\"promotion_dimension_id\":0,\"pinhuo_code\":\"\",\"is_groupon\":0,\"promotion_id\":null}}",
    "shipping_rules": "{\"shipFeeList\":[{\"id\":105,\"gapToFree\":0,\"amountToFree\":0,\"shipFee\":0,"
                      "\"products\":[{\"isGift\":0,\"cartId\":0,\"productId\":10750}],"
                      "\"isFree\":1,\"ruleName\":\"\\u6ee188\\u5305\\u90ae\"}],\"totalFee\":0}",
    "tracking_data": "{\"26\":\"c73400f06fe6f3c9796003c08a0f5a6d\"}",
    "timestamp": times,
    "api_key": "xsx",
    "api_sign": "27DBBE360E67E638B6836B7FFBCBE061"
}






















































































