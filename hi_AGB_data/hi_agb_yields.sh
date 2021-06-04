#!/bin/bash

#elem=p
#elem=he4
#elem=c12
#elem=n14
#elem=o16
#elem=na23
#elem=mg24
#elem=al27
elem=si28
#elem=p31
#elem=s32
#elem=k39
#elem=ca40
#elem=sc45
#elem=ti48
#elem=v51
#elem=cr52
#elem=mn55
#elem=fe56
#elem=ni58
#elem=co59
#elem=cu63
#elem=zn64

### z0.02
awk '{print $1,$3}' ./table/raw_z0.02.txt > ./z0.02/z0.02.txt
awk '$1~/^'$elem'$/' ./z0.02/z0.02.txt > ./z0.02/z0.02_f.txt
cat ./z0.02/z0.02_f.txt | awk '{print NR " " $0;}' > ./z0.02/z0.02_s.txt
cat ./z0.02/z0.02_s.txt | awk '{for (i=1; i<=5; i++);sub($i,"hi_c_",$1);print}' > ./z0.02/z0.02_t.txt
awk '{print $1 $2 "=" $3}' ./z0.02/z0.02_t.txt > ./z0.02/z0.02_$elem.txt

rm ./z0.02/z0.02_f.txt
rm ./z0.02/z0.02_s.txt
rm ./z0.02/z0.02_t.txt

### z0.008
awk '{print $1,$3}' ./table/raw_z0.008.txt > ./z0.008/z0.008.txt
awk '$1~/^'$elem'$/' ./z0.008/z0.008.txt > ./z0.008/z0.008_f.txt
cat ./z0.008/z0.008_f.txt | awk '{print NR " " $0;}' > ./z0.008/z0.008_s.txt
cat ./z0.008/z0.008_s.txt | awk '{for (i=1; i<=5; i++);sub($i,"hi_b_",$1);print}' > ./z0.008/z0.008_t.txt
awk '{print $1 $2 "=" $3}' ./z0.008/z0.008_t.txt > ./z0.008/z0.008_$elem.txt

rm ./z0.008/z0.008_f.txt
rm ./z0.008/z0.008_s.txt
rm ./z0.008/z0.008_t.txt

### z0.004
awk '{print $1,$3}' ./table/raw_z0.004.txt > ./z0.004/z0.004.txt
awk '$1~/^'$elem'$/' ./z0.004/z0.004.txt > ./z0.004/z0.004_f.txt
cat ./z0.004/z0.004_f.txt | awk '{print NR " " $0;}' > ./z0.004/z0.004_s.txt
cat ./z0.004/z0.004_s.txt | awk '{for (i=1; i<=4; i++);sub($i,"hi_a_",$1);print}' > ./z0.004/z0.004_t.txt
awk '{print $1 $2 "=" $3}' ./z0.004/z0.004_t.txt > ./z0.004/z0.004_$elem.txt

rm ./z0.004/z0.004_f.txt
rm ./z0.004/z0.004_s.txt
rm ./z0.004/z0.004_t.txt 

### table connect

awk 1 ./z0.004/z0.004_$elem.txt ./z0.008/z0.008_$elem.txt ./z0.02/z0.02_$elem.txt > $elem.py
mv $elem.py ../hi_AGB_yields/ 
