**`#`** subhawk


**subhawk** is a simple subdomain enumeration tool that discovers subdomains by using a custom or built-in wordlist.

**`##`** Requirements

Before using the tool, you need to install the required libraries. You can do this easily by running the following command:

```bash
pip install -r requirements.txt

## Usage

```
Once the dependencies are installed, you can run the script with the desired options:
python subhawk.py -d example.com


You can also use other options like specifying an output file:
python subhawk.py -d example.com -o output.txt


## Available Options

usage: subhawk.py [-h] -d DOMAIN [-v] [-o OUTPUT] [-l LIST] [-t TIMEOUT]

options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   target domain [example.com]
  -v, --verbose         show valid and invalid subdomains
  -o, --output OUTPUT   save the valid subdomains in a text file
  -l, --list LIST       add list of subdomains [example.txt]
  -t, --timeout TIMEOUT
                        set the timeout (in seconds) for each request. default is 3 seconds

## Author:
Abdullah Fayyad