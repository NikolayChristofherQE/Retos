import sys
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QPainterPath, QPen, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, QMenu, QAction, QToolBar, QToolButton

class DrawingScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mode = "rect"
        self.item = None
        self.start = QPointF()X     #¡Como puedo mejorarlo linea 11?  
        self.end = QPointF()

    def mousePressEvent(self, event):
        self.start = self.end = event.scenePos()
        if self.item:
            self.removeItem(self.item)
        if self.mode == "rect":
            self.item = QGraphicsRectItem(QRectF(self.start, self.end))
        elif self.mode == "ellipse":
            self.item = QGraphicsEllipseItem(QRectF(self.start, self.end))
        elif self.mode == "line":
            self.item = QGraphicsLineItem(QLineF(self.start, self.end))
        elif self.mode == "polygon":
            self.item = QGraphicsPolygonItem(QPolygonF([self.start, self.end]))
        if self.item:
            self.addItem(self.item)

    def mouseMoveEvent(self, event):
        self.end = event.scenePos()
        if self.item:
            if self.mode == "rect":
                self.item.setRect(QRectF(self.start, self.end))
            elif self.mode == "ellipse":
                self.item.setRect(QRectF(self.start, self.end).normalized())
            elif self.mode == "line":
                self.item.setLine(QLineF(self.start, self.end))
            elif self.mode == "polygon":
                path = self.item.graphicsPath()
                path.closeSubpath()
                path.moveTo(self.end)
                path.lineTo(self.start)
                self.item.setPath(path)

class DrawingView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = DrawingScene(self)
        self.setScene(self.scene)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("QGraphicsView { border-image: url(:/img/drawing.png) 0 0 0 0 stretch stretch; }")

        self.setRenderHints(QPainter.Antialiasing | QPainter.QualityHints)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

        self.toolBar = QToolBar(self)
        self.addToolBar(self.toolBar)

        self.rectAction = QAction("Rectangle", self)
        self.rectAction.setCheckable(True)
        self.rectAction.setChecked(True)
        self.rectAction.triggered.connect(lambda: self.setMode("rect"))
        self.toolBar.addAction(self.rectAction)

        self.ellipseAction = QAction("Ellipse", self)
        self.ellipseAction.setCheckable(True)
        self.ellipseAction.triggered.connect(lambda: self.setMode("ellipse"))
        self.toolBar.addAction(self.ellipseAction)

        self.lineAction = QAction("Line", self)
        self.lineAction.setCheckable(True)
        self.lineAction.triggered.connect(lambda: self.setMode("line"))
        self.toolBar.addAction(self.lineAction)

        self.polygonAction = QAction("Polygon", self)
        self.polygonAction.setCheckable(True)
        self.polygonAction.triggered.connect(lambda: self.setMode("polygon"))
        self.toolBar.addAction(self.polygonAction)

    def setMode(self, mode):
        self.scene.mode = mode
        for action in (self.rectAction, self.ellipseAction, self.lineAction, self.polygonAction):
            action.setChecked(action.text() == mode)

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = DrawingView(self)
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    app.setApplicationName("Drawing App")
    app.setWindowIcon(QIcon(":/img/icon.png"))
    window = DrawingApp()
    window.setWindowTitle("Drawing App")
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())