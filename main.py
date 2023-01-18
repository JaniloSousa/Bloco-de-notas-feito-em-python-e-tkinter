# fazendo as importações necessárias para esse projeto
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# criando e configurando minha janela principal
janela = Tk()
janela.title('Bloco de Notas')
janela.geometry('500x500+1250+100')
janela.resizable(False, False)
janela.iconphoto(False, PhotoImage(file='icon_notepad.png'))

# áreas das minhas funções
arq = None
def abrir():
    global arq
    arq = filedialog.askopenfilename() # retorna o caminho absoluto e o nome do arquivo (que você abriu)
    with open(arq, 'r') as arquivo:
        conteudo = arquivo.read()
    bloco.insert(1.0, conteudo)

def salvar(): # para salvar um arquivo que já foi aberto
    global arq
    conteudo = bloco.get(1.0, END)
    with open(arq, 'w') as arquivo:
        arquivo.write(conteudo)

def salvarComo():
    arq = filedialog.asksaveasfilename() # retorna o caminho absoluto e o nome do arquivo (que você quer salvar)
    conteudo = bloco.get('1.0', END)
    with open(arq, 'wt+') as arquivo:
        arquivo.write(conteudo)

# meu widget text. Onde vou escrever
bloco = Text(janela, width=500, height=500, font=('Arial 20'), bg='#7d6159', fg='white')
bloco.pack()

# meu menu bar de opções
menubar = Menu(janela)
opcoes = Menu(menubar)
opcoes.add_command(label='Abrir', command=abrir)
opcoes.add_command(label='Salvar', command=salvar)
opcoes.add_command(label='Salvar Como', command=salvarComo)
opcoes.add_command(label='Sair', command=janela.quit)
janela.config(menu=opcoes)


janela.mainloop()