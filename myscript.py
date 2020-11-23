#!/usr/bin/python3
import subprocess
import os
# This is the codes of the first detailed task.
# Input the protein family name and taxonomic group name (must with quotation marks!).
protein_family = input("Please input your protein family name, like 'glucose-6-phosphatase':")+'[Protein name]'
taxonomic_group = input("Please input your taxonomic group name, like 'Aves':")+'[Organism name]'

# Joint the input names as the search format.
search = protein_family + ' AND ' + taxonomic_group

# Use esearch and efetch to search and download the sequences. 
os.system('esearch -db protein -query \"%s\" | efetch -db protein -format fasta > pro_fam.fasta' % (search))

# Calculate the amount of sequences.
sequence_number = os.system('grep -c ">" pro_fam.fasta')

# If the amount of sequences is larger than 1000, the program will run this loop to ask the user's idea.
while sequence_number > 1000:
        r1=input('The amount of sequences is not allowed to larger than 1000 in most cases, \nwould you want to continue? "y"/"n": ')
        if r1 == 'y':
                break
        elif r1 == 'n':
                r2 = input('Would you to start again? "y"/"n": ')
                if r2 == 'y':
                        os.system('python myscript.py')
                        break
                else:
                     	exit()
			break
        else:
             	print('Please input the right choices!')
                continue

# Return the species and ask whether the user will continue
os.system('python3 species_loop.py')
while True:
	r3 = input('would you want to continue? "y"/"n": ')
	if r3 == "y":
		break
	elif r3 == "n":
		exit()
		break
	else:
		print('Please input the right choices!')
		continue

# 2nd detailed task
# Use clustalo to align multiple sequences.
os.system('clustalo -i pro_fam.fasta -o pro_fam_out.fasta')

# Use cons(EMboss) to make a consequence.
os.system('cons pro_fam_out.fasta pro_fam_outcons.fasta')

# Make a protein database(the sequences we get) to blast.
os.system('makeblastdb -in pro_fam.fasta -input_type fasta -dbtype prot -title pro -out pro')\

# Use blast to align the consequence with each sequence.
os.system('blastp -query pro_fam_outcons.fasta -db pro -out pro_famout.blastp.out -max_target_seqs 250 -outfmt 15')

# Make a document which includes the top 250 similar sequences' names and sequences.
os.system('python3 protein_top250.py')

# 3rd detailed task
# Make a sheet which includes the motif information
os.system('python3 motifs.py')

# 4th detailed task
# Use pepstats to statistic the information of protein properties.
os.system('pepstats protein_top250.txt pro_properties.txt')

# Some operations to make the dir more clearly
os.system('rm output_seq input_seq.fasta pro.*')

