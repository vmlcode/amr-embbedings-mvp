from Bio import SeqIO

def ReadFasta(path):
    response = SeqIO.read(path, "fasta")
    return dict(
        id=response.id,
        seq=response.seq,
        description=response.description,
    )

def kmer(seq, k):
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]
