""" This file contains methods of battery paramerts receiver.
It does following things:
    1. reads the parameters from the console input
    2. after reading every parameter, it prints the following:
        2.1 maximum and minimum values in the incoming stream
        2.2 simple moving average of the last 5 values
"""
BATTERY_PARAMS = ["Temp", "SOC"]

class BmsReceiverConsoleDataParse(object):
    def __init__(self, input_count):
        self.input_count = input_count
    def receive_data_from_console(self):
        self.battery_params_console = []
        for _ in range(self.input_count):
            try:
                self.battery_params_console.append(input())
            except:
                break
        return self.battery_params_console
    def __check_add_sensor_key(self, string_list, params_key):
        sensor_key = string_list[0]+' '+string_list[1]
        if sensor_key not in self.battery_params.keys():
            self.battery_params[sensor_key] = {}
        if params_key not in self.battery_params[sensor_key].keys():
            self.battery_params[sensor_key][params_key] = []
        return sensor_key
    def __check_params_add_to_dict(self, each_string_list, param_key, value):
        if "Sender" in each_string_list:
            sensor_key = self.__check_add_sensor_key(each_string_list, param_key)
            self.battery_params[sensor_key][param_key].append(value)
    def __parse_for_params_and_update(self, each_string_list):
        if "'Temp':" in each_string_list:
            self.__check_params_add_to_dict(each_string_list, "temp", \
                int(each_string_list[each_string_list.index("'Temp':")+1]))
        if "'SOC':" in each_string_list:
            self.__check_params_add_to_dict(each_string_list, "soc", \
                int(each_string_list[each_string_list.index("'SOC':")+1][:-1]))
        return
    def __parse_console_data(self, console_data_list):
        self.battery_params = {}
        for each_string in console_data_list:
            self.__parse_for_params_and_update(each_string.split(" "))
        return self.battery_params
    def receive_parse_console_input(self, update_receive_count=None):
        if update_receive_count:
            self.input_count = update_receive_count
        return self.__parse_console_data(self.receive_data_from_console())
