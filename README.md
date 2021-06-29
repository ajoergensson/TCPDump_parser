# TCPdump_parser
TCPDump parser to analyse traffic

# Use the app in the following way
### sudo tcpdump -nli ens33 | python tcpdump.py

![prnt](https://user-images.githubusercontent.com/32357144/63353242-5b6f3b00-c35a-11e9-82df-935d6dbbbe49.png)

# Issues
Inconsistency with graceful shutdown of threads due to misuse of attributes from local variables (mIP.group(0)). <br />
Having issues to use local variables with the threads.

# Further development
Implement further functions as summarising used protocols.<br />
- DNS Uses often 3 IPs (part of A record resolution).
- (Iterate on line to calculate more than 2 IPs).
