class Entry(object):
    '''
        family = ""
    TaxID = ""
    GeneID = ""
    Type =""
    Sequence = ""
    header = ""
    '''

    def __init__(self, fam):
        self.family = fam


    def setTaxID(self, tax):
        self.taxID = tax
    def setFamily(self, fam):
        self.family = fam
    def setTyp(self, typ):
        self.typ = typ
    def setEC(self, EC):
        self.ecNumber = EC
    def setHeader(self, header):
        self.header = header
    def getFastA(self):
        output = self.header + self.seq + "\n"




