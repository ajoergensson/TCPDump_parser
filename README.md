# TCPdump_parser
TCPDump Parser to analyse traffic

# Use the app in the following way:
## sudo tcpdump -nli ens33 | python tcpdump.py

![prnt](https://user-images.githubusercontent.com/32357144/63353242-5b6f3b00-c35a-11e9-82df-935d6dbbbe49.png)

# Issues
Having issues to use local variables with the threads.

Implement further functions as summarising used protocols.
- DNS Uses often 3 IPs (part of A record resolution).
- (Iterate on line to calculate more than 2 IPs).
