import os
from tkinter import Tk, Label, filedialog, messagebox, Listbox, END
from tkinter import ttk
from PIL import Image


class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de WEBP para PNG")

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 10))
        style.configure('Green.TButton', background='#34c759', foreground='white', font=('Helvetica', 12, 'bold'),
                        borderwidth=3, padding=10)

        self.root.option_add('*TButton.border', 10) 

        self.label_files = Label(root, text="Arquivos WEBP selecionados:")
        self.label_files.pack()

        self.file_listbox = Listbox(root, width=50, height=10)
        self.file_listbox.pack()

        self.add_files_button = ttk.Button(root, text="Adicionar Arquivos", command=self.select_files)
        self.add_files_button.pack(pady=5)

        self.label_output = Label(root, text="Diretório de saída:")
        self.label_output.pack()

        self.output_label = Label(root, text="Nenhum diretório selecionado", fg="gray")
        self.output_label.pack()

        self.choose_dir_button = ttk.Button(root, text="Escolher Diretório de Saída",
                                            command=self.select_output_directory)
        self.choose_dir_button.pack(pady=5)

        self.convert_button = ttk.Button(root, text="Iniciar Conversão", style='Green.TButton',
                                         command=self.start_conversion)
        self.convert_button.pack(pady=20)

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Selecione arquivos WEBP",
            filetypes=[("Arquivos WEBP", "*.webp")],
            multiple=True
        )
        if len(files) > 10:
            messagebox.showerror("Erro", "Selecione no máximo 10 arquivos.")
            files = files[:10]

        self.webp_files = list(files)
        self.file_listbox.delete(0, END)
        for file in self.webp_files:
            self.file_listbox.insert(END, file)

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory(title="Selecione o diretório de saída")
        if self.output_dir:
            self.output_label.config(text=self.output_dir, fg="black")

    def start_conversion(self):
        if not self.webp_files:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado.")
            return
        if not self.output_dir:
            messagebox.showerror("Erro", "Nenhum diretório de saída selecionado.")
            return

        self.convert_images()

    def convert_images(self):
        for webp_file in self.webp_files:
            try:
                img = Image.open(webp_file)
                base_name = os.path.basename(webp_file)
                png_file = os.path.splitext(base_name)[0] + '.png'
                output_path = os.path.join(self.output_dir, png_file)
                img.save(output_path, 'PNG')
                print(f"Convertido: {webp_file} -> {output_path}")
            except Exception as e:
                print(f"Erro ao converter {webp_file}: {e}")

        messagebox.showinfo("Concluído", "Conversão finalizada com sucesso!")


def main():
    root = Tk()
    root.geometry('400x400')
    app = ImageConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
