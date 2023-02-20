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

    def check_attemp_filter(self, check_attempt, check_name):
        for check_dict in check_attempt:
            if check_dict["Name"] == check_name:
                return check_dict["Required"]
        
    def create_temp_stream_output(self, bat, check_attempt, check_name):
        if not self.check_attemp_filter(check_attempt, check_name):
            return None
        temp_limit_json_data = self.get_json_data(self.sender_temp_limit_json_path)
        battery_type_idx = self.select_battery_type(temp_limit_json_data["Temperature_Limit"], bat["Battery_Type"])
        if battery_type_idx == (-1):
            return None
        min_temp = temp_limit_json_data["Temperature_Limit"][battery_type_idx]["Min"]
        max_temp = temp_limit_json_data["Temperature_Limit"][battery_type_idx]["Max"]
        rand_temp_out = self.create_random_value(min_temp, max_temp)
        return rand_temp_out

    def create_SOC_stream_output(self, bat, check_attempt, check_name):
        if not self.check_attemp_filter(check_attempt, check_name):
            return None
        SOC_limit_json_data = self.get_json_data(self.sender_SOC_limit_json)
        battery_type_idx = self.select_battery_type(SOC_limit_json_data["SOC_limit"], bat["Battery_Type"])
        if battery_type_idx == (-1):
            return None
        min_temp = SOC_limit_json_data["SOC_limit"][battery_type_idx]["Min"]
        max_temp = SOC_limit_json_data["SOC_limit"][battery_type_idx]["Max"]
        rand_temp_out = self.create_random_value(min_temp, max_temp)
        return rand_temp_out
    
    def print_console_output(self, temp_rand_out, soc_rand_out, battery_idx, idx, battery_config):
        if temp_rand_out == None:
            temp_rand_out = "xxxx"
        if soc_rand_out == None:
            soc_rand_out = "xxxx"

        print_console = "Sender {} - B{} - {}, 'Temp': {} {}, 'SOC': {}% |".format(battery_idx+1, idx+1, battery_config["Battery_Type"], temp_rand_out, battery_config["Temp_Type"], soc_rand_out)
        print(print_console)
        return print_console

    def create_stream_output(self, test_case_json_data):
        console_out_data = []
        # test_case_json_data = self.get_json_data(self.sender_tc_json_path)
        for idx in range(0, test_case_json_data["Stream_Length"]):
            battery_idx = self.select_random_battery(test_case_json_data["Number_Of_Batteries"])
            battery_config = test_case_json_data["Batteries_List"][battery_idx]
            temp_rand_out = self.create_temp_stream_output(battery_config, test_case_json_data["Check_Attemp"], "Temperature")
            soc_rand_out = self.create_SOC_stream_output(battery_config, test_case_json_data["Check_Attemp"], "SOC")
            # charge_rand_out = self.create_charge_rate_stream_output(battery_config, test_case_json_data["Check_Attemp"], "Charge_Rate")
            print_console = self.print_console_output(temp_rand_out, soc_rand_out, battery_idx, idx, battery_config)
            console_out_data.append(print_console)
        
        return console_out_data
    





