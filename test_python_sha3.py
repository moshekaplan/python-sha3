#! usr/bin/env python

# Use pysha3 from pypi for testing
import sha3
import hashlib 

import python_sha3

def main():
  # My implementation
  python_sha3_functions = [ python_sha3.sha3_224, python_sha3.sha3_256,
                            python_sha3.sha3_384, python_sha3.sha3_512]
  # pysha3
  pysha3_hashes = [hashlib.sha3_224, hashlib.sha3_256, hashlib.sha3_384, hashlib.sha3_512]

  for i,j in zip(python_sha3_functions, pysha3_hashes):
    for x in range(1000):
      x = str(x)
      if i(x).hexdigest() != j(x).hexdigest():
        print (x)
        return
        
if __name__ == '__main__':
  main()
