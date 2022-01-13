import serial
import string
import binascii
s=serial.Serial('com4',9600)
s.open()
#接收
n=s.inwaiting()
if n:
  data= str(binascii.b2a_hex(s.read(n)))[2:-1]
  print(data)
#发送
d=bytes.fromhex('10 11 12 34 3f')
s.write(d)
s.close()