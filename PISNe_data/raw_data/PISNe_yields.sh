#!/bin/bash

for elem in 4He 12C 14N 16O 23Na 24Mg 27Al 28Si 31P 32S 39K 40Ca 45Sc 48Ti 51V 52Cr 55Mn 56Fe 59Co 58Ni 63Cu 64Zn
do

awk '$1~/^'$elem'$/' ./pisne_table.txt > ./pisne_tablea.txt
awk '
{ for (i=1; i<=NF; i++)  { a[NR,i] = $i } } NF>p { p = NF }
END {
    for(j=1; j<=p; j++) { str=a[1,j]; for(i=2; i<=NR; i++){ str=str" "a[i,j]; }
        print str
    }
}' ./pisne_tablea.txt > ./pisne_tableb.txt
sed '1d' ./pisne_tableb.txt > ./pisne_tablec.txt
cat ./pisne_tablec.txt | nl > ./pisne_tabled.txt
sed "s/^/y$elem/g" ./pisne_tabled.txt > ./pisne_tablee.txt
awk '{print $1 $2 "=" $3}' ./pisne_tablee.txt > $elem.py

mv $elem.py ../../PISNe_yields/y$elem.py

for i in a b c d e
do
rm pisne_table${i}.txt
done

done

