import unittest
import os
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_sender import BMS_Sender as BS

class Test_BMS_Sender(unittest.TestCase):

    def regex_match(self, console_out):
        test_regex = r"Sender\s\d+\s\-\sB\d+\s[\w\-\s\,]+\|"
        match_check = True
        for str in console_out:
            if not re.match(test_regex, str):
                match_check = False
        return match_check

    def test_bms_sender_console_regex(self):

        # Creating BMS_Sender Class Object
        sender_obj = BS()

        json_data = sender_obj.get_json_data(sender_obj.sender_tc_json_path)
        for tc in json_data["Sender"]:
            console_out = sender_obj.create_stream_output(tc)
            self.assertTrue(self.regex_match(console_out))
        
if __name__ == "__main__":
    unittest.main()