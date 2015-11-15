#!/usr/bin/env python3.4
import yaml
import argparse

snips = yaml.load(open("/home/aln/.quicksnips/snips.yaml", 'r'))

def get_keys():
	global snips	

	for k in snips.keys():
		print(k)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('snippet', metavar='N', type=str, nargs='?',
                   help='key for snippet')
parser.add_argument('--get-keys', action='store_true',
                   default=False)

args = parser.parse_args()
if args.get_keys:
	get_keys()

else:
	print(snips[args.snippet])
