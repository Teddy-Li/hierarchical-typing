import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='../../data/cfet/train.tsv')
parser.add_argument('--output', type=str, default='../../dump/cfet/ontology.txt')
args = parser.parse_args()

typeset = set()
with open(args.input, 'r', encoding='utf8') as fp:
    lidx = 0
    for line in fp:
        if lidx % 10000 == 0 and lidx > 0:
            print(lidx)
        lidx += 1
        item = line.split('\t')
        types = item[2]
        types = types.strip().split(' ')
        for type in types:
            typeset.add(type)

typelist = list(typeset)
typelist.sort()

with open(args.output, 'w', encoding='utf8') as fp:
    for line in typelist:
        fp.write(line+'\n')

print("Finished!")