# x = "awesome"
#
# def myfunc():
#   print("Python Selenium is " + x)
#
# myfunc()
#
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python Selenium is " + x)
#
# myfunc()
#
# print("Python Selenium is " + x)

# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python Selenium is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

print("Python Selenium is " + x)