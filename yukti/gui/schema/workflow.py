class WorkflowStep:
    def __init__(self, name, inputs, outputs, options=None):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.options = options or {}
class Workflow:
    def __init__(self, steps):
        self.steps = steps
