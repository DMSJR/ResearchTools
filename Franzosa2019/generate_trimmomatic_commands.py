# Name of the file that contains the accession numbers
input_filename = 'SraAccList.txt'

# Name of the output file that will contain the commands
output_filename = 'trimmomatic_commands.txt'

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
        command = f"srun java -jar  /temporario2/dmarques/Trimmomatic/dist/jar/trimmomatic-0.40-rc1.jar PE ../sra/{accession_number}_1.fastq ../sra/{accession_number}_2.fastq {accession_number}_forward_paired.fastq {accession_number}_forward_unpaired.fastq {accession_number}_reverse_paired.fastq {accession_number}_reverse_unpaired.fastq ILLUMINACLIP:TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36 \n"
        # Write the command to the output file
        outfile.write(command)

print(f"Command file '{output_filename}' successfully created.")
