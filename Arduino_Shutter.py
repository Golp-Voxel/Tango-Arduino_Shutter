'''
    This Tango Class device server is for the NewPort AG_UC8 Controller
    
    It uses the qcodes_contrib_drivers basics functions
    
    https://qcodes.github.io/Qcodes_contrib_drivers/examples/Newport_AG-UC8.html

'''


import time
import json
import tango

from tango import AttrQuality, AttrWriteType, DevState, DispLevel, AttReqType, Database
from tango.server import Device, attribute, command
from tango.server import class_property, device_property



class Arduino_Shutter(Device):
    Arduino_Shutter = {}

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
        AG_UC8 =        {
                            "Name"      : <user_name_given_on Connect>,
                            "COM"       : 0,
                        }
    '''    


    @command(dtype_in=str,dtype_out=str)  
    def Connect(self,AG_UC8):
      

        return "Stuff"
    


        
if __name__ == "__main__":
    Arduino_Shutter.run_server()
