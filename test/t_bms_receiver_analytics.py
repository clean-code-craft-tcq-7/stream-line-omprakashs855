import os
import sys
import unittest
from unittest.mock import patch
import json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_receiver_analytics import BmsReceiverAnalytics
"""
0 : normal data
1 : empty list for temp and soc params
2 : only one params
3 : empty dictionary
4 : no params
"""

class TestBmsReceiverAnalytics(unittest.TestCase):
    def test_bms_receiver_analytics_0(self):
        input_0 = {'Sender 2': {'temp': [1, 2, 4, 5, 6, 7], 'soc': [0, 1, 2, 4, 5, 6]}}
        test_obj_0 = BmsReceiverAnalytics(input_0)
        self.assertEqual(test_obj_0.bms_receiver_analytics(),\
            json.dumps({"Sender 2": {"temp": {"min": 1, "max": 7, "sma": 4.8},\
                "soc": {"min": 0, "max": 6, "sma": 3.6}}}))
        return
    def test_bms_receiver_analytics_1(self):
        input_1 = {'Sender 2': {'temp': [], 'soc': []}}
        test_obj_1 = BmsReceiverAnalytics(input_1)
        self.assertEqual(test_obj_1.bms_receiver_analytics(),\
            json.dumps({"Sender 2": {"temp": {"min": None, "max": None, "sma": None},\
                "soc": {"min": None, "max": None, "sma": None}}}))
        return    
    def test_bms_receiver_analytics_2(self):
        input_2 = {'Sender 12': {'temp': [5, 6, 89, 75, 13, 4]}}
        test_obj_2 = BmsReceiverAnalytics(input_2)
        self.assertEqual(test_obj_2.bms_receiver_analytics(),\
            json.dumps({"Sender 12": {"temp": {"min": 4, "max": 89, "sma": 37.4}}}))
        return        
    def test_bms_receiver_analytics_3(self):
        input_3 = {}
        test_obj_3 = BmsReceiverAnalytics(input_3)
        print(test_obj_3.bms_receiver_analytics())
        self.assertEqual(test_obj_3.bms_receiver_analytics(),json.dumps({}))
        return        
    def test_bms_receiver_analytics_4(self):
        input_4 = {'Sender 12': {}}
        test_obj_4 = BmsReceiverAnalytics(input_4)
        self.assertEqual(test_obj_4.bms_receiver_analytics(),json.dumps({'Sender 12': {}}))
        return     