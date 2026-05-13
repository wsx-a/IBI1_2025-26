blosum62 = {
    ('A', 'A'): 4, ('R', 'R'): 5, ('N', 'N'): 6, ('D', 'D'): 6,
    ('C', 'C'): 9, ('Q', 'Q'): 5, ('E', 'E'): 5, ('G', 'G'): 6,
    ('H', 'H'): 8, ('I', 'I'): 4, ('L', 'L'): 4, ('K', 'K'): 5,
    ('M', 'M'): 5, ('F', 'F'): 6, ('P', 'P'): 7, ('S', 'S'): 4,
    ('T', 'T'): 5, ('W', 'W'): 11, ('Y', 'Y'): 7, ('V', 'V'): 4,
}

human = "MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY"
mouse = "MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"
random_seq = "QDILDYFCWWGCSRRVFSDVGRPFRYEGYPRVEVSYQCKQLIHHRGEAWQPRLFDVPIDEIYKVYVMQYAWGKSMSTYIYRNCTKNPGGDDVLSAYFSHIHVMQYWFRENKVAPALLYTEVAHRSRIKEHMNWVHYDATFVMCLFSCIDVLIYNDNRWGWLRIMLIWITWIGFHLGVKCCAGTKQSPYSLSWWMAHERCHVVCFWVVFVCHEFLRFFSSPLSESSLADNFMWWQMVHQGQAFYCWGSRSTCVNQVYFDSPYCDETVPFMGMTNLAKEEPGEVRQNHICC"

def align(seq1, seq2, matrix):
    total_score = 0
    identical = 0
    align_line = ""
    
    for a, b in zip(seq1, seq2):
        score = matrix.get((a, b), matrix.get((b, a), -4))
        total_score += score
        if a == b:
            identical += 1
            align_line += "|"
        else:
            align_line += " "
    
    identity = (identical / len(seq1)) * 100
    return total_score, identity, align_line

print("=== Human vs Mouse ===")
s1, id1, line1 = align(human, mouse, blosum62)
print(human)
print(line1)
print(mouse)
print(f"Score: {s1}, Identity: {id1:.2f}%\n")

print("=== Human vs Random ===")
s2, id2, line2 = align(human, random_seq, blosum62)
print(f"Score: {s2}, Identity: {id2:.2f}%\n")

print("=== Mouse vs Random ===")
s3, id3, line3 = align(mouse, random_seq, blosum62)
print(f"Score: {s3}, Identity: {id3:.2f}%")