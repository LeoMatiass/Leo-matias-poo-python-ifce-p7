# importa todas as funções do tkinter
from tkinter import *
# importa a classe messagebox do tkinter
from tkinter import messagebox
# cria a janela gui
root = Tk()
# cria variáveis globais
v1 = StringVar(root)
v2 = StringVar(root)
# inicia as variáveis
v1.set("linguagem 1")
v2.set("linguagem 2")
# Dicionário que representa o gráfico de código Morse
DiCiONÁRiO_MORSE = {'A':'.-', 'B':'-...','C':'-.-.', 
					'D':'-..', 'E':'.','F':'..-.', 
					'G':'--.', 'H':'....','I':'..', 
					'J':'.---', 'K':'-.-','L':'.-..', 
					'M':'--', 'N':'-.','O':'---', 
					'P':'.--.', 'Q':'--.-','R':'.-.', 
					'S':'...', 'T':'-','U':'..-', 
					'V':'...-', 'W':'.--','X':'-..-', 
					'Y':'-.--', 'Z':'--..','a': '.-', 
					'b':'-...','c':'-.-.', 'd':'-..', 
					'e':'.','f':'..-.', 'g':'--.', 
					'h':'....','i':'..', 'j':'.---', 
					'k':'-.-','l':'.-..', 'm':'--', 
					'n':'-.','o':'---', 'p':'.--.', 
					'q':'--.-','r':'.-.', 's':'...', 
					't':'-', 'u':'..-', 'v':'...-', 
					'w':'.--','x':'-..-', 'y':'-.--', 
					'z':'--..'  }
#Função para limpar ambas as áreas de texto
def limparTudo() :
	l1f.delete(1.0, END)
	l2f.delete(1.0, END)
# Função para realizar a conversão de um idioma para outro
def convert() :
	message = l1f.get("1.0", "end")[:-1]
	if v1.get() == v2.get() :
		# mostra a mensagem de erro
		messagebox.showerror("Não é a mesma linguagem")
		return
	elif v1.get() == "Normal" and v2.get() == "Morse" :
		resultado = en(message)
	elif v1.get() == "Morse" and v2.get() == "Normal" :
		resultado = dc(message)
	else :
		# mostra a mensagem de erro
		messagebox.showerror("Escolha uma linguagem...")
		return
	l2f.insert('end -1 chars', resultado)
# Função para criptografar a string de acordo com o gráfico de código Morse
def en(message):
	c = ''
	for letra in message:
		if letra != ' ':
			# Procura no dicionário e adiciona o código Morse correspondente junto com um espaço para separar os códigos Morse para caracteres diferentes
			c += DiCiONÁRiO_MORSE[letra] + ' '
		else:
			c += ' '
	return c
# Função para descriptografar a string de Morse para Portinglês
def dc(message):
	# espaço extra adicionado no final para acessar o último código morse
	message += ' '
	dc = ''
	citext = ''
	for letra in message:
		# verifica o espaço
		if (letra != ' '):
			# contador para controlar o espaço
			i = 0
			# armazenando código Morse de um único caractere
			citext += letra
		else:
			i += 1
			# if i = 2 que indica uma nova palavra
			if i == 2 :
			# adicionando espaço para separar palavras
				dc += ' '
			else:
				# acessando as chaves usando seus valores
				dc += list(DiCiONÁRiO_MORSE.keys())[
							list(DiCiONÁRiO_MORSE .values()).index(citext)]
				citext = ''
	return dc

if __name__ == "__main__" :	
	# Definição da cor de fundo da janela GUi
	root.config(background = 'white')
	# Definição da configuração da janela GUi (Largura x Altura)
	root.geometry("400x400")
	# Definição do nome da janela da GUi do tkinter
	root.title("Tradutor Morse")
	# Criando o label de Bem vindo 
	headlabel = Label(root, text = 'Bem vindo ao tradutor morse',
							fg = 'black', bg = "white")
	# Criando o label de idioma
	label1 = Label(root, text = "            ",
				fg = 'black', bg = 'white')
	# Criando o label "Da linguagem"
	label2 = Label(root, text = "Da linguagem: ",
				fg = 'black', bg = 'white')
	# Criando o label "Para a Linguagem"
	label3 = Label(root, text = "Para a linguagem: ",
				fg = 'black', bg = 'white')
	# Criando o label de conversão 
	label4 = Label(root, text = "Texto convertido ",
				fg = 'black', bg = 'white')
	# Método de grid que é usado para colocar os widgets nas respectivas posições na estrutura semelhante a uma tabela.
	headlabel.grid(row = 0, column = 1)
	label1.grid(row = 1, column = 0)
	label2.grid(row = 2, column = 0)
	label3.grid(row = 3, column = 0)
	label4.grid(row = 5, column = 0)
	# Cria uma caixa de área de texto para preencher ou digitar as informações.
	l1f = Text(root, height = 5, width = 25,
									font = "lucida 13")
	l2f = Text(root, height = 5, width = 25,
									font = "lucida 13")
	# Definição do preenchimento ao longo do eixo x.
	l1f.grid(row = 1, column = 1, padx = 10)
	l2f.grid(row = 5, column = 1, padx = 10)
	# lista de códigos de linguagem 
	ListadeLinguagens = ["Normal", "Morse"]
	# crie um menu suspenso usando a função OptionMenu que leva o nome da janela, a variável e as opções como argumento. use * antes do nome da lista, para descompactar os valores
	Dalinguagen_op = OptionMenu(root, v1, *ListadeLinguagens)
	ParaLinguagem_op = OptionMenu(root, v2, *ListadeLinguagens)
	Dalinguagen_op.grid(row = 2, column = 1, ipadx = 10)
	ParaLinguagem_op.grid(row = 3, column = 1, ipadx = 10)
	# Cria um botão de "converter" para anexá-lo com função de conversão
	b1 = Button(root, text = "converter", bg = "white", fg = "black",
								command = convert)
	b1.grid(row = 4, column = 1)
	# Cria um botão "Limpar" e anexa com função limparTudo
	b2 = Button(root, text = "Limpar", bg = "white",
					fg = "black", command = limparTudo)
	b2.grid(row = 6, column = 1)
	# inicia GUi
	root.mainloop()