def predict_protein_mass(sequence):
    aa_masses = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }
    total_mass = 0
    sequence = sequence.upper()
    for aa in sequence:
        if aa not in aa_masses:
            return "Error: amino acid '" + aa + "' is not defined."
        total_mass = total_mass + aa_masses[aa]
    return total_mass
protein_seq = "MAGNIFY"
result = predict_protein_mass(protein_seq)
print("Sequence:", protein_seq)
if type(result) == str:
    print(result)
else:
    print("Protein mass:", result, "amu")