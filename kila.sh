#!/bin/bash
# kila.sh
while true; do
if ps ax | grep $1 | grep -v ' grep '; then
killall $1
fi
done