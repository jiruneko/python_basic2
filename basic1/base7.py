# 文字列の一部取り出し、format, islower, isupper

msg = "hello, my name is taro"
print(msg[1:6])
print(msg[6:])
print(msg[1:10:3])
print("hello {}".format("Taro"))
name = "Jiro"
print(f"hello {name}")
print(f"{name=}")

# find, index, rfind, rindex

msg = "ABCDEABC"
print(msg.find("ABC"))
print(msg.rfind("ABC"))
print(msg.index("ABC"))
print(msg.rindex("ABC"))
