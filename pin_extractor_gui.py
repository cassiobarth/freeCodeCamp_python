import tkinter as tk
from tkinter import ttk

# --- Logic from pin_extractor.py ---

def pin_extractor(poems):
    """
    Extracts a secret code from a list of poems.
    """
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.strip().split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                # Use the word at the index corresponding to the line number
                secret_code += str(len(words[line_index]))
            else:
                # If the word doesn't exist, the digit is '0'
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

# Original poems from the exercise
poem1 = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

original_poems = [poem1, poem2, poem3]

# --- Code + line-by-line explanation shown in the "Código Explicado" tab ---
# Each item is (indent_level, code, explanation). explanation="" means a blank/decorative line.
CODE_EXPLANATION = [
    (0, "def pin_extractor(poems):",
        "Define a função. 'poems' é uma lista de poemas (strings)."),
    (1, "secret_codes = []",
        "Cria uma lista vazia que vai guardar o PIN de cada poema."),
    (1, "for poem in poems:",
        "Percorre cada poema, um de cada vez."),
    (2, "secret_code = ''",
        "Começa uma string vazia para montar o PIN deste poema."),
    (2, "lines = poem.strip().split('\\n')",
        "Remove espaços das pontas e quebra o poema em uma lista de linhas."),
    (2, "for line_index, line in enumerate(lines):",
        "Percorre cada linha guardando também seu número (0, 1, 2, ...)."),
    (3, "words = line.split()",
        "Divide a linha em uma lista de palavras."),
    (3, "if len(words) > line_index:",
        "Verifica se existe uma palavra na posição igual ao número da linha."),
    (4, "secret_code += str(len(words[line_index]))",
        "Se existe: pega essa palavra, mede seu tamanho e junta ao PIN."),
    (3, "else:",
        "Caso contrário (a linha é curta demais)..."),
    (4, "secret_code += '0'",
        "...usa o dígito '0' no lugar."),
    (2, "secret_codes.append(secret_code)",
        "Guarda o PIN completo deste poema na lista de resultados."),
    (1, "return secret_codes",
        "Devolve a lista com o PIN de todos os poemas."),
]

# --- GUI Application ---

class PinExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Extrator de PIN")
        self.root.geometry("560x620")

        # --- Style ---
        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"))
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))

        # --- Notebook (tabs) ---
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self._build_interactive_tab()
        self._build_original_tab()
        self._build_explanation_tab()

    def _build_interactive_tab(self):
        """Tab 1: user types a poem and extracts its PIN."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Teste seu Poema")

        ttk.Label(tab, text="Digite seu poema aqui:").pack(anchor="w")
        self.user_text = tk.Text(tab, height=10, width=50, font=("Courier New", 10))
        self.user_text.pack(fill=tk.BOTH, expand=True, pady=5)

        ttk.Button(tab, text="Extrair PIN", command=self.extract_user_pin).pack(pady=5)

        self.user_result_var = tk.StringVar(value="Seu PIN aparecerá aqui.")
        ttk.Label(tab, textvariable=self.user_result_var,
                  foreground="blue", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=5)

    def _build_original_tab(self):
        """Tab 2: shows the original exercise poems and their result."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Exercício Original")

        ttk.Label(tab, text="Poemas Originais:", style="Header.TLabel").pack(anchor="w")

        original_poems_text = tk.Text(tab, height=12, width=50, font=("Courier New", 10))
        original_poems_text.insert(tk.END, "--- Poema 1 ---\n" + poem1 + "\n\n")
        original_poems_text.insert(tk.END, "--- Poema 2 ---\n" + poem2 + "\n\n")
        original_poems_text.insert(tk.END, "--- Poema 3 ---\n" + poem3)
        original_poems_text.config(state=tk.DISABLED, bg="#f0f0f0")  # read-only
        original_poems_text.pack(fill=tk.BOTH, expand=True, pady=5)

        original_result = pin_extractor(original_poems)
        result_text = f"PINs Extraídos: {original_result}"
        ttk.Label(tab, text=result_text, foreground="darkgreen",
                  font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=5)

    def _build_explanation_tab(self):
        """Tab 3: the exercise code with a line-by-line explanation."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Código Explicado")

        ttk.Label(tab, text="Como o código funciona, linha a linha:",
                  style="Header.TLabel").pack(anchor="w", pady=(0, 5))

        # Scrollable text area
        container = ttk.Frame(tab)
        container.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text = tk.Text(container, wrap=tk.WORD, font=("Courier New", 10),
                       yscrollcommand=scrollbar.set, bg="#fcfcfc",
                       padx=8, pady=8, spacing3=4)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text.yview)

        # Text tags for styling code vs. explanation
        text.tag_configure("code", foreground="#0b5394",
                           font=("Courier New", 10, "bold"))
        text.tag_configure("explanation", foreground="#555555",
                           font=("Segoe UI", 9, "italic"), lmargin1=24, lmargin2=24)

        for indent, code, explanation in CODE_EXPLANATION:
            prefix = "    " * indent
            text.insert(tk.END, prefix + code + "\n", "code")
            text.insert(tk.END, "→ " + explanation + "\n\n", "explanation")

        text.config(state=tk.DISABLED)  # read-only

    def extract_user_pin(self):
        """Gets text from the user input and updates the result label."""
        user_poem = self.user_text.get("1.0", tk.END)
        if not user_poem.strip():
            self.user_result_var.set("Por favor, insira um poema.")
            return

        # The function expects a list of poems
        extracted_pin = pin_extractor([user_poem])
        self.user_result_var.set(f"PIN Extraído: {extracted_pin[0]}")

if __name__ == "__main__":
    app_root = tk.Tk()
    app = PinExtractorApp(app_root)
    app_root.mainloop()
