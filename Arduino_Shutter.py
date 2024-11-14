'''
    This Tango Class device server is for the NewPort AG_UC8 Controller
    
    It uses the qcodes_contrib_drivers basics functions
    
    https://qcodes.github.io/Qcodes_contrib_drivers/examples/Newport_AG-UC8.html

'''


import time
import json
import tango
import serial

from tango import AttrQuality, AttrWriteType, DevState, DispLevel, AttReqType, Database
from tango.server import Device, attribute, command
from tango.server import class_property, device_property



class Arduino_Shutter(Device):
    Arduino_Shutter_D = {}

    host = device_property(dtype=str, default_value="localhost")
    port = class_property(dtype=int, default_value=10000)


    def init_device(self):
        super().init_device()
        self.info_stream(f"Connection details: {self.host}:{self.port}")
        self.set_state(DevState.ON)
        self.set_status("Arduino Controlling a Thorlabs Shutter Driver is ON, you need to connect a camera")


    def delete_device(self):
        return 



    '''
        ArduinoInfo =        {
                            "Name"      : <user_name_given_on Connect>,
                            "COM"       : 0
                        }
    '''    


    @command(dtype_in=str,dtype_out=str)  
    def Connect(self,ArduinoInfo):
        AI = json.loads(ArduinoInfo)
        try:
            self.Arduino_Shutter_D[AI["Name"]] = serial.Serial("COM"+str(AI["COM"]), baudrate = 9600)
            return "Device is connected"
        except:
            return "Not possible to connect to the divece"
    
    '''
        Device_to_Open =        {
                                    "Name"      : <user_name_given_on Connect>
                                }
    '''  
    
    @command(dtype_in=str,dtype_out=str)  
    def OpenShutter(self,Device_to_Open):
        DtO=json.loads(Device_to_Open)
        cmd = b'{"action" : "On"}'
        self.Arduino_Shutter_D[DtO["Name"]].flush()
        self.Arduino_Shutter_D[DtO["Name"]].write(cmd)
        self.Arduino_Shutter_D[DtO["Name"]].flush()
        msg = self.Arduino_Shutter_D[DtO["Name"]].read_until(b'\n')
        return msg.decode('utf-8')
    
    @command(dtype_in=str,dtype_out=str)  
    def CloseShutter(self,Device_to_Open):
        DtO=json.loads(Device_to_Open)
        cmd ='{"action" : "Off"}'
        self.Arduino_Shutter_D[DtO["Name"]].write(cmd.encode())
        msg = self.Arduino_Shutter_D[DtO["Name"]].read_until(b'\n')
        return msg.decode('utf-8')
    
    '''
        Device_to_Open =        {
                                    "Name"      : <user_name_given_on Connect>,
                                    "time_ms"   :  100,
                                    "cicles"    :  10   
                                }
    '''  

    @command(dtype_in=str,dtype_out=str)  
    def OperationShutter(self,Device_to_Open):
        DtO=json.loads(Device_to_Open)
        cmd ='{"operation" : {"time_ms":'+str(DtO["time_ms"])+',"cicles":'+str(DtO["cicles"])+'}}'
        self.Arduino_Shutter_D[DtO["Name"]].write(cmd.encode())
        msg = self.Arduino_Shutter_D[DtO["Name"]].read_until(b'\n')
        return msg.decode('utf-8')



        
if __name__ == "__main__":
    Arduino_Shutter.run_server()
