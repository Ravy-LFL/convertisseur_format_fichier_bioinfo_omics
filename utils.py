"""
Cette librairie a pour but de contenir les fonctions nécessaire a la conversion de fichier bed, gmf, et ssam.
"""


"""
faire une fonction du formatage de fichier
organisation de la classe :
    Nom
    Start
    Align
    Start
    strand
"""

def verifie_fichier(sortie:str,extension:str)->str:
    test=sortie.split(".")
    if len(test) > 1 :
        fichier_sortie=open(sortie,"w")
    else :
        fichier_sortie=open(sortie+"."+extension,"w")
    return fichier_sortie
    



def bed2ssam(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier bed en ssam /!/ On n'aura pas l'information 'cigar' nécessaire au fichier ssam, on marquera alors un point.
    """
    fichier_entree=open(entree,"r")
    entree_lue=fichier_entree.readlines()
    fichier_sortie=verifie_fichier(sortie,"ssam")
    #Les fichiers sont initialisé, on va maintenant récupérer les infos qui nous interesse venant du fichier bed.
    for i in entree_lue :
        ligne=i.split("\t")
        Align=ligne[0]
        Start=ligne[1]
        Nom=ligne[3]
        strand=ligne[4].split("\n")[0]
        #ecriture du fichier ssam
        fichier_sortie.write(Nom)
        fichier_sortie.write("\t")
        fichier_sortie.write(strand)
        fichier_sortie.write("\t")
        fichier_sortie.write(Align)
        fichier_sortie.write("\t")
        fichier_sortie.write(Start)
        fichier_sortie.write("\t")
        fichier_sortie.write(".")
        fichier_sortie.write("\n")
    
    fichier_entree.close()
    fichier_sortie.close()
    return fichier_sortie
    #On retourne le fichier de sortie pour pouvoir l'afficher si nécessaire


def bed2gmf(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier bed en gmf, ils possèdent les memes arguments
    """
    dictionnaire={}
    fichier_entree=open(entree,"r")
    entree_lue=fichier_entree.readlines()
    fichier_sortie=verifie_fichier(sortie,"gmf")
    #Les fichiers sont initialisé, on va maintenant récupérer les infos qui nous interesse venant du fichier bed.
    for i in entree_lue :
        ligne=i.split("\t")
        if ligne[3] not in dictionnaire :
            dictionnaire[ligne[3]]=[i]
        else :
            dictionnaire[ligne[3]].append(i)

    for i in dictionnaire.keys():
        fichier_sortie.write("Seq")
        fichier_sortie.write("\t")
        fichier_sortie.write(i)
        fichier_sortie.write("\n")
        for j in dictionnaire[i]:
            fichier_sortie.write("Align")
            fichier_sortie.write("\t")
            ligne_split=j.split("\t")
            fichier_sortie.write(ligne_split[0])
            fichier_sortie.write("\t")
            fichier_sortie.write(ligne_split[1])
            fichier_sortie.write("\t")
            fichier_sortie.write(ligne_split[2])
            fichier_sortie.write("\t")
            fichier_sortie.write(ligne_split[4].split("\n")[0])
            fichier_sortie.write("\n")

    
    fichier_entree.close()
    fichier_sortie.close()
    return fichier_sortie


def ssam2bed(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier ssam en fichier bed
    """
    fichier_entree=open(entree,"r")
    entree_lue=fichier_entree.readlines()
    fichier_sortie=verifie_fichier(sortie,"bed")
    for i in entree_lue:
        ligne=i.split("\t")
        Align=ligne[2]
        Start=ligne[3]
        End="."
        Nom=ligne[0]
        strand=ligne[1]
        if strand == '1':
            strand = '+'
        else :
            strand = '-'
    #ecriture du fichier bed
        fichier_sortie.write(Align)
        fichier_sortie.write("\t")
        fichier_sortie.write(Start)
        fichier_sortie.write("\t")
        fichier_sortie.write(End)
        fichier_sortie.write("\t")
        fichier_sortie.write(Nom)
        fichier_sortie.write("\t")
        fichier_sortie.write(strand)
        fichier_sortie.write("\n")
      
    fichier_entree.close()
    fichier_sortie.close()
    return fichier_sortie

def gmf2bed(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier gmf en fichier bed
    """
    fichier_entree=open(entree,"r")
    entree_lue=fichier_entree.readlines()
    fichier_sortie=verifie_fichier(sortie,"bed")
    for i in entree_lue:
        ligne=i.split("\t")
        if ligne[0] == "Seq":
            Nom=ligne[1]
        else:
            fichier_sortie.write(ligne[1])
            fichier_sortie.write("\t")
            fichier_sortie.write(ligne[2])
            fichier_sortie.write("\t")
            fichier_sortie.write(ligne[3])
            fichier_sortie.write("\t")
            fichier_sortie.write(Nom)
            fichier_sortie.write("\t")
            fichier_sortie.write(ligne[4])
            fichier_sortie.write("\n")

    fichier_entree.close()
    fichier_sortie.close()
    return fichier_sortie

