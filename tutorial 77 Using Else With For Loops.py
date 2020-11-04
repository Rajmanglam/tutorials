khana=["roti","sabji","chawal"]
for i in khana:
    print(i)
else:print("this loop ran succesfully")
# NOTE:else ca only be used if there is no break statement in the for loop
khana2=["roti","sabji","chawal"]
for i in khana:
    if i=="paratha":
        print(i)
        break
else:print("your item was not found")