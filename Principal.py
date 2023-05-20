import re
import xlrd
from io import open
from AnalizadorLexico import analizador
from AnalizadorSintactico import sintactico
import Pila

code = ("int suma ( float a , int b ) { return a + c ; } int main ( ) { int resultado ; resultado = suma ( 13 , 16 ) ; }")

lex = analizador("")
analizador = sintactico() 

lex.analizadorlexico(code)
analizador.compilador(code) 
