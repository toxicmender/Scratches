#!/usr/bin/env bash

echo "Select RSA & RSA as the kind of key \n\nKey size: 4096 \n\n"

gpg --full-generate-key

HASH=$(gpg --list-secret-keys --keyid-format LONG | grep 'sec' | cut -d ' ' -f 2 | cut -d '/' -f 2)

gpg --armor --export $HASH > key.txt

git config --global user.signingkey $HASH

#echo 'export GPG_TTY=$(tty)' >> ~/.bashrc
