# TCPdump_parser
TCPDump Parser to analyse traffic

# Use the app in the following way:
## sudo tcpdump -nli ens33 | python tcpdump.py

#Issues
## Having issues to use local variables with the threads
## Implement further functions as summarising used protocols
	##  53 - DNS Uses often 3 IPs (part of A record resolution)
	## ! Iterate on line to calculate this IP
