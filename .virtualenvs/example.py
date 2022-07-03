from autodetect import AutoDetectSerialPort

if __name__ == '__main__':
    # Example usage:
    # Autodetect
    autoconnect = AutoDetectSerialPort()
    autoconnect.begin()
    print(autoconnect.serial)
    
    # Manual connect
    # first argument is the port
    # second argument is the force flag
    autoconnect = AutoDetectSerialPort("dev/ttyUSB0", 1)
    autoconnect.begin()
    
    # Access the Serial object
    print(autoconnect.serial)