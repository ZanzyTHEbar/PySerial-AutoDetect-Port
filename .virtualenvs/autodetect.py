import sys
import serial
import serial.tools.list_ports
import glob

class AutoDetectSerialPort:
    
    def __init__(self, port = 0, force = 0):
        self.port = port
        self.force = force
        self.serial = None
        
        
    def begin(self):
        if (self.force == 0):
            self.connect_to_serial(*self.serial_ports_auto())
        else:
            self.connect_to_serial(self.port)

    def print_port_details(self):
        ports = serial.tools.list_ports.comports()

        for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))
            
        return ports

    def serial_ports_auto(self):
        
        try:
            ports = serial.tools.list_ports.comports()
            
        except EnvironmentError:
            
            print('Error: could not find any ports using built-in serial module')
            print('Using manual sorting method')
            if sys.platform.startswith('win'):
                ports = ['COM%s' % (i + 1) for i in range(256)]
            elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                # this excludes your current terminal "/dev/tty"
                    ports = glob.glob('/dev/ttyUSB[0-100]*')
            elif sys.platform.startswith('darwin'):
                    ports = glob.glob('/dev/tty.*')
            else:
                raise EnvironmentError('Unsupported platform')
        
        result = []
        for port in ports:
            print("Found port " + port.device)
            try:
                ser = serial.Serial(port)
                if ser.isOpen():
                    ser.close()

                ser.flushInput()
                ser.flushOutput()
                result.append(port)
            except (OSError, serial.SerialException):
                print("Failed to connect to port " + port.device)
                continue
        return result

    def connect_to_serial(self, *ports):
        print("Beginning Connection Handshake...")
        for port in ports:
            print("Attempting connection to port", port)
            try:
                ser = serial.Serial(port, baudrate=9600, timeout=1)
                if ser.isOpen():
                    ser.close()

                ser.flushInput()
                ser.flushOutput()
                print("Connecting to " + ser.name)
                self.serial = ser
            except:
                print("Failed to connect to port", port)
                continue
