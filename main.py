#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init as colorama_init
import argparse
import os
from pack import GETSUB
import textwrap

if not os.path.isdir("result"):
    os.mkdir("result")

colorama_init(autoreset=True)

if __name__ == "__main__":
    ban = """\x1b[32m   _____       __    _______           __         
  / ___/__  __/ /_  / ____(_)___  ____/ /__  _____
  \__ \/ / / / __ \/ /_  / / __ \/ __  / _ \/ ___/
 ___/ / /_/ / /_/ / __/ / / / / / /_/ /  __/ /    
/____/\__,_/_.___/_/   /_/_/ /_/\__,_/\___/_/     

\x1b[37mSubdomain finder and checker
"""
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(ban),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Thanks for using this tools")

    parser.add_argument("-u", "--url",
                        type=str,
                        help="target url")
    parser.add_argument("--check",
                        action="store_true",
                        help="check status code of subdomain")

    args = parser.parse_args()

    if args.url == None:
        parser.print_help()
    else:
        q = GETSUB(args.url, args.check)
        q.request_to_api()
