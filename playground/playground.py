from manim import *

# Cmd+B goes to the definition of an object in the source code.

# export PATH=$PATH:/Users/martynas/.pyenv/versions/3.9.5/envs/manim_env -- addition of this line to .zprofile allows
# to call manim with "manim -pql playground.py" instead of "python -m manim -pql playground.py"

class Playground(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen