#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import random

class GETSUB:

    def __init__(self, sites="", autocheck=False):
        self.sites = sites
        self.autocheck = autocheck
        self.subdolist = []

    #Another Func
    def print_status_code(self, url, scode):
        format = "\x1b[34m[ \x1b[33m* \x1b[34m] \x1b[37m{:<50} -->   \x1b[34m[ {} \x1b[34m]"
        if scode == 200:
            new = format.format(url, "\x1b[32m" + str(scode))
        else:
            new = format.format(url, "\x1b[31m" + str(scode))
        print(new)

    def head(self):
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
        return {"User-Agent": hh}

    def save_file(self, file, url):
        with open("result/"+file, "a") as f:
            f.write(url+"\n")
            f.close()
    #AnotherFunc

    def check_status_code_subdomain(self):
        for sub in self.subdolist:
            try:
                resp = requests.get(sub, headers=self.head(),
                                    timeout=70).status_code
                self.print_status_code(sub, resp)
                self.save_file(str(resp)+".txt", sub)
            except Exception:
                self.print_status_code(sub, "Die")
                self.save_file("die.txt", sub)

    def parsing_subdomain(self, source):
        sub = source.splitlines()
        for s in sub:
            newsub = s.split(",")[0]
            httpsub = "http://"+newsub
            self.subdolist.append(httpsub)
            self.save_file("subdomain.txt", httpsub)
        print("\x1b[34m[ \x1b[32m√ \x1b[34m] \x1b[37mFound {} subdomain in {}".format(
            str(len(self.subdolist)), self.get_root_domain()))

        if self.autocheck:
            self.check_status_code_subdomain()
        else:
            for s in self.subdolist:
                print("\x1b[34m[ \x1b[33m* \x1b[34m] \x1b[37m{}".format(s))

    def get_root_domain(self):
        url = self.sites.replace("www.", "")
        if "://" in url:
            newurl = url.split("/")[2]
        else:
            newurl = url
        if newurl.endswith("/"):
            valid_url = newurl.split("/")[0]
        else:
            valid_url = newurl
        return valid_url

    def request_to_api(self):
        host = self.get_root_domain()
        api = "https://api.hackertarget.com/hostsearch/?q="+host
        try:
            resp = requests.get(api, headers=self.head(), timeout=70)
            if "error invalid host" not in resp.text:
                self.parsing_subdomain(resp.text)
            else:
                print("\x1b[34m[ \x1b[31m× \x1b[34m]\x1b[37m {} is invalid host".format(
                    self.get_root_domain()))
        except Exception:
            print("\x1b[34m[ \x1b[31m! \x1b[34m]\x1b[37m Can\'t connect to api, please check your connection first".format(
                self.get_root_domain()))
