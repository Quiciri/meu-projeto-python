import tkinter as tk
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gustavo e JV Sabino - Adivinhação")
        self.root.geometry("400x380")
        self.root.resizable(False, False)

        self.mostrar_boas_vindas()

    def mostrar_boas_vindas(self):
        # Tela de boas-vindas
        self.frame_boas_vindas = tk.Frame(self.root)
        self.frame_boas_vindas.pack(expand=True)

        self.label_boas_vindas = tk.Label(
            self.frame_boas_vindas,
            text="🎉 Boas-vindas ao jogo de adivinhação do Gustavo e do João! 🎉",
            font=("Arial", 14), wraplength=350, justify='center'
        )
        self.label_boas_vindas.pack(pady=40)

        self.botao_comecar = tk.Button(
            self.frame_boas_vindas,
            text="🎮 Começar Jogo",
            font=("Arial", 12),
            command=self.iniciar_jogo
        )
        self.botao_comecar.pack()

    def iniciar_jogo(self):
        # Remove tela de boas-vindas
        self.frame_boas_vindas.destroy()

        # Lógica do jogo
        self.numero_secreto = random.randint(1, 20)
        self.tentativas = 0
        self.ultimo_palpite = None

        # Widgets do jogo
        self.label_info = tk.Label(self.root, text="Adivinhe o número de 1 a 20!", font=("Arial", 14))
        self.label_info.pack(pady=10)

        self.entry_palpite = tk.Entry(self.root, font=("Arial", 14), justify='center')
        self.entry_palpite.pack(pady=5)
        self.entry_palpite.bind("<Return>", lambda event: self.verificar_palpite())

        self.botao_tentar = tk.Button(self.root, text="Tentar", font=("Arial", 12), command=self.verificar_palpite)
        self.botao_tentar.pack(pady=10)

        self.resultado = tk.Label(self.root, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

        self.label_anterior = tk.Label(self.root, text="Último palpite: -", font=("Arial", 10))
        self.label_anterior.pack()

        self.label_tentativas = tk.Label(self.root, text="Tentativas: 0", font=("Arial", 10))
        self.label_tentativas.pack()

        self.botao_novamente = tk.Button(self.root, text="🔁 Jogar Novamente", font=("Arial", 12),
                                         command=self.reiniciar_jogo)
        self.botao_novamente.pack(pady=10)
        self.botao_novamente.pack_forget()  # Esconde até vencer

    def verificar_palpite(self):
        palpite = self.entry_palpite.get()

        if not palpite.isdigit():
            self.resultado.config(text="Digite um número válido!")
            self.entry_palpite.delete(0, tk.END)
            return

        palpite = int(palpite)
        self.tentativas += 1

        self.ultimo_palpite = palpite
        self.label_anterior.config(text=f"Último palpite: {self.ultimo_palpite}")
        self.label_tentativas.config(text=f"Tentativas: {self.tentativas}")

        if palpite < self.numero_secreto:
            self.resultado.config(text="🔺 Tente um número **maior**.")
        elif palpite > self.numero_secreto:
            self.resultado.config(text="🔻 Tente um número **menor**.")
        else:
            self.resultado.config(text=f"🎉 Parabéns! Você acertou em {self.tentativas} tentativas.")
            self.botao_tentar.config(state="disabled")
            self.entry_palpite.config(state="disabled")
            self.botao_novamente.pack()

        self.entry_palpite.delete(0, tk.END)

    def reiniciar_jogo(self):
        # Remove widgets antigos
        self.label_info.destroy()
        self.entry_palpite.destroy()
        self.botao_tentar.destroy()
        self.resultado.destroy()
        self.label_anterior.destroy()
        self.label_tentativas.destroy()
        self.botao_novamente.destroy()

        # Reinicia o jogo
        self.iniciar_jogo()

# Executa o jogo
janela = tk.Tk()
app = JogoAdivinhacao(janela)
janela.mainloop()
