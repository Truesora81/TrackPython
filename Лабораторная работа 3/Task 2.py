
def find_common_participants(first_group, second_group, splitter = ','):
    return sorted(list(set(first_group.split(splitter)) & set(second_group.split(splitter))))

participants_first_group = 'Иванов|Петров|Сидоров'
participants_second_group = 'Петров|Сидоров|Иванов'

print(find_common_participants(participants_first_group, participants_second_group, '|'))