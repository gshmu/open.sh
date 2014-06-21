#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'mhohai'

with open('6-20.csv', 'rb') as f:
    data = f.readlines()[1:]
i_dict = {}
for n in range(1, len(data)):
    line = data[n].split(',')
    i_dict.setdefault(line[2], {})
    i_dict[line[2]].setdefault("%s%s" % (line[3], line[4].strip()), line[0])
print 'i_dict complete finished'

with open('out.csv', 'w'):
    print 'f.truncate():just clear'
with open('out.csv', 'a') as save:
    for cid in sorted(i_dict.keys(), key=int):
        for dw in range(1, 8):
            for dt in range(1, 5):
                index = "%i%i" % (dw, dt)
                if index in i_dict[cid].keys():
                    default = i_dict[cid][index]
                else:
                    default = '0.00'
                # print "%5s  %3s  %s" % (default, cid, index)
                save.write("%s  %s  %s\n" % (default, cid, index))
print 'Enjoy yourself'
