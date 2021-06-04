#!/bin/bash
#elem=p
#elem=he4
#elem=fe56
#elem=mg24
elem=o16

awk '{print $1,$4}' ./table/table_a2.txt > ./z0.004/z0.004.txt
awk '$1~/^'$elem'$/' ./z0.004/z0.004.txt > ./z0.004/z0.004_f.txt
cat ./z0.004/z0.004_f.txt | awk '{print NR " " $0;}' > ./z0.004/z0.004_s.txt

cat ./z0.004/z0.004_s.txt | awk '{for (i=1; i<=9; i++);sub($i,"d_",$1);print}' > ./z0.004/z0.004_t.txt

awk '{print $1 $2 " " $3}' ./z0.004/z0.004_t.txt > ./z0.004/z0.004_$elem.txt

rm ./z0.004/z0.004_f.txt
rm ./z0.004/z0.004_s.txt
rm ./z0.004/z0.004_t.txt

