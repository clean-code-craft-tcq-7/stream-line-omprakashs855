import subprocess
import random
import os
import json
import re

class BMS_Sender:

    def __init__(self):
        self.root_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
        self.sender_tc_json_path = os.path.join(self.root_dir, "inc", "sender_test_case.json")
        self.sender_temp_limit_json_path = os.path.join(self.root_dir, "inc", "sender_temperature_limit.json")
        self.sender_SOC_limit_json = os.path.join(self.root_dir, "inc", "sender_SOC_limit.json")
        
    def get_json_data(self, path):
        data = {}
        if os.path.exists(path):
            with open(path, 'r') as jsonread:
                data = json.load(jsonread)
        return data
    
    def create_random_value(self, min, max):
        return random.randint(min, max)
    
    def select_random_battery(self, no_of_sender_battery):
        return self.create_random_value(0, no_of_sender_battery-1)

    def select_battery_type(self, temp_list, bat_config_type):
        idx = -1
        for bat_type in temp_list:
            if bat_type["Battery_Type"] == bat_config_type:
                return temp_list.index(bat_type)
        return idx

        
    def create_temp_stream_output(self, idx, battery_idx, bat):
        temp_limit_json_data = self.get_json_data(self.sender_temp_limit_json_path)
        battery_type_idx = self.select_battery_type(temp_limit_json_data["Temperature_Limit"], bat["Battery_Type"])
        if battery_type_idx == None:
            return None
        min_temp = temp_limit_json_data["Temperature_Limit"][battery_type_idx]["Min"]
        max_temp = temp_limit_json_data["Temperature_Limit"][battery_type_idx]["Max"]
        rand_temp_out = self.create_random_value(min_temp, max_temp)
        temp_out_data = "Sender {} - B{} - {}, {}, {} |".format(battery_idx+1, idx+1, bat["Battery_Type"], bat["Temp_Type"], rand_temp_out)
        return rand_temp_out

    def create_SOC_stream_output(self, idx, battery_idx, bat):
        SOC_limit_json_data = self.get_json_data(self.sender_SOC_limit_json)
        battery_type_idx = self.select_battery_type(SOC_limit_json_data["SOC_limit"], bat["Battery_Type"])
        if battery_type_idx == None:
            return None
        min_temp = SOC_limit_json_data["SOC_limit"][battery_type_idx]["Min"]
        max_temp = SOC_limit_json_data["SOC_limit"][battery_type_idx]["Max"]
        rand_temp_out = self.create_random_value(min_temp, max_temp)
        return rand_temp_out
    
    def create_stream_output(self, test_case_json_data):
        console_out_data = []
        # test_case_json_data = self.get_json_data(self.sender_tc_json_path)
        for idx in range(0, test_case_json_data["Stream_Length"]):
            battery_idx = self.select_random_battery(test_case_json_data["Number_Of_Batteries"])
            battery_config = test_case_json_data["Batteries_List"][battery_idx]
            temp_rand_out = self.create_temp_stream_output(idx, battery_idx, battery_config)
            soc_rand_out = self.create_SOC_stream_output(idx, battery_idx, battery_config)
            print_console = "Sender {} - B{} - {}, 'Temp': {} {}, 'SOC': {}% |".format(battery_idx+1, idx+1, battery_config["Battery_Type"], temp_rand_out, battery_config["Temp_Type"], soc_rand_out)
            print(print_console)
            console_out_data.append(print_console)
        
        return console_out_data
    





