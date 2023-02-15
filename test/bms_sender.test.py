import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.bms_sender import BMS_Sender as BS

class Test_BMS_Sender(unittest.TestCase):

    def test_bms_sender_console_regex(self):

        # Creating BMS_Sender Class Object
        sender_obj = BS()

        json_data = sender_obj.get_json_data(sender_obj.sender_tc_json_path)
        for tc in json_data["Sender"]:
            console_out = sender_obj.create_stream_output(tc)
            self.assertTrue(sender_obj.regex_match(console_out))
        
if __name__ == "__main__":
    unittest.main()