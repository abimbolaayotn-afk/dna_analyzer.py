def analyze_dna(sequence):
    dna_seq = sequence.upper()
    length = len(dna_seq)
    count_a = dna_seq.count('A')
    count_c = dna_seq.count('C')
    count_g = dna_seq.count('G')
    count_t = dna_seq.count('T')
    gc_content = ((count_g + count_c) / length) * 100 if length > 0 else 0

    print("--- Analysis Results ---")
    print(f"Original Sequence: {dna_seq}")
    print(f"Total Base Pairs:  {length}")
    print(f"Nucleotide Freq:   A: {count_a} | C: {count_c} | G: {count_g} | T: {count_t}")
    print(f"GC Content:        {gc_content:.2f}%")

sample_dna = "atgctatgctatggccggca"
analyze_dna(sample_dna)
