import board, busio, time

i2c = None

def reconnect():
    global i2c
    print("[INFO]: Acquiring I2C Lock...")
    if i2c:
        try:
            i2c.unlock()
        except:
            pass
    i2c = busio.I2C(board.SCL, board.SDA)
    i2c.try_lock()
    print("[INFO]: I2C Lock Acquired")

def main():
    global i2c

    try:
        reconnect()
    except Exception as error:
        print(error)

    while True:
        try:
            addresses = i2c.scan()
            print([hex(address) for address in addresses])
            for address in addresses:
                buffer = "Anything".encode("utf-8")
                i2c.writeto(address, buffer)
                buffer = bytearray(512)
                i2c.readfrom_into(address, buffer)
                print(buffer)
            time.sleep(1)
        except Exception as error:
            print(error)
            reconnect()
            time.sleep(1)

if __name__ == "__main__":
    main()