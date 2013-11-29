#!/usr/bin/python

import datetime
import subprocess
import cgi 
import cgitb
import time
import sys

cgitb.enable()

print "Content-type: text/html\n\n"
print "<font face=\"verdana\" color=\"green\">"
form=cgi.FieldStorage()

dtn=datetime.datetime.now()
# not really random but most likely different every execution
random=dtn.strftime("%H%M%S")



def run_command(self,*args):
  p=subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  return p.communicate()

if form.getvalue('count'):
   numofpics = form.getvalue('count')
else:
   numofpics = 1

if form.getvalue('seperation'):
   delay = form.getvalue('seperation')
else:
   delay = 1

def run():
    tl, error = run_command('python', '/usr/bin/sudo', '/home/tomc/timelapse/raspitimelapse.sh', '-c', numofpics, '-d', delay, '-w')

    print "<br><a href=/images>Display Images</a></center>"
    print "</font>"

run()
