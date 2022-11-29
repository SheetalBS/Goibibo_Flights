import xlrd
from Library.config_flights import ConfigFlights

def read_locators():
    workbook = xlrd.open_workbook(r"C:\Users\User\Desktop\goibibo data\Goibibo_loctors.xlsx")
    worksheet = workbook.sheet_by_name("Goibibo_locators")
    rows = worksheet.nrows
    d = {}

    for i in range(rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1], row[2])
    return d



def read_data():
    workbook = xlrd.open_workbook(ConfigFlights.TEST_DATA_PATH)
    worksheet = workbook.sheet_by_name('test_data_input')
    rows = worksheet.get_rows()
    header = next(rows)
    columns = worksheet.ncols
    list1 = []
    for i in rows:
        values = ()
        for j in range(columns):
            values +=(i[j].value,)
        list1.append(values)
    return list1

print(read_locators())
print("**************")
print(read_data())