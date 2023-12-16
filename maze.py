import os
import random
import readchar

# Definir las constantes
MAP_WIDTH = 19
MAP_HEIGHT = 11
OBSTACLES_COUNT = 10


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Map:
    def __init__(self):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        self.point = Point((self.width - 2) // 2, (self.height - 2) // 2)
        self.tail = []
        self.obstacles = []
        while len(self.obstacles) < OBSTACLES_COUNT:
            new_obstacle = Point(
                random.randint(1, self.width - 2), random.randint(1, self.height - 2)
            )
            if not any(
                obstacle.x == new_obstacle.x and obstacle.y == new_obstacle.y
                for obstacle in self.obstacles
            ):
                self.obstacles.append(new_obstacle)

    def move_point(self, dx, dy):
        self.tail.insert(0, Point(self.point.x, self.point.y))
        new_x = (self.point.x + dx) % (self.width - 1)
        new_y = (self.point.y + dy) % (self.height - 1)
        if 0 <= new_x < self.width - 1 and 0 <= new_y < self.height - 1:
            self.point.x = new_x
            self.point.y = new_y
        for obstacle in self.obstacles:
            if obstacle.x == self.point.x and obstacle.y == self.point.y:
                self.obstacles.remove(obstacle)
                new_obstacle = Point(
                    random.randint(1, self.width - 2),
                    random.randint(1, self.height - 2),
                )
                while (
                    any(
                        obstacle.x == new_obstacle.x and obstacle.y == new_obstacle.y
                        for obstacle in self.obstacles
                    )
                    or new_obstacle.x == self.point.x
                    and new_obstacle.y == self.point.y
                ):
                    new_obstacle = Point(
                        random.randint(1, self.width - 2),
                        random.randint(1, self.height - 2),
                    )
                self.obstacles.append(new_obstacle)
                break
        else:
            self.tail.pop()

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1:
                    print("|", end="")
                elif y == 0 or y == self.height - 1:
                    print("-", end="")
                elif any(
                    obstacle.x == x - 1 and obstacle.y == y - 1
                    for obstacle in self.obstacles
                ):
                    print("O", end="")
                elif any(tail.x + 1 == x and tail.y + 1 == y for tail in self.tail):
                    print("*", end="")
                elif self.point.x + 1 == x and self.point.y + 1 == y:
                    print("@", end="")
                else:
                    print(" ", end="")
            print()


def main():
    game_map = Map()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        game_map.draw()
        print("Enter your movement (w/a/s/d) or press 'q' to quit: ")
        movement = readchar.readchar()
        if movement == "w":
            game_map.move_point(0, -1)
        elif movement == "a":
            game_map.move_point(-1, 0)
        elif movement == "s":
            game_map.move_point(0, 1)
        elif movement == "d":
            game_map.move_point(1, 0)
        elif movement.lower() == "q":
            break


if __name__ == "__main__":
    main()
