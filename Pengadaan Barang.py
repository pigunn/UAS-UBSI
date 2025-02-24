gudang_barang = []
def menu():
    while True:
        print("*"*40)
        print(" Program Pengadaan barang ".center(40,"="))
        print("*"*40)
        print('''
    1. Tambah Barang
    2. Kurangi / Hapus Barang
    3. Tampilkan Daftar Barang
    4. Total Biaya Pengadaan Barang
    5. Keluar
    ''')
        pilihan = int(input("Masukan pilihan :"))
        if pilihan == 1 :
            tampilkan_gudang_barang()
            while True:
                nama = input("Masukkan nama barang: ")
                jumlah = int(input("Masukkan jumlah barang: "))
                harga = int(input("Masukkan harga satuan barang: "))
                tambah(nama, jumlah, harga)
                lanjut = input("Lanjut menambahkan barang lain? (y/n): ").lower()
                if lanjut != "y":
                    break      
                        
        elif pilihan == 2 :
            while True:
                hapus()   
                lanjut = input("Lanjut menghapus barang lain? (y/n): ").lower()
                if lanjut != "y":
                    break

        elif pilihan == 3 :
            if not gudang_barang:
                print("Belum ada barang yang diadakan.")
            
            tampilkan_gudang_barang()
            while True:
                print("")
                lanjut = input("Press Enter for back!")
                if lanjut == "" :
                    break
            
        elif pilihan == 4 :
            biaya()
            while True:
                print("")
                lanjut = input("Press Enter for back!")
                if lanjut == "" :
                    break
                
        elif pilihan == 5 :
            print(" Terimakasih ".center(40,"="))
            break 
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
def tambah(nama, jumlah, harga):
    for barang in gudang_barang:
        if barang['nama'].lower() == nama.lower():
            barang['jumlah'] += jumlah
            barang['total_harga'] = barang['jumlah'] * barang['harga_satuan']
            print(f"Jumlah barang '{nama}' berhasil ditambahkan. Total jumlah sekarang: {barang['jumlah']}")            
            return
    barang = {
        'nama': nama,
        'jumlah': jumlah,
        'harga_satuan': harga,
        'total_harga': jumlah * harga
    }
    gudang_barang.append(barang)
    print("barang ", nama,  " berhasil ditambahkan")
    
def hapus() :
    if not gudang_barang:
        print("Belum ada barang yang diadakan.")
        return

    tampilkan_gudang_barang()    
    
    pilihan = int(input("Pilih nomor barang yang jumlahnya akan dikurangi: "))
    if 1 <= pilihan <= len(gudang_barang):
        barang = gudang_barang[pilihan - 1]
        print(f"Anda memilih barang: {barang['nama']} dengan jumlah {barang['jumlah']}")
        jumlah_kurang = int(input(f"Masukkan jumlah yang akan dikurangi (max {barang['jumlah']}): "))
                
        if 0 < jumlah_kurang <= barang['jumlah']:
            barang['jumlah'] -= jumlah_kurang
            barang['total_harga'] = barang['jumlah'] * barang['harga_satuan']
            if barang['jumlah'] == 0:
                gudang_barang.pop(pilihan - 1)
                print(f"Barang {barang['nama']} telah habis dan dihapus dari daftar.\n")
            else:
                print(f"Jumlah barang {barang['nama']} berhasil dikurangi menjadi {barang['jumlah']}.\n")
    
                            
def tampilkan_gudang_barang():    
    print("+----+----------------------+--------+-------------------+-------------------+")
    print("| No | Nama Barang          | Jumlah |    Harga Satuan   |    Total Harga    |")
    print("+----+----------------------+--------+-------------------+-------------------+")
    for i, barang in enumerate(gudang_barang):
        print(f"| {i+1:<2} | {barang['nama']:<20} | {barang['jumlah']:<6} | Rp.{barang['harga_satuan']:<14,.2f} | Rp.{barang['total_harga']:<14,.2f} |")
    print("+----+----------------------+--------+-------------------+-------------------+")
        
def biaya():
    tampilkan_gudang_barang()
    total = sum(barang['total_harga'] for barang in gudang_barang)
    print(f"Total Biaya Pengadaan:                                     Rp.{total:,.2f}")

menu()
