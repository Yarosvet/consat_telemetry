from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main_window.ui', self)