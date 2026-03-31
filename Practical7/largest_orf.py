seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']
max_len = 0
for i in range(len(seq)-2):
    if seq[i:i+3] == start_codon:
        for j in range(i+3, len(seq)-2, 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                length = j+3-i
                if length > max_len:
                    max_len = length
                break
print("The length of the largest ORF is:", max_len)
