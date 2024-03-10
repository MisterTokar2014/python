import arcade
class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > 800:
            self.change_x = - self.change_x
        elif self.left < 0:
            self.change_x = - self.change_x
class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("C:/Users/ирина/PycharmProjects/pythonProject73/ball.png", 0.1)
        self.ball.center_x = 400
        self.ball.center_y = 300
        self.ball.change_x = 5

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((111, 238, 206))
        self.ball.draw()

    def on_update(self, delta_time: float):
        self.ball.update()


window = GameWindow(800, 600, "Пинг-понг")
arcade.run()
