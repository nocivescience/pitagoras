from manim import *
class PitagorasScene(Scene):
    def construct(self):
        tripes=[
            [3,4,5],
            [5,12,13],
            [8,15,17],
            [7,24,25],
            [20,21,29],
            [12,35,37],
            [9,40,41],
            [28,45,53],
            [11,60,61],
            [16,63,65],
            [33,56,65],
            [48,55,73],
            [13,84,85],
            [36,77,85],
            [39,80,89],
            [65,72,97],
            [20,99,101],
            [60,91,109],
            [15,112,113],
            [44,117,125],
            [88,105,137],
        ]
        for tripe in tripes[:5]:
            triangle=Polygon(
                ORIGIN,
                ORIGIN+tripe[0]*RIGHT,
                ORIGIN+tripe[0]*RIGHT+tripe[1]*UP,
                stroke_width=2,
            ).set_color(WHITE)
            line_hipo=Line(
                ORIGIN,
                ORIGIN+tripe[0]*RIGHT+tripe[1]*UP,
            ).fade(1)
            elbow=VMobject().set_points_as_corners(
                [LEFT, LEFT+UP, UP]
            )
            elbow.set_height(0.05*triangle.get_height())
            elbow.move_to(triangle.get_corner(DR),DR)
            square=Square(side_length=1)
            side_color=[
                BLUE,
                GREEN,
                RED,
            ]
            square_groups=VGroup()
            for i in range(3):
                square_group=VGroup(*[
                    square.copy().set_color(side_color[i]).shift(x*RIGHT+y*UP)
                    for x in range(tripe[i])
                    for y in range(tripe[i])
                ])
                square_groups.add(square_group)
            group_a, group_b, group_c=square_groups
            group_a.move_to(triangle.get_bottom(), UP)
            group_b.move_to(triangle.get_right(), LEFT)
            group_c.move_to(line_hipo.get_center(), DOWN)
            group_c.rotate(line_hipo.get_angle(), about_point=line_hipo.get_center())
            triangle.add(square_groups)
            triangle.add(elbow)
            triangle.scale(0.5)
            triangle.center()
            triangle.set(height=config['frame_height']-1)
            self.play(FadeIn(triangle[0][0], shift=UP),run_time=.5)
            self.wait(0.5)
            self.play(FadeOut(triangle[0][0], shift=UP), run_time=0.5)
            self.wait(.5)