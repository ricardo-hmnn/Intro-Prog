"""Declarar uma lista que possui nomes de pessoas inventados, outra lista que possui os seus sobrenomes e outra lista que
possui a suas idades. Depois gerar listas individuais associadas a cada pessoa, na qual se encapsulem todos os dados dessa
pessoa. Para isto, pode ser util usar uma propriedade das listas que é a possibilidade de acrescentar elementos usando a função
append."""

nomes = ["Alice","Bruno","Carlo","Daniela","Eduardo","Fernanda","Gustavo","Helena","Isabel","João"]
sobrenomes = ["Almeida","Barbosa","Castro","Dias","Ferreira","Gomes","Lima","Martins","Oliveira","Souza"]
idades = [23,35,29,41,30,27,33,24,38,25]
pessoas = []

for i in range(10):
    pessoas.append([nomes[i],sobrenomes[i],idades[i]])
print(pessoas)