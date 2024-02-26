from . import path_add
import engine
from games import progression


def main():
    engine.start_game(progression)


path_add.ignore_lint_401()


if __name__ == '__main__':
    main()
