import xlsxwriter
fat='aditi'
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(fat+'.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
ull=1
gull='ass'
# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0
# Iterate over the data and write it out row by row.
worksheet.write(0, 0,     'flag')
worksheet.write(0, 1, 'ans')
worksheet.write(1, 0,     ull)
worksheet.write(1, 1, gull)
workbook.close()
