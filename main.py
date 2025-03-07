import flet as ft
from math import pi
from flet import *

#color gradient function




#main

def main(page: Page):
    # page settings
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor= "PINK"

    #create instance

    #add controls
    page.add(
        Stack(
            width=270,
            height = 550,
            clip_behavior=ClipBehavior.HARD_EDGE,
            controls=[],
    )
    )


    #page refresh
    page.update()


ft.app(main)
