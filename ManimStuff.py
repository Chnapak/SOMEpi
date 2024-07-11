from manim import *

class Intro(Scene):
    def construct(self):
        # Set the area for all shapes
        area = 4  # for example, all shapes will have an area of 4 square units

        # Colors for each shape
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, TEAL, PINK, GOLD, MAROON]

        # Create the shapes with same opacity and border color
        square = Square(side_length=np.sqrt(area)).set_fill(colors[0], opacity=0.5).set_stroke(WHITE)
        rectangle = Rectangle(width=4, height=1).set_fill(colors[1], opacity=0.5).set_stroke(WHITE)
        equilateral_triangle = RegularPolygon(n=3).scale(np.sqrt(area) / np.sqrt((3 * np.sqrt(3)) / 4)).set_fill(colors[2], opacity=0.5).set_stroke(WHITE)
        isosceles_triangle = Polygon(
            [0, 2 * np.sqrt(area / 2), 0], [1, 0, 0], [-1, 0, 0]
        ).set_fill(colors[3], opacity=0.5).set_stroke(WHITE)
        irregular_triangle = Polygon(
            [0.5, np.sqrt(area * 2 / 1.75), 0], [1.5, 0, 0], [-1, 0, 0]
        ).set_fill(colors[4], opacity=0.5).set_stroke(WHITE)
        rhombus = Polygon(
            [0, 1, 0], [2, 0, 0], [0, -1, 0], [-2, 0, 0]
        ).set_fill(colors[5], opacity=0.5).set_stroke(WHITE)
        parallelogram = Polygon(
            [3, 1, 0], [2, 0, 0], [-2, 0, 0], [-1, 1, 0]
        ).set_fill(colors[6], opacity=0.5).set_stroke(WHITE)
        trapezoid = Polygon(
            [1, 1, 0], [2, 0, 0], [-2, 0, 0], [-1, 1, 0]
        ).set_fill(colors[7], opacity=0.5).set_stroke(WHITE)
        kite = Polygon(
            [0, 2, 0], [1.5, 0, 0], [0, -2, 0], [-1.5, 0, 0]
        ).set_fill(colors[8], opacity=0.5).set_stroke(WHITE)
        irregular_quadrilateral = Polygon(
            [1.5, 1, 0], [1, 0, 0], [-2, 0, 0], [-1, 1, 0]
        ).set_fill(colors[9], opacity=0.5).set_stroke(WHITE)
        right_triangle = Polygon(
            [0, 2, 0], [0, 0, 0], [2, 0, 0]
        ).set_fill(WHITE, opacity=0.5).set_stroke(WHITE)

        # Formulas for each shape
        formulas = [
            MathTex("s^2").next_to(square, DOWN),
            MathTex("w \\cdot h").next_to(rectangle, DOWN),
            MathTex("\\frac{\\sqrt{3}}{4} a^2").next_to(equilateral_triangle, DOWN),
            MathTex("\\frac{1}{2} b \\cdot h").next_to(isosceles_triangle, DOWN),
            MathTex("\\frac{1}{2} b \\cdot h").next_to(irregular_triangle, DOWN),
            MathTex("\\frac{1}{2} d_1 \\cdot d_2").next_to(rhombus, DOWN),
            MathTex("b \\cdot h").next_to(parallelogram, DOWN),
            MathTex("\\frac{1}{2} (b_1 + b_2) \\cdot h").next_to(trapezoid, DOWN),
            MathTex("\\frac{1}{2} d_1 \\cdot d_2").next_to(kite, DOWN),
            MathTex("\\frac{1}{2} d \\cdot (h_1+h_2)").next_to(irregular_quadrilateral, DOWN),
            MathTex("\\frac{1}{2} b \\cdot h").next_to(right_triangle, DOWN)
        ]

        # List of shapes
        shapes = [square, rectangle, equilateral_triangle, isosceles_triangle,
                  irregular_triangle, rhombus, parallelogram, trapezoid, kite,
                  irregular_quadrilateral]

        # Initial shape
        current_shape = square
        current_formula = formulas[0]
        self.play(Create(current_shape), Write(current_formula))
        self.wait(1)

        # Transform shapes without turning them around
        for i, shape in enumerate(shapes[1:]):
            shape.move_to(current_shape.get_center())
            next_formula = formulas[i+1]
            next_formula.next_to(shape, DOWN)
            self.play(Transform(current_shape, shape), Transform(current_formula, next_formula))
            self.wait(1)

        # Pause before transforming into the right triangle
        self.wait(2)
        right_triangle.move_to(current_shape.get_center())
        next_formula = formulas[-1]
        next_formula.next_to(right_triangle, DOWN)
        self.play(Transform(current_shape, right_triangle), Transform(current_formula, next_formula))
        self.wait(2)

        # Transform the final shape into a square
        final_square = Square(side_length=np.sqrt(area)).set_fill(colors[0], opacity=0.5).set_stroke(WHITE)
        final_square.move_to(current_shape.get_center())
        final_formula = MathTex("s^2").next_to(final_square, DOWN)
        self.play(Transform(current_shape, final_square), Transform(current_formula, final_formula))
        self.wait(2)

# To run the script, save this as a Python file and execute it using the Manim command:
# manim -pql filename.py TransformShapes

class GroundRules(Scene):
    def construct(self):

        irregular_quadrilateral = Polygon(
            [1.5, 1, 0], [1, 0, 0], [-2, 0, 0], [-1, 1, 0]
        ).set_fill(MAROON, opacity=0.5).set_stroke(WHITE)
        
        part_1 = Polygon(
            [1.5, 1, 0], [1, 0, 0], [-2, 0, 0]
        ).set_fill(MAROON_A, opacity=0.5).set_stroke(WHITE)
        part_2 = Polygon(
            [1.5, 1, 0], [-2, 0, 0], [-1, 1, 0]
        ).set_fill(MAROON_B, opacity=0.5).set_stroke(WHITE)



        rectangle_grid = Polygon(
            [1.5, 1, 0], [1.5, 0, 0], [-1, 0, 0], [-1, 1, 0]
        ).set_stroke(WHITE)
        triangle_grid = Polygon(
            [1.5, 1, 0], [1.5, 0, 0], [-1, 0, 0]
        ).set_stroke(WHITE)
        square_grid = Square(
            1
        ).set_stroke(WHITE)

        rectangle_grid.move_to([0,-1,0])
        triangle_grid.next_to(rectangle_grid, LEFT)
        square_grid.next_to(rectangle_grid, RIGHT)

        self.wait(2)
        self.play(FadeIn(irregular_quadrilateral))
        self.wait(1)
        self.play(FadeOut(irregular_quadrilateral), FadeIn(part_1, part_2))
        self.wait(1)
        self.play(FadeIn(rectangle_grid, triangle_grid, square_grid))
        self.wait(1)
        self.play(FadeOut(part_1,part_2,rectangle_grid, triangle_grid, square_grid))
        self.wait(1)
        return super().construct()

class RightTriangle(Scene):
    def construct(self):
        
        square = Square(2).set_fill(RED, opacity=0.5).set_stroke(WHITE)
        rectangle = Rectangle(width=6, height=2).set_fill(GREEN, opacity=0.5).set_stroke(WHITE)
        square.move_to([0,2,0])
        rectangle.move_to([0,-2,0])

        formula_square = MathTex("A = a^2").move_to(square)
        formula_rectangle = MathTex("A = a\\cdot b").move_to(rectangle)
        center_square = Dot().move_to(square)
        center_rectangle = Dot().move_to(rectangle)
        line_square = Line([-0.5,3,0],[0.5,1,0])
        line_rectangle = Line([2,-1,0],[-2,-3,0])

        split_square = Line([-1, 3, 0], [1, 1, 0])
        split_rectangle = Line([3, -1, 0], [-3, -3, 0])

        new_formula_s = MathTex("\\frac{1}{2}a^2", font_size=36).move_to(square, 200*DOWN).move_to(0.5*UP)
        new_formula_r = MathTex("A = \\frac{1}{2}a\\cdot b", font_size=36).move_to(rectangle, 200*UP).move_to(0.5*DOWN)
        self.wait(2)
        self.play(FadeIn(square, rectangle))
        self.wait(1)
        self.play(FadeIn(formula_square, formula_rectangle, runtime = 0.5))
        self.wait(1)
        self.play(FadeOut(formula_square, formula_rectangle, runtime = 0.5))
        self.wait(1)
        self.play(FadeIn(center_square, center_rectangle, runtime = 3))
        self.wait(1)
        self.play(FadeIn(line_square, line_rectangle, runtime = 3))
        self.wait(1)
        self.play(Transform(line_square, split_square), Transform(line_rectangle, split_rectangle))
        self.wait(1)
        self.play(FadeIn(new_formula_r, new_formula_s))
        self.wait(1)
        self.play(FadeOut(new_formula_r, new_formula_s, line_square, line_rectangle, center_square, center_rectangle, square, rectangle))
        return super().construct()

class EquilTriangle(Scene):
    def construct(self):
        a = 5 
        vertex1 = [-a / 2, -a * np.sqrt(3) / 6, 0] 
        vertex2 = [a / 2, -a * np.sqrt(3) / 6, 0]   
        vertex3 = [0, a * np.sqrt(3) / 3, 0]       

        equilTriangle = Polygon(vertex1, vertex2, vertex3)
        
        base_midpoint = [0, -a * np.sqrt(3) / 6, 0]
        midPoint = Dot(base_midpoint).set_color(WHITE)
        
        height = Line(base_midpoint, vertex3)
        
        base = Line(vertex2, vertex1)
        
        right_angle = Angle(line1=height, line2=base, dot=True)
        
        self.play(FadeIn(equilTriangle))
        self.wait(1)
        self.play(FadeIn(midPoint))
        self.wait(1)
        self.play(FadeIn(height))
        self.wait(1)
        self.play(FadeIn(right_angle))
        self.wait(1)

        triangle1 = Polygon(vertex1, base_midpoint, vertex3).set_fill(BLUE_B).set_opacity(0.5)
        triangle2 = Polygon(vertex2, vertex3, base_midpoint).set_fill(BLUE_A).set_opacity(0.5)
        triangle3 = Polygon(vertex1, base_midpoint, vertex3).set_fill(BLUE_A).set_opacity(0.5)


        self.play(FadeOut(equilTriangle, height, midPoint, right_angle), FadeIn(triangle1, triangle2))
        self.wait(1)
        self.play(FadeOut(triangle2), FadeIn(triangle3))
        self.wait(1)
        self.play(FadeOut(triangle1, triangle3))
        self.wait(1)
        trianglea = triangle1.move_to([0,0,0])
        triangleb = triangle3.move_to([0,0,0])

        self.play(FadeIn(triangleb, trianglea))
        self.wait(1)
        self.play(Rotate(triangleb,about_point=[0,0,0],angle=PI))
        self.wait(1)

        basef = MathTex("\\frac{1}{2} b ").move_to(3*UP)
        heightf = MathTex("h").move_to(2*RIGHT)
        area = MathTex("A = \\frac{1}{2}b \\cdot h").move_to([0,0,0])

        self.play(FadeIn(heightf, basef))
        self.wait(1)
        self.play(FadeOut(heightf, basef, trianglea, triangleb))
        self.wait(1)
        self.play(FadeIn(area))
        self.wait(1)
        self.play(FadeOut(area))
        self.wait(1)

        self.play(Create(equilTriangle), Create(midPoint), Create(height))
        self.wait(1)
        
        line = Line(base_midpoint, vertex3).set_color(RED)
        self.play(Create(line))
        self.wait(1)
        self.play(FadeOut(line))
        self.wait(1)

        side_a = MathTex("b").move_to([-2, 1, 0])
        side_a2 = MathTex("\\frac{1}{2}b").next_to(midPoint, LEFT+DOWN)

        self.play(Create(side_a), Create(side_a2))
        self.wait(1)
        self.play(FadeOut(side_a, side_a2, height, equilTriangle, midPoint))

        equation = MathTex("h^2 + (\\frac{1}{2}b)^2 = b^2")
        equation2 = MathTex("h^2=b^2-(\\frac{1}{2}b)^2")
        equation3 = MathTex("h^2=b^2-\\frac{1}{4}b^2")
        equation4 = MathTex("h^2=\\frac{3}{4}b^2")
        equation5 = MathTex("h=\\sqrt{\\frac{3}{4}b^2}")
        equation5 = MathTex("h=\\frac{\\sqrt{3}}{2}b")

        area2=MathTex("\\frac{1}{2}bh=\\frac{\\sqrt{3}}{4}b^2")
        areaF = MathTex("A=\\frac{\\sqrt{3}}{4}b^2")
        
        self.wait(1)
        self.play(Create(equation))
        self.wait(1)
        self.play(Transform(equation, equation2))
        self.wait(1)
        self.play(Transform(equation, equation3))
        self.wait(1)
        self.play(Transform(equation, equation4))
        self.wait(1)
        self.play(Transform(equation, equation5))
        self.wait(1)
        self.play(FadeOut(equation))
        self.wait(1)
        self.play(FadeIn(area2))
        self.wait(1)
        self.play(Transform(area2, areaF))
        self.wait(1)
        self.play(FadeOut(area2))
        self.wait(1)



class IrregularTriangle(Scene):
    def construct(self):
        
        self.wait(1)

        irregular_triangle = Polygon(
            [1, 1.5, 0], [5, -1.5, 0], [-5, -1.5, 0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE)
        
        base_red = Line([-5, -1.5, 0], [5, -1.5, 0]).set_color(RED)

        dassed_line_1 = DashedLine([1, 1.5, 0],[-8,8.25,0],dash_length=0.25)

        dassed_line_2 = DashedLine([1, 1.5, 0],[10,6,0],dash_length=0.25)

        dot_1 = Dot([-1.4, 3.3, 0], radius = 0.1)
        dot_2 = Dot([3, 2.5, 0], radius = 0.1)
        dot_3 = Dot([1, -1.5, 0], radius = 0.1)

        height_1 = Line([-1.4, 3.3, 0], [-5, -1.5, 0]).set_color(RED)
        height_2 = Line([3, 2.5, 0], [5, -1.5, 0]).set_color(RED)
        height_3 = Line([1, -1.5, 0] , [1, 1.5, 0])

        triangle_a = Polygon([1, -1.5, 0] , [1, 1.5, 0], [-5, -1.5, 0]).set_stroke(WHITE).set_color(RED).set_opacity(0.7)
        triangle_b = Polygon([1, -1.5, 0] , [1, 1.5, 0], [5, -1.5, 0]).set_stroke(WHITE).set_color(RED).set_opacity(0.7)

        midpoint_A = Dot([-2, -1.5, 0],radius = 0.075)
        midpoint_B = Dot([3, -1.5, 0],radius = 0.075)

        height_A = Line([-2, -1.5, 0], [-2, 0, 0])
        height_B = Line([3, -1.5, 0], [3, 0, 0])

        part_a = Polygon([-2, -1.5, 0], [-2, 0, 0], [-5, -1.5, 0]).set_stroke(WHITE).set_color(RED).set_opacity(0.5)
        part_b = Polygon([3, -1.5, 0], [3, 0, 0], [5, -1.5, 0]).set_stroke(WHITE).set_color(GREEN).set_opacity(0.5)
        part_C = Polygon([3, 0, 0], [3, -1.5, 0], [1, -1.5, 0], [1, 1.5, 0]).set_stroke(WHITE).set_color(YELLOW).set_opacity(0.5)
        part_D = Polygon([-2, 0, 0], [-2, -1.5, 0], [1, -1.5, 0], [1, 1.5, 0]).set_stroke(WHITE).set_color(ORANGE).set_opacity(0.5)

        axis_a = Dot([-2,0,0])
        axis_b = Dot([3,0,0])

        heightf = MathTex("h").move_to([3.5, 0,0])
        basef = MathTex("?").move_to([1,-2,0])

        b = MathTex("b").move_to([1,-2,0])

        x = MathTex("x").move_to([-2,-2.5,0])
        plus = MathTex("+").move_to([1,-2.5,0])
        y = MathTex("y").move_to([3,-2.5,0])

        x2 = MathTex("\\frac{1}{2}x").move_to([-2,-2.5,0])
        y2 = MathTex("\\frac{1}{2}y").move_to([3,-2.5,0])

        b2 = MathTex("\\frac{1}{2}(x+y)").move_to([1,-2.5,0])
        b3 = MathTex("\\frac{1}{2}b").move_to([1,-2.5,0])

        area = MathTex("A=\\frac{1}{2}bh")

        self.play(FadeIn(irregular_triangle))
        self.wait(1)
        self.play(Create(base_red))
        self.wait(1)
        self.play(Create(dassed_line_1), Create(dassed_line_2), runtime = 3)
        self.wait(1)
        self.play(DrawBorderThenFill(dot_1), DrawBorderThenFill(dot_2), DrawBorderThenFill(dot_3))
        self.wait(1)
        self.play(Create(height_1), Create(height_2), Create(height_3))
        self.wait(1)
        self.play(FadeOut(base_red, dot_1, dot_2, height_1, height_2, dassed_line_1, dassed_line_2), runtime=2)
        self.wait(1)
        self.play(DrawBorderThenFill(triangle_a))
        self.wait(1)
        self.play(DrawBorderThenFill(triangle_b), FadeOut(triangle_a))
        self.wait(1)
        self.play(FadeOut(triangle_b))
        self.wait(1)
        self.play(Create(midpoint_A), Create(midpoint_B))
        self.wait(1)
        self.play(Create(height_A), Create(height_B), runtime=1)
        self.wait(1)
        self.play(FadeOut(irregular_triangle, midpoint_A, midpoint_B, dot_3, height_3, height_A, height_B), FadeIn(part_a, part_b, part_C, part_D), runtime=1)
        self.wait(1)
        self.play(Create(axis_a), Create(axis_b))
        self.wait(1)
        self.play(Rotate(part_a, about_point= [-2,0,0], angle=-PI), Rotate(part_b, about_point= [3,0,0]), runtime=1)
        self.wait(1)
        self.play(Write(basef), Write(heightf))
        self.wait(1)
        self.play(FadeOut(basef, heightf))
        self.wait(1)
        self.play(Rotate(part_a, about_point= [-2,0,0], angle=PI), Rotate(part_b, about_point= [3,0,0], angle=-PI),  runtime=1)
        self.wait(1)
        self.play(FadeIn(b))
        self.wait(1)
        self.play(FadeOut(b), FadeIn(x, plus, y))
        self.wait(1)
        self.play(Rotate(part_a, about_point= [-2,0,0], angle=-PI), Rotate(part_b, about_point= [3,0,0]), runtime=1)
        self.wait(1)
        self.play(FadeOut(x, y), FadeIn(x2, y2))
        self.wait(1)
        self.play(FadeOut(x2, y2, plus), FadeIn(b2))
        self.wait(1)
        self.play(FadeOut(b2),FadeIn(b3, heightf))
        self.wait(1)
        self.play(FadeOut(axis_a, axis_b, part_a, part_b, part_C, part_D, b3, heightf))
        self.wait(1)
        self.play(Create(area))
        self.wait(1)
        self.play(FadeOut(area))
        self.wait(1)

class Parallelogram(Scene):
    def construct(self):
        parallelogram = Polygon(
            [-5, -2, 0], [1, -2, 0], [5, 2, 0], [-1, 2, 0]
        ).set_fill(TEAL, opacity=0.5).set_stroke(WHITE)

        rectangle_A = Polygon(
            [-1, 2, 0], [1, 2, 0], [1, -2, 0], [-1, -2, 0]
        ).set_fill(BLUE, opacity=0.7).set_stroke(RED, width=10)

        triangle_a = Polygon(
            [-5, -2, 0], [-1, 2, 0], [-1, -2, 0]
        ).set_fill(GREEN, opacity=0.7).set_stroke(RED, width=10)

        triangle_b = Polygon(
            [5, 2, 0], [1, -2, 0], [1, 2, 0]
        ).set_fill(GREEN, opacity=0.7).set_stroke(RED, width=10)

        triangle_A = Polygon(
            [1, -2, 0], [5, 2, 0], [5, -2, 0]
        ).set_fill(GREEN, opacity=0.7).set_stroke(RED)


        basef = MathTex("b").move_to([2,-3,0])
        heightf = MathTex("h").move_to([-2,0,0])
        areaf = MathTex("A=bh").move_to([-5,0,0])

        result = Polygon([5, 2, 0], [5, -2, 0], [-1, -2, 0], [-1, 2, 0]).set_fill(GREEN, opacity=0.7).set_stroke(RED)

        self.wait(1)
        self.play(Create(parallelogram))
        self.wait(1)
        self.play(ShowPassingFlash(rectangle_A), runtime = 3)
        self.wait(1)
        self.play(ShowPassingFlash(triangle_a), ShowPassingFlash(triangle_b), runtime = 3)
        self.wait(1)

        triangle_a.set_stroke(width=5)
        triangle_b.set_stroke(width=5)
        rectangle_A.set_stroke(width=5)


        self.play(FadeOut(parallelogram), FadeIn(triangle_a, triangle_b, rectangle_A))
        self.wait(1)
        self.play(Transform(triangle_a, triangle_A))
        self.wait(1)
        self.play(FadeIn(heightf, basef))
        self.wait(1)
        self.play(FadeIn(areaf , result), FadeOut(triangle_a, triangle_b, rectangle_A))
        self.wait(1)

        areaF = MathTex("A=bh").move_to([0,0,0])
        
        self.play(Transform(areaf, areaF, runtime=1), FadeOut(basef, heightf, result))
        self.wait(1)
        self.play(FadeOut(areaf))
        self.wait(1)

class Rhombus(Scene):
    def construct(self):

        
        rhombus = Polygon([-1, 2, 0], [4, 2, 0], [1, -2, 0], [-4, -2, 0]).set_fill(GREEN, opacity=0.7).set_stroke(WHITE)

        dia_1 = DashedLine([1, -2, 0], [-1, 2, 0]).set_stroke(RED)
        dia_2 = DashedLine([-4, -2, 0], [4, 2, 0]).set_stroke(PURPLE)

        alpha = Angle(dia_2, dia_1, dot=True)

        square = Polygon([-4, 3, 0], [1, 3, 0], [1, -2, 0], [-4, -2, 0]).set_fill(GREEN, opacity=0.7).set_stroke(WHITE)

        diag_1 = DashedLine([1, -2, 0], [-4, 3, 0])
        diag_2 = DashedLine([-4, -2, 0], [1, 3, 0])

        beta = Angle(diag_2, diag_1, dot=True)

        self.wait(1)
        self.play(Create(rhombus))
        self.wait(1)
        self.play(Create(dia_1), Create(dia_2))
        self.wait(1)
        self.play(Create(alpha))
        self.wait(1)
        self.play(Transform(rhombus, square), Transform(dia_1, diag_1), Transform(dia_2, diag_2), Transform(alpha, beta))
        self.wait(1)
        self.play(FadeOut(rhombus, dia_1, dia_2, alpha))
        self.wait(1)

        rhombus = Polygon([-1, 2, 0], [4, 2, 0], [1, -2, 0], [-4, -2, 0]).set_fill(GREEN, opacity=0.7).set_stroke(WHITE)

        dia_1 = DashedLine([1, -2, 0], [-1, 2, 0])
        dia_2 = DashedLine([-4, -2, 0], [4, 2, 0])

        alpha = Angle(dia_2, dia_1, dot=True)

        self.play(FadeIn(rhombus, dia_1, dia_2))
        self.wait(1)

        triangle_a = Polygon([-1, 2, 0], [4, 2, 0], [0,0,0]).set_fill(RED, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        triangle_b = Polygon([4, 2, 0], [1, -2, 0], [0,0,0]).set_fill(ORANGE, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        triangle_c = Polygon([1, -2, 0], [-4, -2, 0], [0,0,0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        triangle_d = Polygon([-4, -2, 0], [-1, 2, 0], [0,0,0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        #[-1, 2, 0], [4, 2, 0], [0,0,0]
        #[1, -2, 0], [-4, -2, 0], [0,0,0]
        Triangle_A = Polygon([3,4,0], [0,0,0], [4,2,0]).set_fill(RED, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        Triangle_C = Polygon([0, 0, 0], [-3, -4, 0], [1,-2,0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        Triangle_D = Polygon([1, -2, 0], [4, 2, 0], [5,0,0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        self.play(FadeOut(rhombus, dia_1, dia_2), Create(triangle_a), Create(triangle_b), Create(triangle_c), Create(triangle_d))
        self.wait(1)
        self.play(Transform(triangle_d, Triangle_D), Transform(triangle_a, Triangle_A), Transform(triangle_c, Triangle_C), runtime = 3)
        self.wait(1)

        dia_1 = DashedLine([1, -2, 0], [-1, 2, 0]).set_stroke(RED)
        dia_2 = DashedLine([-4, -2, 0], [4, 2, 0]).set_stroke(PURPLE)

        diag_a = DashedLine([5, 0, 0], [3, 4, 0]).set_stroke(RED)
        diag_b = DashedLine([-3, -4, 0], [5, 0, 0]).set_stroke(PURPLE)

        formula = MathTex("A=\\frac{d_1\\cdot d_2}{2}").move_to([0,3,0])
        formula1 = MathTex("A=\\frac{d_1\\cdot d_2}{2}").move_to([0,0,0])

        self.play(FadeIn(dia_1, dia_2))
        self.wait(1)
        self.play(Transform(dia_1, diag_a), Transform(dia_2, diag_b))
        self.wait(1)
        self.play(Rotate(triangle_a, angle=PI, about_point=[0,0,0]))
        self.wait(1)
        self.play(Create(formula))
        self.wait(1)
        self.play(FadeOut(triangle_a, triangle_b, triangle_c, triangle_d, dia_1, dia_2), Transform(formula, formula1))
        self.wait(1)
        self.play(FadeOut(formula))
        self.wait(1)

class Kite(Scene):
    def construct(self):
        kite = Polygon([-4, 0, 0], [-2,2,0],[4,0,0], [-2,-2,0])

        dia_1 = DashedLine([-2,2,0], [-2,-2,0]).set_stroke(RED)
        dia_2 = DashedLine([-4, 0, 0], [4, 0, 0]).set_stroke(PURPLE)

        self.wait(1)
        self.play(Create(kite))
        self.wait(1) 
        self.play(Create(dia_1),Create(dia_2))
        self.wait(1)
        
        #Rozdělit na části

        partA = Polygon([-4, 0, 0], [-2,2,0], [-2, 0, 0]).set_fill(RED, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        partB = Polygon([-2,2,0], [4,0,0], [-2, 0, 0]).set_fill(ORANGE, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        partC = Polygon([4,0,0], [-2,-2,0], [-2, 0, 0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        partD = Polygon([-2,-2,0], [-2, 0, 0],[-4, 0, 0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        self.play(FadeOut(kite), FadeIn(partA, partB, partC, partD))
        self.wait(1)

        #Posunout části na obdelník

        part_c = Polygon([-2,0,0], [4,-2,0], [4, 0, 0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        part_C = Polygon([-2,2,0], [4,0,0], [4, 2, 0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        part_d = Polygon([-4,-2,0], [-4, 0, 0],[-2, 0, 0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        part_D = Polygon([-4,0,0], [-4, 2, 0],[-2, 2, 0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        part_par = Polygon([4,0,0], [4, 2, 0],[6, 2, 0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)
        part_tra = Polygon([4,2,0], [4, 0, 0],[6, 0, 0]).set_fill(GREEN, opacity=0.5).set_stroke(WHITE, opacity = 0.2, width=0.05)

        

        self.play(Transform(partC, part_c), Transform(partD, part_d), runtime = 2)
        self.wait(1)

        self.play(Transform(partC, part_C), Transform(partD, part_D))
        self.wait(1)
        self.play(Transform(partD, part_par))
        self.wait(1)
        self.play(Transform(partD, part_tra))
        self.wait(1)
        
        formula = MathTex("A=\\frac{d_1\\cdot d_2}{2}").move_to([0,0,0])

        self.play(FadeIn(formula), FadeOut(partA, partB, partC, partD, dia_1, dia_2))
        self.wait(1)
        self.play(FadeOut(formula))
        self.wait(1)

class Trapezoid(Scene):
    def construct(self):
        
        trapezoid = Polygon([-2,3,0], [3,3,0], [4,-3,0], [-4,-3,0]).set_fill(PINK, opacity=0.5).set_stroke(WHITE)

        part_rect = Polygon([-2,3,0], [3,3,0], [3,-3,0], [-2,-3,0]).set_fill(ORANGE, opacity=0.5).set_stroke(WHITE)
        part_triA = Polygon([-2,3,0], [-2,-3,0], [-4,-3,0]).set_fill(RED, opacity=0.5).set_stroke(WHITE)
        part_triB = Polygon([3,3,0], [4,-3,0], [3,-3,0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE)
        plusrect = MathTex("+bh").move_to([0.5,0,0])

        part_tria = Polygon([0.5,3,0], [0.5,-3,0], [-1.5,-3,0]).set_fill(RED, opacity=0.5).set_stroke(WHITE)
        part_trib = Polygon([0.5,3,0], [1.5,-3,0], [0.5,-3,0]).set_fill(YELLOW, opacity=0.5).set_stroke(WHITE)

        triangle = Polygon([0.5,3,0], [1.5,-3,0], [-1.5,-3,0]).set_fill(ORANGE, opacity=0.5).set_stroke(WHITE)
        plustri = MathTex("+\\frac{bh}{2}").move_to([0,0,0])
        question = MathTex("b?").move_to([0,0,0])

        self.wait(1)
        self.play(Create(trapezoid))
        self.wait(1)
        self.play(FadeOut(trapezoid), FadeIn(part_rect, part_triA, part_triB))
        self.wait(1)
        self.play(FadeIn(plusrect))
        self.wait(1)
        self.play(FadeOut(part_rect,plusrect))
        self.wait(1)
        self.play(Transform(part_triA, part_tria), Transform(part_triB, part_trib))
        self.wait(1)
        self.play(FadeIn(triangle), FadeOut(part_triA, part_triB))
        self.wait(1)
        self.play(FadeOut(triangle), FadeIn(plustri))
        self.wait(1)
        self.play(Transform(plustri, question))
        self.wait(1)
        self.play(FadeIn(trapezoid), FadeOut(plustri))
        self.wait(1)

        base0 = Line([-2,3,0], [3,3,0]).set_color(RED)
        b0 = MathTex("b_0").move_to([0.5,2,0])
        base1 = Line([-4,-3,0], [4,-3,0]).set_color(RED)
        b1 = MathTex("b_1").move_to([0, -2, 0])

        self.play(Create(base0), Create(base1))
        self.wait(1)
        self.play(FadeIn(b0, b1))
        self.wait(1)
        self.play(FadeIn(part_rect))
        self.wait(1)
        self.play(FadeOut(part_rect, b0, b1, base0, base1, trapezoid))
        
        trifor = MathTex("b_0\\cdot h + \\frac{b_1-b_0}{2}\\cdot h")
        final = MathTex("\\frac{b_1+b_0}{2}\\cdot h")

        self.wait(1)
        self.play(FadeIn(trifor))
        self.wait(1)
        self.play(Transform(trifor, final))
        self.wait(1)
        self.play(FadeOut(final))
        self.wait(1)

class Quadrateral(Scene):
    def construct(self):
        concave = Text("Concave").move_to([3.5, 3, 0])
        convex = Text("Convex").move_to([-3.5, 3, 0])
        border = Line([0,4,0], [0,-4,0])

        quad_vex = Polygon([-6,-2,0], [-4, 1, 0], [-3, 0.5, 0], [-1, -2, 0]).set_stroke(WHITE).set_fill(BLUE, 0.5)

        quad_cave = Polygon([1,-2,0], [3, 1, 0], [6, -2, 0], [3.5, -0.5, 0]).set_stroke(WHITE).set_fill(BLUE, 0.5) 

        line_1 = Line([3.5, -0.5, 0], [1,-2,0])
        line_2 = Line([3.5, -0.5, 0], [6, -2, 0])
        angle = Angle(line_2, line_1).set_stroke(RED)

        anglegreater = MathTex("\\alpha > 180^\circ").set_color(RED).move_to([3.5,-3,0])

        dia_vex = DashedLine([-6,-2,0], [-3, 0.5, 0])
        dia_cave = DashedLine([1,-2,0], [6, -2, 0])

        #[1,-2,0], [3, 1, 0], [6, -2, 0], [3.5, -0.5, 0]

        tri_a = Polygon([-6,-2,0], [-4, 1, 0], [-3, 0.5, 0]).set_stroke(WHITE).set_fill(GREEN, 0.8)

        tri_b = Polygon([-6,-2,0], [-3, 0.5, 0], [-1, -2, 0]).set_stroke(WHITE).set_fill(GREEN, 0.8)

        tri_p = Polygon([1,-2,0], [3, 1, 0], [6, -2, 0]).set_stroke(WHITE).set_fill(GREEN, 0.8)

        tri_n = Polygon([1,-2,0], [3.5, -0.5, 0], [6, -2, 0]).set_stroke(WHITE).set_fill(RED, 0.8)

        aplusb = MathTex("A+B").move_to([-3.5, -3, 0])

        aplusb[0][0:1].set_color(GREEN)
        aplusb[0][2:3].set_color(GREEN)

        aminusb = MathTex("A-B").move_to([3.5,-3,0])

        aminusb[0][0:1].set_color(GREEN)
        aminusb[0][2:3].set_color(RED)

        ha = Line([-3.344, 0.213,0], [-4,1,0]).set_color(GREEN).set_stroke(width = 10)
        hb = Line([-3.049, 0.459, 0], [-1,-2,0]).set_color(GREEN).set_stroke(width = 10)

        #[1,-2,0], [3, 1, 0], [6, -2, 0], [3.5, -0.5, 0]

        hp = Line([3, -2, 0], [3, 1, 0]).set_color(GREEN).set_stroke(width = 10)
        hn = Line([3.5, -2, 0], [3.5, -0.5, 0]).set_color(RED).set_stroke(width = 10)

        self.wait(1)
        self.play(Write(concave), Write(convex), Create(border))
        self.wait(1)
        self.play(DrawBorderThenFill(quad_vex), DrawBorderThenFill(quad_cave))
        self.wait(1)
        self.play(Create(angle))
        self.wait(1)
        self.play(FadeIn(anglegreater))        
        self.wait(1)
        self.play(FadeOut(angle, anglegreater))
        self.wait(1)
        self.play(Create(dia_vex), Create(dia_cave), runtime = 1)
        self.wait(1)
        self.play(FadeIn(tri_p, tri_a), runtime = 1)
        self.wait(1)
        self.play(FadeOut(tri_p, tri_a), FadeIn(tri_n, tri_b), runtime = 1)
        self.wait(1)
        self.play(FadeOut(tri_n, tri_b))
        self.wait(1)
        self.play(Create(aplusb))
        self.wait(1)
        self.play(Create(aminusb))
        self.wait(1)
        self.play(Create(ha), Create(hb), Create(hp), Create(hn), runtime = 1)
        self.wait(1)



