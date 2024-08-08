import tkinter as tk
from fpdf import FPDF
from num2words import num2words
from datetime import date

# Função para gerar o PDF
def gerar_pdf():
    cliente = nome_inp.get()
    consulta = consulta_inp.get()
    vlr = valor_inp.get()
    vlr_msg = f'{vlr} reais'
    vlr_extenso = num2words(float(vlr), lang='pt-br')
    vlr_extenso_msg = f'{vlr_extenso} reais'
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year
    
    # 2 - Layout do Recibo
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 20)
    img_largura = 210  # Defina a largura da imagem desejada
    img_altura = 297   # Defina a altura da imagem desejada
    pdf.image('dados/recibo_mult.jpg', x=0, y=0, w=img_largura, h=img_altura)
    pdf.text(170, 49, vlr_msg)
    pdf.text(80, 86, cliente)
    pdf.text(80, 108, vlr_extenso_msg)
    pdf.text(80, 135, consulta)
    pdf.set_text_color(0, 0, 0)
    pdf.text(30, 193, str(dia))
    pdf.text(50, 193, str(mes))
    pdf.text(70, 193, str(ano))
    nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}.pdf"
    pdf.output(nome_arquivo)
    resultado_lab.config(text=f'PDF Gerado com sucesso: {nome_arquivo}')

# Criando a Janela
window = tk.Tk()
window.geometry('400x300')
window.title('Gerador de Recibo')

# Adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Adicionando os inputs text
nome_lab = tk.Label(frame, text='Nome')
nome_lab.pack(fill='x', expand=True)

nome_inp = tk.Entry(frame)
nome_inp.pack(fill='x', expand=True)

consulta_lab = tk.Label(frame, text='Consulta')
consulta_lab.pack(fill='x', expand=True)

consulta_inp = tk.Entry(frame)
consulta_inp.pack(fill='x', expand=True)

valor_lab = tk.Label(frame, text='Valor')
valor_lab.pack(fill='x', expand=True)

valor_inp = tk.Entry(frame)
valor_inp.pack(fill='x', expand=True)

# Adicionando o label para exibir o resultado
resultado_lab = tk.Label(frame, text='')
resultado_lab.pack(fill='x', expand=True)

# Adicionando Botão
button = tk.Button(frame, text='Gerar PDF', command=gerar_pdf)
button.pack()

window.mainloop()