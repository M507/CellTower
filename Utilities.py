from config import *

# import modules
import modules.pfsense


def Print_pfsense_credentials(IP = None):
    global host
    global port
    if IP == None:
        modules.pfsense.print_logs(host, port)
    else:
        modules.pfsense.print_logs(host, port, IP)

