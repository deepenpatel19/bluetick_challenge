import unittest



def update_result_array(result=[], _data=[], i=0):
    _first_value = _data[i] + 1
    _last_value = _data[i + 1] - 1
    _value_to_check = _data[i + 1] - _data[i]
    if _first_value == _last_value:
        result.append("{0}".format(_first_value))
    elif _value_to_check != 1:
        result.append("{0} --> {1}".format(_data[i] + 1, _data[i + 1] - 1))
    else:
        pass
    return result


def check_missing_integers_v1(_data=[]):
    """
    This function find missing integers from given `_data` array between 0 and 99 inclusive.
    """
    if _data:
        result = []  # Missing integers in sorted order.
        _data.sort()  # Apply sorting if integers are not sorted.
        for i in range(len(_data)):
            if i < len(_data) - 1:
                if i == 0 and _data[i] != 0:
                    _first_value = 0
                    _last_value = _data[0] - 1
                    if _first_value == _last_value:
                        result.append("{0}".format(_first_value))
                    elif _last_value > _first_value:
                        result.append("{0} --> {1}".format(_first_value, _last_value))

                    result = update_result_array(result=result, _data=_data, i=i)
                else:
                    result = update_result_array(result=result, _data=_data, i=i)
            else:
                _value_of_last_index = _data[-1]
                if _value_of_last_index < 99:
                    result.append("{0} --> {1}".format(_value_of_last_index + 1, 99))
                else:
                    pass
        return result
    else:
        return []



class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = check_missing_integers_v1(_data=[0, 1, 3, 50, 75])
        expected_result = ["2", "4 --> 49", "51 --> 74", "76 --> 99"]
        print("before test ", expected_result, result)
        self.assertEqual(expected_result, result, "Not passed 1.")

    def test_case_2(self):
        result = check_missing_integers_v1(_data=[1, 3, 50, 75])
        expected_result = ["0", "2", "4 --> 49", "51 --> 74", "76 --> 99"]
        print("before test ", expected_result, result)
        self.assertEqual(expected_result, result, "Not passed 2.")

    def test_case_3(self):
        result = check_missing_integers_v1(_data=[1, 3, 50, 75, 99])
        expected_result = ["0", "2", "4 --> 49", "51 --> 74", "76 --> 98"]
        print("before test ", expected_result, result)
        self.assertEqual(expected_result, result, "Not passed 3.")

    def test_case_4(self):
        result = check_missing_integers_v1(_data=[])
        expected_result = []
        print("before test ", expected_result, result)
        self.assertEqual(expected_result, result, "Not passed 4.")

    def test_case_5(self):
        result = check_missing_integers_v1(
            _data=[0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 15, 78, 17, 99]
        )
        expected_result = ["4", "10", "12 --> 14", "16", "18 --> 77", "79 --> 98"]
        print("before test ", expected_result, result)
        self.assertEqual(expected_result, result, "Not passed 5.")


if __name__ == "__main__":
    unittest.main()
