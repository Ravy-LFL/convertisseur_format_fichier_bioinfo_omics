"""
Cette librairie a pour but de contenir les fonctions nécessaire a la conversion de fichier bed, gmf, et ssam.
"""

class fichier_type:
    def __init__(self,Align,Start,Nom,strand,End):
        self.Align=Align
        self.Start=Start
        self.Nom=Nom
        self.Strand=strand
        self.End=End
    
    def __str__(self):
        return(str(self.Align),str(self.Start),str(self.Nom),str(self.strand),str(self.End))


def verif_extensions(sortie:str,extension:str):
    '''
    Cette fonction verifie que l'utilisateur a bien ecrit le nom du fichier avec son extension
    '''
    test=sortie.split(".")
    if len(test) > 1 :
        path=sortie
    else :
        path=sortie+"."+extension   
    return path

def parsing_du_fichier_entree(entree:str):
    '''
    Cette fonction reunis les commandes permettant le parsing des fichiers selon leur extension.
    '''
    liste_objet=[]
    dictionnaire_gmf={}
    fichier_entree=open(entree,"r")
    entree_lue=fichier_entree.readlines()
    if entree.split(".")[1] == "bed" :
        for i in entree_lue:
            ligne=i.split("\t")
            Align=ligne[0]
            Start=ligne[1]
            Nom=ligne[3]
            End=ligne[2]
            strand=ligne[4].split("\n")[0]
            nouveau_objet=fichier_type(Align,Start,Nom,strand,End)
            liste_objet.append(nouveau_objet)
        return liste_objet
    elif entree.split(".")[1] == "ssam" :
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
            liste_objet.append(fichier_type(Align,Start,Nom,strand,End))
        return liste_objet
    elif entree.split(".")[1] == "gmf" : 
        liste_Align=[]
        dictionnaire_gmf={}
        for i in entree_lue:
            ligne=i.split("\t")
            if ligne[0] == "Seq":
                Nom=ligne[1].split("\n")[0]
            if Nom not in dictionnaire_gmf:
                dictionnaire_gmf[Nom]=[]
            else:
                Align=ligne[1].split("\t")[0]
                Start=ligne[2].split("\t")[0]
                Strand=ligne[4].split("\n")[0]
                End=ligne[3].split("\t")[0]
                nouveau_objet=fichier_type(Align,Start,Nom,Strand,End)
                dictionnaire_gmf[nouveau_objet.Nom].append([nouveau_objet.Align,nouveau_objet.Start,nouveau_objet.End,nouveau_objet.Strand])
        return dictionnaire_gmf

def dictionnaire_pour_gmf(liste_objet):
    #On va parser notre liste d'objet en dictionnaire pour que ca soit plus facile a utiliser pour créer le fichier gmf
    dictionnaire_gmf={}
    for i in liste_objet:
        if i.Nom not in dictionnaire_gmf.keys():
            dictionnaire_gmf[i.Nom]=[[i.Align,i.Start,i.Strand,i.End]]
        else :
            dictionnaire_gmf[i.Nom].append([i.Align,i.Start,i.Strand,i.End])
    return dictionnaire_gmf

def dictionnaire_vers_liste(dictionnaire_gmf):
    '''
    Parser un gmf donne un dictionnaire mais notre fonction utilise des liste d'objet, cette fonction va permettre la conversion.
    '''
    liste_objet=[]
    for i in dictionnaire_gmf.keys():
        for j in dictionnaire_gmf[i]:
            Nom=i
            Align=j[0]
            Start=j[1]
            End=j[2]
            Strand=j[3]
            nouveau_objet=fichier_type(Align,Start,Nom,Strand,End)
            liste_objet.append(nouveau_objet)
    return liste_objet
        
    

def ecriture_fichier_sortie(liste_objet,sortie):
    '''
    Cette fonction va ecrire le nouveau fichier en suivant la mise en page prorpes aux différents fichier
    '''
    fichier_sortie=open(sortie,"w")
    if sortie.split(".")[1] == "ssam" :
        for i in liste_objet:
            if i.Strand == "+" or i.Strand == "1":
                strand=("1")
            else:
                strand=("0")
            a_ecrire=str(i.Nom+"\t"+strand+"\t"+i.Align+"\t"+i.Start+"\t"+"."+"\n")
            fichier_sortie.write(a_ecrire)
    if sortie.split(".")[1] == "gmf" :
        dictionnaire=dictionnaire_pour_gmf(liste_objet)
        for i in dictionnaire.keys():
            for j in dictionnaire[i]:
                a_ecrire=str("Seq"+"\t"+i+"\n"+"Align"+"\t"+j[0]+"\t"+j[1]+"\t"+j[3]+"\t"+j[2]+"\n")
                fichier_sortie.write(a_ecrire)
    if sortie.split(".")[1] == "bed" :
        for i in liste_objet:
            a_ecrire=str(i.Align+"\t"+i.Start+"\t"+i.End+"\t"+i.Nom+"\t"+i.Strand+"\n")
            fichier_sortie.write(a_ecrire)
    fichier_sortie.close()
    return fichier_sortie
            

#Fonction Vérifié
def bed2ssam(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier bed en ssam /!/ On n'aura pas l'information 'cigar' nécessaire au fichier ssam, on marquera alors un point.
    """
    fichier_entree=open(entree,"r")
    entree_lue=fichier_entree.readlines()
    fichier_sortie=verif_extensions(sortie,"ssam")
    #Les fichiers sont initialisé, on va maintenant récupérer les infos qui nous interesse venant du fichier bed.
    liste_objet=parsing_du_fichier_entree(entree)
    #ecriture du fichier ssam
    fichier_de_sortie=ecriture_fichier_sortie(liste_objet,fichier_sortie)
    #On retourne le fichier de sortie pour pouvoir l'afficher si nécessaire
    fichier_de_sortie.close()
    return fichier_de_sortie

#Fonction Vérifié
def bed2gmf(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier bed en gmf, ils possèdent les memes arguments
    """
    fichier_sortie=verif_extensions(sortie,"gmf")
    #Les fichiers sont initialisé, on va maintenant récupérer les infos qui nous interesse venant du fichier bed.
    liste_objet=parsing_du_fichier_entree(entree)
    #ecriture du fichier gmf
    fichier_de_sortie=ecriture_fichier_sortie(liste_objet,fichier_sortie)
    fichier_de_sortie.close()
    return fichier_de_sortie

#Fonction Vérifié
def ssam2bed(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier ssam en fichier bed
    """
    fichier_sortie=verif_extensions(sortie,"bed")
    #Parsing du fichier ssam
    liste_objet=parsing_du_fichier_entree(entree)
    #ecriture du fichier bed
    fichier_de_sortie=ecriture_fichier_sortie(liste_objet,fichier_sortie)
    fichier_de_sortie.close()
    return fichier_de_sortie

#Fonction Vérifié
def gmf2bed(entree:str,sortie:str):
    """
    Cette fonction a pour but la conversion d'un fichier gmf en fichier bed
    """
    fichier_sortie=verif_extensions(sortie,"bed")
    #Parsing du fichier gmf
    dictionnaire_objet=parsing_du_fichier_entree(entree)
    #Ecriture du fichier bed
    liste_objet=dictionnaire_vers_liste(dictionnaire_objet)
    fichier_de_sortie=ecriture_fichier_sortie(liste_objet,fichier_sortie)
    fichier_de_sortie.close()
    return fichier_de_sortie
