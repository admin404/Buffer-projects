import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class main():
    def __init__(self):
        super(main, self).__init__()
        
        wid = widget()

class widget():
    def __init__(self):
        super(widget,self).__init__()
        self.init()
        
    def init(self):
        self.button = QPushButton()
        self.button.setText("Press Me")
        
        layout = QGridLayout(self)
        layout.addWidget(self.buutton)
        
if __name__ == "__main__":
    app = QApplicaion(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
