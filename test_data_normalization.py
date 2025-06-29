import unittest
import normalization

class TestNormalization(unittest.TestCase):

    def test_basic_normalization_cur(self):
        input_data = "5   50    EA  J0222      BELT,BX54                   4/25/2025   $8.2500   $412.50"
        expected_data = "5   50    EA  J0222      BELT,BX54                   4/25/2025   8.2500   412.50"
        normalized_data = normalization.data_normalization(input_data)
        self.assertEqual(expected_data, normalized_data)
    
    def test_basic_normalization(self):
        input_data = "5   50    EA  J0222      BELT,BX54                   4/25/2025   $573.4500   $1,146.90"
        expected_data = "5   50    EA  J0222      BELT,BX54                   4/25/2025   573.4500   1146.90"
        normalized_data = normalization.data_normalization(input_data)
        self.assertEqual(expected_data, normalized_data)
    
    def test_basic_normalization_empty(self):
        input_data = ""
        expected_data = ""
        normalized_data = normalization.data_normalization(input_data)
        self.assertEqual(expected_data, normalized_data)
    
    def test_data_normalization(self):
        input_data = "5   50    EA  J0222      BELT,BX54                   4/25/2025   8.2500   412.50"
        expected_data = "5   50    EA  J0222      BELT,BX54                   4/25/2025   8.2500   412.50"
        normalized_data = normalization.data_normalization(input_data)
        self.assertEqual(expected_data, normalized_data)

if __name__ == '__main__':
    unittest.main()
