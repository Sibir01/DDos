# DDos
A simple DDoser program


This is my first simple DDoSer for attacks.

Principle of Operation:

Writing a script to send a large number of packets to a remote machine in order to overload it.
The failure will occur when there are too many packets and the computer cannot process and respond to them.

How does it work?

It uses the requests library to send HTTP requests to the target URL.

It creates a function called dos, which endlessly sends HTTP requests to the specified URL.

The user can specify the number of threads and the URL for the attack via the command-line interface.

Each thread launches the dos function, which endlessly sends requests to the specified URL.

Before sending the request, the code performs some basic checks, such as checking for "http" in the URL and the presence of a dot in the domain.

Attacking websites, etc.
