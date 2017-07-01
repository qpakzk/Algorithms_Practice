"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    lst = []
    for i in range(0, len(s), 2):
        lst.append(s[i: i + 2])
    if len(s) % 2 == 1:
        lst[-1] += '_'

    return lst

from unittest import TestCase

class TestSolutin(TestCase):
    def test_solutin(test):
        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            test.assertEqual(solution(inp), exp)