# Name of the file containing accession numbers
input_filename = 'SraAccList.txt'

# Name of the output file that will contain the commands
output_filename = 'gzip_commands.txt'

# Open the input file for reading
with open(input_filename, 'r') as infile:
    # Read all lines from the file
    accession_numbers = infile.readlines()

# Open the output file for writing
with open(output_filename, 'w') as outfile:
    # For each accession number, create commands and write them to the output file
    for accession_number in accession_numbers:
        # Strip whitespace from around the accession number
        accession_number = accession_number.strip()
        # Create the command for the first file
        command = f"srun gzip {accession_number}_1.fastq\n"
        # Write the command to the output file
        outfile.write(command)
        # Create the command for the second file
        command = f"srun gzip {accession_number}_2.fastq\n"
        # Write the command to the output file
        outfile.write(command)

print(f"Command file '{output_filename}' created successfully.")
