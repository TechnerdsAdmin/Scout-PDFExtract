
import unittest
import datavalidation

class TestReconciliation(unittest.TestCase):

    def test_basic_reconciliation_float(self):
        input_file = "test1.csv"
        expected_data = 1460.05
        normalized_data = datavalidation.calculate_column_sum_csv(input_file, 0)
        self.assertEqual(expected_data, normalized_data)
    
    def test_basic_reconciliation_int(self):
        input_file = "test2.csv"
        expected_data = 325.00
        normalized_data = datavalidation.calculate_column_sum_csv(input_file, 1)
        self.assertEqual(expected_data, normalized_data)
    
    def test_basic_reconciliation_mixing_data(self):
        input_file = "test3.csv"
        expected_data = 6154.65
        normalized_data = datavalidation.calculate_column_sum_csv(input_file, 2)
        self.assertEqual(expected_data, normalized_data)
    
    def test_data_reconciliation_empty(self):
        input_file = ""
        expected_data = 0
        normalized_data = datavalidation.calculate_column_sum_csv(input_file, 0)
        self.assertEqual(expected_data, normalized_data)

if __name__ == '__main__':
    unittest.main()
