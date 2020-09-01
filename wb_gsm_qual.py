
import serial

ser = serial.Serial()
ser.port = "/dev/ttyGSM"
ser.baudrate = 115200
ser.open()

def readData():
    buffer = ""
    while True:
        oneByte = ser.read(1)
        if oneByte == b"\n":
            return buffer
        else:
            buffer += oneByte.decode("ascii")

def sendData(command, timeout):
    fullcommand = "{}\r\n".format(command)
    ser.write_timeout = timeout # This is where you can set the timeout
    bytes_written = ser.write(fullcommand)
    # Check to see if all the data was written
    if bytes_written == len(fullcommand):
        st = format(fullcommand)
    else:
        print('Not all data transferred')


sendData("AT+CSQ", 5) # Expecting "OK" back
temp = format(readData())
s = format(readData())
s1 = int(s[-2:-1])
s2 = -111-(int(s[-5:-3])*-1.9)
s3 = "{\"level\":"+str(s2)+",\"bit-error\":"+str(s1)+",\"version\":\"0.1\"}"
print s3
