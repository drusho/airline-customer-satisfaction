import unittest
import pandas as pd
from scripts.data_cleaning import impute_missing_values


class TestDataCleaning(unittest.TestCase):

    def test_impute_missing_values(self):
        data = {'Arrival Delay in Minutes': [10, 20, None, 40]}
        df = pd.DataFrame(data)
        df_imputed = impute_missing_values(df)
        self.assertFalse(df_imputed.isnull().values.any())


if __name__ == '__main__':
    unittest.main()
