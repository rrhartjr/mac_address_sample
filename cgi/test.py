#!/usr/bin/env python
import os
from urllib.parse import parse_qs

import requests as requests
import cgitb

cgitb.enable()


def send_request(mac_address):
    # go to this URL to confirm message sent
    # this will be replaced with call to marketing site
    requests.post('https://hookb.in/dmpe1b9j1bux8Yjj80Zw', data={'mac_address': mac_address})


def handle_request():
    # get mac address from request
    params = parse_qs(os.environ['QUERY_STRING'])
    if 'mac_address' not in params:
        raise ValueError("MAC address not provided")

    mac_address = params['mac_address'][0]
    send_request(mac_address)

    print("Content-Type: text/html")
    print()
    print(f"""<html><body>
<h3>MAC Address Updated: {mac_address}</h3>
</body></html>
""")


handle_request()