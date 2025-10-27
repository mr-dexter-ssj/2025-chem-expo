# -*- coding: utf-8 -*-
from manimlib.imports import *

class AtomoDeHidrogeno(ThreeDScene):
    def construct(self):
        # 1. Configuracion de la Escena 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # 2. Creacion del Nucleo (Proton)
        proton = Sphere(radius=0.3, resolution=(15, 15), color=RED).set_opacity(0.8)

        # 3. Creacion de la Orbita
        orbita = Circle(radius=2, color=LIGHT_GRAY).rotate(90 * DEGREES, axis=X_AXIS)

        # 4. Creacion del Electron
        electron = Sphere(radius=0.1, resolution=(15, 15), color=BLUE).set_opacity(0.8)
        electron.move_to(orbita.point_from_proportion(0))

        # 5. Creacion de Etiquetas y Textos
        # CORRECCION: Z=1 se cambia a Text
        z_text = Text("Z=1").next_to(proton.get_center())

        info_box = VGroup(
            # CORRECCION: Se cambian todos los TextMobject sin LaTeX a Text
            Text("Info Atomo de Hidrogeno", font_size=35, color=YELLOW),
            Text("No Atomico (Z): 1", font_size=20),
            Text("Electrones de Valencia: 1", font_size=20),
            Text("Peso Molecular: 1.008 u.m.a.", font_size=20),
            Text("Conf Ener: [No Aplica]", font_size=20, color=RED),
            # Este es el unico que mantiene TextMobject por el codigo LaTeX H$_{2}$
            TextMobject("Estado Natural: Gas Diatomico (H$_{2}$)", font_size=20) 
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_corner(UL)

        # 6. Agregando Elementos
        self.add_fixed_in_frame_mobjects(z_text, info_box)
        self.add(proton, orbita, electron)

        # 7. Animacion
        self.play(ShowCreation(proton), ShowCreation(orbita), ShowCreation(electron))
        self.play(FadeIn(info_box, shift=UP), FadeIn(z_text), run_time=1)
        self.wait(1)

        # Mover el electron a lo largo de la orbita
        self.play(MoveAlongPath(electron, orbita), rate_func=linear, run_time=5, loop=True)
        self.wait(5)

        self.stop_ambient_camera_rotation()
        self.wait(1)