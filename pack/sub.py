class GETSUB:

    def __init__(self, sites="", autocheck=False):
        self.sites = sites
        self.autocheck = autocheck
        self.subdolist = []

    def check_status_code_subdomain(self):
        for sub in self.subdolist:
            try:
                resp = requests.get(sub, headers=head(),
                                    timeout=70).status_code
                print_status_code(sub, resp)
                save_file(str(resp)+".txt", sub)
            except Exception:
                print_status_code(sub, "Die")
                save_file("Die.txt", sub)

    def parsing_subdomain(self, source):
        sub = source.splitlines()
        for s in sub:
            newsub = s.split(",")[0]
            httpsub = "http://"+newsub
            self.subdolist.append(httpsub)
            save_file("subdomain.txt", httpsub)
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
            resp = requests.get(api, headers=head(), timeout=70)
            if "error invalid host" not in resp.text:
                self.parsing_subdomain(resp.text)
            else:
                print("\x1b[34m[ \x1b[31m× \x1b[34m]\x1b[37m {} is invalid host".format(
                    self.get_root_domain()))
        except Exception:
            print("\x1b[34m[ \x1b[31m! \x1b[34m]\x1b[37m Can\'t connect to api, please check your connection first".format(
                self.get_root_domain()))
