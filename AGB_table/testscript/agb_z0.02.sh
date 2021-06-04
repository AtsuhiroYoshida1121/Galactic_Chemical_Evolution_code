#!/bin/bash
elem=o16

awk '{print $1,$4}' ./table/table_a2.txt > ./z0.02/z0.02.txt
awk '$1~/^'$elem'$/' ./z0.02/z0.02.txt > ./z0.02/z0.02_f.txt
cat ./z0.02/z0.02_f.txt | awk '{print NR " " $0;}' > ./z0.02/z0.02_s.txt

cat ./z0.02/z0.02_s.txt | awk '{for (i=1; i<=9; i++);sub($i,"d_",$1);print}' > ./z0.02/z0.02_t.txt

awk '{print $1 $2 " " $3}' ./z0.02/z0.02_t.txt > ./z0.02/z0.02_$elem.txt

rm ./z0.02/z0.02_f.txt
rm ./z0.02/z0.02_s.txt
rm ./z0.02/z0.02_t.txt
