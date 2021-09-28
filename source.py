import server

honeypot = server.Server()

honeypot.log_init()

honeypot.log("ls","17")
client_addr = honeypot.listen()

print(client_addr)


