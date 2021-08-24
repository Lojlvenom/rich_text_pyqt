import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class RTE(QMainWindow):

    def __init__(self):
        super(RTE,self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)


app = QApplication(sys.argv)
window = RTE()
window.show()

sys.exit(app.exec_())
