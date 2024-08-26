dna_t = "TTTCCCAAAGGG"
def DNA_strand(dna):
    character_list = []
    for i in dna:
        if i == "T":
            change = i.replace("T","A")
            character_list.append(change)
        elif i == "A":
            change = i.replace("A","T")
            character_list.append(change)
        elif i == "C":
            change = i.replace("C","G")
            character_list.append(change)
        elif i == "G":
            change = i.replace("G","C")
            character_list.append(change)        
    join_list = "".join(character_list)
    return join_list

print(DNA_strand(dna_t))

#Alternative_solution

dna_t = "TTTCCCAAAGGG"

def DNA_strand(dna):
    mapping = {"T": "A", "A": "T", "C": "G", "G": "C"}
    return "".join(mapping[char] for char in dna)

print(DNA_strand(dna_t))