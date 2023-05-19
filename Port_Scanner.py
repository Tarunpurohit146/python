import socket
import argparse
import time
import pyfiglet
class Scan:
    def __init__(self,info):
        self.targetip = info['target'] 
        self.port= info['port']
        self.range=info['range'].split('-') if info['range'] else "1-1000".split('-') # if range is None it will use default range 1-1000
        self.list=[]
    def run_scan(self):
        try:
            if self.targetip==None:
                return "Enter target IP"
            elif self.port==None:
                for port in range(int(self.range[0]),int(self.range[1])+1):
                    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
                        socket.setdefaulttimeout(1) #time out 1s
                        result=sock.connect_ex((self.targetip,port)) # check if connection exists
                        if result==0:
                            self.list.append(f"Open port {port}") # if connection exists it will append to self.list
                return "\n".join(self.list) 
            else:
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
                    socket.setdefaulttimeout(1)
                    result=sock.connect_ex((self.targetip,self.port))
                    if result == 0:
                        self.list.append(f'Open port {self.port}')
                        return f'Port open {self.port}'
                    else:
                        return f"Port close {self.port}"
        except KeyboardInterrupt:
            print("Program Ended")
        except:
            print("Please Enter valid input") 
        
if __name__=="__main__":
    print(pyfiglet.figlet_format("Port Scanner"))
    start_time=time.time()
    print(f"Starting Scan.... \n{time.ctime(start_time)}\n---------------------------------------")
    parser=argparse.ArgumentParser()
    parser.add_argument('-t','--target',type=str,help="Traget Ip  example: -t 192.168.1.1")
    parser.add_argument('-p','--port',type=int,help="Port number  example: -p 80 or -p 22")
    parser.add_argument('-r','--range',type=str,help="Range of ports to scan. Default range is 1-1000 example: -r 1-1000 ,-r 22-100")
    args=parser.parse_args()
    s=Scan(vars(args)) # vars() takes args and conver's into dictionary 
    print(s.run_scan())
    print(f"Scanned in:{start_time-time.time():0.5f}")
