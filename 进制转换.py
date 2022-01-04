import re
chinese = '''
GET http://icanhazip.com/ HTTP/1.1
Host: icanhazip.com
User-Agent: Go-http-client/1.1
Accept-Encoding: gzip
Connection: close
'''
# chinese = '1234567890'
# 字符串生成十六进制
hex_chinese = chinese.encode('gbk')
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
hex_chinese = hex_chinese.hex()
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
hex_chinese = ' '.join(re.findall(r'.{2}', hex_chinese))
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
