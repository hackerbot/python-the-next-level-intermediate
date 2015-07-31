# * arguments & ** key word arguments
#  
# expressions

def F(*args, **kwargs):
    pass

def F(*args, **kwargs):
    for arg in args:
        pring(args)
    print(kwargs)

def F(hair, blood, eyes = 'Green'):
    # hair ~ argument, eyes ~ dict/keyword arg. w/ default value of Green
    print(hair, blood, eyes)

hair_color = 'Brown'
blood_type='o-'

F(hair_color, blood_type)

F(hair_color, blood_type, eyes = 'Blue')