# -*- coding: utf-8 -*-

import sys
import socket
import getopt
import threading
import subprocess

listen             = False
command            = False
upload             = False
execute            = ""
target             = ""
upload_destination = ""
port               = 0


def usage ():
   print "FIXME"
   sys.exit(0)


def client_sender(buffer):
   client = socket.socket(socket.AF_INET, soccket.SOCK.STREAM)
   try:
      # 標的ホストへの接続
      client.connect((target, port))

      if len(buffer):
         client.send(buffer)

      while True:
         # 標的ホストからのデータを待機
         recv_len = 1
         response = ""

         while recv_len:
            data      = client.recv(4096)
            recv_len  = len(data)
            response += data
            if recv_len < 4096:
               break
         print response,

         # 追加の入力を待機
         buffer = raw_input("")
         buffer += "\n"

         # データの送信
         client.send(buffer)
   except:
      print "[*] Exception Exiting."
      #接続の終了
      client.close()

def server_loop():
   global target

   # 待機するIPアドレスが指定されていない場合は、全てのインタフェースで接続を待機
   if not len(target):
      target = "0.0.0.0"

   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind((target, port))

   server.listen(5)

   while True:
      client.socket, addr = server.accept()

      # クライアントからの新しい接続を処理するスレッドの起動
      client_thread = threading.Thread(target=client_handler, args=(client_socket,))
      client_thread.start()

def run_command(command):
   # 文字列の末尾の開業を削除
   command = command.rstrip()

   # コマンドを実行し出力を取得
   try:
      output = subprocess.check_output(
         command,stderr=subprocess.STDOUT, shell=True)

   except:
      output = "Failed to execute command. \r\n"

   # 出力結果をクライアントに送信
   return output

def main():
   global listen
   global port
   global execute
   global command
   global upload_destination
   global target

   if not len(sys.argv[1:]):
      usage()

   # コマンドラインオプション読み込み
   try:
      opts, args = getopt.getopt(
         sys.argv[1:],
         "hle:t:p:cu",
         ["help", "listen", "execute=", "target=", "port=", "command", "upload="])

   except getopt.GetoptError as err:
      print str(err)
      usage()

   for o,a in opts:
      if o in ("-h", "--help"):
         usage()
      elif o in ("-l", "--listen"):
         listen = True
      elif o in ("-e", "--execute")
         execute = a
      elif o in ("-c", "--commandshell"):
         command = True
      elif o in ("-u", "--upload"):
         upload_destination = a
      elif o in ("-t", "--target"):
         target = a
      elif o in ("-p", "--port"):
         port = int(a)
      else:
         assert False, "Unhandled Option"

      # 接続を待機するか、それとも標準入力からデータを受け取って送信するか。
      if not listen and len(target) and port > 0:
         # コマンドラインからの入力を`buffer`に格納。
         # 入力がこないと処理が継続されないので、
         # 標準入力にデータを送らない場合は、 Ctrl-Dを入力すること。
         buffer = sys.stdin.read()

         # データ送信
         client_sender(buffer)

      # 接続待機を開始
      # コマンドラインオプションに応じて、ファイルをアップロード
      # コマンド実行、￥コマンドシェルの実行。
      if listen: 2
         server_loop()

   main()
