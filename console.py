import os                                               
import sys
import time
                                                                                                                
def port_scan():                                        
                                                                
        scan_command = f'python3 /data/data/com.termux/files/home/MIBkit/modulos/pscan.py'                              
        os.system(scan_command)
                                                        
def track_phone():

                                                                
        track_phone_command = f'python3 /data/data/com.termux/files/home/MIBkit/modulos/trackphone.py'
        os.system(track_phone_command)


while True:
        inp = input('>> ')


        if inp == 'exit':
                print('Bye :D')
                time.sleep(1.0)
                break

        elif inp == 'ls':
                list = os.listdir('/data/data/com.termux/files/home/MIBkit/modulos')
                print('~ Tools')
                print(list)

        if inp == 'use':
                print('! RESOLVE LOGO ESSA PORRA')
                print('%s'(sys.argv[1]))

        elif inp == 'pscan':
                port_scan()

        elif inp == 'trackphone':
                track_phone()
