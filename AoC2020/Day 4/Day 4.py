import re

def create_password_dict(input_lines):
    passports = []
    for passport in input_lines:
        passport = passport.split()
        passdict = {}
        for field in passport:
            key = field[0:3]
            value = field[4:]
            passdict.update({key: value})
        passports.append(passdict)
    return passports


def passport_required_fields(passports_file):
    passports = []
    for passport in passports_file:
        if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= passport.keys():
            passports.append(passport)
    return passports


def passport_validation(passports_file):
    passports = []
    for passport in passports_file:
        byr = int(passport["byr"])
        iyr = int(passport["iyr"])
        eyr = int(passport["eyr"])
        hgt = re.search("^(\d*)", passport["hgt"])
        hgtformat = re.search("([a-z]{2})$", passport["hgt"])
        hcl = re.search("^#\w{6}", passport["hcl"])
        if byr > 2002 or byr < 1920 or len(passport["byr"]) != 4:
            print("birth year", byr, "invalid")
        elif iyr > 2020 or iyr < 2010 or len(passport["iyr"]) != 4:
            print("issue year", iyr, "invalid")
        elif eyr > 2030 or eyr < 2020 or len(passport["eyr"]) != 4:
            print("expiration year", eyr, "invalid")
        elif hgtformat is None or hgtformat.group() not in ["cm", "in"]:
            print("height", passport["hgt"], "invalid")
        elif hgt.group() == "":
            print("height", passport["hgt"], "invalid")
        elif hgtformat.group() == "cm" and (int(hgt.group()) > 193 or int(hgt.group()) < 150):
            print("height", passport["hgt"], "invalid")
        elif hgtformat.group() == "in" and (int(hgt.group()) > 76 or int(hgt.group()) < 59):
            print("height", passport["hgt"], "invalid")
        elif hcl is None:
            print("hair colour", passport["hcl"], "invalid")
        elif passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print("eye colour", passport["ecl"], "invalid")
        elif len(passport["pid"]) != 9:
            print("passport id", passport["pid"], "invalid")
        else:
            passports.append(passport)
    return passports


passports_lines = open('input.txt', "r").read().split("\n\n")
passports_lines = [line.replace("\n", " ") for line in passports_lines]


# region --- Assignment 1 ---

passports = create_password_dict(passports_lines)

passports = passport_required_fields(passports)

print(len(passports), "passports valid!")

# endregion

# region --- Assignment 2 ---

passports = passport_validation(passports)
print(len(passports), "passports valid!")

# endregion
