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

# Create 10x10 QGraphicsRectItems (10x10 squares)
for i in range(10):
    for j in range(10):
        square = QGraphicsRectItem(i * 30, j * 30, 30, 30)  # (x, y, width, height) # Create a QGraphicsRectItem (a square)
        square.setBrush(QColor(255, 0, 0)) # Set the square's color (red)
        scene.addItem(square) # Add the square to the scene

# Set the scene for the view
view.setScene(scene)
# Show the view
view.show()

# Start the event loop.
app.exec()




