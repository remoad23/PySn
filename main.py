from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem
import sys
from Snake.Snake import Snake


app = QApplication(sys.argv)

# Create a QGraphicsView
view = QGraphicsView()
view.setFixedSize(1920, 1080)

# Create a QGraphicsScene
scene = QGraphicsScene()

# bloecke spielfeld
squarematrix = []

timer = QTimer()

# die schlange
snake = Snake()

# hier wird die schlange grafisch bewegt
def update_snake():
    # letzter block des letzten koerpreteil kriegt die farbe des spielfeldes
    # alle anderen bloecke (ausser der erste, weil der neu berechnet wird) erhalten die koordinaten des nachfolgers und
    # muessen deswegen nicht gefaerbt werden
    last_bodypart = snake.bodyParts[-1]

    square_of_last_bodypart = squarematrix[last_bodypart.x][last_bodypart.y]

    square_of_last_bodypart.setBrush(QColor(255, 0, 0))

    # hier werden die werte der schlange veraendert
    snake.move_snake("down")

    # erste koerperteil wurde ab hier bewegt und neue position erhaelt rote farbe
    first_bodypart = snake.bodyParts[0]

    square_of_first_bodypart = squarematrix[first_bodypart.x][first_bodypart.y]

    square_of_first_bodypart.setBrush(QColor(0, 255, 0))


# Matrix (spielfeld) erstellen
for i in range(10):
    squares = []
    for j in range(10):
        # (x, y, width, height)
        square = QGraphicsRectItem(i * 100, j * 100, 100, 100)
        # Set the square's color (red)
        square.setBrush(QColor(255, 0, 0))
        squares.append(square)
        # Add the square to the scene
        scene.addItem(square)

    squarematrix.append(squares)

# schlange zu matrix hinzufuegen zum start
for bodypart in snake.bodyParts:
    square_to_brush = squarematrix[bodypart.x][bodypart.y]
    square_to_brush.setBrush(QColor(0, 255, 0))


timer.timeout.connect(update_snake)
timer.start(500)

# Set the scene for the view
view.setScene(scene)
# Show the view
view.show()

# Start the event loop.
app.exec()




