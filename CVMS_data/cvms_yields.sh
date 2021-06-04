#!/bin/bash

for elem in p 4He 12C 14N 16O 23Na 24Mg 27Al 28Si 31P 32S 39K 40Ca 45Sc 48Ti 51V 52Cr 55Mn 56Fe 59Co 58Ni 63Cu 64Zn
do

awk '$1~/^'$elem'$/' ./cvms_table.txt > ./cvms_tablea.txt
awk '
{ for (i=1; i<=NF; i++)  { a[NR,i] = $i } } NF>p { p = NF }
END {
    for(j=1; j<=p; j++) { str=a[1,j]; for(i=2; i<=NR; i++){ str=str" "a[i,j]; }
        print str
    }
}' ./cvms_tablea.txt > ./cvms_tableb.txt
sed '1d' ./cvms_tableb.txt > ./cvms_tablec.txt
sed '1d' ./cvms_tablec.txt > ./cvms_tabled.txt
sed '2d' ./cvms_tabled.txt > ./cvms_tablee.txt
cat ./cvms_tablee.txt | nl > ./cvms_tablef.txt
sed "s/^/y$elem/g" ./cvms_tablef.txt > ./cvms_tableg.txt
awk '{print $1 $2 "=" $3}' ./cvms_tableg.txt > $elem.py

mv $elem.py ~/GCE/Suzuki_Maeda/b4/task_9/test_9-1/CVMS_yields/y$elem.py

for i in a b c d e f g
do
rm cvms_table${i}.txt
done

done
