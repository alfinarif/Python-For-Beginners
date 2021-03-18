# d = {}
# print(type(d))

# dict = {1:'hello',2:'world',3:'bangladesh'}
# print(dict[2])

# data = {
#     'a':'ALFIN',
#     'b':'bangladesh',
#     'c':'cleavercode',
#     'alfin':['dev','prog','des'],
#     'cleavercode':{'dev':'alfin','web':'faysal','gp':'abir'}
# }
# print(data['cleavercode']['dev'])

keys = ['a','b','c','d']
values = ['alfin','bangladesh','cleavercode','development']
data = dict(zip(keys,values))
data['hello']='world'
del data['a']
print(data)
