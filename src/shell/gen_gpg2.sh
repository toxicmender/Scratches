#!/bin/sh

echo "Only useful for generating first gpg key"
echo "Enter key type as \"RSA and RSA\""
echo "Enter key size as \'4096\'"
echo "Choose the rest as required"
echo "key exported (armored) as \"key.txt\""

gpg2 --full-gen-key
HASH=$(gpg2 --list-secret-keys --keyid-format LONG | grep -i sec | cut -d '/' -f 2 | cut -d ' ' -f 1)
gpg2 --armor --export $HASH > key.txt
git config --global user.signingkey $HASH
git config --global commit.gpgsign true
