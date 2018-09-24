import unittest

# Homework 04a: Develop with the Perspective of the Tester in Mind
# Author: Gabrielle McCormack
# Date Completed: 09.23.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack

from github_info import get_info


class MyTestCase(unittest.TestCase):
    #def testUserA(self):
       # self.assertEqual(get_info('gmccorma'), 'Repo: ssw322MGC Number of commits: 30\nRepo: ssw567 Number of commits: 2\nRepo: ssw567hw01 Number of commits: 4\nRepo: ssw567hw02 Number of commits: 9\nRepo: ssw567hw04 Number of commits: 1')

    def testUserA(self):
        self.assertEqual(get_info('richkempinski'), 'Repo: hellogitworld Number of commits: 30\nRepo: helloworld Number of commits: 2\nRepo: Project1 Number of commits: 2\nRepo: threads-of-life Number of commits: 1')

    def testUserB(self):
        self.assertEqual(get_info(''), 'Error, invalid input.')

if __name__ == '__main__':
    unittest.main()
