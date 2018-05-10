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

    def test_GET_all(self):
        with open("tests/mocks/all.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_info(self):
        with open("tests/mocks/info.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/info/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_programstatus(self):
        with open("tests/mocks/programstatus.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/programstatus/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_hoststatus(self):
        with open("tests/mocks/hoststatus.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/hoststatus/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_servicestatus(self):
        with open("tests/mocks/servicestatus.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/servicestatus/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_contactstatus(self):
        with open("tests/mocks/contactstatus.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/contactstatus/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_hostcomment(self):
        with open("tests/mocks/hostcomment.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/hostcomment/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_info_created(self):
        with open("tests/mocks/info_created.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/info/created/").data.decode())
        self.assertEqual(result, expected_output)

    def test_GET_hoststatus_hostname_filter_works(self):
        with open("tests/mocks/hoststatus_irc.json", "r") as f:
            expected_output = json.loads(f.read())

        result = json.loads(self.app.get("/api/hoststatus/irc/").data.decode())
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
