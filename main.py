from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem

# Only needed for access to command line arguments
import sys

from PyQt6.uic.properties import QtGui
from PyQt6.uic.uiparser import QtWidgets

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a QGraphicsView
view = QGraphicsView()
view.setFixedSize(1920, 1080)

# Create a QGraphicsScene
scene = QGraphicsScene()

# Create a QGraphicsRectItem (a square)
square = QGraphicsRectItem(0, 0, 100, 100)  # (x, y, width, height)

# Set the square's color (red)
square.setBrush(QColor(255, 0, 0))

# Add the square to the scene
scene.addItem(square)

# Set the scene for the view
view.setScene(scene)

# Show the view
view.show()

# Start the event loop.
app.exec()

