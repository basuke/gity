# Copyright Aaron Smith 2009
# 
# This file is part of Gity.
# 
# Gity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Gity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Gity. If not, see <http://www.gnu.org/licenses/>.
from _util import *
try:
	import sys,re,os,subprocess
except Exception,e:
	sys.stderr.write(str(e))
	exit(84)
command=""
try:
	from _argv import *
	if not options.misc: raise Exception("Gitty Error: The new stash command requires a stash name.")
	msg=options.misc[0]
	command = "%s %s %s" % (options.git,"stash save",msg)
	rcode,stout,sterr=run_command(command)
	rcode_for_git_exit(rcode,sterr)
	exit(0)
except Exception, e:
	sys.stderr.write("The new stash command through this error: " + str(e))
	sys.stderr.write("\ncommand: %s" % command)
	log_gity_version(options.gityversion)
	log_gitv(options.git)
	exit(84)