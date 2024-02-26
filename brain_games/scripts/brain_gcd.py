from . import path_add
import engine
from games import gcd


def main():
    engine.start_game(gcd)


path_add.ignore_lint_401()


if __name__ == '__main__':
    main()
