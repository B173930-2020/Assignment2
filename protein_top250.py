import pandas as pd
data = pd.read_json('pro_famout.blastp.out', orient='index')
data = data.iloc[0,0]['report']['results']['search']['hits']

# Read original fasta file
with open('pro_fam.fasta', 'r') as f:
    tmp = f.readlines()

# Make a dictionary to pickup sequences.    
more_dict = {}
for i in tmp:
    if i[0] == '>':
        key = i.strip()
        more_dict[key] = ''
    else:
        more_dict[key] += i.strip()

# Get 250 fasta names
fasta = ''
for i in data:
    name = '>' + i['description'][0]['title']
    fasta += '{}\n{}\n'.format(name, more_dict[name])
    
with open('protein_top250.txt', 'w') as f:
    f.write(fasta)
