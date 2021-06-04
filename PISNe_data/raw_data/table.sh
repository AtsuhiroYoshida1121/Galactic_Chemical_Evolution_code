#!/bin/bash


tr -d "\I{ " < pisne_rawdata.txt > a.txt
tr -d "}" < a.txt > b.txt
sed -e 's/&/   /g' b.txt > c.txt
sed -e 's/\\//g' c.txt > d.txt
sed -e 's/EE/ /g' d.txt > pisne_table.txt 

for i in a b c d
do
rm ${i}.txt
done


