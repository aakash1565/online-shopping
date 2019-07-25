import xlsxwriter
import random
import json
from pdf2image import convert_from_path
from PIL import Image

with open("data.json", "r") as read_file:
    jsonData = json.load(read_file)

hotelSelect = "H6"
workbook = xlsxwriter.Workbook('chart_line_' + hotelSelect + '.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

headings = ['Months in 2018-2019', 'Ratings trend']
excelSheetColumns = { "Jan" : 'A2', "Feb" : 'B2', "Mar" : 'C2', "Apr" : 'D2', 'May' : 'E2', 'Apr' : 'F2','May' : 'G2',
                      'Jul' : 'H2', 'Aug' : 'I2', 'Sep': 'J2', 'Oct':'K2', 'Nov':'L2', 'Dec':'M2' }

worksheet.write_row('A1', headings, bold)
worksheet.write_row('A2', ["Jul, 18", jsonData[hotelSelect]["Jul"]])
worksheet.write_row('A3', ["Aug, 18", jsonData[hotelSelect]["Aug"]])
worksheet.write_row('A4', ["Sep, 18", jsonData[hotelSelect]["Sep"]])
worksheet.write_row('A5', ["Oct, 18", jsonData[hotelSelect]["Oct"]])
worksheet.write_row('A6', ["Nov, 18", jsonData[hotelSelect]["Nov"]])
worksheet.write_row('A7', ["Dec, 18", jsonData[hotelSelect]["Dec"]])
worksheet.write_row('A8', ["Jan, 19", jsonData[hotelSelect]["Jan"]])
worksheet.write_row('A9', ["Feb, 19", jsonData[hotelSelect]["Feb"]])
worksheet.write_row('A10', ["Mar, 19", jsonData[hotelSelect]["Mar"]])
worksheet.write_row('A11', ["Apr, 19", jsonData[hotelSelect]["Apr"]])
worksheet.write_row('A12', ["May, 19", jsonData[hotelSelect]["May"]])
worksheet.write_row('A13', ["Jun, 19", jsonData[hotelSelect]["Jun"]])

chart1 = workbook.add_chart({'type': 'line'})

chart1.add_series({

    'name' : '=Sheet1!$B1',
    'categories': '=Sheet1!$A$2:$A$13',
    'values':     '=Sheet1!$B$2:$B$13',
    'data_labels': {'value': True},
})

chart1.set_title ({'name': 'Hotel rating trend (2018-2019)'})
chart1.set_x_axis({'name': 'Months'})
chart1.set_y_axis({'name': 'Rating'})

chart1.set_style(random.randint(1, 13))
chart1.height = chart1.height*1.9
chart1.width = chart1.width*1.6

worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})


workbook.close()

'''pages = convert_from_path('JS.pdf', 200)

pages[0].save('out.jpg', 'JPEG')

image_obj = Image.open('out.jpg')
cropped_image = image_obj.crop([161, 166, 706, 1050])
cropped_image.save('final.jpg')
cropped_image.show()
'''