# import general libraries
import requests
import Utilities
from config import *
from cmd import Cmd


# import modules
import modules.pfsense


class MyPrompt(Cmd):
    prompt = 'Tower-CLI> '
    intro = "Welcome! Type ? to list commands"

    def do_exit(self, inp):
        print("Bye")
        #print("adding '{}'".format(inp))
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_Print_pfsense_credentials(self, line):
        line = line.split(' ')
        IP = line[0]
        if len(IP) >= 1:
            print("IP?")
            Utilities.Print_pfsense_credentials(IP)
        else:
            Utilities.Print_pfsense_credentials()

    def help_Print_pfsense_credentials(self):
        print("Print Pfsense credentials.\n"
              "Usage: Print_pfsense_credentials [<IP> or <empty for all IP Addresses> ]\n"
              "Print_pfsense_credentials 192.168.1.10\n"
              "Print_pfsense_credentials \n")


    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        #print("Default: {}".format(inp))
        print("Try again")

    # do_EOF = do_exit
    # help_EOF = help_exit


if __name__ == '__main__':
    MyPrompt().cmdloop()


