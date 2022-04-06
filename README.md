# vtget
VirusTotal API Download Utility. Written in Python3.

## Installation

To use this, you'll need to create an `api.key` file in the same directory as the `vtget.py` file. This key file must contain your VirusTotal API key. To use the download feature of the VirusTotal API, you'll need a Premium account.

You'll also need to install dependencies:

* `pip install -r requirements.txt`

## Usage

Usage is simple:

```
(.venv) user@host vtget % ./vtget.py --help
usage: vtget.py [-h] HASH

Download files from VirusTotal. Requires API key in `api.key` file.

positional arguments:
  HASH        File hash to download.

optional arguments:
  -h, --help  show this help message and exit

Example: vtget.py "f970438c1f06e2431a11cecd4553c50b"
```