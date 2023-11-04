from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem
# QTimer^^
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

square_size = 30
num_squares = 10
snake_body = 10
snake_list = []

def create_snake():
    for i in range(snake_body):
        x = i * square_size
        square_snake = QGraphicsRectItem(x, 0, 30, 30)
        square_snake.setBrush(QColor(0, 0, 255))
        scene.addItem(square_snake)
        snake_list.append(square_snake)

def move_snake():
    while len(snake_list) < 1:
        scene.removeItem(snake_list.pop(0))

    head = snake_list[-1]
    new_x = head.x() + square_size
    new_y = head.y()
    new_square = QGraphicsRectItem(new_x, new_y, 30, 30)
    new_square.setBrush(QColor(0,0,255))
    scene.addItem(new_square)
    snake_list.append(new_square)

    tail = snake_list[0]
    scene.removeItem(tail)
    snake_list.pop(0)

create_snake()
move_snake()



#snake =[]
#snake_squares = 30
#initial_length = 10

#for s in range(initial_length):
#    snake_body = QGraphicsRectItem(s * snake_squares, 0, snake_squares,snake_squares)
#    snake_body.setBrush(QColor(0, 0, 255))
#    scene.addItem(snake_body)
#    snake.append(snake_body)

#def update_snake():
#    head = snake[0]
#    new_x= head.x() + snake_squares
#    new_y= head.y()
#    new_head = QGraphicsRectItem(new_x, new_y, snake_squares,snake_squares)
#    new_head.setBrush(QColor(0, 0, 255))
#    scene.addItem(new_head)
#    snake.append(new_head)

#    old_tail = snake[0]
#    scene.removeItem(old_tail)
#    snake.pop(0)

#timer = QTimer()
#timer.timeout.connect(update_snake)
#timer.start(100)



# Set the scene for the view
view.setScene(scene)
# Show the view
view.show()

# Start the event loop.
app.exec()




