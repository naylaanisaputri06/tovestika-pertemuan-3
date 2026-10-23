#Tugas
sisi = int(input("Masukkan Sisi Persegi:"))
pilih = input("luas/keliling:")

nay ={
    "keliling" : 4*sisi,
    "luas" : sisi*sisi
}

pesan_error = "Oops, hanya bisa input \"luas\" atau \"keliling\". Periksa kembali input-an Anda"  
print(nay.get(pilih, pesan_error))

