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
        





