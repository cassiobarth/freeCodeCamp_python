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

# --- GUI Application ---

class PinExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Extrator de PIN")
        self.root.geometry("450x550")

        # --- Style ---
        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"))
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))

        # --- Main Frame ---
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Interactive Section ---
        interactive_frame = ttk.LabelFrame(main_frame, text="Teste com seu Poema", padding="10")
        interactive_frame.pack(fill=tk.X, expand=True, side=tk.TOP)

        ttk.Label(interactive_frame, text="Digite seu poema aqui:").pack(anchor="w")
        self.user_text = tk.Text(interactive_frame, height=8, width=50, font=("Courier New", 10))
        self.user_text.pack(fill=tk.X, expand=True, pady=5)

        ttk.Button(interactive_frame, text="Extrair PIN", command=self.extract_user_pin).pack(pady=5)

        self.user_result_var = tk.StringVar(value="Seu PIN aparecerá aqui.")
        ttk.Label(interactive_frame, textvariable=self.user_result_var, foreground="blue").pack(anchor="w", pady=5)

        # --- Original Exercise Section ---
        original_frame = ttk.LabelFrame(main_frame, text="Resolução do Exercício Original", padding="10")
        original_frame.pack(fill=tk.X, expand=True, side=tk.BOTTOM, pady=10)
        
        # Calculate the original result
        original_result = pin_extractor(original_poems)
        
        # Display the result
        ttk.Label(original_frame, text="Poemas Originais:", style="Header.TLabel").pack(anchor="w")
        
        original_poems_text = tk.Text(original_frame, height=10, width=50, font=("Courier New", 10))
        original_poems_text.insert(tk.END, "--- Poema 1 ---\n" + poem1 + "\n\n")
        original_poems_text.insert(tk.END, "--- Poema 2 ---\n" + poem2 + "\n\n")
        original_poems_text.insert(tk.END, "--- Poema 3 ---\n" + poem3)
        original_poems_text.config(state=tk.DISABLED, bg="#f0f0f0") # Make it read-only
        original_poems_text.pack(fill=tk.X, expand=True, pady=5)


        result_text = f"PINs Extraídos: {original_result}"
        ttk.Label(original_frame, text=result_text, foreground="darkgreen", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=5)


    def extract_user_pin(self):
        """
        Gets text from the user input, calls the extractor, and updates the result label.
        """
        user_poem = self.user_text.get("1.0", tk.END)
        if not user_poem.strip():
            self.user_result_var.set("Por favor, insira um poema.")
            return
        
        # The function expects a list of poems
        extracted_pin = pin_extractor([user_poem])
        
        # Display the first (and only) result
        self.user_result_var.set(f"PIN Extraído: {extracted_pin[0]}")

if __name__ == "__main__":
    app_root = tk.Tk()
    app = PinExtractorApp(app_root)
    app_root.mainloop()
