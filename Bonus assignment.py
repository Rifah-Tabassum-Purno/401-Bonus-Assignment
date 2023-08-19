def read_file(filename):
    sequences = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        current_sequence = ''
        current_header = None
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                if current_header is not None:
                    sequences[current_header] = current_sequence
                current_header = line[1:]
                current_sequence = ''
            else:
                current_sequence += line
        if current_header is not None:
            sequences[current_header] = current_sequence
    return sequences

def find_gene(dna_sequence, promoter_sequence):
    promoter_index = dna_sequence.find(promoter_sequence)
    
    if promoter_index == -1:
        print("Promoter sequence not found in the DNA sequence.")
        return False
    
    start_codon = "ATG"
    max_distance_to_promoter = 30
    max_gene_length = 50 * 3  # Converting amino acids to nucleotides
    
    for i in range(promoter_index, min(promoter_index + max_distance_to_promoter, len(dna_sequence) - 2)):
        if dna_sequence[i:i+3] == start_codon:
            gene_sequence = dna_sequence[i:]
            for j in range(0, len(gene_sequence), 3):
                codon = gene_sequence[j:j+3]
                if codon in ("TAA", "TAG", "TGA"):  # Stop codons
                    if j >= max_gene_length:
                        print("Gene found")
                        return True
                    else:
                        break
    print("Gene not found")
    return False

input_file = "sequence.txt"
promoter_sequence = input("Enter the promoter sequence: ").upper()

sequences = read_file(input_file)
if "DNA_sequence" in sequences:
    dna_sequence = sequences["DNA_sequence"]
    dna_sequence = dna_sequence.upper()
    find_gene(dna_sequence, promoter_sequence)
else:
    print("DNA sequence not found in the provided FASTA file.")