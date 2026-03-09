class WorkflowModel:

    def __init__(self):
        self.workflows = []

    def add_workflow(self, workflow):
        self.workflows.append(workflow)

    def get_all(self):
        return self.workflows