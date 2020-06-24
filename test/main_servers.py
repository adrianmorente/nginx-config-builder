#!/usr/bin/python3

import sys
import argparse


def getArguments(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Provides the chosen server\'s configuration file')
    parser.add_argument("-s", "--server", help="Name of the server (nginx, apache).")
    parser.add_argument("-i", "--input", help="Input file containing the set of variables to build the config from")
    parser.add_argument("-o", "--output", help="Destination output file for the generated config.")
    options = parser.parse_args(args)
    return options


def saveConfig(config, file = "server.conf"):
    f = open(file, "w")
    f.write(config.__str__() + "\n")
    f.close()

    print("Config written to " + file + ".")


def nginx():
    from server.config.builder import ServerConfigBuilder

    nginx = ServerConfigBuilder(daemon='on')

    with nginx.add_server() as server:
        server.add_route('/foo', proxy_pass='upstream').end()

    saveConfig(nginx, "nginx.conf")


def apache():
    """
    Still in progress, not really working
    """

    from server.config.builder import ServerConfigBuilder

    apache = ServerConfigBuilder()

    with apache.add_server() as server:
        server.add_route('/index').end()

    saveConfig(apache, "apache.conf")
    pass


def main():
    # Parse chosen server
    options = getArguments(sys.argv[1:])

    if options.server is None:
        print("Error: no server argument has been given to the program.")
    elif options.server == "nginx":
        print("Nginx server specified.")
        nginx()
    elif options.server == "apache":
        print("Apache server specified.")
        apache()
    else:
        print("Error: no suitable server specified.")


if __name__ == "__main__":
    main()
