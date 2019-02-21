#!/usr/bin/env python
"""Test script for the bits-backupify python module."""

import os
import sys

# add bitsapiclient to the path
mypath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(mypath, "bits"))

from bits.backupify import Backupify
from config import clientid, clientsecret


def main():
    """Execute the main funciton."""
    b = Backupify(
        client_id=clientid,
        client_secret=clientsecret,
        verbose=True,
    )
    users = b.get_users()
    print('Retrieved %s users from Backupify.' % (len(users)))

if __name__ == '__main__':
    main()
