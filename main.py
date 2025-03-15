import flet as ft
from flet.core.icons import icons


# class for each task
class Task(ft.Column):
    def __init__(self,task_name,task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete=task_delete
        self.display_task = ft.Checkbox(value=False,label =self.task_name)
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

#         Add the display view and the edit view into the task object using controls since task object is a column




# to do app instance creation
class Todo_App(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What is the next task to be done?",expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls=[
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked),
                ]
            ),
            self.tasks_view,
        ]

    def add_clicked(self,e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()

def main(page: ft.Page):
    page.title = "To-do List App"
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.update()

    todo = Todo_App()


    page.add(todo)



ft.app(main)