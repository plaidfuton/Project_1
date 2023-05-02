from controller import *


def main() -> None:
    '''
    method which initializes the GUI program
    '''
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
