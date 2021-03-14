# python3 file
import hashlib
import fileinput
import sys


def make_manifest(filename, delimiter):
    data = str('').encode('utf-8')
    for line in fileinput.input(filename):
        data = data + str(line).encode('utf-8')

    hl = hashlib.sha256()
    hl.update(data)
    hash = hl.hexdigest()

    manfile = filename + ".mnf"
    fh = open( manfile, "w")
    line = str(filename) + delimiter + str(hash)
    fh.write(line)
    fh.close()

    return manfile


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Creates a manifest file for a filename')
        print('usage: make_manifest filename [delimiter-string]')
        print('\noutput file will be named filename.mnf')
        print('default delimiter string is " | "')
        print('output file contents: [filename | sha256-hex-digest-of-filename], assuming the default delimiter')
        print('\nThe command "openssl sha256 filename > hashcheck.txt" can be used to verify the hash')
        sys.exit(0)
    else:
        filename = sys.argv[1]
        delimiter = ' | '
        if len(sys.argv) > 2:
            delimiter = sys.argv[2]
        outfilename = make_manifest(filename, delimiter)
        print('created ' + outfilename)

