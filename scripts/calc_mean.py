from manim import MovingCameraScene, NumberPlane, NumberLine, Create, GREY, GOLD_A


class MeanCalc(MovingCameraScene):
    def construct(self):
        # 1) Optional: a background grid
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

        # 2) Make a NumberLine from 0..5.5
        axis = NumberLine(
            x_range=[0, 5.5, 1],  # ticks at 0, 1, 2, 3, 4, 5
            include_numbers=True,
            color=GOLD_A,
        )

        # 3) Put the "start" (value=0) at (x=-6, y=-2),
        #    and the "end" (value=5.5) at (x=-6, y=3), for a total length of 5 scene-units.
        axis.put_start_and_end_on(
            [-6, 0, 0],  # scene coords for value=0
            [-6, 5.5, 0],  # scene coords for value=5.5
        )

        # (Optional) color the numbers
        for number in axis.numbers:
            number.set_color(GOLD_A)

        # 4) Animate
        self.play(Create(axis))
        self.wait(1)

        # 5) If you want to zoom out the camera:
        self.play(self.camera.frame.animate.scale(2), run_time=3)
        self.wait(2)
