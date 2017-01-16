# import xlrd
# book = xlrd.open_workbook('demo.xlsx')
# book.sheets()

# sheet = book.sheet_by_index(0)
# sheet.row(1)
# sheet.row_values(1,1)
# 
import xlrd,xlwt

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,u'scores',None)

for row in xrange(1,rsheet.nrows):
	t = sum(rsheet.row_values(row,1))
	rsheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None)


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizental center')

for r in xrange(rsheet.nrows):
	for c in xrange(rsheet.ncols):
		wsheet.write(r,c,rsheet.cell_value(r,c),style)

wbook.save('output.xlsx')