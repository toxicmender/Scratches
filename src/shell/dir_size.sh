#!/usr/bin/env sh

for path in ./*; do
    [ -d "${path}" ] || continue
    dirname="$(basename "${path}")"
    du -bsh $dirname
done
