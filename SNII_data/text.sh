#!/bin/bash
#zz=z0.001
#zz=z0.004
zz=z0.02

tr -d "{\tiny" < $zz.txt > a.txt
tr -d "$" < a.txt > b.txt
tr -d "}" < b.txt > c.txt
tr -d "&" < c.txt > d.txt
tr -d "^" < d.txt > e.txt
sed -e 's/\\t//g' e.txt > f.txt
sed -e 's/\\//g' f.txt > table_$zz.txt

rm a.txt
rm b.txt
rm c.txt
rm d.txt
rm e.txt
rm f.txt
