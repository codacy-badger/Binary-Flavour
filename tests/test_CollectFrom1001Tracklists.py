from DataManager import CollectFrom1001Tracklists

import unittest

class TestCollectData(unittest.TestCase):
    def test_CollectFromListYearBS4(self):
        self.assertEqual(1099, CollectFrom1001Tracklists.CollectFromListYearBS4(2018))

    def test_CollectFromListYearSelenium(self):
        self.assertEqual(1099, CollectFrom1001Tracklists.CollectFromListYearSelenium(2018))


