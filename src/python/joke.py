#!/usr/bin/env python3

import urllib.request
import json
import argparse

def joke(r):
    req = urllib.request.Request("http://api.icndb.com/jokes/"+r)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("HTTP Error code: ", e.code)
    except urllib.error.URLError as e:
        print("URL Error Reason: ", e.reason)
    else:
        full_json = json.loads(response.read())
        return full_json['value']

def categories():
    req = urllib.request.Request("http://api.icndb.com/categories")
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("HTTP Error code: ", e.code)
    except urllib.error.URLError as e:
        print("URL Error Reason: ", e.reason)
    else:
        full_json = json.loads(response.read())
        return full_json['value']

def count():
    req = urllib.request.Request("http://api.icndb.com/jokes/count")
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("HTTP Error code: ", e.code)
    except urllib.error.URLError as e:
        print("URL Error Reason: ", e.reason)
    else:
        full_json = json.loads(response.read())
        return full_json['value']

parser = argparse.ArgumentParser(description="Command line utility with a sense of humour. Uses icndb API to GET a random joke & help improve your sense of humour")
group = parser.add_mutually_exclusive_group()
parser.add_argument("-t", "--type", choices=categories(), help="Type of joke")
group.add_argument("-c", "--count", type=int, choices=[x for x in range(1,count()+1)], help="Number of jokes to display")
group.add_argument("-s", "--specific", type=int, choices=[x for x in range(1,count()+1)], help="Display a specific joke by it's id")
args = parser.parse_args()

if args.specific:
    j = joke(r=str(args.specific))
    print(j['joke'])
elif args.count:
    if args.type in categories():
        j = joke(r=("random/"+str(args.count)+"?limitTo=["+args.type+"]"))
        for i in range(args.count):
            print(j[i]['joke'])
    else:
        j = joke(r=("random/"+str(args.count)))
        for i in range(args.count):
            print(j[i]['joke'])
elif args.type:
    j = joke(r="random?limitTo=["+args.type+"]")
    print(j['joke'])
else:
    j = joke(r="random")
    print(j['joke'])
