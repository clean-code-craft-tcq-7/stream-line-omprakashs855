import unittest
import os
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_sender import BMS_Sender as BS

class Test_BMS_Sender(unittest.TestCase):
    
    def __init__(self):
        self.test_regex = r"Sender\s\w+\-\sB\d+\s[\w\-\s\,]+\|"

    def test_bms_sender_console_regex(self):

        # Creating BMS_Sender Class Object
        sender_obj = BS()
        
        sender_console_data = sender_obj.get_json_data(sender_obj.sender_console_out_json_path)
        
        for data in sender_console_data:
            self.assertRegex(data, self.test_regex)

if __name__ == "__main__":
    unittest.main()