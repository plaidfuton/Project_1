from PyQt5.QtWidgets import *
from view import *


class Controller(QMainWindow, Ui_MainWindow):
    '''
    Class containing the methods that allow GUI functionality
    '''
    def __init__(self, *args, **kwargs) -> None:
        '''
        Method that assigns functions to push buttons present in the GUI
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_positive_cookie.clicked.connect(lambda: self.up('cookie'))
        self.button_positive_sandwich.clicked.connect(lambda: self.up('sandwich'))
        self.button_positive_water.clicked.connect(lambda: self.up('water'))
        self.button_negative_cookie.clicked.connect(lambda: self.down('cookie'))
        self.button_negative_sandwich.clicked.connect(lambda: self.down('sandwich'))
        self.button_negative_water.clicked.connect(lambda: self.down('water'))
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_calculate.clicked.connect(lambda: self.calculate())

    def up(self, button: str) -> None:
        '''
        Method which facilitates the uptick of labels
        relating to the amount of a specific item ordered
        :param button: the name of which "up" button was pressed
        '''
        if button == 'cookie':
            cookie_amount = int(self.label_cookie_amount.text()) + 1
            self.label_cookie_amount.setText(str(cookie_amount))
        elif button == 'sandwich':
            sandwich_amount = int(self.label_sandwich_amount.text()) + 1
            self.label_sandwich_amount.setText(str(sandwich_amount))
        else:
            water_amount = int(self.label_water_amount.text()) + 1
            self.label_water_amount.setText(str(water_amount))

    def down(self, button: str) -> None:
        '''
        method which facilitates the downtick of labels
        relating to the amount of a specific item ordered
        :param button: the name of which "down" button was pressed
        '''
        if button == 'cookie':
            if int(self.label_cookie_amount.text()) == 0:
                pass
            else:
                cookie_amount = int(self.label_cookie_amount.text()) - 1
                self.label_cookie_amount.setText(str(cookie_amount))
        elif button == 'sandwich':
            if int(self.label_sandwich_amount.text()) == 0:
                pass
            else:
                sandwich_amount = int(self.label_sandwich_amount.text()) - 1
                self.label_sandwich_amount.setText(str(sandwich_amount))
        else:
            if int(self.label_water_amount.text()) == 0:
                pass
            else:
                water_amount = int(self.label_water_amount.text()) - 1
                self.label_water_amount.setText(str(water_amount))

    def clear(self) -> None:
        '''
        Method which restores all values in the program to their default values
        '''
        self.label_cookie_amount.setText('0')
        self.label_sandwich_amount.setText('0')
        self.label_water_amount.setText('0')
        self.label_output.setText('Please Enter Your Order')

    def calculate(self) -> None:
        '''
        Method which takes all values stored for items in the GUI and
        calculates the price of the items when put together
        '''
        cookie = int(self.label_cookie_amount.text())
        cookie_total = cookie * 1.5
        sandwich = int(self.label_sandwich_amount.text())
        sandwich_total = sandwich * 4
        water = int(self.label_water_amount.text())
        water_total = water * 1
        total = cookie_total + sandwich_total + water_total
        self.label_output.setText(f'-------------------------\n'
                                  f'({cookie}) - Cookie(s) = ${cookie_total:.2f}\n'
                                  f'({sandwich}) - Sandwich(es) = ${sandwich_total:.2f}\n'
                                  f'({water}) - Water(s) = ${water_total:.2f}\n'
                                  f'-------------------------\n'
                                  f'GRAND TOTAL = ${total:.2f}\n'
                                  f'-------------------------')
