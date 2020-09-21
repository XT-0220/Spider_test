from lxml import etree

text = ''' 
<div> 
  <ul> 
    <li class="item-1">
      <a href="link1.html">first item</a>
    </li> 
    <li class="item-1">
      <a href="link2.html">second item</a>
    </li> 
    <li class="item-inactive">
      <a href="link3.html">third item</a>
    </li> 
    <li class="item-1">
      <a href="link4.html">fourth item</a>
    </li> 
    <li class="item-0">
      a href="link5.html">fifth item</a>
  </ul> 
</div>
'''
# 1.-----------------------------------------------------
# html = etree.HTML(text)
#
# # 获取href的列表和title的列表
# href_list = html.xpath("//li[@class='item-1']/a/@href")
# title_list = html.xpath("//li[@class='item-1']/a/text()")
#
# # 组装成字典
# for href in href_list:
#     item = {}
#     item['href'] = href
#     item['title'] = title_list[href_list.index(href)]
#     print(item)
# 2.--------------------------------------------------
# 先分组，再提取数据，可以避免数据的错乱;对于空值要进行判断
# 根据li标签进行分组
html = etree.HTML(text)
li_list = html.xpath("//li[@class='item-1']")

# 在每一组中继续进行数据的提取
for li in li_list:
    item = {}
    item["href"] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href"))>0 else None
    item["title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()"))>0 else None
    print(item)