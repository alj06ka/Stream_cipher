# binaryEncipher (C++ Library for Python)

Encrypts or decrypts file using LFSR algorithm

## Usage example
```
import binaryEncipher
...
input_file_name = 'test.txt'
output_file_name = 'test1.txt'
key = 21304852 # binary key converted to decimal (integer)
binaryEncipher.encryptFile(input_file_name, output_file_name, key)
```

## Available methods

**encryptFile**

Params:
* input_file_name: path to file to encrypt, string
* output_file_name: path to encrypted file, string
* key: integer value of binary key, integer

Return: 1 if success else 0

**version**
No params:

Return: version of extension

## How to compile
To compile this extension, run:

`python setup.py build`

Make sure that python is installed on your PC.