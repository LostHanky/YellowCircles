import random
import sys

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsView, QVBoxLayout, QMainWindow, QGraphicsScene, \
    QGraphicsEllipseItem


class UI_MainWindow(QWidget):
    def setupUI(self, MainWindow):
        MainWindow.resize(600, 500)
        self.centralwidget = QWidget(MainWindow)
        self.graficsView = QGraphicsView(self.centralwidget)
        self.dButton = QPushButton("Рисовать", self.centralwidget)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.addWidget(self.graficsView)
        self.layout.addWidget(self.dButton)
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setupUI(self)
        self.scene = QGraphicsScene()
        self.ui.graficsView.setScene(self.scene)
        self.ui.dButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        d = random.randint(20, 150)
        vert = self.ui.graficsView.height()
        hor = vert = self.ui.graficsView.width()
        x = random.randint(d, max(d, hor - d))
        y = random.randint(d, max(d, vert - d))
        ellipse = QGraphicsEllipseItem(x, y, d, d)
        color = QColor(
            #random.randint(50, 255),
            #random.randint(50, 255),
            #random.randint(50, 255),
            255, 255, 0
        )
        ellipse.setPen(color)
        ellipse.setBrush(color)

        self.scene.addItem(ellipse)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())