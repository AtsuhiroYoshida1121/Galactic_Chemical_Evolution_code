#!/bin/bash

#for elem in c12 fe56 mg24 o16
#for elem in n14 na23 al27 si28 p31 s32 ni58 co59 
for elem in zn64 ca40 k39 sc45 ti48 v51 cr52 mn55

do 

sed -e "s/cu63/${elem}/g" small.txt > ${elem}.txt

done

#cat c12.txt fe56.txt mg24.txt o16.txt > fin.txt
#cat n14.txt na23.txt al27.txt si28.txt p31.txt s32.txt ni58.txt co59.txt > fin.txt
cat zn64.txt ca40.txt k39.txt sc45.txt ti48.txt v51.txt cr52.txt mn55.txt > fin.txt

#for elem in c12 fe56 mg24 o16
#for elem in n14 na23 al27 si28 p31 s32 ni58 co59 
for elem in zn64 ca40 k39 sc45 ti48 v51 cr52 mn55
do

rm ${elem}.txt

done
