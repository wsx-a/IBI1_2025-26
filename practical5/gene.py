genes = {'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3, 'ESR1':10.7}
genes['MYC'] = 11.6
import matplotlib.pyplot as plt
plt.bar(genes.keys(), genes.values())
plt.xlabel("Gene")
plt.ylabel("Expression")
plt.title("Gene Expression Levels")
plt.show()
target_gene = 'TP53'
if target_gene in genes:
    print(target_gene, 'expression value is', genes[target_gene])
else:
    print('Error: gene not found')
average = sum(genes.values()) / len(genes)
print('Average gene expression is', average)