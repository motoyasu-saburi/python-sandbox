# -*- coding: utf-8 -*-

import sys
import  socket
import threading

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    server.bind((local_host, local_port))
  except:
    print "[!!] Failed to listen on %s:%d" % (local_host, local_port)
    print "[!!] Check for other listening sockets or correct permissions."
    sys.exit(0)

  print "[*] Listening on %s:%d" % (local_host, local_port)

  server.listen(5)

  while True:
    client_socket, addr = server.accept()

    # ローカル側からの接続情報を表示
    print "[==>] Received incoming connection from %s:%d" % (addr[0], addr[1])

    # リモートホストと通信するためのスレッドを開始
    proxy_thread = threading.Thread(
      target=proxy_hander,
      args=(client_socket, remotehost, remote_port, receive_first))

    proxy_thread.start()