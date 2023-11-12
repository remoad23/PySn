# import sys
#
#
# class Request:
#
#     #Settings
#     __headersize = 512
#
#     # Header
#     __headerpairs = {}
#
#     #Body
#     __bodypairs = {}
#
#     def serializetobytes(self,content):
#         return bytes(content)
#
#     def serializetoobject(self, content):
#
#         keyvaluepairsasstring = content.Split(",")
#
#         for keyandvalue in keyvaluepairsasstring:
#             splitkeyvalue = keyandvalue.Split(";")
#             key = splitkeyvalue[0]
#             value = splitkeyvalue[1]
#             type = splitkeyvalue[2]
#
#             if type == "string":
#                 value = str(value)
#             elif type == "int":
#                 value = int(value)
#             elif type == "float":
#                 value = float(value)
#             elif type == "bool":
#                 value = bool(value)
#             else:
#                 raise Exception("Data type not matched")
#
#             if not self.headerisfull():
#                 self.__headerpairs[key] = value
#             else:
#                 self.__bodypairs[key] = value
#
#
#
#     def headerisfull(self):
#         return sys.getsizeof(self.__headerpairs) == self.__headersize
#
