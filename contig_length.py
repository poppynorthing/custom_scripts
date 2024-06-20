#!/usr/bin/env python3

#Note: The base of this script was generated from chatGPT on 20June2024, and edited by me (poppy northing) subsequently
#Explanation:
#parse_fasta(filename):

#This function takes a filename as input and returns a dictionary sequences where keys are sequence names and values are sequence lengths.
#It reads through the FASTA file line by line. When encountering a line starting with '>', it assumes it's a sequence header and extracts the sequence name.
#For subsequent lines (which contain the sequence itself), it calculates the length of the sequence and accumulates it in sequence_length.
#After encountering a new sequence header or reaching the end of the file, it stores the previous sequence's name and length in the sequences dictionary.
#main():

#This function serves as the entry point of the script.
#It checks if the script is called with exactly one argument (the input FASTA filename).
#If the argument count is correct, it calls parse_fasta(filename) to parse the FASTA file and retrieve the sequence name and length information.
#Finally, it iterates through the dictionary returned by parse_fasta() and prints each sequence's name and length.
#Usage:
#Save the script into a file (e.g., fasta_parser.py) and run it from the command line with the input FASTA file as an argument:
#python contig_length.py input.fasta


def parse_fasta(filename):
    sequences = {}  # Dictionary to store sequence names and lengths

    with open(filename, 'r') as f:
        sequence_name = ''
        sequence_length = 0

        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if sequence_name:
                    sequences[sequence_name] = sequence_length
                sequence_name = line[1:]
                sequence_length = 0
            else:
                sequence_length += len(line)

        # Add the last sequence after EOF
        if sequence_name:
            sequences[sequence_name] = sequence_length

    return sequences

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py input.fasta")
        return
    
    filename = sys.argv[1]
    sequences = parse_fasta(filename)

    for name, length in sequences.items():
        print(f"Sequence: {name}, Length: {length}")

if __name__ == "__main__":
    main()