#There exists a magic variable called *args
#Actually, only the asterix is mandatory, which means that this magic variable
#could be named -> *woop or *myvars or even *yay and it would still work.
#but *args is a convention that is used, so I would recommend we stick to it.

def testmyargs(firstArgument,*args):
    print("This is my first Argument ->", firstArgument)
    for argument in args:
        print("Passed argument -> ", argument)



testmyargs("woop","wap","wep","wip")

