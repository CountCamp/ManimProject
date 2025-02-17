from manim import (
    MovingCameraScene,
    NumberPlane,
    NumberLine,
    Create,
    GREY,
    GOLD_A,
    DEGREES,
    UP,
)


class MeanCalc01(MovingCameraScene):
    def construct(self):
        # 1) Background grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.8,
            },
        )
        self.add(grid)

        # 2) Make a horizontal NumberLine from 0..5.5
        axis = NumberLine(
            x_range=[0, 5.5, 1],
            include_numbers=True,
            label_direction=UP,  # "Above" in local coords
            color=GOLD_A,
        )

        # Rotate 90° around value=0 => vertical in scene
        zero_local = axis.n2p(0)
        axis.rotate(90 * DEGREES, about_point=zero_local)

        # Shift so "0" is at (-6, 0) in scene coords
        current_zero_scene = axis.n2p(0)
        shift_vec = [-6 - current_zero_scene[0], 0 - current_zero_scene[1], 0]
        axis.shift(shift_vec)

        # 3) Rotate each label horizontally
        #    (in Manim 0.19, we use axis.numbers instead of axis.label_items)
        for label_mob in axis.numbers:
            label_mob.rotate(-90 * DEGREES, about_point=label_mob.get_center())

        # Animate creation
        self.play(Create(axis))
        self.wait(1)

        # 4) (Optional) Move & zoom camera
        self.play(self.camera.frame.animate.move_to(axis.n2p(0)).scale(2), run_time=3)
        self.wait(2)
