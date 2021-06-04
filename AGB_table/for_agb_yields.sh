#!/bin/bash

for elem in p he4 c12 n14 o16 na23 mg24 al27 si28 p31 s32 k39 ca40 sc45 ti48 v51 cr52 mn55 fe56 ni58 co59 cu63 zn64

do

### z0.02

awk '{print $1,$4}' ./table/table_a2.txt > ./z0.02/z0.02.txt
awk '$1~/^'$elem'$/' ./z0.02/z0.02.txt > ./z0.02/z0.02_f.txt
cat ./z0.02/z0.02_f.txt | awk '{print NR " " $0;}' > ./z0.02/z0.02_s.txt

cat ./z0.02/z0.02_s.txt | awk '{for (i=1; i<=9; i++);sub($i,"d_",$1);print}' > ./z0.02/z0.02_t.txt
awk '{print $1 $2 "=" $3}' ./z0.02/z0.02_t.txt > ./z0.02/z0.02_$elem.txt

rm ./z0.02/z0.02_f.txt
rm ./z0.02/z0.02_s.txt
rm ./z0.02/z0.02_t.txt

### z0.008

awk '{print $1,$4}' ./table/table_a3.txt > ./z0.008/z0.008.txt
awk '$1~/^'$elem'$/' ./z0.008/z0.008.txt > ./z0.008/z0.008_f.txt
cat ./z0.008/z0.008_f.txt | awk '{print NR " " $0;}' > ./z0.008/z0.008_s.txt

cat ./z0.008/z0.008_s.txt | awk '{for (i=1; i<=9; i++);sub($i,"c_",$1);print}' > ./z0.008/z0.008_t.txt

awk '{print $1 $2 "=" $3}' ./z0.008/z0.008_t.txt > ./z0.008/z0.008_$elem.txt

rm ./z0.008/z0.008_f.txt
rm ./z0.008/z0.008_s.txt
rm ./z0.008/z0.008_t.txt


### z0.004

awk '{print $1,$4}' ./table/table_a4.txt > ./z0.004/z0.004.txt
awk '$1~/^'$elem'$/' ./z0.004/z0.004.txt > ./z0.004/z0.004_f.txt
cat ./z0.004/z0.004_f.txt | awk '{print NR " " $0;}' > ./z0.004/z0.004_s.txt

cat ./z0.004/z0.004_s.txt | awk '{for (i=1; i<=9; i++);sub($i,"b_",$1);print}' > ./z0.004/z0.004_t.txt

awk '{print $1 $2 "=" $3}' ./z0.004/z0.004_t.txt > ./z0.004/z0.004_$elem.txt

rm ./z0.004/z0.004_f.txt
rm ./z0.004/z0.004_s.txt
rm ./z0.004/z0.004_t.txt

### z0.0001

awk '{print $1,$4}' ./table/table_a5.txt > ./z0.0001/z0.0001.txt
awk '$1~/^'$elem'$/' ./z0.0001/z0.0001.txt > ./z0.0001/z0.0001_f.txt
cat ./z0.0001/z0.0001_f.txt | awk '{print NR " " $0;}' > ./z0.0001/z0.0001_s.txt

cat ./z0.0001/z0.0001_s.txt | awk '{for (i=1; i<=9; i++);sub($i,"a_",$1);print}' > ./z0.0001/z0.0001_t.txt

awk '{print $1 $2 "=" $3}' ./z0.0001/z0.0001_t.txt > ./z0.0001/z0.0001_$elem.txt

rm ./z0.0001/z0.0001_f.txt
rm ./z0.0001/z0.0001_s.txt
rm ./z0.0001/z0.0001_t.txt


### table connect

awk 1 ./z0.0001/z0.0001_$elem.txt ./z0.004/z0.004_$elem.txt ./z0.008/z0.008_$elem.txt ./z0.02/z0.02_$elem.txt > $elem.py
mv $elem.py ../AGB_yields/

done


