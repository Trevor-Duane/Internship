from sys import argv
from os.path import exists

scipt, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)
print "does the output file exist %s" % exists(to_file)

print "ready, press enter to return and control_c to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright, all done"

out_file.close()
in_file.close()
