#!/bin/bash
python GCE_model.py

mv -f FeHvsT.csv Data/time_evol/
mv -f SFR.csv Data/time_evol/
mv -f metal.csv Data/time_evol/
mv -f MgFevsT.csv Data/time_evol/
mv -f OFevsT.csv Data/time_evol/
mv -f MgFevsredshift.csv Data/time_evol/

mv -f Fe56_agb.csv Data/time_evol/
mv -f Fe56_agb_feh.csv Data/time_evol/
mv -f Fe56_ccsn.csv Data/time_evol/
mv -f Fe56_ccsn_feh.csv Data/time_evol/
mv -f Mg24_agb.csv Data/time_evol/
mv -f Mg24_agb_feh.csv Data/time_evol/
mv -f Mg24_ccsn.csv Data/time_evol/
mv -f Mg24_ccsn_feh.csv Data/time_evol/
mv -f SFR_T.csv Data/time_evol/
mv -f SFR_feh.csv Data/time_evol/

mv -f FeHvsMgFe.csv Data/abundance/ 
mv -f FeHvsOFe.csv Data/abundance/
mv -f FeHvsCFe.csv Data/abundance/
mv -f FeHvsNFe.csv Data/abundance/
mv -f FeHvsSFe.csv Data/abundance/
mv -f FeHvsCaFe.csv Data/abundance/
mv -f OHvsFeO.csv Data/abundance/

mv -f H.csv Data/time_evol/
mv -f Mg24.csv Data/time_evol/
mv -f O16.csv Data/time_evol/
mv -f N14.csv Data/time_evol/
mv -f S32.csv Data/time_evol/
mv -f Fe56.csv Data/time_evol/
mv -f He4.csv Data/time_evol/
mv -f C12.csv Data/time_evol/
mv -f Ca40.csv Data/time_evol/
mv -f AlFevsT.csv Data/time_evol/
mv -f CFevsT.csv Data/time_evol/
mv -f CoFevsT.csv Data/time_evol/
mv -f CrFevsT.csv Data/time_evol/
mv -f MnFevsT.csv Data/time_evol/
mv -f NFevsT.csv Data/time_evol/
mv -f NiFevsT.csv Data/time_evol/
mv -f ScFevsT.csv Data/time_evol/
mv -f SiFevsT.csv Data/time_evol/
mv -f TiFevsT.csv Data/time_evol/

rm -r __pycache__

mv -f FeHvsAlFe.csv Data/abundance/
mv -f FeHvsCoFe.csv Data/abundance/
mv -f FeHvsCrFe.csv Data/abundance/
mv -f FeHvsCuFe.csv Data/abundance/
mv -f FeHvsKFe.csv Data/abundance/
mv -f FeHvsMnFe.csv Data/abundance/
mv -f FeHvsNaFe.csv Data/abundance/
mv -f FeHvsNiFe.csv Data/abundance/
mv -f FeHvsPFe.csv Data/abundance/
mv -f FeHvsScFe.csv Data/abundance/
mv -f FeHvsTiFe.csv Data/abundance/
mv -f FeHvsVFe.csv Data/abundance/
mv -f FeHvsZnFe.csv Data/abundance/
mv -f FeHvsSiFe.csv Data/abundance/
mv -f Al27.csv Data/time_evol/
mv -f Co59.csv Data/time_evol/
mv -f Cr52.csv Data/time_evol/
mv -f Cu63.csv Data/time_evol/
mv -f K39.csv Data/time_evol/
mv -f Mn55.csv Data/time_evol/
mv -f Na23.csv Data/time_evol/
mv -f Ni58.csv Data/time_evol/
mv -f P31.csv Data/time_evol/
mv -f Sc45.csv Data/time_evol/
mv -f Ti48.csv Data/time_evol/
mv -f V51.csv Data/time_evol/
mv -f Zn64.csv Data/time_evol/
