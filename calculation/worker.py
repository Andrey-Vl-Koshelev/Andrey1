from calculation import employee


class Worker(employee.Employee):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.sum = 600

    def worker(self):
        return f'Заработная плата: {self.code} {self.name} - {self.sum * 40}'
