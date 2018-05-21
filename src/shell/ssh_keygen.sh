#!/usr/bin/env bash

# Generate key with email as label

ssh-keygen -t rsa -b 4096 -C "danish.parvez19@gmail.com"

# 

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_rsa

# Testing connection to GitHub

ssh -T git@github.com

