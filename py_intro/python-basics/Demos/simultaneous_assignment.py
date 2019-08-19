#Switch b and a. Attempt 1. The Wrong Way.
a=5
b=10
a=b
b=a
print("ATTEMPT 1. The Wrong Way.")
print(a)
print(b)

#Switch b and a. Attempt 2. A Way that Works.
a=5
b=10
temp=a
a=b
b=temp
print("ATTEMPT 2. A Way that Works.")
print(a)
print(b)

#Switch b and a. Attempt 3. The Python Way.
a=5
b=10
a,b = b,a
print("ATTEMPT 3. The Python Way.")
print(a)
print(b)