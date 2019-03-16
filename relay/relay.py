import sys
import relay_controller
import argparse
import cmd_parse

if __name__ == "__main__":
    command = cmd_parse.CMDParse(sys.argv[1:]).parse()
    relay_controller.Relay(command).parse()
