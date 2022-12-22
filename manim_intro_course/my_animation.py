from manim import *

class Pauses(Scene):
    def small_pause(self, n=0.5):
        self.wait(n)

    def pause(self, n=1.5):
        self.wait(n)
    
    def medium_pause(self, n=3):
        self.wait(n)

    def long_pause(self, n=5):
        self.wait(n)


class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(GrowFromCenter(circle))
        self.wait()

class Example(Scene):
    def construct(self):
        s = Square()
        t = Triangle()
        c = Circle()
        text = Text("Hello, world!", color=BLUE)

        self.add(s) # Add square
        self.wait() # 1s pause (default)

        self.add(t, c) # Add triangle and circle
        self.wait(2) # 2s pause (default)

        self.add(text) # Add text

        self.remove(c) # Remove circle

        self.wait(0.5) # 0.5s pause

