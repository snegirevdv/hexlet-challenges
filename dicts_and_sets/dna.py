# https://ru.hexlet.io/challenges/python_dicts_to_rna_exercise


def to_rna(dna: str) -> str:
    DNA_TO_RNA = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    return "".join(DNA_TO_RNA[nt] for nt in dna)


def test_to_rna():
    assert to_rna("C") == "G"
    assert to_rna("G") == "C"
    assert to_rna("T") == "A"
    assert to_rna("A") == "U"
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"


test_to_rna()
