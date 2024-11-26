# Name of the file containing the accession numbers
input_filename = 'SraAccList.txt'

# Name of the output file that will contain the commands
output_filename = 'megahit_commands.txt'

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
        command = f"srun megahit -r ../flash/{accession_number}.extendedFrags.fastq -1 ../bowtie2/{accession_number}_paired_bt2_filtered.1 -2 ../bowtie2/{accession_number}_paired_bt2_filtered.2 -o {accession_number}_output\n"
        # Write the command to the output file
        outfile.write(command)

print(f"Command file '{output_filename}' created successfully.")
