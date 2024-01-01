# https://ru.hexlet.io/challenges/python_dicts_to_rna_exercise


def to_rna(dna: str) -> str:
    DNA_TO_RNA = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    return "".join(DNA_TO_RNA[nt] for nt in dna)

