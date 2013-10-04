#!/bin/bash
count=0
while read line
do
    count=$(expr $count + 1)
done < $1
echo "El fichero $1 tiene $count líneas"