class Entry(object):
    '''
        family = ""
    TaxID = ""
    GeneID = ""
    Type =""
    Sequence = ""
    header = ""
    '''

    def __init__(self, fam, EC, tax, typ, header, seq):
        self.family = fam
        self.ecNumber = EC
        self.taxID = tax
        self.typ = typ
        self.header = header
        self.seq = seq


    def setTaxID(self, tax):
        self.taxID = tax
    def setTyp(self, typ1):
        self.typ = typ1
    def setHeader(self, header):
        self.header = header
    def setSeq(self, seq):
        self.seq = seq

    @staticmethod
    def printInFastA(l):
        test = ""
        for x in l:
            test += "hallo"
            test += x.seq + "\n"

        file = open("test.txt", "w")
        file.write(test)
        file.close()


