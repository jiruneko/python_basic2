# 文字列型

fruit = "apple"
print(fruit)
print(type(fruit))

new_fruit = fruit + "banana"
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = "banana"
print(fruit[2])
print(fruit[-1])

byte_fruit = fruit.encode("utf-8")
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode("utf-8")
print(str_fruit)
print(type(str_fruit))

# count

msg = "ABCDEABC"
print(msg.count("ABCDE"))

# startswith, endswith

print(msg.startswith("ABECD"))
print(msg.endswith("BC"))

# strip, rstrip, lstrip

msg = " ABC "
print(msg)
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())
msg = "ABCDEFABC"
print(msg.strip("CBA"))
print(msg.lstrip("CBA"))
print(msg.rstrip("CBA"))

# upper, lower, swapcase, replace, capitalize

msg = "abcABC"
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = "ABCDEABC"
msg_r = msg.replace("ABC", "FFF")
print(msg_r)

msg = "hello world"
print(msg.capitalize())
