print("Script is running....")

import hashlib

def generate_checksums(filename):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

        return md5.hexdigest(),sha1.hexdigest(),sha256.hexdigest()
    
def compare_checksums(filename, checksums_to_compare):
        print(f"Comparing checksums for file:{filename}")
        checksums = generate_checksums(filename)

        for i, (generated, to_compare) in enumerate(zip(checksums,checksums_to_compare)):
            if generated != to_compare:
                print(f"Checksum{i+1} does not match: {generated} !={to_compare}")
                return False

        print("All checksums match.")
        return True
    
def read_checksums_from_file(checksums_file):
        print(f"Reading checksums from file: {checksums_file}")
        with open(checksums_file, 'r') as file:
            lines = file.readlines()
            checksums = [line.strip() for line in lines]
        return checksums
    
if __name__ == "__main__":
        file_to_check = "orgdoc.txt"
        checksums_file = "check_sums.txt"
        checksums_to_compare = read_checksums_from_file(checksums_file)
        compare_checksums(file_to_check,checksums_to_compare)