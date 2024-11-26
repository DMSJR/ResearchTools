# Input and output file names
input_filename = 'proteinList.txt'
file_list_filename = 'SraAccList.txt'
output_filename = 'diamond_commands_samples.txt'

# Open the input file to read the accession numbers
with open(input_filename, 'r') as infile:
    proteinReferences = infile.readlines()

# Open the file list for reading the file names
with open(file_list_filename, 'r') as filelist:
    fileNames = filelist.readlines()

# Open the output file to write the commands
with open(output_filename, 'w') as outfile:
    # For each accession number
    for protein in proteinReferences:
        protein = protein.strip()
        # For each file name
        for fileName in fileNames:
            fileName = fileName.strip()
            # Extract the relevant part of the file name to use in the output
            output_prefix = fileName.split('_')[0]
            # Create the command using the accession number and the file name
            command = f"srun diamond blastp -q ../prodigal/{fileName}_proteins.faa -d ../../diamond_db/{protein} -o {output_prefix}_{protein}.tsv -f 6 qseqid qlen sallseqid slen evalue length pident\n"
            # Write the command to the output file
            outfile.write(command)

print(f"Command file '{output_filename}' created successfully.")
