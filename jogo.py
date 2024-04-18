import random
from peewee import *

db = SqliteDatabase('pontos.db')

class Pontos(Model):
    name = CharField()
    pontuacao = CharField(default="0")

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([Pontos])





palavras = ["banana", "carro", "casa", "computador", "amor", "feliz", "sol", "lua", "gato", "cachorro",
            "futebol", "livro", "janela", "porta", "chave", "telefone", "aventura", "montanha", "praia", "oceano",
            "frio", "quente", "azul", "verde", "vermelho", "amarelo", "rosa", "laranja", "chocolate", "morango",
            "abacaxi", "kiwi", "melancia", "uva", "pessego", "melao", "maca", "pera", "banana", "laranja",
            "limao", "lima", "abobora", "batata", "cenoura", "tomate", "alface", "espinafre", "brocolis", "queijo",
            "presunto", "pao", "bolo", "sorvete", "cha", "cafe", "agua", "suco", "leite", "refrigerante", "cerveja",
            "vinho", "whisky", "vodka", "rum", "tequila", "martini", "mojito", "caipirinha", "samba", "rock", "jazz",
            "classico", "eletronico", "pop", "country", "hip-hop", "reggae", "rumba", "tango", "salsa", "merengue",
            "bachata", "folclore", "bossa nova", "forro", "sertanejo", "axe", "funk", "rap", "musica", "danca",
            "arte", "pintura", "escultura", "teatro", "cinema", "literatura", "poesia", "romance", "aventura"]

a = 0
vida = 10
pontos = 0
letras = []


for pontuacao in Pontos.select():
    print(f'Nome: {pontuacao.name}, pontuação: {pontuacao.pontuacao}')


nome = input("Qual seu Nome: ")


palavra_escolhida = random.choice(palavras)

for letra in palavra_escolhida:
    a += 1

print("A palavra escolhida contem", a, "letras\n")

while True:
        print("Sua vida atual é de: ",vida)
        palpite = input("\nFaça sua Escolha: ")
        if palpite == palavra_escolhida:
            print("Parabens voce acertou a palavra [", palavra_escolhida, "]")
            print("Sua pontuação final foi de: ",pontos)
            pontos += 15
            try:
                jogador = Pontos.get(name=nome)
                jogador.pontuacao = pontos
                jogador.save()
            except Pontos.DoesNotExist:
                user = Pontos.create(name=nome, pontuacao=pontos)
            break
        if palpite not in letras:
            letras.append(palpite)
            if palpite in palavra_escolhida:
                print("\nParabens, a sua escolha estava correta, existe a letra [", palpite,"] na palavra\n")
                pontos += 5
            else:
                print("\nErrado, essa palavra não contem essa letra. Você perdeu 1 ponto\n")
                vida-=1
        else:
            print("\nVoce ja usou essa letra\n")
        if vida == 0:
            print("\nVocê perdeu!!\n")
            print("A palavra era: ",palavra_escolhida,"\n")
            print("Sua pontuação final foi de: ",pontos)
            try:
                jogador = Pontos.get(name=nome)
                jogador.pontuacao = pontos
                jogador.save()
            except Pontos.DoesNotExist:
                user = Pontos.create(name=nome, pontuacao=pontos)
            break
