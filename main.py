from manager import Manager
from sql_base import DataBase


def main():
    base = DataBase()
    base.create_base()
    manager = Manager()
    manager.run()


if __name__ == "__main__":
    main()
