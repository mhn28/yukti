class Plot4D:
    def __init__(self, result):
        self.result = result
    def render(self, axes, time_index):
        raise NotImplementedError
