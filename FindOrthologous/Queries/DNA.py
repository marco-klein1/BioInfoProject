from Bio import Entrez

from FindOrthologous.Entry import Entry
import copy
Entrez.email = "s.vorbrugg@yahoo.de"


def runDNAPipeline(dic):
    l = getGeneID(dic)
    ö = []
    for x in l:
        ä = copy.deepcopy(dic)
        ö.append(getSequenceParameters(x))
    p = []
    for m in ö:
        p.append(rightOrder(m[0],m[1], m[2]))
    return p



def getGeneID(dic):
    handle = Entrez.esearch(db="gene", retmax=10000, term=dic["ec"] + ' AND"' + dic["family"] + '"[porgn:__txid' + dic["TaxID"] + ']')
    record = Entrez.read(handle)
    handle.close()
    GeneIDs = record['IdList']
    return GeneIDs

def getSequenceParameters(GeneID):
    handle = Entrez.esummary(db="gene", id=GeneID)
    record15 = Entrez.read(handle)
    handle.close()
    start_temp = int(record15['DocumentSummarySet']['DocumentSummary'][0]['GenomicInfo'][0]['ChrStart'])
    stop_temp = int(record15['DocumentSummarySet']['DocumentSummary'][0]['GenomicInfo'][0]['ChrStop'])
    chra = record15['DocumentSummarySet']['DocumentSummary'][0]['GenomicInfo'][0]['ChrAccVer']
    return [start_temp,stop_temp, chra]


def getSeq(start, stop, chra):
    handle2 = Entrez.efetch(db="nucleotide", id=chra, rettype="fasta", seq_start=start + 1, seq_stop=stop + 1)
    seu = ""
    for x in handle2.readlines():
        if x.startswith('>'):
            continue;
        else:
            seu += x
        handle2.close()
    return seu.replace("\n", "");



complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
def comp(seqq):
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seqq))
    return reverse_complement

def rightOrder(start_temp, stop_temp, chra):
    sqq2 = ''
    start = 0
    stop = 0
    if start_temp > stop_temp:
        start = stop_temp
        stop = start_temp
        sqq = getSeq(start, stop, chra)
        sqq2 = comp(sqq)
    else:
        sqq2 = getSeq(start_temp, stop_temp, chra)
    return sqq2





