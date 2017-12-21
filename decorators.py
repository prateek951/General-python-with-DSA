
# @classmethod    These are called decorators

# Decorators extends the behaviour of the function on which it is used
# on without modifying the function itself used in django 

# just a wrapper function

def cough_dec(func):
    def func_wrapper():
        # code before function
        print('*cough*')
        func()
        # code after function
        print('*cough*')
    return func_wrapper

@cough_dec
def question():
    print ('Can you give a discount on that??')


question()    


@cough_dec
def answer():
    
    print('Fuck you!!')

answer()