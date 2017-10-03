def SayHello(firstName,lastname):
    #the % operator can be display strings see here 
    # Official and newer way is to use str.format()
    # -> https://docs.python.org/3.3/library/stdtypes.html#printf-style-string-formatting
    print("hello %s" % firstName);



SayHello('woop')