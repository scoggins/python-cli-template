#!/usr/bin/env python3

import configparser
import argparse
import logging


def main():

    parser = argparse.ArgumentParser(
        description="Some New Project")

    parser.add_argument(
        "-c", "--config",
        help="Config file",
        type=argparse.FileType('r'),
        default="config.ini")

    parser.add_argument(
        "--debug",
        help="Enable debugging output",
        action="store_true")

    parser.add_argument(
        "--commit",
        help="Actually make changes",
        default=False,
        action="store_true")

    args = parser.parse_args()

    format = '{asctime} - {levelname} - {message}'
    if not args.commit:
        format = '{asctime} - {levelname} - [NO COMMIT] - {message}'
    level = logging.INFO
    if args.debug:
        level = logging.DEBUG

    logging.basicConfig(level=level, format=format, style="{")
    logging.debug("Debug logging active")

    # Load the mailman config
    config = configparser.ConfigParser()
    config.read_file(args.config)

    # Custom Code Here


if __name__ == "__main__":
    main()
