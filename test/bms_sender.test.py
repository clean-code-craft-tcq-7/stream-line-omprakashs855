import unittest
import os
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_sender import BMS_Sender as BS

class Test_BMS_Sender(unittest.TestCase):

    def regex_match(self, console_out):
        test_regex = r"Sender\s\d+ - B\d+ - [\w\-\s]+, 'Temp': \w+ \w+, 'SOC': \w+% \|"
        match_check = True
        for str in console_out:
            if not re.match(test_regex, str):
                match_check = False
        return match_check
    
    def print_sender_request_id(self, idx):
        print("-------------------")
        print("Sender Request : {}".format(idx+1))
        print("-------------------")

    def test_bms_sender_console_regex(self):

        # Creating BMS_Sender Class Object
        sender_obj = BS()

        json_data = sender_obj.get_json_data(sender_obj.sender_tc_json_path)
        for idx, tc in enumerate(json_data["Sender"]):
            self.print_sender_request_id(idx)
            console_out = sender_obj.create_stream_output(tc)
            self.assertTrue(self.regex_match(console_out))
        
if __name__ == "__main__":
    unittest.main()