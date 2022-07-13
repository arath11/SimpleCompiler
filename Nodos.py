from ast import While
from os import TMP_MAX
from folium import DivIcon
from pip import main


class Nodos:
    def __init__( self ) :
        self.datos=[]
        
    def agregar(self,dato):
        self.datos.append(dato)

    def agregarDcl(self,dato,dato1):#floats o ints
        tmp={'type':dato.get('type'),'val':dato1.get('val')}
        self.datos.append(tmp)

    def agregarPrint(self,dato,dato1):#prints
        tmp={'type':dato.get('type'),'val':dato1.get('val')}
        self.datos.append(tmp)

    def agregarAssign(self,dato,dato1,dato2):#decalraciones
        tmp={'type':dato1.get('type'),'val':dato.get('val'),'val1':dato2.get('val')}
        self.datos.append(tmp)

    def agregarSumYRes(self,dato,dato1):#sumas o resta
        tmp={'type':dato.get('type'),'val':dato1.get('val')}
        self.datos.append(tmp)  

    def imprimir(self):
        print('Datos en nodos')
        contadorTabs=0
        for i in range(len(self.datos)):
            if self.datos[i].get('type')=='plus' or self.datos[i].get('type')=='minus':
                contadorTabs=contadorTabs+1
            else:
                contadorTabs=0
            tabs=""
            for j in range(contadorTabs):
                tabs+='\t'
            print(f'{tabs} {self.datos[i]}')
        #print(self.datos)

    def codigo3(self):
        valido = True
        print("Codigo 3 direcciónes")
        floats=[]
        ints=[]
        arreglo=[]
        string=""
        for i in range(len(self.datos)-1,-1,-1):
            if(self.datos[i].get('type')=='assign' or self.datos[i].get('type')=='plus' or self.datos[i].get('type')=='minus'):
                if(self.datos[i].get('type')=='plus'):
                    string=string+" + "+self.datos[i].get('val')
                elif(self.datos[i].get('type')=='minus'):
                    string=string+" + "+self.datos[i].get('val')
                elif(self.datos[i].get('type')=='assign'):
                    string=self.datos[i].get('val')+" = "+ self.datos[i].get('val1')+string
                    arreglo.append(string)
                    string=""
                else:
                    exit()
            elif self.datos[i].get('type')=='floatdcl':
                floats.append(self.datos[i].get('val'))
            elif self.datos[i].get('type')=='intdcl':
                ints.append(self.datos[i].get('val'))

        # print()
        # print(arreglo)
        # print()
        r=0
        for i in range(1,len(arreglo)+1):
            #print(arreglo[-i])
            dividido=arreglo[-i].split(' ')
            if len(dividido)>3:
                #todo meter a una cola y revisar 
                stack=[]
                for j in dividido:
                    stack.append(j)
                print(stack)

                a1=stack.pop()
                signo=stack.pop()
                print(f'r{r}={stack.pop()}{signo}{a1}')
                r+=1
                #print(stack[len(stack)-1])            
                while(not (stack[len(stack)-1] == '=')):                    
                    signo=stack.pop()
                    print(f'r{r}=r{r-1}{signo}{stack.pop()}')
                    r+=1
                stack.pop()#signo de igual 
                print(f'{stack.pop()}=r{r}')
            else:
                
                    
                
                print(f'{dividido[0]} {dividido[1]} {dividido[2]}')

            
        return 1

        
def main():
    prueba=Nodos()
    a={'type':'float'}
    b={'type':'id', 'val':'a'}
    prueba.agregarDcl(a,b)
    prueba.agregarDcl(a,b)
    prueba.imprimir()




    
