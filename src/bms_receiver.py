""" This file contains methods of battery paramerts receiver.
It does following things:
    1. reads the parameters from the console input
    2. after reading every parameter, it prints the following:
        2.1 maximum and minimum values in the incoming stream
        2.2 simple moving average of the last 5 values
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_receiver_parse_data import BmsReceiverConsoleDataParse
from src.bms_receiver_analytics import BmsReceiverAnalytics

STREAM_LENGTH = 50

def data_parse_analytics():
    bms_rx_data_parse_obj = BmsReceiverConsoleDataParse(STREAM_LENGTH)
    parsed_data = bms_rx_data_parse_obj.receive_parse_console_input()
    # print("parsed_data: ", parsed_data)
    bms_rx_analytics_obj = BmsReceiverAnalytics(parsed_data)
    return bms_rx_analytics_obj.bms_receiver_analytics()