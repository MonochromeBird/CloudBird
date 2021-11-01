#!/usr/bin/env python3
from os import check_output, PIPE
with open("cloudbirdinstall.log","a") as log:
	log.write(check_output('sudo cp cloudbird.service /lib/systemd/system/', shell = True, stdout=PIPE).decode())
	log.write(check_output('sudo cp * /usr/bin/ -rf', shell = True, stdout=PIPE).decode())
print('Active `cloudbird.service` for a better experience.')
exit(0)
