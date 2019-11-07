import  telnetlib
import threading

def telnet_1(ip,port):
    server = telnetlib.Telnet()
    with open('D:\\test\\test.txt', 'a') as f:
        try:
             server.open(ip,port)

             print ('{} {}端口通'.format(ip,port),file=f)

        except Exception:

             print('{} {}端口不通'.format(ip, port),file=f)

        finally:
             server.close()


def main(ip_1,port_1):

     #dirc={"172.21.150.17":19000}
     #for ip, port in dirc.items():

     telnet_1(ip_1,port_1)


if __name__ == '__main__':
     main()
