import flet as ft
from app.view.main_view import MainView
from app.controller.workflow_controller import WorkflowController


def main(page: ft.Page):

    page.title = "業務マニュアルアプリ"
    page.window_width = 900
    page.window_height = 700

    controller = WorkflowController()
    view = MainView(page, controller)

    view.build()


ft.app(target=main)