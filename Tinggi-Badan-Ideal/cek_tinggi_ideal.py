import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import os

class EstimasiTinggiIdealApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estimasi Tinggi Ideal Berdasarkan Berat Badan")

        container = ttk.Frame(self.root, padding=20)
        container.pack()

        # Frame input
        input_frame = ttk.LabelFrame(container, text="Masukkan Data", padding=15)
        input_frame.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        ttk.Label(input_frame, text="Berat Badan (kg):").grid(row=0, column=0, sticky="w")
        self.entry_berat = ttk.Entry(input_frame, bootstyle="primary")
        self.entry_berat.grid(row=1, column=0, padx=5, pady=5)

        ttk.Label(input_frame, text="Jenis Kelamin:").grid(row=0, column=1, sticky="w", padx=15)
        self.gender_box = ttk.Combobox(
            input_frame, values=["Laki-laki", "Perempuan"],
            state="readonly", width=14, bootstyle="primary"
        )
        self.gender_box.current(0)
        self.gender_box.grid(row=1, column=1, padx=15, pady=5)
        self.gender_box.bind("<<ComboboxSelected>>", self.update_image)

        # Tombol proses
        ttk.Button(container, text="Cek Tinggi Ideal",
                   bootstyle="success", command=self.hitung_tinggi
        ).grid(row=1, column=0, pady=10)

        # Frame hasil
        self.result_frame = ttk.LabelFrame(container, text="Estimasi Tinggi Ideal", padding=15)
        self.result_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.result_label = ttk.Label(self.result_frame, text="", justify="left")
        self.result_label.pack()

        # Gambar
        self.image_label = ttk.Label(container)
        self.image_label.grid(row=0, column=1, rowspan=3, padx=20)

        self.load_images()
        self.update_image()

    def load_images(self):
        base_dir = os.path.dirname(__file__)
        self.img_laki = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "img", "Cowok.png")).resize((120, 120)))
        self.img_perempuan = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "img", "Cewek.png")).resize((120, 120)))

    def update_image(self, event=None):
        if self.gender_box.get() == "Perempuan":
            self.image_label.configure(image=self.img_perempuan)
        else:
            self.image_label.configure(image=self.img_laki)

    def hitung_tinggi(self):
        try:
            berat = float(self.entry_berat.get())
            gender = self.gender_box.get()

            if gender == "Laki-laki":
                tinggi_ideal = (berat / 0.9) + 100
            else:
                tinggi_ideal = (berat / 0.85) + 100

            self.result_label.config(text=(
                f"Jenis Kelamin : {gender}\n"
                f"Berat Badan   : {berat:.1f} kg\n"
                f"Tinggi Ideal  : {tinggi_ideal:.1f} cm"
            ))
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid untuk berat badan.")

root = ttk.Window(themename="darkly")
app = EstimasiTinggiIdealApp(root)
root.mainloop()
