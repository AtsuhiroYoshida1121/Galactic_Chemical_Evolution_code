#!/bin/bash

/opt/local/bin/gnuplot > load 'AlFe.plt'
/opt/local/bin/gnuplot > load 'CFe.plt'
/opt/local/bin/gnuplot > load 'CaFe.plt'
/opt/local/bin/gnuplot > load 'CoFe.plt'
/opt/local/bin/gnuplot > load 'CrFe.plt'
/opt/local/bin/gnuplot > load 'CuFe.plt'
/opt/local/bin/gnuplot > load 'KFe.plt'
/opt/local/bin/gnuplot > load 'MgFe.plt'
/opt/local/bin/gnuplot > load 'MnFe.plt'
/opt/local/bin/gnuplot > load 'NFe.plt'
/opt/local/bin/gnuplot > load 'NaFe.plt'
/opt/local/bin/gnuplot > load 'NiFe.plt'
/opt/local/bin/gnuplot > load 'OFe.plt'
/opt/local/bin/gnuplot > load 'PFe.plt'
/opt/local/bin/gnuplot > load 'SFe.plt'
/opt/local/bin/gnuplot > load 'ScFe.plt'
/opt/local/bin/gnuplot > load 'TiFe.plt'
/opt/local/bin/gnuplot > load 'VFe.plt'
/opt/local/bin/gnuplot > load 'ZnFe.plt'
/opt/local/bin/gnuplot > load 'SiFe.plt'
/opt/local/bin/gnuplot > load 'FeO.plt'
/opt/local/bin/gnuplot > load 'FeMg_redshift.plt'
/opt/local/bin/gnuplot > load 'OFe_selection.plt'
/opt/local/bin/gnuplot > load 'FeO_selection.plt'

mv AlFe.pdf PDF/
mv CFe.pdf PDF/
mv CaFe.pdf PDF/
mv CoFe.pdf PDF/
mv CrFe.pdf PDF/
mv CuFe.pdf PDF/
mv KFe.pdf PDF/
mv MgFe.pdf PDF/
mv MnFe.pdf PDF/
mv NFe.pdf PDF/
mv NaFe.pdf PDF/
mv NiFe.pdf PDF/
mv OFe.pdf PDF/
mv OFe_selection.pdf PDF/
mv FeO_selection.pdf PDF/
mv PFe.pdf PDF/
mv ScFe.pdf PDF/
mv TiFe.pdf PDF/
mv VFe.pdf PDF/
mv ZnFe.pdf PDF/
mv SiFe.pdf PDF/
mv FeO.pdf PDF/
mv FeMg_redshift.pdf PDF/

cp -r PDF ~/Desktop/ 
