from calculation import employee


class Administrative(employee.Employee):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.sum = 1500

    def administrative_worker(self):
        return f'Заработная плата: {self.code} {self.name} - {self.sum}'