gudang_barang = []
def menu ():
    while True:
        print ("*"*40)
        print (" Program Pengadaan Barang ". center(40,"="))
        print ("*"*40)
        print (''' 
    1. Tambah Barang 
    2. Kurangi / Hapus Barang
    3. Tampilkan Daftar Barang
    4. Total Biaya Pengadaan Barang 
    5. Keluar
    ''')
        pilihan = int(input("Masukan Pilihan : "))
        if pilihan == 1 :
        tampilkan_gudang_barang()
        while True :
            nama = input("Masukan Nama Barang: ")
            jumlah = int(input("Masukan Jumlah Barang: "))
            harga = int(input("Masukan Harga Satuan Barang: "))
            (nama,jumlah,harga)
            harga