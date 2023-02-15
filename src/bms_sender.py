import subprocess
import random
import os
import json

class BMS_Sender:

    def __init__(self):
        self.root_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
        self.sender_tc_json_path = os.path.join(self.root_dir, "inc", "sender_test_case.json")
        self.sender_temp_limit_json_path = os.path.join(self.root_dir, "inc", "sender_temperature_limit.json")
        self.sender_console_out_json_path = os.path.join(self.root_dir, "inc", "sender_console_output.json") 
        
    def get_json_data(self, path):
        data = {}
        if os.path.exists(path):
            with open(path, 'r') as jsonread:
                data = json.load(jsonread)
        return data

    def celcius_to_Fahr(self, C_temp):
        # Convert Celcius to Fahrenheit
        F_temp = (C_temp*(9/5)) + 32
        return F_temp
    
    def Fahr_to_celcius(self, F_temp):
        # Convert Fahrenheit to Celcius
        C_temp = (F_temp - 32)*(5/9)
        return C_temp
    
    def create_random_value(self, min, max):
        return random.randint(min, max)
