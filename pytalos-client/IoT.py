import serial
import time
import io
from client import *

Datoin='';



Bandera = False
cl = client("http://192.168.5.200:8545")
def Envia_BCH(Dato):
        global cl
        result = cl.call_sm(Dato)
        print("resultado: ",result)

def Recibe_valor():
        while True:
                try:
                        Datoin=str(ESP32Lora.read(3))
                        Datoin=Datoin.lstrip('b')
                        Datoin=Datoin.strip('\'')
                        if (len(Datoin))>2:
                                print(Datoin)
                                Envia_BCH(int(Datoin))
                        Datoin=''
                        ESP32Lora.reset_input_buffer()
                        ESP32Lora.reset_output_buffer()
                        break

                except KeyboardInterrupt:
                        print("Exiting")
                        break
                time.sleep(0.1)


try:
        ESP32Lora = serial.Serial('/dev/ttyUSB0',115200, timeout=1)
        time.sleep(1.8)

        ESP32Lora.reset_input_buffer()
        ESP32Lora.reset_output_buffer()


except serial.SerialException:
    print('Port is not available')
    Bandera = True

except serial.portNotOpenError:
    print('Attempting to use a port that is not open')
    print('End of script')
    Bandera = True


while True:
        if Bandera:
                print('ESP32 Lora sin conexion')
        else:
                Recibe_valor()
                time.sleep(0.2)
