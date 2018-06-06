'''
run "py.test tutorial/test.py -q"  for test
'''

import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()   # 修改config的时候需要调用

    def tearDown(self):
        testing.tearDown()              # 修改config的时候需要调用

    def test_hello_world(self):
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)