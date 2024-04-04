# comma separated values
with open('./students.csv') as file:
    for line in sorted(file):
        # student = line.rstrip().split(',')
        # print(f'{student[0]} - {student[2]} - {student[1]}')
        name, house, patronus = line.rstrip().split(',')
        print(f'{name} - {patronus} - {house}')