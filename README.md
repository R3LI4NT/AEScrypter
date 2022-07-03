# AEScrypter
Encrypt and Decrypt files with Advanced Encryption Standard.

## Usage
| DESCRIPTION | COMMAND |
| ------------- | ------------- |
| Encrypt file | -e / --encrypt |
| Decrypt file | -d / --decrypt |
| Buffer size (128 / 192 / 256) | -b / --buffersize |
| Password to encrypt and decrypt file | -p / --password |
| Request help | -h / --help |

## Insallation
```
> git clone https://github.com/R3LI4NT/AEScrypter

> cd AEScrypter

> pip3 install -r requirements.txt

> sudo apt-get install shred
```

`EXAMPLE:` **File ENCRYPTED**
```python
python3 AEScrypter.py -e <file> -b <buffersize> -p <password>
```

![file_ENCRYPTED](https://user-images.githubusercontent.com/75953873/177024091-193802d8-8f47-44cc-9fe9-9f3f422e8d35.png)


`EXAMPLE:` **File DECRYPTED**
```python
python3 AEScrypter.py -d <file> -b <buffersize> -p <password>
```

![file_DECRYPTED](https://user-images.githubusercontent.com/75953873/177024097-89f3f294-68e2-4e90-a6f1-5eac1ff22ef2.png)


**Package powered by:** https://www.aescrypt.com/
