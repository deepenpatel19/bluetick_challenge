import unittest


def check_missing_integers(_data=[]):
    """
    This function find missing integers from given `_data` array between 0 and 99 inclusive.
    """
    if _data:
        result = []  # Missing integers in sorted order.
        _data.sort()  # Apply sorting if integers are not sorted.
        for i in range(len(_data)):
            _value = _data[i]
            # print("Index and value", i, _value)
            if 0 == _value:
                # print("value is 0")
                pass
            elif i < len(_data) - 1:
                # print("index is less than length of data")
                _value_to_add = _data[i + 1] - _value
                # print("value to add", _value_to_add)
                _fist_value = _value + 1
                _last_value = _data[i + 1] - 1
                if _fist_value == _last_value:
                    result.append("{0}".format(_fist_value))
                else:
                    result.append("{0} --> {1}".format(_value + 1, _data[i + 1] - 1))
            else:
                # print("else block")
                _value_of_last_index = _data[-1]
                # print("last index value", _value_of_last_index)
                if _value_of_last_index < 99:
                    result.append("{0} --> {1}".format(_value_of_last_index + 1, 99))
                else:
                    pass
        # print("final result", result)
        return result
    else:
        return []


class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = check_missing_integers(_data=[0, 1, 3, 50, 75])
        self.assertEqual(
            ["2", "4 --> 49", "51 --> 74", "76 --> 99"], result, "Not passed 1."
        )

    def test_case_2(self):
        result = check_missing_integers(_data=[1, 3, 50, 75])
        self.assertEqual(
            ["0", "2", "4 --> 49", "51 --> 74", "76 --> 99"], result, "Not passed 2."
        )

    def test_case_3(self):
        result = check_missing_integers(_data=[1, 3, 50, 75, 99])
        self.assertEqual(
            ["0", "2", "4 --> 49", "51 --> 74", "76 --> 98"], result, "Not passed 3."
        )


if __name__ == "__main__":
    unittest.main()
