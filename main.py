import flet as ft

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
    toto = Todo_App()

    page.add(todo)
    page.add(toto)


ft.app(main)