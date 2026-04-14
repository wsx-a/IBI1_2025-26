def predict_protein_mass(sequence):
    # amino acid masses (amu)
    aa_masses = {
        "A": 89.09,
        "R": 174.20,
        "N": 132.12,
        "D": 133.10,
        "C": 121.15,
        "Q": 146.15,
        "E": 147.13,
        "G": 75.07,
        "H": 155.16,
        "I": 131.17,
        "L": 131.17,
        "K": 146.19,
        "M": 149.21,
        "F": 165.19,
        "P": 115.13,
        "S": 105.09,
        "T": 119.12,
        "W": 204.23,
        "Y": 181.19,
        "V": 117.15
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
print("Protein mass:", result, "amu")