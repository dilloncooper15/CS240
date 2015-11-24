# CS 240 Lab 01
# Dillon J. Cooper

# Exercise 1


def main():
    filename = input('Which file would you like to backup?')
    new_filename = filename + '.bak'
    backup_file(new_filename, filename)


def backup_file(new_filename, filename):
    """ (file open for reading) -> NoneType
    Retrieves user input.
    """

    backup = open(new_filename, 'w')
    source = open(filename, 'r')
    new_source = source.read()
    backup.write(new_source)
    new_source.close()
    backup.close()


if __name__ == '__main__':
    main()

# Exercise 2


def parse():
    """ (file open for reading) -> NoneType
    Reads the contents of alkaline_metals.txt and stores it in a list of lists\
    with each inner list containing the name, atomic number, and atomic weight\
    for an element.
    """
    alkaline_metals = []
    for line in open('alkaline_metals.txt'):
        alkaline_metals.append(line.strip().split(' '))
    return(alkaline_metals)

# Exercise 3


def skip_header(reader):
    """ (file open for reading) -> str
    Skip the header in reader and return the first real piece of data.
    """
    line = reader.readline()
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()
    return line


def process_file(reader):
    """ (file open for reading) -> NoneType
    Read and print the data from reader, which must start with a single\
    description line, then a sequence of lines beginning with '#', then a\
    sequence of data.
    """
    line = skip_header(reader).strip()
    print(line)
    print(reader.read())


# Exercise 4


import time_series


def smallest_value_skip(reader):
    """ (file open for reading) -> NoneType
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header.  Skip missing values, which
    are indicated with a hyphen.
    """

    line = time_series.skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    if line != '':
        smallest = int(line)

        for line in reader:
            line = line.strip()
            if line != '-':
                continue
            value = int(line)
            smallest = min(smallest, value)

    return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))


# Exercise 5


def read_molecule(reader):
    """ (file open for reading) -> list or NoneType

    Read a single molecule from reader and return it, or return None to signal
    end of file.  The first item in the result is the name of the compound;
    each list contains an atom type and the X, Y, and Z coordinates of that
    atom.
    """

    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

    if not (line.startswith('CMNT') or line.isspace()):
        # Name of the molecule: "COMPND   name"
        key, name = line.split()

        # Other lines are either "END" or "ATOM num atom_type x y z"
        molecule = [name]
    else:
        molecule = None

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            key, num, atom_type, x, y, z = line.split()
            if molecule is None:
                molecule = []
            molecule.append([atom_type, x, y, z])

    return molecule


def read_all_molecules(reader):
    """ (file open for reading) -> list
    Read zero or more molecules from reader, returning a list of the molecule
    information.
    """

    # The list of molecule information.
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:  # None is treated as False in an if statement
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)
