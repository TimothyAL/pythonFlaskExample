from flask import Blueprint, request, Response

functions = Blueprint('functions', __name__, url_prefix='/back/functions')

@functions.route('/', methods=['GET'])
def instructions():
    return Response('please provide 2 numbers to the function you would like to perform', status=200)

@functions.route('/add/<number1>&<number2>', methods=['GET'])
def add(number1,number2):
    try:
        answer = str(int(number1) + int(number2))
        return Response(answer, status=200)
    except TypeError:
        return Response('You must supply this function with two numbers')

@functions.route('/multiply/<number1>&<number2>', methods=['GET'])
def multiply(number1,number2):
    try:
        answer = str(int(number1) * int(number2))
        return Response(answer, status=200)
    except TypeError:
        return Response('You must supply this function with two numbers')

@functions.route('/divide/<number1>&<number2>', methods=['GET'])
def devide(number1,number2):
    try:
        answer = str(int(number1) / int(number2))
        return Response(answer, status=200)
    except TypeError:
        return Response('You must supply this function with two numbers')

@functions.route('/exponent/<number1>&<number2>', methods=['GET'])
def exponent(number1,number2):
    try:
        answer = str(int(number1) ** int(number2))
        return Response(answer, status=200)
    except TypeError:
        return Response('You must supply this function with two numbers')



@functions.route('/subtract/<number1>&<number2>', methods=['GET'])
def subtract(number1, number2):
    try:
        answer = str(int(number1) - int(number2))
        return Response(answer, status=200)
    except TypeError:
        return Response('You must supply this function with two numbers')