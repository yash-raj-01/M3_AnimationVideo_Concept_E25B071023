from manim import *
import numpy as np

# Configure resolution and styling
config.background_color = "#0e1117"

class LinearTransformationSceneComplete(MovingCameraScene):
    def construct(self):
        # -------------------------------------------------------------------------
        # Color Palette (Classic 3Blue1Brown aesthetic)
        # -------------------------------------------------------------------------
        COLOR_I = "#2ecc71"        # Emerald green for i-hat
        COLOR_J = "#e74c3c"        # Coral red for j-hat
        COLOR_V = "#f1c40f"        # Vivid yellow for vector v
        COLOR_EIGEN1 = "#9b59b6"   # Purple for eigenvector 1
        COLOR_EIGEN2 = "#1abc9c"   # Turquoise for eigenvector 2
        COLOR_AREA = "#f39c12"     # Amber gold for area / determinant
        COLOR_COLLAPSE = "#e67e22" # Orange for singular dimension collapse
        COLOR_ACCENT = "#3498db"   # Cyan/blue for callouts and titles

        # =========================================================================
        # CHAPTER 1: INTRODUCING LINEAR TRANSFORMATIONS (~45s)
        # =========================================================================
        title = Text("Linear Transformations", font_size=44, weight=BOLD, color=WHITE)
        subtitle = Text("A Geometric Masterclass · The Essence of Linear Algebra", font_size=22, color="#bdc3c7")
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3).to_edge(UP, buff=0.8)

        self.play(FadeIn(title_group, shift=DOWN * 0.4), run_time=2.0)
        self.wait(3.0)

        # What does "Linear" mean?
        rule_box = Rectangle(width=11.2, height=2.4, color=COLOR_ACCENT, fill_color="#151e27", fill_opacity=0.92)
        rule_box.round_corners(0.2)
        rule_title = Text("What makes a transformation 'LINEAR'?", font_size=23, weight=BOLD, color=COLOR_ACCENT)
        rule_1 = Text("1. The ORIGIN remains fixed at (0, 0). It never moves or translates.", font_size=18, color=WHITE)
        rule_2 = Text("2. All GRID LINES remain straight lines (no curving, warping, or bending).", font_size=18, color=WHITE)
        rule_3 = Text("3. Parallel grid lines remain PARALLEL and EVENLY SPACED across space.", font_size=18, color=WHITE)
        rules_text = VGroup(rule_title, rule_1, rule_2, rule_3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rules_group = VGroup(rule_box, rules_text).move_to(DOWN * 0.4)
        rules_text.move_to(rule_box.get_center())

        self.play(FadeIn(rules_group, shift=UP * 0.3), run_time=2.0)
        self.wait(5.5)

        # Contrast: What is NOT linear?
        non_linear_card = Text("Why Linearity matters: Contrast with Non-Linearity", font_size=20, weight=BOLD, color="#e74c3c").to_edge(UP, buff=0.6)
        non_linear_bg = SurroundingRectangle(non_linear_card, color="#e74c3c", fill_color="#0e1117", fill_opacity=0.9, corner_radius=0.15, buff=0.15)
        non_linear_header = VGroup(non_linear_bg, non_linear_card)

        non_linear_demo_box = Text(
            "If the origin moves: f(v) = A · v + b  →  Translation (Affine, not Linear!)\n"
            "If grid lines curve: f(x, y) = [x², y²]ᵀ  →  Curves space (Non-linear!)\n\n"
            "In Linear Transformations: (0, 0) is sacred, and lines remain rigid & straight.",
            font_size=16,
            color=WHITE,
            line_spacing=1.3
        )
        nl_surround = SurroundingRectangle(non_linear_demo_box, color="#e74c3c", fill_color="#1f0f0f", fill_opacity=0.92, corner_radius=0.15, buff=0.22)
        nl_group = VGroup(nl_surround, non_linear_demo_box).to_edge(DOWN, buff=0.6)

        self.play(FadeOut(rules_group), FadeOut(title_group), FadeIn(non_linear_header), FadeIn(nl_group, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)
        self.play(FadeOut(non_linear_header), FadeOut(nl_group), run_time=1.5)

        # Create Cartesian NumberPlane
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_color": "#1e3a5f", "stroke_width": 1.5, "stroke_opacity": 0.55},
            axis_config={"stroke_color": "#7f8c8d", "stroke_width": 2.5}
        )
        self.play(Create(plane), run_time=2.5)
        self.wait(2.5)

        # Introduce Basis Vectors
        origin = plane.coords_to_point(0, 0)
        i_hat = Arrow(origin, plane.coords_to_point(1, 0), buff=0, color=COLOR_I, stroke_width=6, max_tip_length_to_length_ratio=0.25)
        j_hat = Arrow(origin, plane.coords_to_point(0, 1), buff=0, color=COLOR_J, stroke_width=6, max_tip_length_to_length_ratio=0.25)

        i_label = Text("î = [1, 0]ᵀ", font_size=20, weight=BOLD, color=COLOR_I).next_to(i_hat, DOWN, buff=0.2)
        j_label = Text("ĵ = [0, 1]ᵀ", font_size=20, weight=BOLD, color=COLOR_J).next_to(j_hat, LEFT, buff=0.2)

        basis_card = Text("Standard Basis Vectors: î and ĵ define our entire coordinate system", font_size=22, color=WHITE).to_edge(UP, buff=0.6)
        basis_bg = SurroundingRectangle(basis_card, color="#34495e", fill_color="#0e1117", fill_opacity=0.9, corner_radius=0.15, buff=0.15)
        basis_header = VGroup(basis_bg, basis_card)

        self.play(
            GrowArrow(i_hat),
            GrowArrow(j_hat),
            FadeIn(i_label),
            FadeIn(j_label),
            FadeIn(basis_header),
            run_time=2.0
        )
        self.wait(6.0)

        # Show linear combination for arbitrary vector v = 2*i + 1.5*j
        v_demo_pt = plane.coords_to_point(2.0, 1.5)
        v_demo = Arrow(origin, v_demo_pt, buff=0, color=COLOR_V, stroke_width=5)
        v_demo_lbl = Text("v = 2.0 î + 1.5 ĵ", font_size=18, weight=BOLD, color=COLOR_V).next_to(v_demo_pt, UR, buff=0.15)

        proj_x = DashedLine(plane.coords_to_point(2.0, 0), v_demo_pt, color=COLOR_J, stroke_width=2.5, stroke_opacity=0.8)
        proj_y = DashedLine(plane.coords_to_point(0, 1.5), v_demo_pt, color=COLOR_I, stroke_width=2.5, stroke_opacity=0.8)

        comb_note = Text(
            "Every vector in 2D space is a linear combination of î and ĵ:\n"
            "v = x · î + y · ĵ\n\n"
            "Because linearity preserves the grid, wherever î and ĵ land\n"
            "COMPLETELY determines where every other vector must land!",
            font_size=17,
            color=WHITE,
            line_spacing=1.3
        )
        comb_box = SurroundingRectangle(comb_note, color=COLOR_V, fill_color="#181810", fill_opacity=0.94, corner_radius=0.15, buff=0.22)
        comb_group = VGroup(comb_box, comb_note).to_corner(DR, buff=0.5)

        self.play(GrowArrow(v_demo), FadeIn(v_demo_lbl), Create(proj_x), Create(proj_y), run_time=2.0)
        self.play(FadeIn(comb_group, shift=LEFT * 0.3), run_time=1.8)
        self.wait(8.5)

        self.play(
            FadeOut(v_demo),
            FadeOut(v_demo_lbl),
            FadeOut(proj_x),
            FadeOut(proj_y),
            FadeOut(comb_group),
            FadeOut(basis_header),
            run_time=1.5
        )

        # =========================================================================
        # CHAPTER 2: THE MATRIX AS A RECIPE & GRID DEFORMATION (~55s)
        # =========================================================================
        recipe_title = Text("A Matrix is simply the final coordinates of î and ĵ!", font_size=23, weight=BOLD, color=WHITE).to_edge(UP, buff=0.5)
        recipe_bg = SurroundingRectangle(recipe_title, color="#34495e", fill_color="#0e1117", fill_opacity=0.92, corner_radius=0.15, buff=0.15)
        recipe_header = VGroup(recipe_bg, recipe_title)

        mat_label = Text("A = ", font_size=25, weight=BOLD, color=WHITE)
        col1_text = Text(" 2.0\n 0.5", font_size=22, weight=BOLD, color=COLOR_I)
        col2_text = Text(" 1.0\n 1.5", font_size=22, weight=BOLD, color=COLOR_J)
        left_bracket = Text("[", font_size=42, color=WHITE)
        right_bracket = Text("]", font_size=42, color=WHITE)

        col_group = VGroup(col1_text, col2_text).arrange(RIGHT, buff=0.45)
        left_bracket.next_to(col_group, LEFT, buff=0.15)
        right_bracket.next_to(col_group, RIGHT, buff=0.15)
        mat_label.next_to(left_bracket, LEFT, buff=0.2)

        matrix_badge = VGroup(mat_label, left_bracket, col_group, right_bracket)
        badge_bg = SurroundingRectangle(matrix_badge, color="#2980b9", fill_color="#101924", fill_opacity=0.95, corner_radius=0.15, buff=0.22)
        matrix_display = VGroup(badge_bg, matrix_badge).to_corner(UL, buff=0.6)

        col1_desc = Text("Col 1: Where î lands  →  [2.0, 0.5]ᵀ", font_size=16, weight=BOLD, color=COLOR_I).next_to(matrix_display, DOWN, aligned_edge=LEFT, buff=0.2)
        col2_desc = Text("Col 2: Where ĵ lands  →  [1.0, 1.5]ᵀ", font_size=16, weight=BOLD, color=COLOR_J).next_to(col1_desc, DOWN, aligned_edge=LEFT, buff=0.12)

        self.play(FadeIn(recipe_header), FadeIn(matrix_display), FadeIn(col1_desc), FadeIn(col2_desc), run_time=2.0)
        self.wait(6.5)

        matrix_A = [[2.0, 1.0], [0.5, 1.5]]
        new_i_pt = 2.0 * RIGHT + 0.5 * UP
        new_j_pt = 1.0 * RIGHT + 1.5 * UP

        i_hat_target = Arrow(origin, new_i_pt, buff=0, color=COLOR_I, stroke_width=6, max_tip_length_to_length_ratio=0.25)
        j_hat_target = Arrow(origin, new_j_pt, buff=0, color=COLOR_J, stroke_width=6, max_tip_length_to_length_ratio=0.25)
        i_label_target = Text("A · î = [2, 0.5]ᵀ", font_size=18, weight=BOLD, color=COLOR_I).next_to(new_i_pt, DR, buff=0.15)
        j_label_target = Text("A · ĵ = [1, 1.5]ᵀ", font_size=18, weight=BOLD, color=COLOR_J).next_to(new_j_pt, UL, buff=0.15)

        anim_note = Text("Watch space deform: lines stay parallel and evenly spaced", font_size=20, color="#bdc3c7").to_edge(DOWN, buff=0.5)
        anim_bg = SurroundingRectangle(anim_note, color="#34495e", fill_color="#0e1117", fill_opacity=0.88, corner_radius=0.1, buff=0.12)
        anim_group = VGroup(anim_bg, anim_note)

        self.play(FadeIn(anim_group), run_time=1.2)
        self.play(
            plane.animate.apply_matrix(matrix_A),
            Transform(i_hat, i_hat_target),
            Transform(j_hat, j_hat_target),
            Transform(i_label, i_label_target),
            Transform(j_label, j_label_target),
            run_time=8.5,
            rate_func=smooth
        )
        self.wait(7.5)

        # Step-by-step point tracking u = [3, -2]^T -> A * u = [4.0, -1.5]^T
        test_u_pt = 4.0 * RIGHT - 1.5 * UP
        test_u = Arrow(origin, test_u_pt, buff=0, color="#00ffff", stroke_width=5)
        test_lbl = Text("u = 3.0 î - 2.0 ĵ  →  A · u = [4.0, -1.5]ᵀ", font_size=17, weight=BOLD, color="#00ffff").next_to(test_u_pt, DR, buff=0.15)

        calc_box_text = Text(
            "Matrix Multiplication is just combining columns:\n"
            "A · [3, -2]ᵀ = 3 · [2.0, 0.5]ᵀ + (-2) · [1.0, 1.5]ᵀ\n"
            "             = [6.0, 1.5]ᵀ + [-2.0, -3.0]ᵀ\n"
            "             = [4.0, -1.5]ᵀ",
            font_size=16,
            color=WHITE,
            line_spacing=1.25
        )
        calc_box = SurroundingRectangle(calc_box_text, color="#00ffff", fill_color="#0a1a1f", fill_opacity=0.94, corner_radius=0.15, buff=0.22)
        calc_group = VGroup(calc_box, calc_box_text).to_corner(DR, buff=0.5)

        self.play(GrowArrow(test_u), FadeIn(test_lbl), FadeIn(calc_group, shift=LEFT * 0.3), run_time=2.0)
        self.wait(9.0)
        self.play(FadeOut(test_u), FadeOut(test_lbl), FadeOut(calc_group), FadeOut(anim_group), FadeOut(recipe_header), run_time=1.5)

        # =========================================================================
        # CHAPTER 3: EFFECTS ON LENGTHS, DIRECTIONS & BOTH EIGENVECTORS (~50s)
        # =========================================================================
        length_title = Text("Effect 1: LENGTHS & DIRECTIONS Change", font_size=23, weight=BOLD, color=COLOR_V).to_edge(UP, buff=0.5)
        length_bg = SurroundingRectangle(length_title, color=COLOR_V, fill_color="#0e1117", fill_opacity=0.92, corner_radius=0.15, buff=0.15)
        length_header = VGroup(length_bg, length_title)

        v_target_pt = 4.0 * RIGHT + 2.25 * UP
        vec_v = Arrow(origin, v_target_pt, buff=0, color=COLOR_V, stroke_width=6)
        vec_v_lbl = Text("v = 1.5 î + 1.0 ĵ  →  A · v = [4.0, 2.25]ᵀ", font_size=18, weight=BOLD, color=COLOR_V).next_to(v_target_pt, UR, buff=0.15)

        vector_info_text = Text(
            "• Length has stretched: ||v|| = 1.80  →  ||A v|| = 4.59\n"
            "• Direction has rotated: Angle shifted by ~4.3°\n"
            "• In general, vectors change both length and direction!",
            font_size=17,
            color=WHITE,
            line_spacing=1.3
        )
        vector_info_box = SurroundingRectangle(vector_info_text, color=COLOR_V, fill_color="#181810", fill_opacity=0.92, corner_radius=0.15, buff=0.2)
        vector_info_group = VGroup(vector_info_box, vector_info_text).to_corner(DR, buff=0.5)

        self.play(FadeIn(length_header), GrowArrow(vec_v), FadeIn(vec_v_lbl), run_time=2.0)
        self.play(FadeIn(vector_info_group, shift=LEFT * 0.3), run_time=1.8)
        self.wait(8.5)

        # EIGENVECTOR 1: [2, 1]^T with lambda = 2.5
        eigen1_pt = 5.0 * RIGHT + 2.5 * UP
        eigen1_span = Line(origin - 2.5 * (2*RIGHT + UP), origin + 3.0 * (2*RIGHT + UP), color=COLOR_EIGEN1, stroke_width=3, stroke_opacity=0.7)
        eigen1_vec = Arrow(origin, eigen1_pt, buff=0, color=COLOR_EIGEN1, stroke_width=6)
        eigen1_lbl = Text("Eigenvector 1: e₁ = [2, 1]ᵀ (λ₁ = 2.5)", font_size=18, weight=BOLD, color=COLOR_EIGEN1).next_to(eigen1_pt, UL, buff=0.15)

        eigen1_note = Text(
            "SPECIAL DIRECTION: Eigenvector 1 (λ₁ = 2.5)\n"
            "• It DOES NOT rotate at all!\n"
            "• Stays perfectly along its original span line.\n"
            "• Stretches purely by a factor of λ₁ = 2.5.",
            font_size=17,
            color=WHITE,
            line_spacing=1.3
        )
        eigen1_box = SurroundingRectangle(eigen1_note, color=COLOR_EIGEN1, fill_color="#1d1222", fill_opacity=0.94, corner_radius=0.15, buff=0.2)
        eigen1_group = VGroup(eigen1_box, eigen1_note).to_corner(DR, buff=0.5)

        self.play(
            FadeOut(vec_v),
            FadeOut(vec_v_lbl),
            FadeOut(vector_info_group),
            Create(eigen1_span),
            GrowArrow(eigen1_vec),
            FadeIn(eigen1_lbl),
            FadeIn(eigen1_group, shift=LEFT * 0.3),
            run_time=2.2
        )
        self.wait(9.5)

        # EIGENVECTOR 2: [-1, 1]^T with lambda = 1.0 (Completely unchanged line!)
        eigen2_pt = -1.0 * RIGHT + 1.0 * UP
        eigen2_span = Line(origin - 3.0 * (-RIGHT + UP), origin + 3.0 * (-RIGHT + UP), color=COLOR_EIGEN2, stroke_width=3, stroke_opacity=0.7)
        eigen2_vec = Arrow(origin, eigen2_pt, buff=0, color=COLOR_EIGEN2, stroke_width=6)
        eigen2_lbl = Text("Eigenvector 2: e₂ = [-1, 1]ᵀ (λ₂ = 1.0)", font_size=18, weight=BOLD, color=COLOR_EIGEN2).next_to(eigen2_pt, UL, buff=0.15)

        eigen2_note = Text(
            "SPECIAL DIRECTION: Eigenvector 2 (λ₂ = 1.0)\n"
            "• With eigenvalue λ₂ = 1.0, this vector is INVARIANT!\n"
            "• Every point on the line y = -x stays exactly where it started.\n"
            "• Matrix A has two distinct eigen-directions.",
            font_size=17,
            color=WHITE,
            line_spacing=1.3
        )
        eigen2_box = SurroundingRectangle(eigen2_note, color=COLOR_EIGEN2, fill_color="#0e1f1c", fill_opacity=0.94, corner_radius=0.15, buff=0.2)
        eigen2_group = VGroup(eigen2_box, eigen2_note).to_corner(DR, buff=0.5)

        self.play(
            FadeOut(eigen1_span),
            FadeOut(eigen1_vec),
            FadeOut(eigen1_lbl),
            FadeOut(eigen1_group),
            Create(eigen2_span),
            GrowArrow(eigen2_vec),
            FadeIn(eigen2_lbl),
            FadeIn(eigen2_group, shift=LEFT * 0.3),
            run_time=2.2
        )
        self.wait(10.0)

        self.play(
            FadeOut(eigen2_span),
            FadeOut(eigen2_vec),
            FadeOut(eigen2_lbl),
            FadeOut(eigen2_group),
            FadeOut(length_header),
            run_time=1.5
        )

        # =========================================================================
        # CHAPTER 4: AREA SCALING AND THE DETERMINANT (~50s)
        # =========================================================================
        area_title = Text("Effect 2: AREA Scaling is the DETERMINANT", font_size=23, weight=BOLD, color=COLOR_AREA).to_edge(UP, buff=0.5)
        area_bg = SurroundingRectangle(area_title, color=COLOR_AREA, fill_color="#0e1117", fill_opacity=0.92, corner_radius=0.15, buff=0.15)
        area_header = VGroup(area_bg, area_title)

        p0 = origin
        p1 = new_i_pt
        p2 = new_i_pt + new_j_pt
        p3 = new_j_pt

        parallelogram = Polygon(p0, p1, p2, p3, color=COLOR_AREA, fill_color=COLOR_AREA, fill_opacity=0.45, stroke_width=3)
        area_tag = Text("Transformed Area\n= det(A) = 2.5", font_size=18, weight=BOLD, color=WHITE).move_to((p0 + p2) / 2)

        det_math_text = Text(
            "Determinant: The Factor by Which Areas Scale\n\n"
            "det(A) = ad - bc\n"
            "       = (2.0)(1.5) - (1.0)(0.5)\n"
            "       = 3.0 - 0.5\n"
            "       = 2.5\n\n"
            "• Original 1x1 Unit Square had Area = 1.0\n"
            "• New Deformed Parallelogram has Area = 2.5\n"
            "• EVERY shape on the grid scales its area by exactly 2.5x!",
            font_size=16,
            color=WHITE,
            line_spacing=1.25
        )
        det_math_box = SurroundingRectangle(det_math_text, color=COLOR_AREA, fill_color="#1c1409", fill_opacity=0.94, corner_radius=0.15, buff=0.22)
        det_math_group = VGroup(det_math_box, det_math_text).to_corner(DR, buff=0.5)

        self.play(FadeIn(area_header), DrawBorderThenFill(parallelogram), FadeIn(area_tag), run_time=2.2)
        self.play(FadeIn(det_math_group, shift=LEFT * 0.3), run_time=2.0)
        self.wait(10.5)

        # Three Area Scaling Regimes
        scaling_types_text = Text(
            "The Three Area Scaling Regimes:\n\n"
            "• |det(A)| > 1: Expansion (Space stretches, areas grow)\n"
            "• |det(A)| = 1: Area-Preserving (Pure rotations & simple shears)\n"
            "• 0 < |det(A)| < 1: Compression (Space contracts, areas shrink)\n\n"
            "In our matrix: det(A) = 2.5 > 1, so every region expands by 250%!",
            font_size=16,
            color=WHITE,
            line_spacing=1.3
        )
        scaling_box = SurroundingRectangle(scaling_types_text, color=COLOR_AREA, fill_color="#1c1409", fill_opacity=0.95, corner_radius=0.15, buff=0.22)
        scaling_group = VGroup(scaling_box, scaling_types_text).to_corner(DR, buff=0.5)

        circle_demo = Circle(radius=0.6, color=COLOR_ACCENT, fill_color=COLOR_ACCENT, fill_opacity=0.35, stroke_width=2.5).move_to(plane.coords_to_point(-1.5, 0.5))
        circle_lbl = Text("Circle Area: π r²  →  Scales by 2.5x as an Ellipse!", font_size=16, color=COLOR_ACCENT).next_to(circle_demo, UP, buff=0.15)

        self.play(FadeOut(det_math_group), FadeIn(scaling_group, shift=LEFT * 0.3), FadeIn(circle_demo), FadeIn(circle_lbl), run_time=2.0)
        self.wait(9.5)

        self.play(
            FadeOut(parallelogram),
            FadeOut(area_tag),
            FadeOut(scaling_group),
            FadeOut(circle_demo),
            FadeOut(circle_lbl),
            FadeOut(area_header),
            FadeOut(matrix_display),
            FadeOut(col1_desc),
            FadeOut(col2_desc),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(plane),
            run_time=1.5
        )

        # =========================================================================
        # CHAPTER 5: ORIENTATION & NEGATIVE DETERMINANT (~45s)
        # =========================================================================
        orient_title = Text("Effect 3: ORIENTATION & Negative Determinants", font_size=23, weight=BOLD, color="#e67e22").to_edge(UP, buff=0.5)
        orient_bg = SurroundingRectangle(orient_title, color="#e67e22", fill_color="#0e1117", fill_opacity=0.92, corner_radius=0.15, buff=0.15)
        orient_header = VGroup(orient_bg, orient_title)

        plane2 = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_color": "#1e3a5f", "stroke_width": 1.5, "stroke_opacity": 0.55},
            axis_config={"stroke_color": "#7f8c8d", "stroke_width": 2.5}
        )

        i2 = Arrow(origin, plane2.coords_to_point(1, 0), buff=0, color=COLOR_I, stroke_width=6)
        j2 = Arrow(origin, plane2.coords_to_point(0, 1), buff=0, color=COLOR_J, stroke_width=6)
        i2_lbl = Text("î", font_size=22, weight=BOLD, color=COLOR_I).next_to(i2, DOWN, buff=0.15)
        j2_lbl = Text("ĵ", font_size=22, weight=BOLD, color=COLOR_J).next_to(j2, LEFT, buff=0.15)

        orient_arc = CurvedArrow(
            plane2.coords_to_point(0.7, 0.1),
            plane2.coords_to_point(0.1, 0.7),
            color=YELLOW,
            angle=-TAU / 8
        )
        ccw_note = Text("Standard Orientation: ĵ is COUNTER-CLOCKWISE from î (+)", font_size=16, color=YELLOW).next_to(orient_arc, UR, buff=0.15)

        self.play(FadeIn(plane2), GrowArrow(i2), GrowArrow(j2), FadeIn(i2_lbl), FadeIn(j2_lbl), FadeIn(orient_header), run_time=2.0)
        self.play(Create(orient_arc), FadeIn(ccw_note), run_time=1.5)
        self.wait(4.0)

        b_label = Text("B = ", font_size=25, weight=BOLD, color=WHITE)
        b_col1 = Text("-1.0\n 0.0", font_size=22, weight=BOLD, color=COLOR_I)
        b_col2 = Text(" 0.0\n 1.0", font_size=22, weight=BOLD, color=COLOR_J)
        b_lb = Text("[", font_size=42, color=WHITE)
        b_rb = Text("]", font_size=42, color=WHITE)
        b_cols = VGroup(b_col1, b_col2).arrange(RIGHT, buff=0.45)
        b_lb.next_to(b_cols, LEFT, buff=0.15)
        b_rb.next_to(b_cols, RIGHT, buff=0.15)
        b_label.next_to(b_lb, LEFT, buff=0.2)
        b_mat = VGroup(b_label, b_lb, b_cols, b_rb)
        b_bg = SurroundingRectangle(b_mat, color="#e67e22", fill_color="#18120b", fill_opacity=0.95, corner_radius=0.15, buff=0.22)
        b_display = VGroup(b_bg, b_mat).to_corner(UL, buff=0.6)

        det_b_note = Text("det(B) = -1.0  (< 0)", font_size=19, weight=BOLD, color="#e74c3c").next_to(b_display, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(FadeIn(b_display), FadeIn(det_b_note), FadeOut(orient_arc), FadeOut(ccw_note), run_time=1.5)

        matrix_B = [[-1.0, 0.0], [0.0, 1.0]]
        new_i2_pt = plane2.coords_to_point(-1, 0)
        new_j2_pt = plane2.coords_to_point(0, 1)

        i2_target = Arrow(origin, new_i2_pt, buff=0, color=COLOR_I, stroke_width=6)
        j2_target = Arrow(origin, new_j2_pt, buff=0, color=COLOR_J, stroke_width=6)
        i2_lbl_target = Text("B · î = [-1, 0]ᵀ", font_size=17, weight=BOLD, color=COLOR_I).next_to(new_i2_pt, DOWN, buff=0.15)
        j2_lbl_target = Text("B · ĵ = [0, 1]ᵀ", font_size=17, weight=BOLD, color=COLOR_J).next_to(new_j2_pt, RIGHT, buff=0.15)

        flip_explanation = Text(
            "ORIENTATION IS INVERTED!\n\n"
            "• The plane has been flipped over like a sheet of paper.\n"
            "• Now ĵ is CLOCKWISE from î (chirality reversed).\n"
            "• A negative determinant indicates an orientation inversion.",
            font_size=17,
            color=WHITE,
            line_spacing=1.35
        )
        flip_box = SurroundingRectangle(flip_explanation, color="#e74c3c", fill_color="#210e0e", fill_opacity=0.94, corner_radius=0.15, buff=0.22)
        flip_group = VGroup(flip_box, flip_explanation).to_corner(DR, buff=0.5)

        self.play(
            plane2.animate.apply_matrix(matrix_B),
            Transform(i2, i2_target),
            Transform(j2, j2_target),
            Transform(i2_lbl, i2_lbl_target),
            Transform(j2_lbl, j2_lbl_target),
            run_time=7.5,
            rate_func=smooth
        )
        self.play(FadeIn(flip_group, shift=LEFT * 0.3), run_time=1.8)
        self.wait(10.0)

        self.play(
            FadeOut(plane2),
            FadeOut(i2),
            FadeOut(j2),
            FadeOut(i2_lbl),
            FadeOut(j2_lbl),
            FadeOut(b_display),
            FadeOut(det_b_note),
            FadeOut(flip_group),
            FadeOut(orient_header),
            run_time=1.5
        )

        # =========================================================================
        # CHAPTER 6: ZERO DETERMINANT & DIMENSIONAL COLLAPSE (~45s)
        # =========================================================================
        collapse_title = Text("What happens when det(A) = 0? Dimension Collapse!", font_size=23, weight=BOLD, color=COLOR_COLLAPSE).to_edge(UP, buff=0.5)
        collapse_bg = SurroundingRectangle(collapse_title, color=COLOR_COLLAPSE, fill_color="#0e1117", fill_opacity=0.92, corner_radius=0.15, buff=0.15)
        collapse_header = VGroup(collapse_bg, collapse_title)

        plane3 = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_color": "#1e3a5f", "stroke_width": 1.5, "stroke_opacity": 0.55},
            axis_config={"stroke_color": "#7f8c8d", "stroke_width": 2.5}
        )

        i3 = Arrow(origin, plane3.coords_to_point(1, 0), buff=0, color=COLOR_I, stroke_width=6)
        j3 = Arrow(origin, plane3.coords_to_point(0, 1), buff=0, color=COLOR_J, stroke_width=6)

        c_label = Text("C = ", font_size=25, weight=BOLD, color=WHITE)
        c_col1 = Text(" 1.0\n 0.5", font_size=22, weight=BOLD, color=COLOR_I)
        c_col2 = Text(" 2.0\n 1.0", font_size=22, weight=BOLD, color=COLOR_J)
        c_lb = Text("[", font_size=42, color=WHITE)
        c_rb = Text("]", font_size=42, color=WHITE)
        c_cols = VGroup(c_col1, c_col2).arrange(RIGHT, buff=0.45)
        c_lb.next_to(c_cols, LEFT, buff=0.15)
        c_rb.next_to(c_cols, RIGHT, buff=0.15)
        c_label.next_to(c_lb, LEFT, buff=0.2)
        c_mat = VGroup(c_label, c_lb, c_cols, c_rb)
        c_bg = SurroundingRectangle(c_mat, color=COLOR_COLLAPSE, fill_color="#18120b", fill_opacity=0.95, corner_radius=0.15, buff=0.22)
        c_display = VGroup(c_bg, c_mat).to_corner(UL, buff=0.6)

        det_c_note = Text("det(C) = 1(1) - 2(0.5) = 0", font_size=19, weight=BOLD, color="#e74c3c").next_to(c_display, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(FadeIn(plane3), GrowArrow(i3), GrowArrow(j3), FadeIn(collapse_header), FadeIn(c_display), FadeIn(det_c_note), run_time=2.0)
        self.wait(3.5)

        matrix_C = [[1.0, 2.0], [0.5, 1.0]]
        i3_target = Arrow(origin, plane3.coords_to_point(1.0, 0.5), buff=0, color=COLOR_I, stroke_width=6)
        j3_target = Arrow(origin, plane3.coords_to_point(2.0, 1.0), buff=0, color=COLOR_J, stroke_width=6)

        collapse_msg = Text(
            "ALL OF 2D SPACE SQUISHES ONTO A 1D LINE!\n\n"
            "• Area is scaled by 0: 2D area is completely eliminated.\n"
            "• Infinite input vectors map to identical output points.\n"
            "• Information is lost forever: matrix C has NO INVERSE (singular)!",
            font_size=17,
            color=WHITE,
            line_spacing=1.35
        )
        collapse_msg_box = SurroundingRectangle(collapse_msg, color="#e74c3c", fill_color="#240c0c", fill_opacity=0.95, corner_radius=0.15, buff=0.22)
        collapse_msg_group = VGroup(collapse_msg_box, collapse_msg).to_corner(DR, buff=0.5)

        self.play(
            plane3.animate.apply_matrix(matrix_C),
            Transform(i3, i3_target),
            Transform(j3, j3_target),
            run_time=7.5,
            rate_func=smooth
        )
        self.play(FadeIn(collapse_msg_group, shift=LEFT * 0.3), run_time=1.8)
        self.wait(9.5)

        # Rank and Column Space
        rank_text = Text(
            "Column Space & Rank:\n\n"
            "• The set of all possible outputs is called the COLUMN SPACE.\n"
            "• When 2D space squishes to a 1D line, Rank = 1.\n"
            "• Full rank (Rank 2) requires det ≠ 0.\n"
            "• If Rank < 2, det = 0, and no unique inverse exists!",
            font_size=16,
            color=WHITE,
            line_spacing=1.35
        )
        rank_box = SurroundingRectangle(rank_text, color=COLOR_COLLAPSE, fill_color="#240c0c", fill_opacity=0.95, corner_radius=0.15, buff=0.22)
        rank_group = VGroup(rank_box, rank_text).to_corner(DR, buff=0.5)

        self.play(FadeOut(collapse_msg_group), FadeIn(rank_group, shift=LEFT * 0.3), run_time=1.8)
        self.wait(9.5)

        self.play(
            FadeOut(plane3),
            FadeOut(i3),
            FadeOut(j3),
            FadeOut(c_display),
            FadeOut(det_c_note),
            FadeOut(rank_group),
            FadeOut(collapse_header),
            run_time=1.5
        )

        # =========================================================================
        # CHAPTER 7: MASTER SUMMARY & PHILOSOPHICAL RECAP (~25s)
        # =========================================================================
        summary_title = Text("The Geometric Essence of Linear Algebra", font_size=32, weight=BOLD, color=WHITE).to_edge(UP, buff=0.7)

        summary_card = Rectangle(width=11.8, height=5.2, color=COLOR_ACCENT, fill_color="#0d141d", fill_opacity=0.96)
        summary_card.round_corners(0.25)

        summary_data = [
            ("Matrix Columns", "Where basis vectors î and ĵ land; fully describes the transformation.", COLOR_I),
            ("Grid Deformation", "Origin stays fixed at (0, 0); lines remain parallel, straight, & evenly spaced.", COLOR_ACCENT),
            ("Lengths & Directions", "Vectors stretch & rotate via A · v. Eigenvectors keep their original direction.", COLOR_V),
            ("Area Scaling", "The magnitude |det(A)| dictates the scaling factor of every 2D area.", COLOR_AREA),
            ("Orientation", "Sign of det(A): (+) preserves handedness, (-) flips space like a pancake.", "#e74c3c"),
            ("det(A) = 0", "Dimension collapse: full 2D plane squished into a 1D line or 0D point (singular).", COLOR_COLLAPSE),
        ]

        summary_mobs = []
        for term, desc, col in summary_data:
            t_term = Text(term + ":", font_size=18, weight=BOLD, color=col)
            t_desc = Text(desc, font_size=16, color=WHITE)
            row = VGroup(t_term, t_desc).arrange(RIGHT, buff=0.25)
            summary_mobs.append(row)

        all_summary_rows = VGroup(*summary_mobs).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        summary_panel = VGroup(summary_card, all_summary_rows)
        all_summary_rows.move_to(summary_card.get_center())

        self.play(FadeIn(summary_title, shift=DOWN * 0.3), FadeIn(summary_panel, shift=UP * 0.3), run_time=2.0)
        self.wait(11.0)

        quote_text = Text('"Think with geometry, compute with matrices." · Grant Sanderson (3Blue1Brown)', font_size=19, color="#95a5a6")
        quote_text.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(quote_text), run_time=1.5)
        self.wait(6.5)

        self.play(FadeOut(summary_title), FadeOut(summary_panel), FadeOut(quote_text), run_time=2.0)
        self.wait(1.0)
