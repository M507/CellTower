import requests


def get_data(host, port):
    # api-endpoint
    URL = "http://{}:{}/logs/pfsense/_search".format(host, port)

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    return r.json()


"""
Print all credentials


Standard outputs:
========================
IP: 192.168.1.254
TYPE: Pfsense credentials
USERNAME: admin
PASSWORD: pfsense
========================
"""


def print_logs(host, port, specific_ip = None):
    data = get_data(host, port)
    HITs = data['hits']
    for hit in HITs['hits']:
        print("========================")
        ID = str(hit['_id']).replace('DOT', '.')
        if specific_ip is not None:
            if ID != specific_ip:
                continue
        USERNAME = hit['_source']['username']
        PASSWORD = hit['_source']['password']
        print("IP: " + ID)
        print("TYPE: Pfsense credentials")
        print("USERNAME: " + USERNAME)
        print("PASSWORD: " + PASSWORD)
    print("========================")


if __name__ == '__main__':
    # Host
    host = "10.10.1.140"
    # Port
    port = "9200"
    print_logs(host, port)
