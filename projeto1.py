# ESSA VERSAO TEM OS PREFIXOS DOS MODULOS NAS FUNCOES QUE VAO BUSCAR FUNCOES DEFINIDAS NOUTROS MODULOS


import random
from math import log
from math import sqrt
from math import inf
import ModGrafos as gr
import ModInd as i




##GRAFOS
# g=[[1,2,3,4],[[1,2],[1,3],[2,3],[3,2],[2,4],[3,4]]]
# nos(g)=[1,2,3,4]
# arestas(g)= [[1,2],[1,3],[2,3],[3,2],[2,4],[3,4]]

def nos(g):
    return g[0]

def arestas(g):
    return g[1]

def copias(g,k): #cada elemento de "copias" é um individuo inicial
    r=[]
    for x in arestas(g):
        r+=[x]*k
    for j in range(len(r)):
        r[j]= [r[j],[], j+1]
    return r

def numnos(g):
    return len(nos(g))











### INDIVIDUOS
#    individuo = [caminho, pos]
#    pos=[x,y,z]
#    caminho=[lista de nos por onde passa]
#    comprimento de individuo = len(individuo[0])

def ind(caminho, pos,ID):
    return [caminho, pos, ID]

def caminho(ind):
    return ind[0] # = len(caminho(ind))

def posicao(ind):
    return ind[1]

def ID(ind):
    return ind[2]

def size(ind):
    return len(ind[0])

def novoind():
    return[[],[],[]]

def novocaminho(ind,caminho):
    ind[0]=caminho
    return ind

def novapos(ind,pos):
    ind[1]=pos
    return ind

def novoID(ind,ID):
    ind[2]=ID
    return ind

def first(ind):
    return caminho(ind)[0]

def last(ind):
    return caminho(ind)[-1]











#SOPA

def exprandom(m):
    x=random()
    return -m*log(x)


def posInicial(g,k): #equivale as condicoes da sopa inicialmente
    r = gr.copias(g,k)
    sopa=[]

    for copia in r:
        a=i.novoind()
        a=i.novocaminho(a,i.caminho(copia))
        a=i.novoID(a,i.ID(copia))
        pos=[float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1)))]
        a=i.novapos(a,pos)
        sopa=sopa+[a]

    return sopa

def conjposicoes(sopa): #lista de todas as coordenadas utilizadas ate agora
    c=[]
    for individuo in sopa:
        c=c+[i.posicao(individuo)]
    return c

def conjIDS(sopa):
    r=[]
    for individuo in sopa:
        r=r+[i.ID(individuo)]
    return r

def nID(sopa):
    return conjIDS(sopa)[-1]+1

def addS(ind,sopa):
    sopa+=[ind]
    return sopa

def removeS(ind,sopa):
    return [x for x in sopa if x!=ind]
    
def distancia(ind1,ind2):
    [x1,y1,z1] = i.posicao(ind1)
    [x2,y2,z2] = i.posicao(ind2)
    distancia =sqrt(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))   
    return distancia

def listacomp(ind,sopa):
    listac=[]
    for individuo in sopa:
        if i.last(ind) == i.first(individuo) and (ind != individuo):
            listac+=[individuo]
    return listac
     
def maisprox(ind1,sopa):
    d=+inf
    m=[]
    for individuo in listacomp(ind1,sopa):
          if distancia(ind1,individuo)<=d:
              d=distancia(ind1,individuo)
              m=individuo
    return m

def cincoprox(ind1,sopa):
    cinco=[]
    falta=listacomp(ind1,sopa)
    while len(cinco)<5 and falta!=[]:
        cinco=cinco + [maisprox(ind1,falta)]
        falta.remove(maisprox(ind1,falta))
    return cinco     











            
## CAP
def event(t,k,IDe):
    if k=="con" or k=="des" or k=="cis":
        return [t,k,IDe]

def kind(e):
    if e[1]=="con" or e[1]=="des" or e[1]=="cis":
        return e[1]

def time(e):
    return e[0]

def IDe(e):
    return e[2]

def addE(c,e):
    return [x for x in c if time(x)<time(e)] + [e] + [x for x in c if time(x)>time(e)]

def removeE(c,e):
    return [x for x in c if x!=e]

def nextE(c):       # current event no simulador
    if len(c)>0:
        return c[0]
    else:
        print("A cap está vazia")
        
def delE(cap):     # elimina da cap o current event no fim do ciclo
    if len(cap)>0:
        return cap[1:]
    else:print("Erro de delE! A cap está vazia")
 
        
 
    
 
    
 
    

    


### EVENTOS:: concatenação,deslocação, cisão ("con", "des", "cis")

def con(ind1,sopa): 
    #ind 2 é um aleatorio dos "cincoprox (ind1,sopa)" 
    ind2=random.choice(cincoprox(ind1,sopa))
    
    ind3=novoind()
    ind3=novocaminho(ind3,caminho(ind1)[:-1]+caminho(ind2))
    ind3=novapos(ind3,[(posicao(ind1)[0]+posicao(ind2)[0])/2 , (posicao(ind1)[1]+posicao(ind2)[1])/2 , (posicao(ind1)[2]+posicao(ind2)[2])/2 ])
    ind3=novoID(ind3,nID(sopa))
    return ind3

def des(ind):

    x=posicao(ind)[0]
    y=posicao(ind)[1]
    z=posicao(ind)[2]
    
    c=size(ind)
    
    novox=float("{:.8f}".format(random.uniform(x-(1/c), x+(1/c)))) 
    novoy=float("{:.8f}".format(random.uniform(y-(1/c), y+(1/c))))
    novoz=float("{:.8f}".format(random.uniform(z-(1/c), z+(1/c))))
    while novox>1 or novox<0:
        novox=float("{:.8f}".format(random.uniform(x-(1/c), x+(1/c))))
    while novoy>1 or novoy<0 :
        novoy=float("{:.8f}".format(random.uniform(y-(1/c), y+(1/c))))
    while novoz>1 or novoz<0:
        novoz=float("{:.8f}".format(random.uniform(z-(1/c), z+(1/c))))
    pos=[novox,novoy,novoz]        
    ind=novapos(ind,pos)
    return ind
    
        









#SELEÇÃO

def od(ind,o,d):
    if i.first(ind)!=o or i.last(ind)!=d:
        return False
    else:
        return True
    
def length(ind,g):
    if i.size(ind)!=gr.numnos(g):
        return False
    else:
        return True
    
def todos(ind,g):
    ok=True 
    for x in gr.nos(g):
        if x not in i.caminho(ind):
            ok=False
    return ok   

def hamilton(ind,g,o,d):
    if od(ind,o,d) and length(ind,g) and todos(ind,g):
        return True
    else:
        return False
    
def final(sopa,g,o,d):
    r=[]
    for individuo in sopa:
        if hamilton(individuo,g,o,d):
            r+=[[i.caminho(individuo)]]
    return r
