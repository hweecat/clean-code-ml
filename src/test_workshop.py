import unittest
import pandas as pd
from src.workshop import add
from pandas.testing import assert_frame_equal

class TestWorkshop(unittest.TestCase):
    def test_add_1_and_1_should_equal_2(self, add):
        expected = 2

        actual = add(1,1)

        #assert
        self.assertEqual(expected, actual)

    def test_impute_nans_should_fill_nans_with_median_value(self):
        # arrange
        df = pd.DataFrame({
            'some_column': [1, np.nan]
        })
        # expected
        expected = pd.DataFrame({
            'some_column': [1, 1]
        })
        # actual
        actual = impute_nans(df, columns=['some_column'])
        #assert
        assert_frame_equal(expected, actual)

