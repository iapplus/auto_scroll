from lxml import etree

tree = etree.HTML("""
    <div><a href="baidu.com">链接</a></div>
""")
form = etree.tostring(tree,encoding='utf-8').decode()
print(form)
x = tree.xpath("//div/a/@href")
print(x)