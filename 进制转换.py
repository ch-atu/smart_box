import re
chinese = '''
中国人不骗中国人
'''
# chinese = '1234567890'
# 字符串生成十六进制
hex_chinese = chinese.encode('gbk')
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
hex_chinese = hex_chinese.hex()
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
hex_chinese = ' '.join(re.findall(r'.{2}', hex_chinese))
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
print(chinese)
