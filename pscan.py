import socket
import queue
import threading

def Pscan():

        # Imports
        import socket
        import queue
        import threading

        
        ip = input("# Target ip: ")
        # Queue list
        q = queue.Queue()


        # Add ports in queue
        for i in range(1, 65536):
                q.put(i)


        # Scan script
        def scan():                                     

                while not q.empty():
                        port = q.get()
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

                                try:
                                        c = s.connect((ip, port))
                                        print(f'[+] {port} - OPEN')

                                except:
                                        pass
                        q.task_done()

        # Create threads
        for i in range(50):


                t = threading.Thread(target=scan, daemon=True)
                t.start()


        # Finish
        q.join()
        print('\nfinished :D')
