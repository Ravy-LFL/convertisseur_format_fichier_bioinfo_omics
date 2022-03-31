import sys
import utils
entree=sys.argv[1]

try :
    (len(sys.argv[2])/1)
    ecran=False
    sortie=sys.argv[2]
except :
    ecran=True
    sortie="./.sortie"

utils.ssam2bed(entree,sortie,ecran)