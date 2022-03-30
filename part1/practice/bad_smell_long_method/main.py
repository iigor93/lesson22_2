# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_data(string):
    data = [line.split(';') for line in string.split('\n')]
    return data


def sort_data(data):
    return sorted(data, key=lambda age: int(age[1]))


def _filter(data):
    return [line for line in data if int(line[1]) > 18]


def get_users_list():

    data = read_data(csv)
    data = sort_data(data)
    return _filter(data)


if __name__ == '__main__':
    print(get_users_list())
