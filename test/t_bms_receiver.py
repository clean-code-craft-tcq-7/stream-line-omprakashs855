import os
import sys
import json
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_receiver import data_parse_analytics, send_to_console
from t_bms_receiver_parse_data import receiver_test_data_2,\
    receiver_test_data_5

SIMULATED_VALUES_COUNT = 0
SENDER_STREAM_PREFIX = "-------------------\nSender Request : 1\n-------------------\n"
SENDER_STREAM_DATA_FORMAT = "Sender 2 - B1 - Li-ion, 'Temp': {} Celcius, 'SOC': {}% |\n"
SIMULATED_VALUES = [[10,50],[15,20],[25,50],[0,0],[75,9],\
                    [99,999]]


def receiver_test_data_0(self):
    test_data = []
    test_data.append(SENDER_STREAM_PREFIX)
    for i in range(SIMULATED_VALUES_COUNT):
        test_data.append(SENDER_STREAM_DATA_FORMAT.format(SIMULATED_VALUES[i][0],\
            SIMULATED_VALUES[i][1]))
    # print("receiver_test_data_0 : ", test_data)
    return test_data

class TestBmsReceiverClass(unittest.TestCase):
    def test_send_to_console(self):
        """ this test case is to test send_to_console method """
        with patch('builtins.print') as mock_print:
            send_to_console("Hello")
            mock_print.assert_called_once_with('Hello')      
    def test_data_parse_analytics_0(self):
        global SIMULATED_VALUES_COUNT
        SIMULATED_VALUES_COUNT = 5
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', \
            receiver_test_data_0):
            self.assertEqual(data_parse_analytics(), \
                '{"Sender 2": {"temp": {"min": 0, "max": 75, "sma": 25.0}, "soc": {"min": 0, "max": 50, "sma": 25.8}}}')
        return
    def test_data_parse_analytics_1(self):
        global SIMULATED_VALUES_COUNT
        SIMULATED_VALUES_COUNT = 0
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', \
            receiver_test_data_0):
            # print("test_data_parse_analytics_0`", type(data_parse_analytics()), data_parse_analytics())
            self.assertEqual(data_parse_analytics(), '{}')
        return    
    def test_data_parse_analytics_1(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', \
            receiver_test_data_2):
            self.assertEqual(data_parse_analytics(), "{}")
        return        
    def test_data_parse_analytics_2(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', \
            receiver_test_data_5):
            self.assertEqual(data_parse_analytics(), "{}")
        return     