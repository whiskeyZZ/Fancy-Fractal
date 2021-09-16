from turtle import *
from colors import Color


class Fractal:

    def build_tree(self, t, branch_length, shorten_by, angle, direction):
        match direction:
            case "Normal":
                turn_one = t.left
                turn_two = t.right
            case "Mirror":
                turn_one = t.right
                turn_two = t.left
        if branch_length > 5:
            speed = Color.get_speed(Color)
            t.speed(speed)
            t.forward(branch_length)
            new_length = branch_length - shorten_by
            #t.left(angle)
            turn_one(angle)
            self.build_tree(t, new_length, shorten_by, angle, direction)
            #t.right(angle * 2)
            turn_two(angle * 2)
            self.build_tree(t, new_length, shorten_by, angle, direction)
            #t.left(angle)
            turn_one(angle)
            t.backward(branch_length)

    def tree(self, t, color, fancy_1, fancy_2, fancy_3, direction):
        t.setheading(90)
        t.color(color[1])
        self.build_tree(t, fancy_1, fancy_3, fancy_2, direction)

    def koch_curve(self, t, iterations, length, shortening_factor, angle, direction):
        speed = Color.get_speed(Color)
        t.speed(speed)
        match direction:
            case "Normal":
                turn_one = t.left
                turn_two = t.right
            case "Mirror":
                turn_one = t.right
                turn_two = t.left
        if iterations <= 0:
            t.forward(length)
        else:
            iterations = iterations - 1
            length = length / shortening_factor
            self.koch_curve(t, iterations, length, shortening_factor, angle, direction)
            #t.left(angle)
            turn_one(angle)
            self.koch_curve(t, iterations, length, shortening_factor, angle, direction)
            #t.right(angle * 2)
            turn_two(angle * 2)
            self.koch_curve(t, iterations, length, shortening_factor, angle, direction)
            #t.left(angle)
            turn_one(angle)
            self.koch_curve(t, iterations, length, shortening_factor, angle, direction)
    
    def koch(self, t, color, iterations, length, shortening_factor, direction):
        t.color(color[1])
        for i in range(3):
            self.koch_curve(t, iterations, length, shortening_factor, 60, direction)
            t.right(120)

    def polygon(self, t, color, sides, side_len, offset, direction):
        t.color(color[1])
        speed = Color.get_speed(Color)
        t.speed(speed)
        match direction:
            case "Normal":
                turn_one = t.left
                turn_two = t.right
            case "Mirror":
                turn_one = t.right
                turn_two = t.left
        for i in range(0, int(sides)):
            t.forward(side_len)
            turn_one(360/sides)
        if side_len > 0:
            turn_one(offset)
            self.polygon(t, color, sides, side_len-1, offset, direction)