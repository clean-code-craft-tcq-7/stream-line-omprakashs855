import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_receiver_parse_data import BmsReceiverConsoleDataParse

SENDER_STREAM_PREFIX = "-------------------\nSender Request : 1\n-------------------\n"
SENDER_STREAM_DATA_FORMAT = "Sender 2 - B1 - Li-ion, 'Temp': {} Celcius, 'SOC': {}% |\n"
SIMULATED_VALUES = [[10,50],[15,20],[25,50],[0,0],[75,9],\
                    [99,999]]
"""
0. with normal data string
1. string with no values
2. string with no parameters
3. string with no sender id
4. empty string
5. junk string
5. string with one parameter
"""

SIMULATED_VALUES_COUNT = 0
def receiver_test_data(self):
    test_data = []
    test_data.append(SENDER_STREAM_PREFIX)
    for i in range(SIMULATED_VALUES_COUNT):
        test_data.append(SENDER_STREAM_DATA_FORMAT.format(SIMULATED_VALUES[i][0],\
            SIMULATED_VALUES[i][1]))
    return test_data

def receiver_test_data_2(self):
    test_data_2 = []
    test_data_2.append(SENDER_STREAM_PREFIX)
    test_data_2.append("Sender 2 - B1 - Li-ion, {} Celcius,  {}% |\n".format(15,66))
    return test_data_2

def receiver_test_data_3(self):
    test_data_3 = []
    test_data_3.append(SENDER_STREAM_PREFIX)
    test_data_3.append(" 2 - B1 - Li-ion, {} Celcius,  {}% |\n".format(37,93))
    test_data_3.append(" 2 - B1 - Li-ion, {} Celcius,  {}% |\n".format(0,9))
    return test_data_3

def receiver_test_data_4(self):
    test_data_4 = []
    test_data_4.append("")
    test_data_4.append(" ")
    test_data_4.append(" ")
    return test_data_4

def receiver_test_data_5(self):
    test_data_5 = []
    test_data_5.append("Hello")
    test_data_5.append("World!")
    test_data_5.append("Good Morning")
    return test_data_5

def receiver_test_data_6(self):
    test_data_6 = []
    test_data_6.append(SENDER_STREAM_PREFIX)
    test_data_6.append("Sender 2 - B1 - Li-ion, 'Temp': {} Celcius|\n".format(15))
    test_data_6.append("Sender 1 - B1 - Li-ion, 'SOC': {}% |\n".format(125))
    return test_data_6


class TestBmsReceiver(unittest.TestCase):
    def test_receive_parse_console_input_0(self):
        global SIMULATED_VALUES_COUNT
        SIMULATED_VALUES_COUNT = 2
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data):
            bms_receiver_parse_obj_0 = BmsReceiverConsoleDataParse(2)
            self.assertEqual(bms_receiver_parse_obj_0.receive_parse_console_input(), \
                {'Sender 2': {'temp': [10, 15], 'soc': [50, 20]}})
        return
    def test_receive_parse_console_input_1(self):
        global SIMULATED_VALUES_COUNT
        SIMULATED_VALUES_COUNT = 0
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data):
            bms_receiver_parse_obj_1 = BmsReceiverConsoleDataParse(5)
            self.assertEqual(bms_receiver_parse_obj_1.receive_parse_console_input(), {})
        return  
    def test_receive_parse_console_input_2(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data_2):
            bms_receiver_parse_obj_2 = BmsReceiverConsoleDataParse(15)
            self.assertEqual(bms_receiver_parse_obj_2.receive_parse_console_input(), {})
        return      
    def test_receive_parse_console_input_3(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data_3):
            bms_receiver_parse_obj_3 = BmsReceiverConsoleDataParse(15)
            self.assertEqual(bms_receiver_parse_obj_3.receive_parse_console_input(), {})
        return     
    def test_receive_parse_console_input_4(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data_4):
            bms_receiver_parse_obj_4 = BmsReceiverConsoleDataParse(1)
            self.assertEqual(bms_receiver_parse_obj_4.receive_parse_console_input(), {})
        return      
    def test_receive_parse_console_input_5(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data_5):
            bms_receiver_parse_obj_5 = BmsReceiverConsoleDataParse(50)
            self.assertEqual(bms_receiver_parse_obj_5.receive_parse_console_input(), {})
        return    
    def test_receive_parse_console_input_6(self):
        with patch('src.bms_receiver_parse_data.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data_6):
            bms_receiver_parse_obj_6 = BmsReceiverConsoleDataParse(37)
            self.assertEqual(bms_receiver_parse_obj_6.receive_parse_console_input(), \
                {'Sender 2': {'temp': [15]}, 'Sender 1': {'soc': [125]}})
        return     