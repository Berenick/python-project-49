from . import path_add
import engine
from games import calc


def main():
    engine.start_game(calc)


path_add.ignore_lint_401()


if __name__ == '__main__':
    main()
