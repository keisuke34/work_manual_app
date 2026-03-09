import flet as ft


class MainView:

    def __init__(self, page, controller):
        self.page = page
        self.controller = controller

    def build(self):

        self.title_input = ft.TextField(label="業務タイトル")

        add_button = ft.ElevatedButton(
            "追加",
            on_click=self.add_workflow
        )

        self.list_view = ft.Column()

        self.page.add(
            ft.Text("業務マニュアル", size=30),
            self.title_input,
            add_button,
            self.list_view
        )

    def add_workflow(self, e):

        title = self.title_input.value

        if title:
            self.controller.add_workflow(title)

        self.refresh_list()

        self.title_input.value = ""
        self.page.update()

    def refresh_list(self):

        self.list_view.controls.clear()

        workflows = self.controller.get_workflows()

        for w in workflows:
            self.list_view.controls.append(
                ft.Text(w["title"])
            )

        self.page.update()