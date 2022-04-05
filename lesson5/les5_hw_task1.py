"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple


def set_business_data(set_dict: dict):

    Company = namedtuple('Company',
                         """name_company
                         first_quarter_earnings
                         second_quarter_earnings
                         third_quarter_earnings
                         fourth_quarter_earnings
                         average_profit
                         total_profit""",
                         defaults=[None, None, None, None, None, None, None])
    set_dict['total_profit'] = sum(
        [float(val) for val in list(set_dict.values())[1:]])
    set_dict['average_profit'] = set_dict['total_profit'] / 4

    company = Company(**set_dict)
    return company


_dict = {'name_company': '',
         'first_quarter_earnings': 0,
         'second_quarter_earnings': 0,
         'third_quarter_earnings': 0,
         'fourth_quarter_earnings': 0}

enterprises = []
text = 'больше'

commands = ['exit', 'end input']
command = ''
while command != commands[0]:
    command = input(f'Введите команду из списка {commands}\n'
                    f'или "Enter" для ввода данных: ')
    if command == commands[1]:
        avr_prof = sum([company["total_profit"]
                        for company in enterprises])/len(enterprises)
        """
        # не обязательный цикл добавления в очередь по среднему значению
        for company in enterprises:
            if float(company['total_profit']) > avr_prof:
                sorted_companies.append(company)
                print(f'{company["name_company"]}'
                      f' - {company["total_profit"]}')
            elif float(company['total_profit']) < avr_prof:
                sorted_companies.appendleft(company)"""

        print(f'Среди следующих компаний:\n'
              f'{[comp["name_company"] for comp in enterprises]}\n'
              f'Cредняя прибыль равна: {avr_prof}')
        enterprises = sorted(enterprises, key=lambda x: x["total_profit"])
        print([f'{com["name_company"]} - {com["total_profit"]}'
               for com in enterprises if com["total_profit"] > avr_prof])
        break

    elif command == '':
        set_dict = {key: input(f'Введите {key}: ')
                    for key, val in _dict.items()}
        enterprises.append(set_business_data(set_dict)._asdict())
    else:
        pass
