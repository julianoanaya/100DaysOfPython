from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.write(f"Score = {self.score}", False, "center", ("Arial", 24, "normal"))
        # self.refresh_score()
