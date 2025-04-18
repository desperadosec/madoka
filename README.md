# Madoka

Harness for adversarial testing of Magika

Fundamentally we need to:

* Generate corpus of non-exe files
* Load Magika
* Find which files aren't identified as executable
* Verify which of these files still crash

Methods to profile against each other:
Atheris:
    - Build clang for Atheris
    - Python harness to instantiate Magik model
    - In-memory byte buffer is function arg under fuzz
    - Check magik output

AFL-Fuzz:
    - Mutate trivial segfault, or other crash into ELF
    - Run against file as input
    - Mass classify via Magika

HyperPOM
    - Experimental, is this worthwhile?
    - Does natively support AARCH64
    - Hypervisor speed is promising

