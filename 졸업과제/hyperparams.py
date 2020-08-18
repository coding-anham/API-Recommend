#!/usr/bin/python3
BASE_PATH = "data/"
SEQ_PATH = BASE_PATH + "sequence/"
STR_PATH = BASE_PATH + "structure/"
CLF_PATH = "clf/"
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
    },
    "rand"  : {
        0   : "npz/random_apt0.npz",
        1   : "npz/random_apt1.npz",
        2   : "npz/random_apt2.npz",
        3   : "npz/random_apt3.npz",
        4   : "npz/random_apt4.npz",
        5   : "npz/random_apt5.npz",
        6   : "npz/random_apt6.npz",
        7   : "npz/random_apt7.npz",
        8   : "npz/random_apt8.npz",
        9   : "npz/random_apt9.npz"
    },
    "genetic"   : {
        0   : "npz/genetic_apt0.npz",
        1   : "npz/genetic_apt1.npz",
        2   : "npz/genetic_apt2.npz",
        3   : "npz/genetic_apt3.npz",
        4   : "npz/genetic_apt4.npz",
        5   : "npz/genetic_apt5.npz",
        6   : "npz/genetic_apt6.npz",
        7   : "npz/genetic_apt7.npz",
        8   : "npz/genetic_apt8.npz",
        9   : "npz/genetic_apt9.npz"
    },
    "protein" : "npz/protein.npz",
    "mix"   : "npz/mix.npz"
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
    },
    "rand"  : {
        0   : BASE_PATH + "random_apt0.csv",
        1   : BASE_PATH + "random_apt1.csv",
        2   : BASE_PATH + "random_apt2.csv",
        3   : BASE_PATH + "random_apt3.csv",
        4   : BASE_PATH + "random_apt4.csv",
        5   : BASE_PATH + "random_apt5.csv",
        6   : BASE_PATH + "random_apt6.csv",
        7   : BASE_PATH + "random_apt7.csv",
        8   : BASE_PATH + "random_apt8.csv",
        9   : BASE_PATH + "random_apt9.csv"
    },
    "genetic"   : {
        0   : BASE_PATH + "genetic_apt0.csv",
        1   : BASE_PATH + "genetic_apt1.csv",
        2   : BASE_PATH + "genetic_apt2.csv",
        3   : BASE_PATH + "genetic_apt3.csv",
        4   : BASE_PATH + "genetic_apt4.csv",
        5   : BASE_PATH + "genetic_apt5.csv",
        6   : BASE_PATH + "genetic_apt6.csv",
        7   : BASE_PATH + "genetic_apt7.csv",
        8   : BASE_PATH + "genetic_apt8.csv",
        9   : BASE_PATH + "genetic_apt9.csv"
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

PIC_PATH = {
    "randomForests": {
        "A": CLF_PATH + "randomForests_A.pickle",
        "B": CLF_PATH + "randomForests_B.pickle"
    },
    "mix_randomForests": CLF_PATH + "mix_randomForests.pickle"
    ,
    "svm": {
        "A": CLF_PATH + "svm_A.pickle",
        "B": CLF_PATH + "svm_B.pickle"
    },
    "NaiveBayesClassifier": {
        "A": CLF_PATH + "NaiveBayesClassifier_A.pickle",
        "B": CLF_PATH + "NaiveBayesClassifier_B.pickle"
    },
    "BaggingLinearsvmClassifier": {
        "A": CLF_PATH + "BaggingLinearsvmClassifier_A.pickle",
        "B": CLF_PATH + "BaggingLinearsvmClassifier_B.pickle"
    },
    "BaggingKNeighborsClassifier": {
        "A": CLF_PATH + "BaggingKNeighborsClassifier_A.pickle",
        "B": CLF_PATH + "BaggingKNeighborsClassifier_B.pickle"
    },
    "GradientBoost": {
        "A": CLF_PATH + "GradientBoost_A.pickle",
        "B": CLF_PATH + "GradientBoost_B.pickle"
    },
    "BaggingRandomForestClassifier": {
        "A": CLF_PATH + "BaggingRandomForestClassifier_A.pickle",
        "B": CLF_PATH + "BaggingRandomForestClassifier_B.pickle"
    },
    "Voting": {
        "A": CLF_PATH + "Voting_A.pickle",
        "B": CLF_PATH + "Voting_B.pickle"
    }
}