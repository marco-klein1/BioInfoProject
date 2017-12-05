from Bio import Entrez
Entrez.email = "s.vorbrugg@yahoo.de"

def runProteinPipeline(EC, family, ID):
    l = getProteinID(EC, family,ID)
    print(len(l))
    o = []
    for x in l:
        o.append(getFasta(x))
    return o

def getProteinID(EC, family, ID):
    handle = Entrez.esearch(db="protein", retmax=10000, term=EC + ' AND"' + family + '"[porgn:__txid' + ID + ']')
    record = Entrez.read(handle)
    handle.close()
    return record['IdList']

def getFasta(ID):
    handle2 = Entrez.efetch(db="protein", id=ID, rettype="fasta")
    seu = ""
    for x in handle2.readlines():
        if x.startswith('>'):
            continue;
        else:

            seu += x
    handle2.close()
    return seu.replace("\n", "");








