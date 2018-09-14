import ecoboxlib as lib
import time

if __name__ == '__main__':
    def cloud_connect():
        status = lib.get_switchstate('STATUS', 'status')
        try:
            if status == 'P':
                token = lib.get_token()
                if token:
                    lib.modify_switchstate('TOKEN', 'token', token)
                    if lib.send_config():
                        lib.modify_switchstate('STATUS', 'status', 'I')
                        print("CONFIG Successfully updated")
                    else:
                        print("CONFIG Update Failed")
            else:
                resp = lib.send_pinger()
                if not resp:
                    print("Pinger failed to reach cloud engine.")
        except Exception as e:
            print("type error: " + str(e))
    while True:
        cloud_connect()
        time.sleep(60)

