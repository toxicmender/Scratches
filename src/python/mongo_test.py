#!/usr/bin/env python3

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

choice = (input("Are you using MongoDB locally (using localhost:27017) [y/n]? ")).lower()
if choice == 'y' or choice == 'yes':
    client = MongoClient()
    db = client.admin
else:
    # connect to MongoDB
    u = input("Enter your connection string to MongoDB: ")
    p = int(input("Enter port number: "))
    client = MongoClient(u, p)
    db = client.admin

# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
