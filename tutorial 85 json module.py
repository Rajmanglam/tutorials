# in this tutorial we will learn about the functions and uses of json module
# json module means "javascript object notation" using this we can push or pull data into
# the web browser very easily
import json
# json date is set between double quotes and does not have comments and is saved with a
# .json extention
data='{"var1":"hb","var2":"last"}'#here we have put var1,hb,
# var2,last in double quotes
print(data)
parser = json.loads(data)#here json.load will parse the data example.data
print(parser)
print(type(parser))
print(parser['var1'])
#now let's learn about json.dump
data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
print(data2)
#Here we have created a dictionary in this if we directly transverse it into json then it will show error because the
#documentation of python and javascript are different so to make such objects javascript compatible we use json.dump like this
data2dump=json.dumps(data2)#this will convert it into a javascript compatible object
print(data2dump)
