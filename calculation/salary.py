from calculation import administrative, worker, sales


def main():
    salary_administrative = administrative.Administrative('Административного работника', 'Валерия Задорожного')
    print(salary_administrative.administrative_worker())
    salary_worker = worker.Worker('Рабочего', 'Ильи Кромина')
    print(salary_worker.worker())
    salary_sales = sales.Sales('Торгового представителя', 'Николая Хорольского')
    print(salary_sales.sales_representative())


if __name__ == '__main__':
    main()

# stdout:
# Заработная плата: Административного работника Валерия Задорожного - 1500
# Заработная плата: Рабочего Ильи Кромина - 24000
# Заработная плата: Торгового представителя Николая Хорольского - 1625.0
