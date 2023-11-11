# import UdpClient
# import UdpServer
# import socket
# import threading
#
# class UdpConnection:
#
#     __HostIP = ""
#     __Port = ""
#     __Child = None
#     __Socket = None
#     __Thread = None
#     __ClosedRequested = False
#
#
#     def __init__(self, hostip, port, childconnection):
#         self.HostIp = hostip
#         self.Port = port
#         self.__Child = childconnection
#
#
#     def __del__(self):
#         self.__closeconnection(self)
#
#
#     def listen(self, loopmethod):
#         while not self.__ClosedRequested:
#             loopmethod()
#
#
#     def _buildconnection(self):
#         if self.__Child is UdpClient:
#             self.__Thread = threading.Thread(self.__buildconnectionforclient(self))
#
#         elif self.__Child is UdpServer:
#             self.__Thread = threading.Thread(self.__buildconnectionforserver(self))
#
#         else:
#             raise Exception("No Servertype set.Set the servertype in constructor")
#
#
#     def __closeconnection(self):
#         self.__Socket.close()
#
#
#     # ------------------ Server specific Methods -------------------------------------
#     def __buildconnectionforserver(self, methodtopasstothread):
#         self.__Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.__Socket.connect((self.__HostIP, self.__Port))
#
#
#     # ------------------ Client specific Methods -------------------------------------
#     def __buildconnectionforclient(self):
#         self.__Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#
