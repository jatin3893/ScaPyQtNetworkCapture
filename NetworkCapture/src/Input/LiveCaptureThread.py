import threading
from scapy.all import *

class LiveCaptureThread(threading.Thread):
	def __init__(self, liveCaptureObj):
		threading.Thread.__init__(self)
		self.stop = threading.Event()
		self.liveCaptureObj = liveCaptureObj
		self.flag = False

	def run(self):
		try:
			sniff(prn=self.recv)
		except Exception:
			pass

	def recv(self, packet):
		if self.flag:
			raise Exception('Stop Packet Capturing')
		self.liveCaptureObj.packetList.append(packet)
		self.liveCaptureObj.packetBuffer.append(packet)
		print 'recv'
		print packet.summary()