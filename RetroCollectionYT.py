import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import yt_dlp

class RetroCollectionYTConvert:
    def __init__(self, root):
        self.root = root
        self.root.title("RetroCollection YT Convert")
        self.root.geometry("400x250")

        # Rótulo
        self.label = tk.Label(root, text="URL do vídeo do YouTube:")
        self.label.pack(pady=10)

        # Entrada de URL
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        # Menu de qualidade
        self.quality_label = tk.Label(root, text="Escolha a qualidade do vídeo:")
        self.quality_label.pack(pady=5)

        self.quality_options = ["Melhor Qualidade (até 720p)", "480p", "360p", "240p"]
        self.selected_quality = tk.StringVar()
        self.selected_quality.set(self.quality_options[0])

        self.quality_menu = tk.OptionMenu(root, self.selected_quality, *self.quality_options)
        self.quality_menu.pack(pady=5)

        # Botão de download de vídeo (.mp4)
        self.download_video_btn = tk.Button(root, text="Baixar Vídeo (.mp4)", command=self.download_video)
        self.download_video_btn.pack(pady=5)

        # Botão de download de áudio (.m4a)
        self.download_audio_btn = tk.Button(root, text="Baixar Áudio (.m4a)", command=self.download_audio)
        self.download_audio_btn.pack(pady=5)

        # Versão no canto inferior direito
        self.version_label = tk.Label(root, text="pré alpha 0.0.1 RetroCollection YT", anchor='se')
        self.version_label.pack(side="bottom", anchor="se", padx=10, pady=5)

    def get_video_format(self):
        quality_map = {
            "Melhor Qualidade (até 720p)": "best[height<=720][ext=mp4]",
            "480p": "best[height<=480][ext=mp4]",
            "360p": "best[height<=360][ext=mp4]",
            "240p": "best[height<=240][ext=mp4]",
        }
        return quality_map[self.selected_quality.get()]

    def download_video(self):
        url = self.url_entry.get()
        if url:
            save_path = filedialog.askdirectory()
            if save_path:
                ydl_opts = {
                    'format': self.get_video_format(),
                    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                }
                self.download(url, ydl_opts, "vídeo")
            else:
                messagebox.showerror("Erro", "Selecione uma pasta para salvar o arquivo.")
        else:
            messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")

    def download_audio(self):
        url = self.url_entry.get()
        if url:
            save_path = filedialog.askdirectory()
            if save_path:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                }
                self.download(url, ydl_opts, "áudio")
            else:
                messagebox.showerror("Erro", "Selecione uma pasta para salvar o arquivo.")
        else:
            messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")

    def download(self, url, ydl_opts, download_type):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Sucesso", f"{download_type.capitalize()} baixado com sucesso!")
        except yt_dlp.utils.DownloadError as e:
            messagebox.showerror("Erro", f"Erro ao baixar o {download_type}: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado ao baixar o {download_type}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RetroCollectionYTConvert(root)
    root.mainloop()
