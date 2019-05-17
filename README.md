# getbob
Commandline tool to download Defold's Bob

### Download
Install with `pip install getbob`

Can also be used as a python module


### Usage

```
$ getbob --help
usage: getbob [-h] [-o, --output OUTPUT] [-v [VERSION]] [-f] [--verbose]

Commandline tool to download Defold's Bob

required arguments:
  -o, --output OUTPUT   File name of the output

optional arguments:
  -h, --help            show this help message and exit
  -v [VERSION], --version [VERSION]
                        Which version to download, if not provided the latest
                        stable will be used. Either: sha1 string, version
                        string (1.2.152) or 'beta'
  -f, --force           Overwrite already downloaded bob
  --verbose             Print verbose output

```