#!/usr/bin/env python3
# encoding: utf-8

import sys

def letter2number(letter):
    """Converts a letter to the corresponding number,
    e.g. A = 10, B = 11, ... Z = 35

    :letter: Arbitrary input letter
    :returns: Corresponding number

    """
    values = list(range(10,36))
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
            "Z"]
    mapping = dict()
    for (v,a) in zip(values, alphabet):
        mapping.update({a: v})

    return mapping.get(letter.capitalize())

def prepareIBAN(iban):
    """Prepares an IBAN for the mod 97 calculation

    :iban: valid german IBAN
    :returns: prepared IBAN for modulo calculation

    """
    letters = iban[0:2]
    checksum = iban[2:4]
    numbers = iban[4:]

    return numbers + str(letter2number(letters[0])) + \
        str(letter2number(letters[1])) + checksum

def validIBAN(iban):
    """Do the actual calculation

    :iban: german IBAN
    :returns: boolean, if iban is valid

    """
    if len(iban) != 22:
        raise Exception("IBAN does not have the correct lenght")
        return 1
    else:
        return int(prepareIBAN(iban)) % 97 == 1

def buildIBAN(blz, knr):
    """Build a valid german IBAN

    :blz: Bankleitzahl
    :knr: Konto-Nr.
    :returns: valid IBAN

    """
    letters = "DE"
    knr = knr.zfill(18-len(blz))
    numbers = blz + knr

    for c in range(2,99):
        checksum = str(c).zfill(2)
        iban = letters + str(checksum) + numbers
        if validIBAN(iban):
            return iban
        else:
            continue
    raise Exception("No valid IBAN possible with given BLZ and Konto")
    return 1

def usage():
    """Help function to explain the usage
    :returns: Help message to explain the usage.

    """
    print("Usage: ./main.py <BLZ> <Konto>")
    return 1

if __name__ == "__main__":
    if len(sys.argv[1:]) != 2:
        usage()
    else:
        print(buildIBAN(str(sys.argv[1]), str(sys.argv[2])))
