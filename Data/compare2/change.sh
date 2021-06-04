#!/bin/bash

for elem in C N O Na Mg Al Si P S K Ca Sc Ti V Cr Mn Co Ni Cu Zn 
do

sed -e s/Al/$elem/g AlFe.plt > ${elem}Fe1.plt
sed -e s/metaldelay/PISNe/g ${elem}Fe1.plt > ${elem}Fe2.plt
cp ${elem}Fe2.plt ${elem}Fe.plt

rm ${elem}Fe1.plt
rm ${elem}Fe2.plt

done 

