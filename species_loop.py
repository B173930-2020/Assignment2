import re
from collections import Counter

# Pick up the species names in pro_fam.fasta(all sequences document) and count their amounts.
with open('pro_fam.fasta', 'r') as f:
    tmp = f.read()
    
tax_result = re.findall('\[(.*?)\]', tmp)
tmp = Counter(tax_result)

# top10 species names
for i in tmp.most_common(10):
    print(i)
print('all species:', len(set(tax_result)))
