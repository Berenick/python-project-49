#!/usr/bin/env python3
import sys
import os
DIR_NAME = os.path.dirname(__file__)
DIR_NAME += '/../'
print(DIR_NAME)
sys.path.append(DIR_NAME)
import cli
def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
if __name__ == '__main__':
    main()