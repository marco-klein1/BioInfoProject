from FindOrthologous.Entry import Entry
from FindOrthologous.Entry import *
from FindOrthologous.Queries import DNA
from FindOrthologous.Queries import Tax
import copy

fam = 'Pseudonocardiaceae'
EC = '5.3.1.8'

k = {"family": fam, "ec": EC}
Tax.getTaxonomy(k)
print(k["TaxID"])
print("test")


n = DNA.runDNAPipeline(k)
#p = []
#for x in n:
#    test = Entry(obj.family, obj.ecNumber,"","","","")
#    test.setSeq(x)
#    test.setTyp("DNA")
#    test.setTaxID(TaxID)
#    p.append(test)
#print(len(p))


#Entry.printInFastA(p)


#print(len(n))
#l = Protein.runProteinPipeline(EC, fam, TaxID)
#print(l)

