import socket
import queue
import threading

def Pscan():


        ip = input(" Target ip: ")
        q = queue.Queue()


        for i in range(1, 65536):
                q.put(i)


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


        for i in range(50):


                t = threading.Thread(target=scan, daemon=True)
                t.start()


        q.join()
        print('\nfinished :D')
