input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stop_codons = ["TAA", "TAG", "TGA"]
genes = []
header = ""
sequence = ""
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if header != "":
                genes.append((header, sequence))
            header = line
            sequence = ""
        else:
            squence = sequence + line
    if header != "":
        genes.append((header, sequence))
def get_gene_name(header_line):
    parts = header_line.split()
    for part in parts:
        if part.startswith("gene:"):
            return part.replace("gene:", "")
    return parts[0].replace(">", "")
def find_in_frame_stops(seq):
    found_stops = set()
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            # read codons from this ATG
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break
    return sorted(found_stops)
with open(output_file, "w") as out:
    for header, seq in genes:
        gene_name = get_gene_name(header)
        found = find_in_frame_stops(seq)
        if len(found) > 0:
            stop_text = ",".join(found)
            out.write(">" + gene_name + " " + stop_text + "\n")
            out.write(seq + "\n")
print("Finished.")
print("Output written to:", output_file)






