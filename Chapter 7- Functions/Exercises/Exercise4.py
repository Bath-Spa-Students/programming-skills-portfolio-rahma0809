def make_shirt(size=' Large',message='I love python'):
    summary =('\n''Creating a'+ size +'-sized shirt with the message:'+message)
    print(summary)

#default message
make_shirt()

#medium size 
make_shirt(size=" Medium")
make_shirt(size=" Small", message="Hello")
