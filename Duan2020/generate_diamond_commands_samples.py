# Nome dos arquivos de entrada e saída
input_filename = 'proteinList.txt'
file_list_filename = 'SraAccList.txt'
output_filename = 'diamond_commands_samples.txt'

# Abre o arquivo de entrada para leitura dos accession numbers
with open(input_filename, 'r') as infile:
    proteinReferences = infile.readlines()

# Abre o arquivo de lista de arquivos para leitura dos nomes dos arquivos
with open(file_list_filename, 'r') as filelist:
    fileNames = filelist.readlines()

# Abre o arquivo de saída para escrita dos comandos
with open(output_filename, 'w') as outfile:
    # Para cada accession number
    for protein in proteinReferences:
        protein = protein.strip()
        # Para cada nome de arquivo
        for fileName in fileNames:
            fileName = fileName.strip()
            # Extrai a parte relevante do nome do arquivo para usar na saída
            output_prefix = fileName.split('_')[0]
            # Cria o comando usando o accession number e o nome do arquivo
            command = f"srun diamond blastp -q ../prodigal/{fileName}_proteins.faa -d ../../diamond_db/{protein} -o {output_prefix}_{protein}.tsv -f 6 qseqid qlen sallseqid slen evalue length pident\n"
            # Escreve o comando no arquivo de saída
            outfile.write(command)

print(f"Arquivo de comandos '{output_filename}' criado com sucesso.")