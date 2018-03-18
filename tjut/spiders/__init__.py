# # This package will contain the spiders of your Scrapy project
# #
# # Please refer to the documentation for information on how to create and manage
# # your spiders.
# # coding=utf-8
# import sys
# import requests
# from lxml import etree
# import re
# import StringIO
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# response = requests.get('http://news.tjut.edu.cn/info/1002/18224.htm')
# # print response.content
# response = etree.HTML(response.content)
#
# title = response.xpath('//*[@id="main"]/div[2]/div[1]/table/tbody/tr/td/form/table/tr[1]//text()')[0]
# temp = response.xpath('//script[2]/text()')[0]
# wbnewsid = re.search(r"getClickTimes\('(\d*)','(\d*)','(.*?)',''\)",temp).group(1)
# owner = re.search(r"getClickTimes\('(\d*)','(\d*)','(.*?)',''\)",temp).group(2)
# count = requests.get('http://news.tjut.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={}&owner={}'.format(wbnewsid, owner)).json()['wbshowtimes']
#
# list_one = response.xpath('//*[@id="main"]/div[2]/div[1]/table/tbody/tr/td/form/table//tr[2]/td/span/text()')
# list_one.insert(-1, str(count))
# print ''.join(list_one)
# content = response.xpath('//*[@id="main"]/div[2]/div[1]/table/tbody/tr/td/form/table//tr[4]/td/div/div/p')
# # print len(content)
#
#
#
#
#
# from docx import Document
# from docx.shared import Inches
#
# document = Document()
# document.add_heading(title, 0)
#
# document.add_heading(''.join(list_one), level=2)
#
# for i in content:
#     if i.xpath('./img/@src'):
#         path = i.xpath('./img/@src')[0][5:]
#         path = path[path.rfind('/'):]
#         # with open('../../news'+path, 'wb') as f:
#         #     f.write(requests.get('http://news.tjut.edu.cn'+i.xpath('./img/@src')[0][5:]).content)
#         # s = requests.get('http://news.tjut.edu.cn' + i.xpath('./img/@src')[0][5:]).content
#         img = StringIO.StringIO()
#         img.write(requests.get('http://news.tjut.edu.cn'+i.xpath('./img/@src')[0][5:]).content)
#         img.seek(0)
#         document.add_picture(img, width=Inches(6))
#
#     else:
#         document.add_paragraph(i.xpath('string(.)'))
#         print i.xpath('string(.)')
#
#
# # document.add_page_break()
#
#
#
# document.save('../../news/'+title.encode('utf-8')+'.docx')
#
