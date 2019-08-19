try:
    1/0
except Exception as e:
    print(type(e)) #prints object type
    print(e) #prints value of str(e)