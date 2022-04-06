#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""VirusTotal API Download Tool."""

import argparse
import os

import vt
from vt.error import APIError


def main():
    """Download the file specified on the command line."""
    # Parse command line arguments for file hashes.
    parser = argparse.ArgumentParser(
        description="Download files from VirusTotal. Requires API key in `api.key` file.",
        epilog='Example: vtget.py "f970438c1f06e2431a11cecd4553c50b"',
    )
    parser.add_argument(
        "hash",
        metavar="HASH",
        help="File hash to download.",
    )
    args = parser.parse_args()

    # Load the api key.
    with open("api.key", "rb") as key_file:
        api_key = key_file.readlines()[0].strip()

    # Create a VirusTotal client instance.
    client = vt.Client(api_key.decode("utf-8"))

    # Download the file.
    print("Downloading file...")
    try:
        with open(args.hash, "wb") as sample_file:
            client.download_file(args.hash, sample_file)
        print(f"File saved as: {args.hash}")
    except APIError as error:
        os.unlink(args.hash)
        if error.args[0] == "NotFoundError":
            print("File not found.")
        else:
            raise error
    finally:
        client.close()


# Execute the script.
if __name__ == "__main__":
    main()
