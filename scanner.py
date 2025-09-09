
import sys, socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])  #translate hostname into ipv4
else:
	print("invalid amount of arguments.")
	print("Sytanx: python3 scanner.py <ip>")
	
# 2 arguments total: 0 is scanner.py and 1 is ur ip address


print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting program:")
	sys.exit()
	
except socket.gaierror:
	print("\nHost name could not resolve")
	sys.exit()

except socket.error:
	print("\nCould not connect to server.")
	sys.exit()
