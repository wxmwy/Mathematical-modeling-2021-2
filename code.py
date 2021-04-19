import numpy as np
from openpyxl import load_workbook


def read_data(path):

    workbook = load_workbook(path)
    booksheet = workbook.active
    rows = booksheet.rows
    columns = booksheet.columns

    food = np.zeros((600,4))
    fire = np.zeros((600,4))

    start = np.zeros((3))
    end = np.zeros((3))

    fire_cnt = 0
    food_cnt = 0
    cnt = 0

    # 迭代所有的行
    for row in rows:
        cnt = cnt + 1
        cell_data_1 = booksheet.cell(row=cnt, column=2).value
        cell_data_2 = booksheet.cell(row=cnt, column=3).value
        cell_data_3 = booksheet.cell(row=cnt, column=4).value
        cell_data_4 = booksheet.cell(row=cnt, column=5).value
        cell_data_5 = booksheet.cell(row=cnt, column=6).value

        if (cell_data_5 == 0):
            if(cnt == 2):
                start[0] = cell_data_1
                start[1] = cell_data_2
                start[2] = cell_data_3
            else:
                end[0] = cell_data_1
                end[1] = cell_data_2
                end[2] = cell_data_3

        if(cell_data_5 != 0 and cnt != 1):
            if(cell_data_4 == 0):
                fire[fire_cnt][0] = cell_data_1
                fire[fire_cnt][1] = cell_data_2
                fire[fire_cnt][2] = cell_data_3
                fire[fire_cnt][3] = cell_data_5
                fire_cnt += 1
            else:
                food[food_cnt][0] = cell_data_1
                food[food_cnt][1] = cell_data_2
                food[food_cnt][2] = cell_data_3
                food[food_cnt][3] = cell_data_5
                food_cnt += 1

    fire.resize((fire_cnt, 4))
    food.resize((food_cnt, 4))

    return start, end, fire, food


def problem1(start, end, fire, food):
    print()


def problem2(start, end, fire, food):
    print()


def problem3(start, end, fire, food):
    print()


def main():
    data_path = "C:\\Users\\lenovo\\Desktop\\path.xlsx"
    start, end, fire, food = read_data(data_path)
    print("fire_cnt is ", fire.shape)
    print("food_cnt is ", food.shape)
    print("start at ", start)
    print("end at ", end)
    problem1(start, end, fire, food)
    problem2(start, end, fire, food)
    problem3(start, end, fire, food)


main()