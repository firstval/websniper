#!/usr/bin/env python
# WebSniper Framework
# Web application security testing framework
# __        __   _    ____        _
# \ \      / /__| |__/ ___| _ __ (_)_ __   ___ _ __
#  \ \ /\ / / _ \ '_ \___ \| '_ \| | '_ \ / _ \ '__|
#   \ V  V /  __/ |_) |__) | | | | | |_) |  __/ |
#    \_/\_/ \___|_.__/____/|_| |_|_| .__/ \___|_|
#                                  |_|
#
# description:       WebSniper Framework main
# author:            @semprix, @shipcod3, @godflux
# platform:          Python
# version:           1.0

import core, helper
import time, signal

wsniper_print = helper.sniperconsole.consoleprint()
wsniper_show = helper.snipershow.showprints()
wsniper_signal = helper.snipersignal.signalhandler()
wsniper_cmd = core.cmd
wsniper_func = core.core.funcs()

class wsniper_main_console(wsniper_cmd.Cmd):
    wsniper_print.banner()
    prompt = wsniper_print.prompt()
    current_console = prompt

    def sigint_handler(signum, frame):
        return

    def wsniper(self):
        self.prompt = "websniper>"
        self.prefunc = "main_"
        return

    # main console

    def main_credits(self, ignored):
    	wsniper_print.credits()
    	return

    def main_show(self, shopt):
    	wsniper_show.listmodsdesc(shopt)
    	return

    def main_help(self, ignored):
        wsniper_print.help()
        return

    def main_quit(self, line):
        print '[***] Shutting Down WebSniper cleanly....'
        print ''
        time.sleep(3)
        return wsniper_main_console().postcmd(self,line)

    def main_modules(self, ignored):
        self.prompt = "websniper>modules>"
        self.prefunc = "modulesconsole_"
        return

    def main_recon(self, ignored):
        self.prompt = "websniper>modules>recon>"
        self.prefunc = "reconconsole_"
        return

    def main_discovery(self, ignored):
        self.prompt = "websniper>modules>discovery>"
        self.prefunc = "discoveryconsole_"
        return

    def main_vulnerability(self, ignored):
        self.prompt = "websniper>modules>vulnerability>"
        self.prefunc = "vulnerabilityconsole_"
        return

    # modules console

    def modulesconsole_recon(self, ignored):
        self.prompt = "websniper>modules>recon>"
        self.prefunc = "reconconsole_"
        return

    def modulesconsole_discovery(self, ignored):
        self.prompt = "websniper>modules>discovery>"
        self.prefunc = "discoveryconsole_"
        return

    def modulesconsole_vulnerability(self, ignored):
        self.prompt = "websniper>modules>vulnerability>"
        self.prefunc = "vulnerabilityconsole_"
        return

    def modulesconsole_exploits(self, ignored):
        self.prompt = "websniper>modules>exploits>"
        self.prefunc = "exploitsconsole_"
        return

    def modulesconsole_list(self, ignored):
        wsniper_show.listmods()
        return

    def modulesconsole_back(self, ignored):
        self.wsniper()

    # discovery specific

    def discoveryconsole_run(self, module_name):
        data = {}
        data['type'] = 'discovery'
        data['name'] = module_name
        wsniper_func.run_module(data)
        return

    def discoveryconsole_back(self, ignored):
        self.main_modules("*")

    # recon specific

    def reconconsole_run(self, module_name):
        data = {}
        data['type'] = 'recon'
        data['name'] = module_name
        wsniper_func.run_module(data)
        return

    def reconconsole_back(self, ignored):
        self.main_modules("*")

    # vulnerability specific

    def vulnerabilityconsole_run(self, module_name):
        data = {}
        data['type'] = 'vulnerability'
        data['name'] = module_name
        wsniper_func.run_module(data)
        return

    def vulnerabilityconsole_back(self, ignored):
        self.main_modules("*")

    # exploits specific

    def exploitsconsole_run(self, module_name):
        data = {}
        data['type'] = 'exploits'
        data['name'] = module_name
        wsniper_func.run_module(data)
        return

    def exploitsconsole_back(self, ignored):
        self.main_modules("*")

if __name__ == '__main__':
    wsniper_main_console().cmdloop()
