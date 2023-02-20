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
        
    def create_temp_stream_output(self, idx, battery_idx, bat):
        temp_limit_json_data = self.get_json_data(self.sender_temp_limit_json_path)
        min_temp = temp_limit_json_data["Temperature_Limit"]["Min"]
        max_temp = temp_limit_json_data["Temperature_Limit"]["Max"]
        rand_temp_out = self.create_random_value(min_temp, max_temp)
        out_data = "Sender {} - B{} - {}, {}, {} |".format(battery_idx+1, idx+1, bat["Battery_Type"], bat["Temp_Type"], rand_temp_out)
        print(out_data)
        return out_data
    
    def create_stream_output(self, test_case_json_data):
        console_out_data = []
        # test_case_json_data = self.get_json_data(self.sender_tc_json_path)
        for idx in range(0, test_case_json_data["Stream_Length"]):
            battery_idx = self.select_random_battery(test_case_json_data["Number_Of_Batteries"])
            battery_config = test_case_json_data["Batteries_List"][battery_idx]
            console_out_data.append(self.create_temp_stream_output(idx, battery_idx, battery_config))
        
        return console_out_data
    





