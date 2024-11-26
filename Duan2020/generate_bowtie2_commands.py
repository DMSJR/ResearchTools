# Name of the file containing accession numbers
input_filename = 'SraAccList.txt'

# Name of the output file that will contain the commands
output_filename = 'bowtie2_commands.txt'

# Open the input file for reading
with open(input_filename, 'r') as infile:
    # Read all lines from the file
    accession_numbers = infile.readlines()

# Open the output file for writing
with open(output_filename, 'w') as outfile:
    # For each accession number, create a command and write it to the output file
    for accession_number in accession_numbers:
        # Strip whitespace from around the accession number
        accession_number = accession_number.strip()
        # Create the command using the accession number
        command = f"srun /temporario2/dmarques/.conda/envs/IC/bin/bowtie2 -x human_genome -1 ../trimmomatic/{accession_number}_forward_paired.fastq -2 ../trimmomatic/{accession_number}_reverse_paired.fastq --un-conc {accession_number}_paired_bt2_filtered\n"
        # Write the command to the output file
        outfile.write(command)

print(f"Command file '{output_filename}' created successfully.")
