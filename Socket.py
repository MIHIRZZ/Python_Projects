import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)       without this it can receive very fast
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

# Code: http://www.py4e.com/code3/urljpeg.py

# Ans:
"""
5120 5120
2140 7260
5120 12380
2140 14520
5120 19640
5120 24760
2828 27588
5120 32708
3592 36300
5120 41420
5120 46540
1376 47916
5120 53036
5120 58156
1376 59532
5120 64652
5120 69772
2828 72600
5120 77720
5044 82764
5120 87884
5120 93004
2828 95832
5120 100952
5120 106072
1376 107448
5120 112568
5120 117688
5120 122808
5120 127928
5120 133048
536 133584
5120 138704
5120 143824
5120 148944
5120 154064
5120 159184
1988 161172
5120 166292
5120 171412
5120 176532
5120 181652
5120 186772
536 187308
5120 192428
5120 197548
5120 202668
5120 207788
5120 212908
4892 217800
5120 222920
5120 228040
2568 230608
Header length 394
HTTP/1.1 200 OK
Date: Sun, 13 Mar 2022 15:19:45 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Mon, 15 May 2017 12:27:40 GMT
ETag: "38342-54f8f2e5b6277"
Accept-Ranges: bytes
Content-Length: 230210
Vary: Accept-Encoding
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: image/jpeg
"""
