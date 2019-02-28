from DataManager import CollectFrom1001Tracklists

import unittest

class TestCollectData(unittest.TestCase):
    def test_CollectFromListYearSelenium(self):
        self.assertEqual(1098, CollectFrom1001Tracklists.CollectFromListYearSelenium(2018))
