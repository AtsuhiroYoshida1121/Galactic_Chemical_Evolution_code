#!/bin/bash

for elem in 4He 12C 14N 16O 23Na 24Mg 27Al 28Si 31P 32S 39K 40Ca 45Sc 48Ti 51V 52Cr 55Mn 56Fe 59Co 58Ni 63Cu 64Zn p
#elem=12C
do

sed -e "s/4He/${elem}/g" def.txt > ${elem}.txt

done


cat p.txt 4He.txt 12C.txt 14N.txt 16O.txt 23Na.txt 24Mg.txt 27Al.txt 28Si.txt 31P.txt 32S.txt 39K.txt 40Ca.txt 45Sc.txt 48Ti.txt 51V.txt 52Cr.txt 55Mn.txt 56Fe.txt 59Co.txt 58Ni.txt 63Cu.txt 64Zn.txt > complete.txt


for elem in p 4He 12C 14N 16O 23Na 24Mg 27Al 28Si 31P 32S 39K 40Ca 45Sc 48Ti 51V 52Cr 55Mn 56Fe 59Co 58Ni 63Cu 64Zn
do

rm ${elem}.txt

done

