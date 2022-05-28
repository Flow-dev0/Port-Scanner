import threading
import socket
import json

open_port_list = []

try:
    f = open("target_connection.config", "r")
    target = (f.readline())
except:
    print("Provide a valid IP address in 'target_connection' file ")


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect_ex((target, port))

        # Store list of open ports
        if con == 0:
            print("Port {} is open".format(port))
            open_port_list.append(port)

        data = {
            "open_port": open_port_list
        }

        with open("open_ports.json", "w") as write_file:
            json.dump(data, write_file)

        con.close()
    except:
        pass


multi = 1
for x in range(1, 65535):
    t = threading.Thread(target=portscan, kwargs={"port": multi})
    multi += 1
    t.start()
