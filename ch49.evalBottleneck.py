## Profiling

## In your Terminal execute:

## $ python -m cProfile crypt.py

## OR - In your script

## import cProfile
## cProfile.run('test()')

## We have now determined a Bottle neck in our code

##      Eval() -->  578/981 = 59%

# Eval is a built-in module SO can only be solved in to ways:
##  - Fewer Calls
##  - Easier Calls

##  Easier calls doesn't make much sence for Eval.
##  Fewer Calls is the way to go.

## How? --> Lets Talk About Eval

## Eval Steps:
## - Parse the String
## - Builds a Tree (char, numbers, expressions)
## - Completes the datastructure
## - Now to execute

## A ton of duplicate work for our script

## Can we do a bunch of this work in a functions then pass it to Eval()
## The function will pre-compile our work.
## Eval() will run only once to solve the problem.