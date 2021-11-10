import requests
from colorama import init as colorama_init
import argparse
import os, random
from pack import GETSUB
import textwrap

if not os.path.isdir("result"):
    os.mkdir("result")

def head():
    h = """Mozilla/4.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.1245.0 Safari/537.36
Mozilla/4.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0
Mozilla/4.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19
Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1
Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100
Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30
Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.60 Safari/534.30
Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13
Mozilla/5.0 (Macintosh; AMD Mac OS X 10_8_2) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/18.6.872
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36""".splitlines()
    hh = random.choice(h)
    return hh

colorama_init(autoreset=True)

def print_status_code(url, scode):
    format = "\x1b[34m[ \x1b[33m* \x1b[34m] \x1b[37m{:<50} -->   \x1b[34m[ {} \x1b[34m]"
    if scode == 200:
        new = format.format(url, "\x1b[32m" + str(scode))
    else:
        new = format.format(url, "\x1b[31m" + str(scode))
    print(new)


def save_file(file, url):
    with open("result/"+file, "a") as f:
        f.write(url+"\n")
        f.close()
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
                        required=True,
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