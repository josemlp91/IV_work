import random
import time

#Ordenacion burbuja

def MatrizToList(matriz):
	vec= [0 for x in range(len(matriz)*len(matriz))]
	c=0
	for i in range (0,len(matriz)):
		for j in range (0,len(matriz)):
			vec[c]=matriz[i][j]
			c=c+1
	return vec


def ListToMatriz(lista,dim):
	a=[0]*dim
	matriz=[a]*dim
	con=0
	for i in range (0,dim):
		for j in range (0,dim):
			matriz[i][j]=lista[con]
			con+=1
	return matriz



def GeneraMatriz(dim):
	a=[0]*dim
	matriz=[a]*dim
	for i in range (0,dim):
		for j in range (0,dim):
			matriz[i][j]=random.randint(1,50)
	return matriz


def GeneraLista(dim):
	lista=[0]*dim
	for i in range (0,dim):
		lista[i]=random.randint(1,50)
	return lista




def swap (elem1, elem2):
	aux=elem1
	elem1=elem2
	elem2=aux


def Burbuja(lista, begin, end):
	aux=0
	for i in range(begin,end-1):
		for j in range(end-1,i,-1):
			if (lista[j]<lista[j-1]):
				aux=lista[j]
				lista[j]=lista[j-1]
				lista[j-1]=aux
				#swap(lista[j],lista[j-1])


def Seleccion (lista, begin,end):
	aux=0
	for i in range(begin,end-1):
		minimo=i
		for j in range(begin+1,end-1):
			if (lista[minimo]>lista[j]):
				minimo=j
				aux=lista[j]
				lista[j]=lista[j-1]
				lista[j-1]=aux




      


ListaAleat1=GeneraLista(10000)
ListaAleat2=GeneraLista(10)



#print (ListaAleat1)
#print (ListaAleat2)

Burbuja (ListaAleat1,0,len(ListaAleat1))
Seleccion(ListaAleat2,0,len(ListaAleat2))


#print (ListaAleat1)
#print (ListaAleat2)

#Tiempo Burbuja
inicio = time.time()

Burbuja (ListaAleat1,0,len(ListaAleat1))

fin = time.time()
tiempo_total_Burbuja = fin - inicio


#Tiempo Seleccion
inicio = time.time()

Seleccion (ListaAleat1,0,len(ListaAleat1))

fin = time.time()
tiempo_total_Seleccion = fin - inicio


print (str(tiempo_total_Burbuja))

print (str(tiempo_total_Seleccion))