import socket

# This part is like just dialing the phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#this is your first hello on that call
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) # your hello got sent out to server side

# this is we are recieveing that hello from server side
while True:
    data = mysock.recv(5120) #we are receiving 512 character
    if (len(data) < 1): #if the data is no more in the file just break the loop and close the connection
        break
    print(data.decode())
mysock.close()

# Ans:
"""
HTTP/1.1 200 OK
Date: Sun, 13 Mar 2022 15:21:11 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief

"""
