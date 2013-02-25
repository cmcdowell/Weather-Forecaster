#!/usr/bin/env python

import urllib2
import sys
import argparse
import xml.etree.ElementTree as etree


def main():

    base_url = 'http://weather.yahooapis.com/forecastrss?w='
    WOEID = '44544'

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-c',
        '--celsius',
        action='store_true',
        help='display temperature in Celsius'
    )

    group.add_argument(
        '-f',
        '--fahrenheit',
        action='store_true',
        help='display temperature in Fahrenheit'
    )

    parser.add_argument(
        '-t',
        '--forecast',
        action = 'store_true',
        help = 'display forcast for tomorrow'
    )

    args = parser.parse_args()

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'CLI Weather forecast script')]

    url = base_url + WOEID + '&u=c'
    units = 'C'

    if args.fahrenheit:
        url = base_url + WOEID
        units = 'F'

    try:
        xml = opener.open(url)
    except Exception as e:
        print 'An error has occurred', e
        sys.exit()

    tree = etree.parse(xml)
    root = tree.getroot()
    item = root[0].find('item')
    condition = item.find('{http://xml.weather.yahoo.com/ns/rss/1.0}condition').attrib

    print u'{0}, {1}, {2}\u00B0{3}'.format(
        condition['date'],
        condition['text'],
        condition['temp'],
        units
    )


if __name__ == '__main__':
    main()
