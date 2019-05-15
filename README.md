# getbob
Commandline tool to download Defold's Bob

### Download
Install with `pip install getbob`

Can also be used as a python module


### Usage

```
$ getbob --help
usage: getbob [-h] [--output OUTPUT] [--version [VERSION]] [--force]
                   [--verbose]

Arguments:
  -h, --help           show this help message and exit
  --output OUTPUT      File name of the output, required
  --version [VERSION]  Which version to download, if not provided the latest
                       stable will be used. Either: sha1 string, version
                       string (1.2.152) or 'beta'
  --force              Overwrite already downloaded bob
  --verbose            Print verbose output

```