import pandas as pd
import os

data = pd.read_json('pro_famout.blastp.out', orient='index')
data = data.iloc[0,0]['report']['results']['search']['hits']

# The beginning codes like task2's
with open('pro_fam.fasta', 'r') as f:
    tmp = f.readlines()
    
more_dict = {}
for i in tmp:
    if i[0] == '>':
        key = i[1:].strip()
        more_dict[key] = ''
    else:
        more_dict[key] += i.strip()

# Put task2 loop's each fasta variable as the inputseq to run patmatmotifs function.
# Use the same name input_seq and output_seq to cover each time. This can make the tmp file only two files.
motif = pd.DataFrame()
for i in data:
    fasta = ''
    name = i['description'][0]['title']
    fasta = '>{}\n{}\n'.format(name, more_dict[name])
    with open('input_seq.fasta', 'w') as f:
        f.write(fasta)
    os.system('patmatmotifs input_seq.fasta output_seq')

    with open('output_seq', 'r') as f:
        tmp = f.readlines()
   
# Scan and store the Motif name.
    results = []
    for j in tmp:
        if 'Motif' in j:
            results.append(j.strip())

    motif.loc[name, 'motif'] = str(results)

motif.to_csv('all_motifs.csv')
