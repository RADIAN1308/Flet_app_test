import flet as ft
from math import pi
from flet import *

#color gradient function

def create_darkness():
    gradient = LinearGradient(
        begin= alignment.top_center,
        end=alignment.bottom_center,
        colors=[
            "#484848",
            "#444444",
            "#424242",
            "#3b3b3b",
            "#373737",
            "#353535",
            "#343434",
            "#2f2f2f",
            "#2b2b2b",
        ]
    )
    return gradient





#main

def main(page: Page):
    # page settings
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor= "#ffffff"

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
