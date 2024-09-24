# Main console function
def main_console():


        # Imports
        import os
        import sys
        import time

        # Tool function import
        from pscan import Pscan
        from trackphone import Tracker
        from dnsr import DNSResolver


        # Console
        while True:
                inp = input('>> ')


                if inp == 'exit':
                        print('Bye :D')
                        time.sleep(1.0)
                        break

                elif inp == 'ls':
                        print("""~ Tools
pscan
trackphone
dnsr\n""")

                elif inp == 'clear':
                        os.system('clear')

                elif inp == 'use':
                        print('! RESOLVE LOGO ESSA PORRA')
                        print('%s'(sys.argv[1]))

                elif inp == 'pscan':
                        Pscan()

                elif inp == 'trackphone':
                        Tracker()

                elif inp == 'dnsr':
                        DNSResolver()


# Exec console
main_console()
