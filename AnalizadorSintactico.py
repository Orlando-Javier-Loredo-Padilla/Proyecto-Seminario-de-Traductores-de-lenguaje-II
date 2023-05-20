from io import open
import os
import subprocess
from AnalizadorLexico import analizador
import ArbolSintactico
import Pila 
from Pila import stack
import AnalizadorSemantico

class sintactico:

    def __init__(self):
        
        self.pila = stack()
        self.gramatica = []
        self.popElements = []
        self.nombreRegla = []
        self.matrizGramatica = []

   
    def readFile(self):

        file = open("compilador.lr","r")
        fullString = file.readlines()

        self.gramatica.append("52")
        self.popElements.append("0")
        self.nombreRegla.append(" ")

        for i in range(1,54):

            #Guarda la linea
            line = fullString[i]
            line = line[:-1].split("\t")

            if i != 53:

                self.gramatica.append(line[0])
                self.popElements.append(line[1])
                self.nombreRegla.append(line[2])

            elif i == 53:

                self.gramatica.append(line[0])
                self.popElements.append(line[1])
                self.nombreRegla.append(" ")


        for i in range(54,148):

            line = fullString[i]
            line = line[:-1].split("\t")
            self.matrizGramatica.append(line)

        file.close()


    def compilador(self,e):
        

        self.readFile()
        self.pila.limpiar()
        lexico = analizador(e)
            
        e = e + " $"
        entradaDividida = e.split(" ")


        primerNT = Pila.noTerminal("$","$",2)
        primerEstado = Pila.estado("0","",3)
        self.pila.push(primerNT)
        self.pila.push(primerEstado)

        valida = False
        cont = 0
        valorTabla = ""

        while valida == False:

      
            (tipo,valor) = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont])) 
            topePila = int(self.pila.top().returnValor())
            valorTabla = int(self.matrizGramatica[topePila][valor])
                  
            if valorTabla == 0:

                print("\n Código no aceptado")
                break

            elif valorTabla > 0:

                terminal = Pila.terminal(entradaDividida[cont],"",1)
                estado = Pila.estado(str(valorTabla),"",3)

                self.pila.push(terminal)
                self.pila.push(estado)

                cont+=1

            elif valorTabla < 0:
                
                if valorTabla == -1:

                    print("\nEntrada aceptada")
                    valida = True
                    
                    analizadorSem = AnalizadorSemantico.Semantico()
                    self.pila.pop()
                    elemento = self.pila.pop()
                    print(f"Entrada: {lexico.entrada}\n")
                    print("+++++++++++++++Arbol Sintactico+++++++++++++++\n")
                    elemento.nodo.printRegla()
                    analizadorSem.createFile()
                    
                    file = open('Codigo.asm','a+')
                    analizadorSem.analiza(elemento.nodo,file)
                    file.close()
                    analizadorSem.muestraErrores()
                    analizadorSem.mostrararchivo()
                    
                    batchFile = open('createEXE.bat','a+')
                    firstCommand = 'c:\masm32' +'\\'+'bin\ml /c /Zd /coff traduccion.asm\n'
                    secondCommand = 'c:\masm32'+'\\'+ 'bin\link /subsystem:console traduccion.obj'
                    batchFile.write(firstCommand)
                    batchFile.write(secondCommand)
                    batchFile.write('\ncmd /c del "%~f0"&exit')
                    batchFile.close()
                    subprocess.Popen('createEXE.bat',shell=True)
                    
                    break
                
                nodo = ArbolSintactico.Nodo()
                valorTabla+=1
                numeroEliminar = int(self.popElements[abs(valorTabla)])
                nomRegla = self.nombreRegla[abs(valorTabla)]
                nodo.regla = nomRegla

                if numeroEliminar > 0:

                    for i in range(int(numeroEliminar)*2):

                        elemento = self.pila.pop()
                        if i%2 == 1:

                            nodo.elementosEliminados.append(elemento)
                    
                topePila = int(self.pila.top().returnValor())
                reglaReal = str(abs(valorTabla))
                regla = int(self.gramatica[abs(valorTabla)])
                valorTabla = self.matrizGramatica[topePila][regla]

                noTerminal = Pila.noTerminal(reglaReal,nomRegla,2)
                noTerminal.nodo = nodo
                estado = Pila.estado(str(valorTabla),"",3)

                self.pila.push(noTerminal)
                self.pila.push(estado)
                