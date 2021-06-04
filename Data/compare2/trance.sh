#!/bin/bash
elem=SiFe
elem2=Si
sed s/CFe/$elem/g CFe.plt > $elem2.plt
sed s/C/$elem2/g $elem2.plt > $elem.plt
/opt/local/bin/gnuplot > load $elem.plt
mv $elem.pdf PDF/
rm $elem2.plt
rm load
