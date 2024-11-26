import xml.etree.ElementTree as ET
import csv
import re

# Function to extract data from the XML
def extract_srr_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = []
    
    # Iterating through each experiment package in the XML
    for experiment_package in root.findall('EXPERIMENT_PACKAGE'):
        # Finding the RUN tag with alias and accession
        run = experiment_package.find(".//RUN")
        if run is not None:
            srr = run.get('accession')  # SRR
            run_alias = run.get('alias')  # Alias like PRISM_7843.1_kneaddata_paired_2.fq.gz
            
            if run_alias:
                # Extract the part of the name before the dot (PRISM_7843 in this case)
                sample_alias = run_alias.split('.')[0]
                
                # Add the SRR and sample name (sample_alias) to the list
                data.append((sample_alias, srr))
    
    return data

# Function to read the CSV and create a dictionary of conditions
def read_conditions_from_csv(csv_file):
    conditions = {}
    
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)  # Skip the header
        
        for row in reader:
            sample_id = row[0]
            
            # Case PRISM|XXXX -> PRISM_XXXX
            if 'PRISM|' in sample_id:
                sample_id = sample_id.replace('|', '_')
            
            # Case Validation|LLDeep_XXXX -> LLDeep_XXXX
            elif 'Validation|LLDeep_' in sample_id:
                sample_id = sample_id.replace('Validation|', '')
            
            # Case Validation|UMCGXXXXXXX -> UMCGXXXXXXX (considering the first part if there's a dot)
            elif 'Validation|UMCG' in sample_id:
                match = re.search(r'UMCG\d+', sample_id)
                if match:
                    sample_id = match.group(0)
            
            diagnosis = row[1]
            conditions[sample_id] = diagnosis
    
    return conditions

# Function to combine the data and generate the TSV
def generate_tsv(output_file, xml_data, conditions):
    with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(['SRR', 'Participant_ID', 'Diagnosis'])
        
        for sample_alias, srr in xml_data:
            diagnosis = conditions.get(sample_alias, 'Unknown')  # If not found in CSV, mark as "Unknown"
            writer.writerow([srr, sample_alias, diagnosis])

# File paths
xml_file = 'SraExperimentPackage.xml'
csv_file = 'individuos-condicoes.csv'
output_file = 'SRR-condicoes.tsv'

# Extracting data from the XML and CSV
xml_data = extract_srr_from_xml(xml_file)
conditions = read_conditions_from_csv(csv_file)

# Generating the final TSV file
generate_tsv(output_file, xml_data, conditions)

print("TSV file generated successfully.")
