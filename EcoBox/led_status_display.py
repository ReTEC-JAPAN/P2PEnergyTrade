import time
import RPi.GPIO as gpio
import ecoboxlib as lib

if __name__ == '__main__':

    # blinking function
    def blink(pin,msg):
        gpio.output(pin, gpio.HIGH)
        time.sleep(1)
        gpio.output(pin, gpio.LOW)
        time.sleep(1)
        print("LED Blinking on GPIO Port: " + str(pin) + " indicating status: " + msg)
        return

    def trigger_led():
        status = lib.get_switchstate('STATUS', 'status')
        fromgrid = lib.get_switchstate('STATE', 'grid_supply')
        togrid = lib.get_switchstate('STATE', 'grid_dump')

        gpio.setmode(gpio.BCM)

        gpio.setup(4, gpio.OUT)
        gpio.setup(17, gpio.OUT)
        gpio.setup(18, gpio.OUT)
        gpio.setup(24, gpio.OUT)

        gpio.output(4, gpio.LOW)
        gpio.setup(17, gpio.LOW)
        gpio.setup(18, gpio.LOW)
        gpio.setup(24, gpio.LOW)

        if status == 'I':
            for i in range(0, 10):
                gpio.output(4, gpio.HIGH)
                time.sleep(1)
                gpio.output(4, gpio.LOW)
                time.sleep(1)
            print("LED Blinking on GPIO Port 4 (Installed)")
        if status == 'R':
            if fromgrid == 'ON':
                for i in range(0, 10):
                    gpio.output(17, gpio.HIGH)
                    gpio.output(18,gpio.HIGH)
                    if togrid == 'ON':
                        gpio.output(24, gpio.HIGH)
                    time.sleep(1)
                    gpio.output(17, gpio.LOW)
                    gpio.output(18, gpio.LOW)
                    gpio.output(24, gpio.LOW)
                    time.sleep(1)
                print("LED Blinking on GPIO Port 17 (Registered) & 18 (FromGrid)")
            elif togrid == 'ON':
                for i in range(0, 10):
                    gpio.output(17, gpio.HIGH)
                    gpio.output(24, gpio.HIGH)
                    time.sleep(1)
                    gpio.output(17, gpio.LOW)
                    gpio.output(24, gpio.LOW)
                    time.sleep(1)
                print("LED Blinking on GPIO Port 17 (Registered) & 24 (TOGrid)")
            else:
                for i in range(0, 10):
                    gpio.output(17, gpio.HIGH)
                    time.sleep(1)
                    gpio.output(17, gpio.LOW)
                    time.sleep(1)
                print("LED Blinking on GPIO Port 17 (Registered)")
        # set up a list of the channels your program has used

        channels_used = [4, 17, 18, 24]
        for channel in channels_used:
            gpio.cleanup(channel)
        #gpio.cleanup()
        return

    # Run main program by calling trigger_led function
    trigger_led()
