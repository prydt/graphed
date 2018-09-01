#!/usr/bin/env python3
import scraper
import os

if __name__ == '__main__':
    # TODO add server interface

    # this is just for testing
    scraper.getData(os.environ['HUSERNAME'], os.environ['HPASSWORD'])
