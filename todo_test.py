from flet import *
import flet as ft
def main(page: Page):
    # colors used
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"
    # container object
    container = Container(
        # object properties
        width=500,height=850,bgcolor=BG,

    )
    page.add(container)

ft.app(main)