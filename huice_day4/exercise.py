# -*-coding:utf-8-*-

import json,urllib2

class Restaurant(object):
    restaurant_name='haogaoxing'
    cuisine_type='noodle'

    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print self.restaurant_name
        print self.cuisine_type
    def open_restaurant(self):
        print self.restaurant_name, '餐馆正在营业'

sta = Restaurant('bugaoxing', 'xican')
sta.describe_restaurant()
sta.open_restaurant()

