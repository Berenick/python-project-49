import sys
import os
DIR_NAME = os.path.dirname(__file__)
DIR_NAME += '/../'
print(DIR_NAME)
sys.path.append(DIR_NAME)
import even_help


def main():
    even_help.even_game()
    

if __name__ == '__main__':
    main()
        