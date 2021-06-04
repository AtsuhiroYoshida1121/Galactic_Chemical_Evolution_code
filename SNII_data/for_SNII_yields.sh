#!/bin/bash

#elem=p 
#elem=4He 
#elem=12C 
#elem=14N 
#elem=16O 
#elem=23Na 
#elem=24Mg 
#elem=27Al
elem=28Si 
#elem=31P 
#elem=32S 
#elem=39K 
#elem=40Ca 
#elem=45Sc 
#elem=48Ti 
#elem=51V 
#elem=52Cr 
#elem=55Mn 
#elem=56Fe 
#elem=59Co 
#elem=58Ni 
#elem=63Cu 
#elem=64Zn 

for elem in p 4He 12C 14N 16O 23Na 24Mg 27Al 28Si 31P 32S 39K 40Ca 45Sc 48Ti 51V 52Cr 55Mn 56Fe 59Co 58Ni 63Cu 64Zn

do

### z0

awk '$1~/^'$elem'$/' ./table/table_z0.txt > ./table/table_z0a.txt
awk '
{ for (i=1; i<=NF; i++)  { a[NR,i] = $i } } NF>p { p = NF }
END {
    for(j=1; j<=p; j++) { str=a[1,j]; for(i=2; i<=NR; i++){ str=str" "a[i,j]; }
        print str
    }
}' ./table/table_z0a.txt > ./table/table_z0b.txt
sed '1d' ./table/table_z0b.txt > ./table/table_z0c.txt
cat ./table/table_z0c.txt | nl > ./table/table_z0d.txt
sed "s/^/a_y$elem/g" ./table/table_z0d.txt > ./table/table_z0e.txt
awk '{print $1 $2 "=" $3}' ./table/table_z0e.txt >a_$elem.py

rm ./table/table_z0a.txt
rm ./table/table_z0b.txt
rm ./table/table_z0c.txt
rm ./table/table_z0d.txt
rm ./table/table_z0e.txt 

### z0.001

awk '$1~/^'$elem'$/' ./table/table_z0.001.txt > ./table/table_z0.001a.txt
awk '
{ for (i=1; i<=NF; i++) { a[NR,i] = $i } } NF>p { p = NF }
END {
for(j=1; j<=p; j++) { str=a[1,j]; for(i=2; i<=NR; i++){ str=str" "a[i,j]; }
print str
}
}' ./table/table_z0.001a.txt > ./table/table_z0.001b.txt
sed '1d' ./table/table_z0.001b.txt > ./table/table_z0.001c.txt
cat ./table/table_z0.001c.txt | nl > ./table/table_z0.001d.txt
sed "s/^/b_y$elem/g" ./table/table_z0.001d.txt > ./table/table_z0.001e.txt
awk '{print $1 $2 "=" $3}' ./table/table_z0.001e.txt > b_$elem.py

rm ./table/table_z0.001a.txt
rm ./table/table_z0.001b.txt
rm ./table/table_z0.001c.txt
rm ./table/table_z0.001d.txt
rm ./table/table_z0.001e.txt



### z0.004

awk '$1~/^'$elem'$/' ./table/table_z0.004.txt > ./table/table_z0.004a.txt
awk '
{ for (i=1; i<=NF; i++) { a[NR,i] = $i } } NF>p { p = NF }
END {
for(j=1; j<=p; j++) { str=a[1,j]; for(i=2; i<=NR; i++){ str=str" "a[i,j]; }
print str
}
}' ./table/table_z0.004a.txt > ./table/table_z0.004b.txt
sed '1d' ./table/table_z0.004b.txt > ./table/table_z0.004c.txt
cat ./table/table_z0.004c.txt | nl > ./table/table_z0.004d.txt
sed "s/^/c_y$elem/g" ./table/table_z0.004d.txt > ./table/table_z0.004e.txt
awk '{print $1 $2 "=" $3}' ./table/table_z0.004e.txt > c_$elem.py

rm ./table/table_z0.004a.txt
rm ./table/table_z0.004b.txt
rm ./table/table_z0.004c.txt
rm ./table/table_z0.004d.txt
rm ./table/table_z0.004e.txt 

### z0.02

awk '$1~/^'$elem'$/' ./table/table_z0.02.txt > ./table/table_z0.02a.txt
awk '
{ for (i=1; i<=NF; i++) { a[NR,i] = $i } } NF>p { p = NF }
END {
for(j=1; j<=p; j++) { str=a[1,j]; for(i=2; i<=NR; i++){ str=str" "a[i,j]; }
print str
}
}' ./table/table_z0.02a.txt > ./table/table_z0.02b.txt
sed '1d' ./table/table_z0.02b.txt > ./table/table_z0.02c.txt
cat ./table/table_z0.02c.txt | nl > ./table/table_z0.02d.txt
sed "s/^/d_y$elem/g" ./table/table_z0.02d.txt > ./table/table_z0.02e.txt
awk '{print $1 $2 "=" $3}' ./table/table_z0.02e.txt > d_$elem.py

rm ./table/table_z0.02a.txt
rm ./table/table_z0.02b.txt
rm ./table/table_z0.02c.txt
rm ./table/table_z0.02d.txt
rm ./table/table_z0.02e.txt

### file connect

awk 1 a_$elem.py b_$elem.py c_$elem.py d_$elem.py > $elem.py
mv $elem.py ../SNII_yields/y$elem.py
rm a_$elem.py b_$elem.py c_$elem.py d_$elem.py

done
