class PlotBase:
    def __init__(self, result):
        self.result = result
    def render(self):
        raise NotImplementedError
