import tkinter as tk
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gustavo e JV Sabino - Adivinhação")
        self.root.geometry("400x380")
        self.root.resizable(False, False)

        self.iniciar_jogo()

    def iniciar_jogo(self):
        # Lógica do jogo
        self.numero_secreto = random.randint(1, 20)
        self.tentativas = 0
        self.ultimo_palpite = None

        # Widgets
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
            self.botao_novamente.pack()  # Mostra botão "jogar novamente"

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

        # Reinicia tudo
        self.iniciar_jogo()

# Executa o jogo
janela = tk.Tk()
app = JogoAdivinhacao(janela)
janela.mainloop()
