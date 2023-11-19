from Snake.BodyPart import BodyPart


class Snake:

    bodyParts = []

    #hinzufuegen von 3 koerperteile der schlange
    def __init__(self):
        body_part_to_add1 = BodyPart(4, 2)
        self.bodyParts.append(body_part_to_add1)

        body_part_to_add2 = BodyPart(3, 2)
        self.bodyParts.append(body_part_to_add2)

        body_part_to_add3 = BodyPart(2, 2)
        self.bodyParts.append(body_part_to_add3)

    # fuer dich noch nicht interessant
    def add_bodypart(self, x, y, direction):
        body_part_to_add = BodyPart(x, y)

        xforward = 0
        yforward = 0

        if direction == "up":
            yforward = 1
        if direction == "down":
            yforward = -1
        if direction == "left":
            xforward = 1
        if direction == "right":
            xforward = -1

        body_part_to_add.x = self.bodyParts[-1].x + xforward
        body_part_to_add.y = self.bodyParts[-1].y + yforward

        self.bodyParts.append(body_part_to_add)

    def move_snake(self, direction):

        xforward = 0
        yforward = 0

        if direction == "up":
            yforward = -1
        if direction == "down":
            yforward = 1
        if direction == "left":
            xforward = -1
        if direction == "right":
            xforward = 1


        length_of_bodypart = len(self.bodyParts)

        # schlange von letzten koerperteil durch gehen bis zum zweiten teil
        # iteriertes koperteil erhaelt position von seinen nachfolger
        # bzw bodyParts[2] kriegt dann die werte von bodyParts[1]
        for x in reversed(range(1, 3)):
            current_bodypart = self.bodyParts[x]
            predecessor = self.bodyParts[x-1]

            current_bodypart.x = predecessor.x
            current_bodypart.y = predecessor.y

        self.bodyParts[0].x += xforward
        self.bodyParts[0].y += yforward
