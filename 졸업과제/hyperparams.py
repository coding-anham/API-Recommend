#!/usr/bin/python3
BASE_PATH = "data/"
SEQ_PATH = BASE_PATH + "sequence/"
STR_PATH = BASE_PATH + "structure/"
NPZ_PATH = {
    "NPInter" : "npz/NPInter.npz",
    "RPI" : {
        1807 : "npz/RPI1807.npz",
        2241 : "npz/RPI2241.npz",
        369  : "npz/RPI369.npz",
        488  : "npz/RPI488.npz"
    },
    "API" : {
        "A_train"   : "npz/API_A_train.npz",
        "B_train"   : "npz/API_B_train.npz",
        "A_test"    : "npz/API_A_test.npz",
        "B_test"    : "npz/API_B_test.npz"
    }

}

PAIRS_PATH = {
    "NPInter" : BASE_PATH + "NPInter_pairs.txt",
    "RPI" : {
        1807 : BASE_PATH + "RPI1807_pairs.txt",
        2241 : BASE_PATH + "RPI2241_pairs.txt",
        369  : BASE_PATH + "RPI369_pairs.txt",
        488  : BASE_PATH + "RPI488_pairs.txt"
    },
    "API" : {
        "A_train"   : BASE_PATH + "benchmark_A_train_sequences.csv",
        "B_train"   : BASE_PATH + "benchmark_B_train_sequences.csv",
        "A_test"    : BASE_PATH + "benchmark_A_test_sequences.csv",
        "B_test"    : BASE_PATH + "benchmark_B_test_sequences.csv"
    }
}
SEQ_PATH = {
    "NPInter" : {
        "RNA"     : SEQ_PATH + "NPinter_rna_seq.fa",
        "Protein" : SEQ_PATH + "NPinter_protein_seq.fa"
    },
    "RPI" : {
        1807 : {
            "RNA"     : SEQ_PATH + "RPI1807_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI1807_protein_seq.fa"
        },
        2241 : {
            "RNA"     : SEQ_PATH + "RPI2241_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI2241_protein_seq.fa"
        },
        369  : {
            "RNA"     : SEQ_PATH + "RPI369_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI369_protein_seq.fa"
        },
        488  : {
            "RNA"     : SEQ_PATH + "RPI488_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI488_protein_seq.fa"
        }
    }
}