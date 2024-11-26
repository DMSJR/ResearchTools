# Name of the file that contains the accession numbers
input_filename = 'SraAccList.txt'

# Name of the output file that will contain the commands
output_filename = 'prodigal_commands.txt'

# Open the input file for reading
with open(input_filename, 'r') as infile:
    # Read all lines from the file
    accession_numbers = infile.readlines()

# Open the output file for writing
with open(output_filename, 'w') as outfile:
    # For each accession number, create a command and write it to the output file
    for accession_number in accession_numbers:
        # Remove whitespace around the accession number
        accession_number = accession_number.strip()
        # Create the command using the accession number
        command = f"srun /temporario2/dmarques/Prodigal/Prodigal-GoogleImport/prodigal -i ../megahit/{accession_number}_output/final.contigs.fa -o {accession_number}_coordinates -a {accession_number}_proteins.faa -d {accession_number}_genes.fasta\n"
        # Write the command to the output file
        outfile.write(command)

print(f"Command file '{output_filename}' successfully created.")
