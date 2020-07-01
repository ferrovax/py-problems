def reverse_complement(dna):
    r, index = [], len(dna) -1

    while index >= 0:
        if dna[index] == 'A':
            r.append('T')
        elif dna[index] == 'T':
            r.append('A')
        elif dna[index] == 'C':
            r.append('G')
        elif dna[index] == 'G':
            r.append('C')

        index -= 1

    return ''.join(r)

#DNA = "GGCTGATAGAACGAATAGGTGAGCTCTCCGTGTTAGCAGGAAATTTAGCGCACCAAAGCAGAAGCGACACTCACGACCGATTGAACGTACCCTTGGGGGACCAGCCTACATTGCAAGGGTGATGTCCCTCCTCCGATCTTTACTACCATGGGCCTAAGATTACGTGAGGCTTACGCTACGGCCCTATTACTGTGGGGCTCAGGTCACTTGGCTATCCGCACCAGAATTAGGCAGTTATCCCGCATACGAGTAGCAACAGACTAAAACTATGATATTCTCTGGAATGCGCGGATTCAGCCATCCAGTTGCCATAAAGCTTGCACCTCGGTTACACGAAAATGGGGGCATAGCAGGGTGTGGATTCAATTCGACCTGTCTCCCTGGAATATGGAGATGCGTTTCGCATTCTGAGCTGGATGTCAGTGGCGGACCTTAAACTAAGACGGGCAGAGCACCGCTAAAAGCTGCCGAGGGATGAACACACTGGGACCTCGCCCACAGCGACGAAGCGAGAAAGAGTCTCCAGCGCACGGTTGTTAAGAAATAGGAAGTAAGGGATAAGCGTCCAATGCCACATCGACACGCAATTATCACTTAACAGGTGAAGGTAAATTAAGGCAGAGTTCAGCAACGCGTCGTATTTTTGAACTGAAAGGAGCGGAGATGCGCACTGATTACTTATAATTCCGTCTGCGCTTTTCGCAAATACTCGCGGAGGACAAAGCTCTGGTTGTGAAAGAACGGCGCTTGCGTCTGGCGGTGCTAGCTATGCCGATCTAAGGCTTACTTTTCTAGCCAGGTGATGCTCTGTTACTGAATGGGTCCATCAGCTTTTACGCCAGCTAGCGAGTCCG"

#print(reverse_complement(DNA))
