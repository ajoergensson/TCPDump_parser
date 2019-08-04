## Having issues to use local variables with the threads

## Implement further functions as summarising used protocols
	##  53 - DNS Uses often 3 IPs (part of A record resolution)
	## ! Iterate on line to calculate this IP
 
import sys, time, os, signal, socket, re, threading, schedule
import array as arr
from collections import Counter

## Regex for IP and bytes in stout
pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
pattern_b = re.compile(r'(?:\({1}[0-9]{1,3}\){1})|(?:[0-9]{1,3}$)')

## Initializing variables 
k=0
bytes_out=0
bytes_in=0
t_k=0
t_bytes_in=0
t_bytes_out=0
mylist=[""]
newlist=[""]


class Controller(object):
    def __init__(self, interval=10):
        self.interval = interval

    def job(self):
	update(k)	
	## Calc top addresses & show top 10 (IP ,nr of connectons)  
	newlist = sort(mylist);

class ThreadController(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ThreadController, self).__init__()
        self.controller = Controller(*args, **kwargs)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        schedule.every(self.controller.interval).seconds.do(self.controller.job)
        while not self.stopped():
            schedule.run_pending()


def signal_handler(signum, frame):
    controller_threads = [thread for thread in threading.enumerate() if isinstance(thread, ThreadController)]
    for controller_thread in controller_threads:
	print '------------------------------'
	print '\nYou chose to end the program'
	print '\nNumber of total lines passed: %d' %  (k)
	print 'Total bytes: %s sent ' % (bytes_out)
	print 'Total bytes: %s received ' % (bytes_in)
	print '------------------------------'	       
	## Top 10 (IP ,nr of connectons)
	newlist = sort(mylist);
        controller_thread.stop()
    sys.exit(1)

def sort(self):
	count = Counter(self)
	self = []
	cc = 0
	print 'Top 10 IPs: '
	while (len(count) > 0) and (cc < 10):
    		c = count.most_common(1)
		if c[0][0]:
    			print'%s %d connections' % (c[0][0], c[0][1])
    		del count[c[0][0]]
    		cc += 1
	if len(count) != 0:
        	print '+ %d other IPs' % len(count)
        	count = 0
	return self 

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def update(self):
	print '------------------------------'
    	print'\nPrinting every 10 seconds.'
   	print 'Number of lines passed: %d' %  (k)
    	print 'Total bytes: %s sent ' % (bytes_out)
   	print 'Total bytes: %s received ' % (bytes_in)
	print '------------------------------'	

##  	Start of main
if __name__ == "__main__":

	controller1 = ThreadController()	
	signal.signal(signal.SIGINT, signal_handler)
        ## Make this a controller
	controller1.start()

	## Saving client IP
	usr_IP = get_ip();
	print '\n## This is the client IP of the machine %s ##' % (usr_IP)

	while True:
		f = open(os.path.join('file.txt'), 'w')
		try:
			while True:		
				line = sys.stdin.readline()
				f.write(line)
				mb = re.search(pattern_b, line)
				if mb is not None or '':
					m21 = re.sub(r'[\(\)]','',mb.group(0))
					mIP = re.search(pattern, line)
				if mIP is not None or '':
					mylist.append(mIP.group(0))
				if (mIP.group(0) == usr_IP):
					bytes_out += int(m21)
				else:
					bytes_in += int(m21)
				k += 1		
			f.close()

		except KeyboardInterrupt:
			sys.stdout.flush()
			pass
 
	while True: time.sleep(0.1)
