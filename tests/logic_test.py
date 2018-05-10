import json
import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), ''))

from nagiosapi import app
from nagiosapi.logic import object_list_from_status_dat


class NagiosAPITestCase(unittest.TestCase):
    def setUp(self):
        os.environ["NAGIOS_STATUS_PATH"] = "tests/mocks/status.dat"
        self.app = app.test_client()

    def test_object_list_from_status_dat(self):
        with open("tests/mocks/all.json", "r") as f:
            expected_output = json.loads(f.read())

        self.assertEqual(expected_output, object_list_from_status_dat())


if __name__ == '__main__':
    unittest.main()
