import flet as ft

def main(page: ft.Page):
    hello_world = ft.Text(value="Hello World")

    page.add(
        ft.ResponsiveRow(
            [
                hello_world
            ]

        )
    )

ft.app(main)