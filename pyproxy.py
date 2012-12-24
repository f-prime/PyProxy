import socket, sys, threading


class PyProxy:

    def __init__(self):
        self.port = int(sys.argv[1])
        self.debug = True

    def main_loop(self):
        try:
            sock = socket.socket()
      	    sock.bind(("", self.port))
      	    sock.listen(1)
	    print "PyProxy has started"
      	    while True:
                browser, conn = sock.accept()
                if self.debug:
	    	    print browser
		data = browser.recv(1024)
		if self.debug:
		    print data
   	  	try:
		    url = data.split()[4]
		except:
		    pass
		if self.debug:
		    print url
		threading.Thread(target=self.send, args=(url, browser, data)).start()
	except Exception, error:
	    if self.debug:
		print error
	    pass

    def send(self, url, browser, data):

        try:
	    transfer = socket.socket()
	    transfer.connect((url, 80))
	    transfer.send(data)
	    while True:
	        html = transfer.recv(1024)
		browser.send(html)
		if "</html>" in html:
		    if self.debug:
			print "DONE"
		    browser.close()
		    transfer.close()
		    break
	except Exception, error:
	    if self.debug:
		print error
	    pass

if __name__ == "__main__":
    PyProxy().main_loop()
       
