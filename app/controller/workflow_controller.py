from app.model.workflow_model import WorkflowModel


class WorkflowController:

    def __init__(self):
        self.model = WorkflowModel()

    def add_workflow(self, title):
        workflow = {
            "title": title,
            "steps": []
        }
        self.model.add_workflow(workflow)

    def get_workflows(self):
        return self.model.get_all()