import unittest
from unittest import mock
from unittest.mock import Mock
import json

# Homework 05a: Isolate External Dependencies
# Author: Gabrielle McCormack
# Date Completed: 09.30.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack

from github_info import get_info


class MyTestCase(unittest.TestCase):
    #def testUserA(self):
    # self.assertEqual(get_info('gmccorma'), 'Repo: ssw322MGC Number of commits: 30\nRepo: ssw567 Number of
    # commits: 2\nRepo: ssw567hw01 Number of commits: 4\nRepo: ssw567hw02 Number of commits: 9\nRepo: ssw567hw04
    # Number of commits: 1')

    @mock.patch('github_info.requests.get')
    def testUserA(self, injected_mock):
        mock_req = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        # mock getting repos
        mock_req[0].json.return_value = json.loads(
            '[ { "id": 28765791, "node_id": "MDEwOlJlcG9zaXRvcnkyODc2NTc5MQ==", "name": "hellogitworld" }, '
            '{ "id": 144656027, "node_id": "MDEwOlJlcG9zaXRvcnkxNDQ2NTYwMjc=", "name": "helloworld" }, '
            '{ "id": 151335858,"node_id": "MDEwOlJlcG9zaXRvcnkxNTEzMzU4NTg=", "name": "Mocks" }, '
            '{ "id": 28765763, "node_id": "MDEwOlJlcG9zaXRvcnkyODc2NTc2Mw==", "name": "Project1" }, '
            '{ "id": 7468415, "node_id": "MDEwOlJlcG9zaXRvcnk3NDY4NDE1", "name": "threads-of-life" } ]'
                                                   )
        # commit number for hellogitworld
        mock_req[1].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" },'
            '{ "message": "5" }, '
            '{ "message": "6" }, '
            '{ "message": "7" }, '
            '{ "message": "8" }, '
            '{ "message": "9" }, '
            '{ "message": "10" }, '
            '{ "message": "11" }, '
            '{ "message": "12" }, '
            '{ "message": "13" }, '
            '{ "message": "14" }, '
            '{ "message": "15" }, '
            '{ "message": "16" }, '
            '{ "message": "17" }, '
            '{ "message": "18" }, '
            '{ "message": "19" }, '
            '{ "message": "20" }, '
            '{ "message": "21" }, '
            '{ "message": "22" }, '
            '{ "message": "23" }, '
            '{ "message": "24" }, '
            '{ "message": "25" }, '
            '{ "message": "26" }, '
            '{ "message": "27" }, '
            '{ "message": "28" }, '
            '{ "message": "29" }, '
            '{ "message": "30" } ]'
        )

        # commit number for helloworld
        mock_req[2].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" }, '
            '{ "message": "5" }, '
            '{ "message": "6" } ]'
        )

        # commit number for Mocks
        mock_req[3].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" }, '
            '{ "message": "5" }, '
            '{ "message": "6" }, '
            '{ "message": "7" }, '
            '{ "message": "8" } ]'
        )

        # commit number for Project1
        mock_req[4].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" } ]'
        )
        # commit number fo threads-of-life
        mock_req[5].json.return_value = json.loads(
            '[ { "message": "1" } ]'
        )
        injected_mock.side_effect = mock_req

        self.assertEqual(get_info('richkempinski'), 'Repo: hellogitworld Number of commits: 30\nRepo: helloworld '
                                                    'Number of commits: 6\nRepo: Mocks Number of commits: 8\nRepo: '
                                                    'Project1 Number of commits: 2\nRepo: threads-of-life Number of '
                                                    'commits: 1')


    def testUserB(self):
        self.assertEqual(get_info(''), 'Error, invalid input.')

if __name__ == '__main__':
    unittest.main()
