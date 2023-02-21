import sys
import os
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import unittest

SENDER_STREAM_PREFIX = "-------------------\nSender Request : 1\n-------------------\n"
SENDER_STREAM_DATA_FORMAT = "Sender 2 - B1 - Li-ion, 'Temp': {} Celcius, 'SOC': {}% |\n"
SIMULATED_VALUES = [[10,50],
                    [15,20]]

SIMULATED_VALUES_COUNT = 0
def receiver_test_data(self):
    stream_count = SIMULATED_VALUES_COUNT
    # test_data = SENDER_STREAM_PREFIX
    # for i in range(stream_count):
    #     test_data += SENDER_STREAM_DATA_FORMAT.format(SIMULATED_VALUES[i][0],\
    #         SIMULATED_VALUES[i][1])
    test_data = []
    test_data.append(SENDER_STREAM_PREFIX)
    for i in range(stream_count):
        test_data.append(SENDER_STREAM_DATA_FORMAT.format(SIMULATED_VALUES[i][0],\
            SIMULATED_VALUES[i][1]))
    return test_data

class TestBmsReceiver(unittest.TestCase):
    def test_receive_data_from_console(self):
        return
    def test_parse_console_data(self):
        return
    def test_receive_parse_console_input(self):
        global SIMULATED_VALUES_COUNT
        from src.bms_receiver import BmsReceiverConsoleDataParse
        SIMULATED_VALUES_COUNT = 2
        with patch('src.bms_receiver.BmsReceiverConsoleDataParse.receive_data_from_console', receiver_test_data):
            bms_receiver_parse_obj = BmsReceiverConsoleDataParse(2)
            output = bms_receiver_parse_obj.receive_parse_console_input(2)
            print("output : ", output)
        return