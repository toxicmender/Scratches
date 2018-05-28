#!/usr/bin/env python3
# coding: utf-8

import shodan

print ("""
 /$$$$$$$$ /$$                       /$$$$$$ /$$               /$$ /$$                              /$$$$$           /$$
|__  $$__/| $$                      |_  $$_/| $$              | $$|__/                             |__  $$          | $$
   | $$   | $$$$$$$   /$$$$$$         | $$ /$$$$$$    /$$$$$$ | $$ /$$  /$$$$$$  /$$$$$$$             | $$  /$$$$$$ | $$$$$$$
   | $$   | $$__  $$ /$$__  $$        | $$|_  $$_/   |____  $$| $$| $$ |____  $$| $$__  $$            | $$ /$$__  $$| $$__  $$
   | $$   | $$  \ $$| $$$$$$$$        | $$  | $$      /$$$$$$$| $$| $$  /$$$$$$$| $$  \ $$       /$$  | $$| $$  \ $$| $$  \ $$
   | $$   | $$  | $$| $$_____/        | $$  | $$ /$$ /$$__  $$| $$| $$ /$$__  $$| $$  | $$      | $$  | $$| $$  | $$| $$  | $$
   | $$   | $$  | $$|  $$$$$$$       /$$$$$$|  $$$$/|  $$$$$$$| $$| $$|  $$$$$$$| $$  | $$      |  $$$$$$/|  $$$$$$/| $$$$$$$/
   |__/   |__/  |__/ \_______/      |______/ \___/   \_______/|__/|__/ \_______/|__/  |__/       \______/  \______/ |_______/
                                     Using the SHODAN API to identify HackingTeam C&C Servers.
                                     Python3 version of the original from https://github.com/0x27/TheItalianJob
""")

SHODAN_API_KEY = "" #API Key Here
api = shodan.Shodan(SHODAN_API_KEY)
try:
    # Search Shodan
    results = api.search("Apache/2.4.4 (Unix) OpenSSL/1.0.0g 290")

    # Show the results
    print("[+] ITALIANS FOUND: {}".format(results['total']))
    for result in results['matches']:
        print("[!] ITALIAN DISCOVERED: {}".format(result['ip_str']))
            # hack(result['ip_str'].strip()) # h4v3 j00 th3 0bay w4r3z?!
except shodan.APIError as e:
    print("Error: {}".format(e))
