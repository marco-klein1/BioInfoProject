import DNA
import Tax
import copy
import Protein;


from Entry import Entry

fam = 'Pseudonocardiaceae'
EC = '5.3.1.8'
o = Entry(fam)
TaxID = Tax.getTaxonomy(o.family)



#n = DNA.runDNAPipeline(EC, fam, TaxID)
#print(len(n))
#l = Protein.runProteinPipeline(EC, fam, TaxID)
#print(l)


