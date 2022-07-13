from Tokens import Tokens
from Nodos import Nodos

global index
global lines
index = 0


def peek():
    global index
    global lines
    return lines[index]

def advance():
    global index
    val = peek()
    index = index + 1
    return val

def eof():
    global lines
    global index
    return index >= len(lines)

def scan_digits():
    ans = {
        "val": ""
    }
    while peek() in "0123456789":
        ans["val"] = ans["val"] + advance()
    if peek() != ".":
        ans["type"] = "inum"
    else:
        ans["type"] = "fnum"
        ans["val"] = ans["val"] + advance()
        while peek() in "0123456789":
            ans["val"] = ans["val"] + advance()     
    return ans


def scanner():
    ans = {}
    while not eof() and (peek() == " " or peek() == "\n"):
        advance()
    if eof():
        ans["type"] = "$"
    else:
        if peek() in "0123456789":
            ans = scan_digits()
        else :
            ch = advance()
            if ch in "abcdeghjklmnoqrstuvwxyz":
                ans["type"] = "id"
                ans["val"] = ch
            elif ch == "f":
                ans["type"] = "floatdcl"
            elif ch == "i":
                ans["type"] = "intdcl"
            elif ch == "p":
                ans["type"] = "print"
            elif ch == "=":
                ans["type"] = "assign"
            elif ch == "+":
                ans["type"] = "plus"
            elif ch == "-":
                ans["type"] = "minus"
            else:
                print("error léxico")
                exit()
    return ans

#iniciar 
nodos=Nodos()

def expr(tokens):
    if tokens.peek()['type'] == 'minus' :    
        print(tokens.peek())
        dato=tokens.peek()#-
        tokens.next()
        print(tokens.peek())
        dato1=tokens.peek()#dato
        nodos.agregarSumYRes(dato,dato1)
        tokens.next()
        if tokens.peek()['type'] == 'minus' or tokens.peek()['type'] == 'plus' :
            return expr(tokens)
        else:
            return 0
        #se vuelve  a llamar a si mismo 
    elif tokens.peek()['type'] == 'plus':    
        print(tokens.peek())
        dato=tokens.peek()#+
        tokens.next()
        print(tokens.peek())
        dato1=tokens.peek()
        nodos.agregarSumYRes(dato,dato1)
        tokens.next()
        
        if tokens.peek()['type'] == 'minus' or tokens.peek()['type'] == 'plus' :
            return expr(tokens)
        else:
            return 0
        #se vuelve  a llamar a si mismo 
    else:
        #lambda 
        1

def stm(tokens):
    if tokens.peek()['type'] == 'id':       
        datoo=tokens.peek()
        print(tokens.peek())#valor
        tokens.next()
        if tokens.peek()['type'] == 'assign':       
            dato=tokens.peek()
            print(tokens.peek())#asignar
            tokens.next()
            dato1=tokens.peek()
            print(tokens.peek())#dato
            nodos.agregarAssign(datoo,dato,dato1)   
            tokens.next()#+ o -
        if tokens.peek()['type'] == 'minus' or tokens.peek()['type'] == 'plus':    
            #llamar la funcion 
            expr(tokens)
            return 0
        return 0
    else:
        if tokens.peek()['type'] == 'print':   
            print(tokens.peek())
            dato=tokens.peek()
            tokens.next()
            print(tokens.peek())
            dato1=(tokens.peek())
            nodos.agregarPrint(dato,dato1)
            return 0
        else:
            exit()
            return 1

def stmts(tokens):
    if tokens.peek()['type'] == 'id' or tokens.peek()['type'] == 'print':    
        if stm(tokens)==0:
            stmts(tokens)
    else:
        if tokens.peek()['type'] == '$':    
            print()
            nodos.imprimir()
            nodos.codigo3()
            #print(1)
            exit()
        else:            
            print("error léxico")
            exit()

def dcl(tokens):
    if tokens.peek()['type'] == 'floatdcl':
        print(tokens.peek())
        dato=(tokens.peek())
        tokens.next()
        print(tokens.peek())
        dato1=(tokens.peek())
        nodos.agregarDcl(dato,dato1)
        tokens.next()
        return 0
    elif tokens.peek()['type']=='intdcl':
        print(tokens.peek())
        dato=(tokens.peek())
        tokens.next()
        dato1=(tokens.peek())
        print(tokens.peek())
        tokens.next()
        nodos.agregarDcl(dato,dato1)
        return 0
    else:
        return 1
        print("error léxico")
        exit()


def dcls(tokens):
    if dcl(tokens) ==0:
        dcls(tokens)

def prog(tokens):
    
    dcls(tokens)
    stmts(tokens)

with open('input.txt') as f:
    lines = f.read()

tokens = Tokens()
while not eof():
    tokens.append(scanner())
tokens.append(scanner())

prog(tokens)