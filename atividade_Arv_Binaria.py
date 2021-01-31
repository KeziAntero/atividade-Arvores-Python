class No :
    valor = None 
    f_esq = None 
    f_dir = None
    
    def __init__(self,valor,f_esq=None,f_dir=None) :
        self.valor = valor 
        self.f_esq = f_esq 
        self.f_dir = f_dir

    def __str__(self) :
        return str(self.valor)

#a) Crie uma função chamada valor_nos(no) que me informe quais são os valores das nos.

    def valor_nos(self, valor) : 
  
        if self.valor:
            if valor < self.valor:
                if self.f_esq is None:
                    self.f_esq = No(valor)
                else:
                    self.f_esq.valor_nos(valor)
            elif valor > self.valor:
                if self.f_dir is None:
                    self.f_dir = No(valor)
                else:
                    self.f_dir.valor_nos(valor)
        else:
            self.valor = valor

    def imprimi_arv(self):
        if self.f_esq:
            self.f_esq.imprimi_arv()
        print( self.valor),
        if self.f_dir:
            self.f_dir.imprimi_arv()


root = No(27)
root.valor_nos(14)
root.valor_nos(35)
root.valor_nos(31)
root.valor_nos(11)
root.valor_nos(19)
root.valor_nos(2)

root.imprimi_arv()


#b) Crie uma função chamada altura(no) que me informe qual a altura da árvore. 

def altura(no) :
    if no is None:
        return 0;

    else :

        altura_esq = altura(no.f_esq) 
        altura_dir = altura(no.f_dir)
                
        if (altura_esq > altura_dir):
            return altura_esq+1
        else:
            return altura_dir+1
                   
print ("A altura da arvore e: %d" %(altura(root))) 


#c) Crie uma função chamada quantidade_nos(no) que me informe a quantidade de nós de uma árvore. 

def quantidade_nos(no):
    if no is None:
        return 0;
    else :
        return 1 + quantidade_nos(no.f_esq) + quantidade_nos(no.f_dir)

print ("A quantidade de nos e: %d" %(quantidade_nos(root)))            

#d) Crie uma função chamada buscar(no,valor) que encontre qual é o nó que possui o valor valor e retorne o Nó encontrado, 
# deve retornar None se não encontrar.

def buscar(no, valor):
    if no is None:
        print(f'{valor} nao foi encontrado na arvore')
        return
    if no.valor == valor:
        print(f'{valor} foi encontrado na arvore')
        return no
    if valor > no.valor:
        buscar(no.f_dir, valor)
    else:
        buscar(no.f_esq, valor)

if __name__ == '__main__':
        buscar(root, 7) 


         