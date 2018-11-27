#include <iostream>
#include </usr/include/python3.7/Python.h>
#include <fstream>
#include <stdio.h>

class Key
/*Class for creating encryption key */
{
    int key;
    int *Polinomial;
    int PolinomialSize;
private:
    int m_mask;
public:
    Key(int m_key, int *m_Polinomial, int m_PolinomialSize)
    /*Initializing starting key value and Polinomial*/
    {
        key = m_key;
        Polinomial = m_Polinomial;
        PolinomialSize = m_PolinomialSize;
        m_mask = GenerateMask(m_Polinomial[0]);
    }

    char get_key_byte()
    /*
     * Generating byte of encrypted key
     * :params: None
     * :return: byte of encrypted key
    */
    {
        char newByte = 0;
        for(int i = 0; i < 8; i++)
        {
            char lastBit = GetBit(key, Polinomial[0]);
            newByte = InsertLastBit(newByte, lastBit);
            for (int j = 1; j < PolinomialSize; j++)
            {
                lastBit ^= GetBit(key, Polinomial[j]);
            }
            key = InsertLastBit(key, lastBit);
            key = RemoveBit(key, m_mask);

        }
        return newByte;
    }
private:
    char GetBit(int key, int bitPosition)
    /*
     * :param key: Key from which is needed to get key
     * :param bitPosition: Position of bit in key
     * :return: bit on selected position
    */
    {
        return char((key >> (bitPosition - 1)) & 1);
    }

    char InsertLastBit(char key, char bit)
    /*
     * Inserting new bit to the end of value
     * :param key: variable to insert bit
     * :param bit: bit to insert
     * :return: new value with inserted bit
    */
    {
        return (key << 1) | bit;
    }

    int InsertLastBit(int key, char bit)
    /*
     * Inserting new bit to the end of value
     * :param key: variable to insert bit
     * :param bit: bit to insert
     * :return: new value with inserted bit
    */
    {
        return (key << 1) | bit;
    }

    int RemoveBit(int key, int mask)
    /*
     * Removing bit that has been shifted to the left
     * e.g. Polinomial {23, 5} and after shifts 24th bit
     * has appeared. This function removes this bit
     * :param key: value from which is needed to remove bit
     * :param mask: mask of removing this bit
    */
    {
        return key & mask;
    }

    int GenerateMask(int bit)
    /*
     * Generating mask for removing extra bits, that
     * has been shifted in process of generating key
     * :param bit: last bit that need to be saved, e.g
     * :return: mask to remove this bits
    */
    {
        int mask = 0;
        for (int i = 0; i < bit; i++){
            mask = (mask << 1) + 1;
        }
        return mask;
    }
};

class Encryption
/*
 * Class that handling file encryption
 * It encrypts input file to output file
 * with encryption key
*/
{
    char *InputFileName;
    char *OutputFileName;
    int EncryptionKey;
private:
/*
 * Defining size of buffer for I/O operations
 * */
#define BUFFERSIZE 1024
    int PolinomialSize = 2;
public:
    Encryption(char *Input, char *Output, int key)
    {
        InputFileName = Input;
        OutputFileName = Output;
        EncryptionKey = key;
    }

    int EncryptFile()
    /*
     * Main function of encryption file
     * It is getting input and output file values, generating encryption key
     * and encrypts file
    */
    {
        FILE *InputFile, *OutputFile, *KeyByteFile;
        char buf[BUFFERSIZE];
        char keyBuf[BUFFERSIZE];
        long n;
        int Polinomial[] = {23, 5};
        Key EncryptKeyGenerator(EncryptionKey, Polinomial, PolinomialSize);
        InputFile = fopen(InputFileName, "rb");
        OutputFile = fopen(OutputFileName, "wb");
        KeyByteFile = fopen("tmp.bin", "wb");
        while (n = fread(buf, sizeof(char), BUFFERSIZE, InputFile))
        {
            for (int i = 0; i < BUFFERSIZE; i++)
            {
                char byte = EncryptKeyGenerator.get_key_byte();
                buf[i] ^= byte;
                keyBuf[i] = byte;
            }
            fwrite(buf, sizeof(char), n, OutputFile);
            fwrite(keyBuf, sizeof(char), n, KeyByteFile);
        }
        fcloseall();
        return 1;
    }
};

static PyObject* encryptFile(PyObject* self, PyObject* args)
{
    char* InputFileName;
    char* OutputFileName;
    int key;
    if (!PyArg_ParseTuple(args, "ssi", &InputFileName, &OutputFileName, &key))
        return NULL;
    Encryption Enc(InputFileName, OutputFileName, key);
    return Py_BuildValue("i", Enc.EncryptFile());
};

static PyObject* version(PyObject* self)
{
    return Py_BuildValue("s", "Version 1.0");
}

static PyMethodDef myMethods[] = {
        {"encryptFile", encryptFile, METH_VARARGS, "Encrypting file using binary key encryption"},
        {"version", (PyCFunction)version, METH_NOARGS, "Returns version of extension"},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef binaryEncipher = {
        PyModuleDef_HEAD_INIT,
        "binaryEncipher",
        "Binary Encryption Module",
        -1,
        myMethods
};

PyMODINIT_FUNC PyInit_binaryEncipher(void)
{
    return PyModule_Create(&binaryEncipher);
}

// Unit self-testing
//int main()
//{
//    char InputFileName[] = "test.txt";
//    char OutputFileName[] = "test1.txt";
//    int key = 5592405;
//    Encryption Enc(InputFileName, OutputFileName, key);
//    int test = Enc.EncryptFile();
//}