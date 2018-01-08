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
   # TODO: 後で

def server_loop():
   # TODO: 後で


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
      if listen:
         server_loop()

   main()
