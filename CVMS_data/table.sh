#!/bin/bash


tr -d "$^{" < cvms_rawdata.txt > a.txt
tr -d "}$" < a.txt > b.txt
sed -e 's/\\//g' b.txt > c.txt
sed -e 's/&/   /g' c.txt > fin.txt

awk '{print $1, $2, $3, $4, $5}' fin.txt > d.txt
awk '{print $6, $7, $8, $9, $10}' fin.txt > e.txt

cat d.txt  e.txt > cvms_table.txt

for i in a b c d e
do
rm ${i}.txt
done

