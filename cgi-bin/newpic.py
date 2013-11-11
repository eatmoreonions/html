#!/usr/bin/python

import datetime
import subprocess
import cgi 
import cgitb
import time
import sys

sys.path.append('/home/pi/python/Adafruit-Raspberry-Pi-Python-Code/Adafruit_BMP085')
from Adafruit_BMP085 import BMP085

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

effect=form["effect"].value
exposure=form["exposure"].value

def run():

  newpic, error = run_command('python', '/usr/bin/sudo', '/usr/bin/raspistill', '-t', '1', '-rot', '180','-ifx', effect, '-ex', exposure, '-w', '800', '-h', '800', '-o', '/var/www/images/still.jpg')

  print "<center><img src=/images/still.jpg?dummy=%s" % random
  print " width=800 height=800></center>"

  print "<center>%s" % dtn.strftime("%A %b %d %I:%M:%S")
  print "<br><a href=/index.html>Back</a></center>"
  print "</font>"

run()
