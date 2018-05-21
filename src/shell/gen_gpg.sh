#!/bin/sh

echo "Only useful for generating first gpg key\n\n"
echo "Enter key type as \"RSA and RSA\"\n\n"
echo "Enter key size as \'4096\'\n\n"
echo "Choose the rest as required\n\n"
echo "key exported (armored) as \"key.txt\"\n\n"

gpg --gen-key
HASH=$(gpg --list-secret-keys --keyid-format LONG | grep -e 4096 | head -1 | cut -d '/' -f 2 | cut -d ' ' -f 1)
gpg --armor --export $HASH > key.txt
git config --global user.signingkey $HASH
git config --global commit.gpgsign true
