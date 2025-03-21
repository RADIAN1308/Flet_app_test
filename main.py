import flet as ft
from flet.core.icons import Icons

# to do app instance creation
class Todo_App(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What is the next task to be done?",expand=True)
        self.tasks = ft.Column()

        #Tabs for filtering all active and completed tasks
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All"), ft.Tab(text="Active"), ft.Tab(text="Completed")],
        )

        #Task view container
        self.Tbox = ft.Container(
            bgcolor="#872341",
            padding=20,
            border_radius=20,
            content=self.tasks
        )
        self.width = 600
        self.controls=[
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked),
                ]
            ),
            self.Tbox,

        ]




    def add_clicked(self,e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_status_change(self, e):
        self.update()

    def task_delete(self,task):
        self.tasks.controls.remove(task)
        self.update()

        # before updating function

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                    status == "All"
                    or (status == "Active" and task.completed == False)
                    or (status == "Completed" and task.completed)
            )

    def tabs_changed(self, e):
        self.update()

# class for each task
class Task(ft.Column):
    def __init__(self,task_name,task_status_change,task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete=task_delete
        self.display_task = ft.Checkbox(value=False,label =self.task_name,on_change=self.status_changed)
        self.edit_name =ft.TextField(expand=1)
        # display view section
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_ROUNDED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_ROUNDED,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        )
                    ],

                )
            ]

        )
        # help
        # edit view section
        self.edit_view = ft.Row(
            # set to false as initial so that we can toggle it to true later in the function
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon = ft.Icons.DONE_ROUNDED,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                )
            ]
        )

        # Add the display view and the edit view into the task object using controls since task object is a column
        self.controls= [self.display_view,self.edit_view]


    def edit_clicked(self,e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible =False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self,e):
        self.display_task.label = self.edit_name.value
        self.edit_view.visible = False
        self.display_view.visible = True
        self.update()
        # change status after click

    def status_changed(self,e):
        self.completed = self.display_task.value
        self.task_status_change()

    def delete_clicked(self,e):
        self.task_delete(self)



def main(page: ft.Page):
    page.title = "To-do List App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = Todo_App()
    #Main app view

    box = ft.Container(
        border_radius=20,
        padding=40,
        bgcolor="#09122C",
        height=600,
        width=450,
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(
                            content=ft.Icon(Icons.MENU_ROUNDED)
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(Icons.NOTIFICATIONS_ROUNDED),
                                    ft.Icon(Icons.PERSON_2_ROUNDED)
                                ]
                            )
                        )

                    ]

                ),
                todo
            ]
        )
    )




    page.add(box)




ft.app(main)