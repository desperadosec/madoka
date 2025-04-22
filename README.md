# Madoka

A harness for adversarial testing of Magika

## Introduction

Defensive security tools that analyze malware are often dependent on static analyzers and file classifiers to establish baseline information about a sample. Google released Magika, a performant ML based file classifier that has an advertised 99% accuracy rating, and has already been integrated into various analysis stacks. But this, and other file classifiers are potentially vulnerable to errors as well as polyglots-- files that can be correctly classified as more than one type.

Compounding this problem is the gap between what a specification states is a valid file, and what real-world systems will interpret as a valid file.

To this end, Madoka is a barebones harness to use file mutation and fuzzing to produce output files that are incorrectly classified by Magika (or other static signatures) yet are still interpreted as valid by a target process.

## How to deploy the ELF fuzzer/polyglot finder



## Methodology
Fundamentally we need to:

* Generate a corpus of mutated ELF executable files
* Load Magika
* Find which files aren't identified as executable
* Verify which of these files still crash

## Building your own fuzz harness

The seed input examples that are included with Madoka are based on known crashing files, and the validation step is to simply verify that they still crash. However, there is the possibility of adding your own targets and fuzz scenarios by overriding the Verify with your own callable, and adding seed inputs to mutate it.


