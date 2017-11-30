class Entry:
    '''
        family = ""
    TaxID = ""
    GeneID = ""
    Type =""
    Sequence = ""
    header = ""
    '''
    def __init__(self, EC):
        self.ecNumber = EC
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
    def set

    def getFastA(self):
        output = self.header + self.seq + "\n"




