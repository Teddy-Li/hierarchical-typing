import random
from datetime import datetime
random.seed(datetime.now())

with open('./crowdsourced.tsv', 'r', encoding='utf8') as fp:
	lines = fp.readlines()

crowd_train = []
crowd_dev = []
crowd_test = []

for line in lines:
	flag = random.choice([0, 1, 2])
	if flag == 0:
		crowd_train.append(line)
	elif flag == 1:
		crowd_dev.append(line)
	elif flag == 2:
		crowd_test.append(line)

crowd_traindev = crowd_train + crowd_dev

with open('crowd_train.tsv', 'w', encoding='utf8') as fp:
	for line in crowd_train:
		fp.write(line)

with open('crowd_dev.tsv', 'w', encoding='utf8') as fp:
	for line in crowd_dev:
		fp.write(line)

with open('crowd_test.tsv', 'w', encoding='utf8') as fp:
	for line in crowd_test:
		fp.write(line)

with open('crowd_traindev.tsv', 'w', encoding='utf8') as fp:
	for line in crowd_traindev:
		fp.write(line)