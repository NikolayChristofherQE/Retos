import sys
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsLineItem, QGraphicsTextItem, QMainWindow

class DiagramScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(DiagramScene, self).__init__(parent)
        self.setSceneRect(0, 0, 800, 600)
        self.setBackgroundBrush(QBrush(QColor(255, 255, 255)))

        # Add a rectangle
        rect = QGraphicsRectItem(0, 0, 100, 50)
        rect.setBrush(QBrush(QColor(255, 0, 0)))
        self.addItem(rect)

        # Add a polygon
        polygon = QGraphicsPolygonItem(QPolygonF([QPointF(150, 0), QPointF(200, 50), QPointF(250, 0), QPointF(200, -50)]))
        polygon.setBrush(QBrush(QColor(0, 255, 0)))
        self.addItem(polygon)

        # Add a line
        line = QGraphicsLineItem(QLineF(300, 0, 400, 50))
        line.setPen(QPen(QColor(0, 0, 255), 2))
        self.addItem(line)

        # Add a text
        text = QGraphicsTextItem("Hello, PyQt5!")
        text.setPos(500, 0)
        text.setDefaultTextColor(QColor(0, 0, 0))
        self.addItem(text)

classMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        scene = DiagramScene(self)
        view = QGraphicsView(scene, self)
        self.setCentralWidget(view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())