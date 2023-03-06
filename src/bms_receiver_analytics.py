""" This file contains methods of battery paramerts receiver.
It does following things:
    1. after reading every parameter, it prints the following:
        1.1 maximum and minimum values in the incoming stream
        1.2 simple moving average of the last 5 values
"""
import json

class BmsReceiverAnalytics(object):
    def __init__(self, bms_params_data):
        self.__bms_params_data = bms_params_data
        self.__bms_analytics_out = {}
        self.__sma_period = 5
        return
    def __get_sma_from_list(self, sensor_data_list):
        if len(sensor_data_list) < self.__sma_period:
            period = len(sensor_data_list)
        else:
            period = self.__sma_period
        return sum(sensor_data_list[-period:])/period
    def __sma_of_sensor_data(self, sensor_data, analytics_data):
        if sensor_data:
            analytics_data["sma"] = self.__get_sma_from_list(sensor_data)
        else:
            analytics_data["sma"] = None
        return
    def __get_max_from_list(self, sensor_data_list):
        return max(sensor_data_list)
    def __max_of_sensor_data(self, sensor_data, analytics_data):
        if sensor_data:
            analytics_data["max"] = self.__get_max_from_list(sensor_data)
        else:
            analytics_data["max"] = None
        return
    def __get_min_from_list(self, sensor_data_list):
        return min(sensor_data_list)
    def __min_of_sensor_data(self, sensor_data, analytics_data):
        if sensor_data:
            analytics_data["min"] = self.__get_min_from_list(sensor_data)
        else:
            analytics_data["min"] = None            
        return
    def __analytics_on_params(self, each_sensor_key):
        for each_param_key in self.__bms_params_data[each_sensor_key].keys():
            self.__bms_analytics_out[each_sensor_key][each_param_key] = {}   
            self.__min_of_sensor_data(self.__bms_params_data[each_sensor_key][each_param_key],\
                self.__bms_analytics_out[each_sensor_key][each_param_key])
            self.__max_of_sensor_data(self.__bms_params_data[each_sensor_key][each_param_key],\
                self.__bms_analytics_out[each_sensor_key][each_param_key])
            self.__sma_of_sensor_data(self.__bms_params_data[each_sensor_key][each_param_key],\
                self.__bms_analytics_out[each_sensor_key][each_param_key])        
    def bms_receiver_analytics(self):
        for each_sensor_key in self.__bms_params_data.keys():
            self.__bms_analytics_out[each_sensor_key] = {}
            self.__analytics_on_params(each_sensor_key)
        return json.dumps(self.__bms_analytics_out)
    