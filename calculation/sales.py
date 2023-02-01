from calculation import employee


class Sales(employee.Employee):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.sum = 1250

    def sales_representative(self):
        return f'Заработная плата: {self.code} {self.name} - {self.sum + (self.sum / 100 * 30)}'