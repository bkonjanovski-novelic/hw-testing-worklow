import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
 
def echo_serial(input: bytes):
        if not isinstance(input, (bytes)) or len(input) != 1:  
                raise TypeError("Input must be a single byte")  
        ser.write(input)
        res = ser.read(1)
        return res.decode()