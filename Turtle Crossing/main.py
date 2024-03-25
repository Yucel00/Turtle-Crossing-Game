import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
car_manager=CarManager()
score=Scoreboard()


screen.onkey(player.up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.all_cars:
        if car.distance(player)<25:
            game_is_on=False
            score.game_over()

    if player.level_up_control():

        player.go_to_start()
        car_manager.level_up()
        score.level_score()

screen.exitonclick()
