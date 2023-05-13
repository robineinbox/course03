import unittest
from utils import *

class TestFunctions(unittest.TestCase):

    def test_get_data(self):
        data = get_data()
        self.assertTrue(isinstance(data, list))
        self.assertGreater(len(data), 0)

    def test_get_filtered_data(self):
        data = [{'from': 'abc', 'to': 'def'}, {'from': '', 'to': 'ghi'}, {'from': 'jkl', 'to': ''}]
        filtered_data = get_filtered_data(data, True)
        self.assertEqual(len(filtered_data), 1)
        self.assertEqual(filtered_data[0], {'from': 'abc', 'to': 'def'})

    def test_get_last_values(self):
        data = [{'date': '2022-01-01', 'value': 1}, {'date': '2022-01-02', 'value': 2},
                {'date': '2022-01-03', 'value': 3}, {'date': '2022-01-04', 'value': 4},
                {'date': '2022-01-05', 'value': 5}]
        last_values = get_last_values(data, 3)
        self.assertEqual(len(last_values), 3)
        self.assertEqual(last_values, [{'date': '2022-01-03', 'value': 3},
                                       {'date': '2022-01-04', 'value': 4},
                                       {'date': '2022-01-05', 'value': 5}])

    def test_get_formated_data(self):
        data = [{'date': '2022-01-01', 'value': 1}, {'date': '2022-01-02', 'value': 2}]
        formated_data = get_formated_data(data)
        self.assertEqual(len(formated_data), 2)
        self.assertEqual(formated_data[0], '2022-01-01: 1')
        self.assertEqual(formated_data[1], '2022-01-02: 2')

if __name__ == '__main__':
    unittest.main()