from flet import *
import flet as ft
def main(page: Page):
    # colors used
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"
    # categories card
    categories_card = Row(
        #insert a scroll wheel
        scroll=ScrollMode.AUTO,


    )
    categories = ['Business','Family','Friends','Work']
    for x in categories:
        #appends a container to the Row
        categories_card.controls.append(
            Container(
                bgcolor=BG,height=110,width=200,border_radius=20,padding=10
            )
        )
    #pages and their contents
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )

                    ]
                ),
                Container(height=20),
                Text(value='What\'s up Calvyin!'),
                Text(value='CATEGORIES'),
                Container(
                    padding=padding.only(top=10,bottom=20),
                    content=categories_card
                )
            ]
        )
    )
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400, height=650, bgcolor=FG,
                border_radius=35,
                padding=padding.only(top=50,left=20,right=20,bottom=5),
                #we use column instead of container since container can hold only one widget while the column widget can hold more
                content=Column(
                    controls=[
                        first_page_contents
                    ]

                )
            )
        ]
    )
    # container object
    container = Container(
        # object properties
        width=400,height=650,bgcolor=BG,
        border_radius=35,
        content= Stack(
            controls=[
                page_1,
                page_2

            ]
        )

    )
    page.add(container)

ft.app(main)