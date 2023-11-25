import tkinter as tk
import sqlite3
from tkinter import messagebox

def simpan_data_ke_sqlite(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):

# Membuka atau membuat database SQLite
    conn = sqlite3.connect("tkinter.tkinter.db")
    cursor = conn.cursor()

# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS Nilai_Siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa TEXT,
                    biologi INTEGER,
                    fisika INTEGER, 
                    inggris INTEGER,
                    prediksi_fakultas TEXT)''')
# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, Inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                    (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))

# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

#Untuk memberi nama judul
top = tk.Tk()
top.title("kelas b") 
top.geometry("500x500") 
top.resizable(False, False)
def Prediksi_Fakultas(biologi, fisika, inggris):
    if fisika < biologi > inggris:
        return "kedokteran"
    elif biologi < fisika > inggris:
        return "teknik"
    elif biologi < inggris > fisika:
        return "bahasa"
    else :
        return "belum ada"


#Menampilkan fungsi
def show():
    namaMhs = Siswa1.get()
    matkul1 = Biologi1.get()
    matkul2 = Fisika1.get()
    matkul3 = Inggris1.get()
    hasilMhs = f"Nama Mahasiswa: {namaMhs}"
    hasilmk1 = f"Mata Kuliah 1: {matkul1}"
    hasilmk2 = f"Mata Kuliah 2: {matkul2}"
    hasilmk3 = f"Mata Kuliah 3: {matkul3}"

    prediksi = Prediksi_Fakultas(matkul1, matkul2, matkul3)

    hasilPrediksi = f"Hasil Prediksi: {prediksi}"

    label_hasilMhs.config(text=hasilMhs)
    label_hasilmk1.config(text=hasilmk1)
    label_hasilmk2.config(text=hasilmk2)
    label_hasilmk3.config(text=hasilmk3)
    label_hasilprediksi.config(text=hasilPrediksi)
    if not matkul1 and not matkul2 and not matkul3 and not namaMhs:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlite(namaMhs, matkul1, matkul2,matkul3,prediksi)
        messagebox.showinfo("Info","Data Tersimpan")


# Label judul
label_judul = tk.Label(top, text="Prediksi Prodi Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat frame inputan
frame_input = tk.LabelFrame(top, labelanchor="n",pady=10, padx=10)
frame_input.pack()
# Label nama Mahasiswa
Siswa = tk.Label(frame_input, text="Masukkan Nama Anda: ")
Siswa.grid(row=0, column=0, pady=10)
Siswa1 = tk.Entry(frame_input)
Siswa1.grid(row=0,column=1)

# Label nilai Biologi
Biologi = tk.Label(frame_input, text="Masukkan nilai Biologi: ")
Biologi.grid(row=1, column=0, pady=10)
Biologi1 = tk.Entry(frame_input)
Biologi1.grid(row=1,column=1)

# Label nilai Fisika
Fisika = tk.Label(frame_input, text="Masukkan nilai Fisika: ")
Fisika.grid(row=2, column=0, pady=10)
Fisika1 = tk.Entry(frame_input)
Fisika1.grid(row=2,column=1)

# Label nilai Inggris
Inggris = tk.Label(frame_input, text="Masukkan nilai Inggris: ")
Inggris.grid(row=3, column=0, pady=10)
Inggris1 = tk.Entry(frame_input)
Inggris1.grid(row=3,column=1)

# Label Hasil

# Tombol submit  Hasil
TS_hasil = tk.Button(top, text="Submit", command=show)
TS_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(top,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

# Label hasil mk1,mk2,mk3
label_hasilMhs = tk.Label(frame_hasil, text="")
label_hasilMhs.pack()

label_hasilmk1 =  tk.Label(frame_hasil,text="")
label_hasilmk1.pack()

label_hasilmk2 =  tk.Label(frame_hasil,text="")
label_hasilmk2.pack()

label_hasilmk3 =  tk.Label(frame_hasil,text="")
label_hasilmk3.pack()

label_hasilprediksi = tk.Label(frame_hasil, text="")
label_hasilprediksi.pack()

top.mainloop()