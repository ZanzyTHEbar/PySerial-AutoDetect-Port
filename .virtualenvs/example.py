from autodetect import AutoDetectSerialPort

if __name__ == '__main__':
    # Example usage:
    # Autodetect
    autoconnect = AutoDetectSerialPort()
    autoconnect.begin()
    print(autoconnect.serial)
    
    # Manual connect linux
    # first argument is the port
    # second argument is the force flag
    autoconnect = AutoDetectSerialPort("dev/ttyUSB0", 1)
    autoconnect.begin()
    
    # Access the Serial object
    print(autoconnect.serial)
    
    # Manual connect Windows
    # first argument is the port
    # second argument is the force flag
    autoconnect = AutoDetectSerialPort("COM5", 1)
    autoconnect.begin()
    
    # Access the Serial object
    print(autoconnect.serial)