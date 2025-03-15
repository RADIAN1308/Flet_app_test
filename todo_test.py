from flet import *
import flet as ft
def main(page: Page):
    page.window.height = 700,
    page.window.width = 500,
    # colors used
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"



    #Tasks column
    tasks = Column(

    )


    # categories card
    categories_card = Row(
        #insert a scroll wheel
        scroll=ScrollMode.AUTO,


    )
    categories = ['Business','Family','Friends','Work']
    for i, x in enumerate(categories):
        #appends a container to the Row
        categories_card.controls.append(
            Container(
                bgcolor=BG,height=110,width=200,border_radius=20,padding=10,
                content = Column(
                    controls=[
                        Text(value="40 tasks"),
                        Text(x),
                        Container(
                            width= 170,
                            height=5,
                            border_radius=20,
                            padding= padding.only(right=30*i)
                            ,content= Container(
                                bgcolor=PINK
                            )
                        )
                    ]

                )
            )
        )


    #pages and their contents
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
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

                ),
                Container(height=18),
                Text(value="TODAY'S TASKS: "),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon=icons.ADD,on_click=lambda e: page.go('/create_task')
                        )
                    ]
                ),
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

# create task page
    create_task_view = Container(
        content=Column(
            controls=[
                Text(value="LOLOLOLOLLOLOLOLOL!!!!!!!")
            ]
        )

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


    # pages required for each route change made into a dictionary / is home route viz container
    pages = {
        "/": View(
            "/",
            [
                container,
            ],
        ),
        "/create_task": View(
            "/create_task",
            [create_task_view],
        ),
    }

    # route change and view switch function
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

ft.app(main)