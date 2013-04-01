Summary
-------

This tool will help you check if a list of IP's have been blacklisted. The regular expression code has been borrowed from [recon-ng](https://bitbucket.org/LaNMaSteR53/recon-ng/pull-request/51/ipvoid-module/diff).
The tool requires you to have a smtp email address to send out notifications.
Please run this through cron.

Requirements
------------
Python requests library, can be installed by

pip install requests

Configurations
--------------

In the conf.py file setup the smtp server credentials. 
This script is tested to work with gmail's smtp server.

Once that is done, create a simple file with a list of ipaddresses, the file name can be changed in conf.py.

Enjoy! 
