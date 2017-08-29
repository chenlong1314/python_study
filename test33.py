# -*- coding: utf-8 -*-
import xlrd
import matplotlib.pyplot  as plt

workbook = xlrd.open_workbook('student.xlsx')
sheet = workbook.sheet_by_index(0)
row_count = sheet.nrows
col_count = sheet.ncols

datax = []
for i in range(1, row_count):
    datax.append(sheet.cell_value(i,5))


datay = []
for j in range(1, row_count):
    datay.append(sheet.cell_value(j,2))


print(datax)
print(datay)
plt.title("student")
plt.xlabel("name")
plt.ylabel("scores")
plt.bar(datay,datax)
plt.show()




