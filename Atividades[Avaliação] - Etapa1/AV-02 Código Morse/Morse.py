from tkinter import *
from tkinter import messagebox
root = Tk()
v1 = StringVar(root)
v2 = StringVar(root)
v1.set("linguagem 1")
v2.set("linguagem 2")
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
def limparTudo() :
	l1f.delete(1.0, END)
	l2f.delete(1.0, END)
def convert() :
	message = l1f.get("1.0", "end")[:-1]
	if v1.get() == v2.get() :
		messagebox.showerror("Não é a mesma linguagem")
		return
	elif v1.get() == "Normal" and v2.get() == "Morse" :
		resultado = en(message)
	elif v1.get() == "Morse" and v2.get() == "Normal" :
		resultado = dc(message)
	else :
		messagebox.showerror("Escolha uma linguagem...")
		return
	l2f.insert('end -1 chars', resultado)
def en(message):
	c = ''
	for letra in message:
		if letra != ' ':
			c += DiCiONÁRiO_MORSE[letra] + ' '
		else:
			c += ' '
	return c
def dc(message):
	message += ' '
	dc = ''
	citext = ''
	for letra in message:
		if (letra != ' '):
			i = 0
			citext += letra
		else:
			i += 1
			if i == 2 :
				dc += ' '
			else:
				dc += list(DiCiONÁRiO_MORSE.keys())[
							list(DiCiONÁRiO_MORSE .values()).index(citext)]
				citext = ''
	return dc
if __name__ == "__main__" :	
	root.config(background = 'white')
	root.geometry("400x400")
	root.title("Tradutor Morse")
	headlabel = Label(root, text = 'Bem vindo ao tradutor morse',
							fg = 'black', bg = "white")
	label1 = Label(root, text = "            ",
				fg = 'black', bg = 'white')
	label2 = Label(root, text = "Da linguagem: ",
				fg = 'black', bg = 'white')
	label3 = Label(root, text = "Para a linguagem: ",
				fg = 'black', bg = 'white')
	label4 = Label(root, text = "Texto convertido ",
				fg = 'black', bg = 'white')
	headlabel.grid(row = 0, column = 1)
	label1.grid(row = 1, column = 0)
	label2.grid(row = 2, column = 0)
	label3.grid(row = 3, column = 0)
	label4.grid(row = 5, column = 0)
	l1f = Text(root, height = 5, width = 25,
									font = "lucida 13")
	l2f = Text(root, height = 5, width = 25,
									font = "lucida 13")
	l1f.grid(row = 1, column = 1, padx = 10)
	l2f.grid(row = 5, column = 1, padx = 10)
	ListadeLinguagens = ["Normal", "Morse"]
	Dalinguagen_op = OptionMenu(root, v1, *ListadeLinguagens)
	ParaLinguagem_op = OptionMenu(root, v2, *ListadeLinguagens)
	Dalinguagen_op.grid(row = 2, column = 1, ipadx = 10)
	ParaLinguagem_op.grid(row = 3, column = 1, ipadx = 10)
	b1 = Button(root, text = "converter", bg = "white", fg = "black",
								command = convert)
	b1.grid(row = 4, column = 1)
	b2 = Button(root, text = "Limpar", bg = "white",
					fg = "black", command = limparTudo)
	b2.grid(row = 6, column = 1)
	root.mainloop()