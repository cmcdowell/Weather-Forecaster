#!/usr/bin/env python

import urllib2
import sys
import os
import argparse
import xml.etree.ElementTree as etree
from ConfigParser import SafeConfigParser, Error


def main():

    base_url = 'http://weather.yahooapis.com/forecastrss?w='

    argument_parser = argparse.ArgumentParser()
    group = argument_parser.add_mutually_exclusive_group()
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

    argument_parser.add_argument(
        '-d',
        '--forecast',
        action='store_true',
        help='display more detailed forecast'
    )

    args = argument_parser.parse_args()

    config_parser = SafeConfigParser()

    path = os.path.split(os.path.realpath(__file__))[0]

    try:
        config_parser.read(path + '/settings.ini')
        settings = dict(config_parser.items('location'))
    except Error:
        print 'settings.ini location section not found'
        sys.exit()

    try:
        woeid = settings['woeid']
    except KeyError:
        print 'No woeid setting'
        sys.exit()

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'CLI Weather forecast script')]

    url = base_url + woeid + '&u=c'
    units = 'C'

    if args.fahrenheit:
        url = base_url + woeid
        units = 'F'

    try:
        xml = opener.open(url)
    except Exception as e:
        print 'An error has occurred', e
        sys.exit()

    tree = etree.parse(xml)
    root = tree.getroot()
    item = root[0].find('item')

    if args.forecast:
        forecasts = item.findall('{http://xml.weather.yahoo.com/ns/rss/1.0}forecast')

        for forecast in forecasts:
            forecast = forecast.attrib

            print u'\n{0} {1}\n\tlow {2}\u00B0{3}\n\thigh {4}\u00B0{3}\n\t{5}\n'.format(
                forecast['day'],
                forecast['date'],
                forecast['low'],
                units,
                forecast['high'],
                forecast['text']
            )
    else:

        condition = item.find('{http://xml.weather.yahoo.com/ns/rss/1.0}condition').attrib

        print u'{0}, {1}, {2}\u00B0{3}'.format(
            condition['date'],
            condition['text'],
            condition['temp'],
            units
        )


if __name__ == '__main__':
    main()
