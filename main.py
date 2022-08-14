from manager import Manager
from sql_base import Base


def main():
    base = Base()
    base.create_base()
    manager = Manager()
    manager.log()


if __name__ == "__main__":
    main()
