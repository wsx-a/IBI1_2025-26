import matplotlib.pyplot as plt
input_file = "E:/IBI1/IBI1_2025-26/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
valid_stops = ["TAA", "TAG", "TGA"]
user_stop = input("Enter a stop codon (TAA, TAG, or TGA): ").upper()
if user_stop not in valid_stops:
    print("Invalid input. Please enter TAA, TAG, or TGA.")
    exit()
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
            sequence = sequence + line
    if header != "":
        genes.append((header, sequence))
def get_longest_orf_before_stop(seq, stop_codon):
    longest_orf = ""
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            current_orf = ""
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                current_orf = current_orf + codon
                if codon == stop_codon:
                    if len(current_orf) > len(longest_orf):
                        longest_orf = current_orf
                    break
                if codon in valid_stops and codon != stop_codon:
                    break
    return longest_orf
codon_counts = {}
for header, seq in genes:
    longest_orf = get_longest_orf_before_stop(seq, user_stop)
    if longest_orf != "":
        coding_part = longest_orf[:-3]
        for i in range(0, len(coding_part) - 2, 3):
            codon = coding_part[i:i+3]
            if codon in codon_counts:
                codon_counts[codon] = codon_counts[codon] + 1
            else:
                codon_counts[codon] = 1
print("Codon counts upstream of", user_stop)
for codon in sorted(codon_counts):
    print(codon, codon_counts[codon])
labels = list(codon_counts.keys())
sizes = list(codon_counts.values())
plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Codon frequency upstream of " + user_stop)
plt.savefig("codon_pie_chart_" + user_stop + ".png")
plt.close()
print("Pie chart saved as:", "codon_pie_chart_" + user_stop + ".png")