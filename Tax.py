from Bio import Entrez

Entrez.email = "s.vorbrugg@yahoo.de"

def getTaxonomy(family):
    handle1 = Entrez.esearch(db="taxonomy", term=family)
    record1 = Entrez.read(handle1)
    handle1.close();
    ID = str(record1['IdList'][0])
    print(ID)
    return ID