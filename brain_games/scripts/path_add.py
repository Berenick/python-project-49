import sys
import os
DIR_NAME = os.path.dirname(__file__)
DIR_NAME += '/../'
print(DIR_NAME)
sys.path.append(DIR_NAME)


def ignore_lint_401():
    a = 3
    a + 2
