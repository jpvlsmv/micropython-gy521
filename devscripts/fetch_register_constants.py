#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Pull down the MPU6050 datasheet from Invensys and extract the register
    contents
"""
DS_url='https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf'

import logging 
logging.basicConfig( level = logging.ERROR )
log = logging.getLogger(__name__)
loglvls = [ logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG ]

def main(args):
    log.debug("Debug logging set")
    log.info("Info logging set")
    log.warning("Warn logging set")
    log.error("Errors logging set (default)")

    import requests
    r = requests.get(args.url)
    log.info(f'HTTP response status {r.status_code}')
    

if __name__ == "__main__":
    import argparse
    cli = argparse.ArgumentParser(
                   description = 'Extract tables from Invensys datasheet',
		   formatter_class=argparse.ArgumentDefaultsHelpFormatter,
		   )
    cli.add_argument('-v', '--verbose', dest="ll",  help='increase verbose',
                     action='count', default=0)
    cli.add_argument('-d', '--debug',   dest="ll",  help='debug', 
                     action='store_const', const=3)
    cli.add_argument('-u', '--url',     dest="url", help='Datasheet URL', 
                     action='store', default=DS_url)

    args = cli.parse_args()
    print(f'args: {args}')
    log.setLevel( loglvls[min(args.ll,len(loglvls)-1)] )
    main(args)
