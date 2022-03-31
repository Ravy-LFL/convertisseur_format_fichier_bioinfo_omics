#Exemple d'utilisation : python3 convert entrée.bed sortie.ssam
import FormatLibrairie
import sys

commande=sys.argv[1]
fichier_entree=sys.argv[2]
fichier_sortie=sys.argv[3]

extension_entree=fichier_entree.split(".")[1]
extension_sortie=fichier_sortie.split(".")[1]

if len(extension_entree)==0 or len(extension_sortie)==0:
    raise TypeError(" Veuillez verifier que les fichiers d'entrée et sorties possède une extension ! ")

if commande == "convert":
    '''
    Si la commande tapé est convert on va appeler les fonctions de la librairie selon l'extension des fichiers d'entree et de sortie.
    '''
    if extension_entree == "bed" and extension_sortie == "ssam":
        print("C'est parti ! ")    
        sortie=(FormatLibrairie.bed2ssam(fichier_entree,fichier_sortie))
    elif extension_entree == "bed" and extension_sortie == "gmf":
        print("C'est parti ! ") 
        sortie=FormatLibrairie.bed2gmf(fichier_entree,fichier_sortie)
    elif extension_entree == "ssam" and extension_sortie == "bed":
        print("C'est parti ! ") 
        sortie=FormatLibrairie.ssam2bed(fichier_entree,fichier_sortie)
    elif extension_entree == "gmf" and extension_sortie == "bed":
        print("C'est parti ! ") 
        sortie=FormatLibrairie.gmf2bed(fichier_entree,fichier_sortie)

else :
    print("quelque chose a rater...")
