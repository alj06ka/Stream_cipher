# Stream cipher
Python implementation of stream cipher using LFSR algorithm

This algorithm uses key with length of 23. But it's easy to change.

### Speed of encrypting
To improve encrypting algorithm, I have made 2 implementation of LFSR algorithm:
1. Python implementation
2. Own C++ library for python.

C++ library increased speed of encryption in **~15 times**. Pretty fast, I think :)
This library in `binaryEncipher` folder.

### How to run
To run GUI interface you need to implement gui.py script.

### File description

1. gui.py

Main file. Includes interface for interacting with encipher.

2. encryption.py

Includes classes for encryption and key generating in python
Works not as fast as C++ library implementation, so not used in GUI.
From this file only string_to_int and bits_from_file function is used.

3. check_input.py

Includes function for checking correctness of input cypher key.

4. binaryEncipher.so

C++ library extension. More info in `binaryEncipher/` folder