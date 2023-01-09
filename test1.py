import sys
from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QLabel, QMainWindow, QCheckBox


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
 
    def setupUI(self):
        self.setWindowTitle('Заказ в Макдональдсе')
        self.setGeometry(300, 200, 800, 600)

        self.check_box_1 = QCheckBox(self)
        self.check_box_1.move(10, 10)
        self.check_box_2 = QCheckBox(self)
        self.check_box_2.move(10, 40)
        self.check_box_3 = QCheckBox(self)
        self.check_box_3.move(10, 70)
        self.check_box_4 = QCheckBox(self)
        self.check_box_4.move(10, 100)

        self.lable_1 = QLabel('Чизбургер', self)
        self.lable_1.move(40, 10)
        self.lable_2 = QLabel('Гамбургер', self)
        self.lable_2.move(40, 40)
        self.lable_3 = QLabel('Кока-кола', self)
        self.lable_3.move(40, 70)
        self.lable_4 = QLabel('Нагетсы', self)
        self.lable_4.move(40, 100)
        
        self.plain = QPlainTextEdit(self)
        self.plain.resize(200, 200)
        self.plain.move(10, 150)
        self.plain.setReadOnly(True)

        self.check_box_1.stateChanged.connect(self.run)
        self.check_box_2.stateChanged.connect(self.run)
        self.check_box_3.stateChanged.connect(self.run)
        self.check_box_4.stateChanged.connect(self.run)
    
    def run(self):
        
        self.plain.setPlainText('Ваш заказ:\n')
        if self.sender() is self.check_box_1:
            self.plain.appendPlainText('\nЧизбургер\n')
        elif self.sender() is self.check_box_2:
            self.plain.appendPlainText('\nГамбургер\n')
        elif self.sender() is self.check_box_3:
            self.plain.appendPlainText('\nКока-кола\n')
        elif self.sender() is self.check_box_4:
            self.plain.appendPlainText('\nНагетсы\n')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
