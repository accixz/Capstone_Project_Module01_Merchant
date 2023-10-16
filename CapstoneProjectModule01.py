#Data
listmerchant = [
    {
        'id': 'A0001',
        'nama merchant': 'Maju Bersama',
        'telp': '0211111111',
        'alamat': 'Jl. Manyar No 1',
        'email': 'majubersama@gmail.com'
    },
    {
        'id': 'B0002',
        'nama merchant': 'Florist',
        'telp': '0212222222',
        'alamat': 'Jl. Maanyar Ketoarjo No 9',
        'email': 'florist@gmail.com'
    },
    {
        'id':'C0003',
        'nama merchant': 'Maju Mapan',
        'telp': '0213333333',
        'alamat': 'Jl. Darmahusada No 23',
        'email': 'majumapan@yahoo.co.id'
    },
    {
        'id': 'D0004',
        'nama merchant': 'Klontong Jaya',
        'telp': '0214444444',
        'alamat': 'Jl. Klampis No 100',
        'email': 'klontongjaya@yahoo.com'
    },
    {
        'id': 'E0005',
        'nama merchant': 'Jaya Jaya',
        'telp': '0215555555',
        'alamat': 'Jl. Manyar Tirtoyoso No 99',
        'email': 'jayajaya@hotmail.com'
    }
]

#Main Menu
def mainmenu():
    while True:
        print('''
===========================================================================================================
||****************************************Welcome to List of Merchant************************************||
===========================================================================================================

List Menu: 
1. Menampilkan Merchant
2. Menambah Merchant
3. Mengupdate Merchant
4. Menghapus Merchant
5. Keluar program
''')
        menu = input ("Masukkan menu yang akan dijalankan : ")

        if menu == '1':
            menampilkanmerchant()
        elif menu == '2':
            menambahkanmerchant()
        elif menu == '3':
            mengupdatemerchant()
        elif menu == '4':
            menghapusmerchant()
        elif menu == '5':
            keluarprogram()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            mainmenu()
            
#Back to Sub Menu
def kembali():
    while True:
        kembali= input ("\nKembali ke sub menu (Y/N):").upper()
        if kembali == "Y":
            break

#Show Data
def lihatmerchant():
    print ('\nDaftar Merchant: \nID \t | Nama \t | Telp \t | Alamat \t\t | Email')
    for i in range (len(listmerchant)):
        print('{} \t | {} \t | {} \t | {} \t | {}'.format(listmerchant [i]['id'], listmerchant[i]['nama merchant'], listmerchant[i]['telp'], listmerchant[i]['alamat'],listmerchant[i]['email']))

#Read Data
def menampilkanmerchant():
    while True:
        print('''
---------------------------------------------------------------------------------
|                                   MENU 1                                      |
|                             MENAMPILKAN MERCHANT                              |
---------------------------------------------------------------------------------
1. Menampilkan semua list 
2. Menampilkan list berdasarkan ID
3. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            if len(listmerchant)!=0:
                lihatmerchant()
                kembali()
                menampilkanmerchant()
            else: 
                print ('\nData tidak tersedia')
                kembali()
                menampilkanmerchant()
        elif pilihan == '2':
            if len(listmerchant)!=0:
                idcari = input("\nMasukkan id yang dicari: ").upper()
                for i in range(len(listmerchant)):
                    if idcari == listmerchant[i]['id']:
                        print ('\nDaftar Merchant: \nID \t | Nama \t | Telp \t | Alamat \t\t | Email')
                        print ('{} \t | {} \t | {} \t | {} \t | {}'.format(listmerchant[i]['id'], listmerchant[i]['nama merchant'], listmerchant[i]['telp'], listmerchant[i]['alamat'],listmerchant[i]['email']))
                        kembali()
                        menampilkanmerchant()
                else:
                    print ('\nData tidak tersedia')
                    kembali()
                    menampilkanmerchant()
            else:
                print ('\nData tidak tersedia')
                kembali()
                menampilkanmerchant()
        elif pilihan == '3':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            menampilkanmerchant()

#Create Data
def menambahkanmerchant():
    lihatmerchant()
    while True:
        print('''
---------------------------------------------------------------------------------
|                                   MENU 2                                      |
|                              MENAMBAH MERCHANT                                |
---------------------------------------------------------------------------------
1. Menambahkan merchant
2. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            idmerchant = input ('\nMasukkan id merchant:').upper()
            for i in range(len(listmerchant)):
                if idmerchant == listmerchant[i]['id']:
                    print ('\nData sudah tersedia')
                    kembali()
                    menambahkanmerchant()
            else: 
                nama = input ('Masukkan nama merchant:').capitalize()
                telp = input ('Masukkan nomor telepon merchant:')
                alamat = input ('Masukkan alamat merchant:').title()
                email = input ('Masukkan email merchant:').lower()
                cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                if cek == 'Y':
                    listmerchant.append(
                        {'id': idmerchant,
                        'nama merchant': nama, 
                        'telp': telp, 
                        'alamat': alamat, 
                        'email': email})
                    print ('\nData berhasil disimpan')
                    kembali()
                    menambahkanmerchant()
                else:
                    print("\nData tidak tersimpan")
                    kembali()
                    menambahkanmerchant()
        elif pilihan == '2':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            menambahkanmerchant()

#Update Data
def mengupdatemerchant():
    lihatmerchant()
    while True:
        print('''
--------------------------------------------------------------------------------
|                                   MENU 3                                     |
|                             MENGUPDATE MERCHANT                              |
--------------------------------------------------------------------------------
1. Mengubah informasi merchant
2. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            idupdate = input('\nMasukkan id merchant yang ingin diupdate:').upper()
            for i in range(len(listmerchant)):
                if idupdate == listmerchant[i]['id']:
                    print ('\nDaftar merchant: \nID \t | Nama \t | Telp \t | Alamat \t\t | Email')
                    print ('{} \t | {} \t | {} \t | {} \t | {}'.format(listmerchant[i]['id'], listmerchant[i]['nama merchant'], listmerchant[i]['telp'], listmerchant[i]['alamat'],listmerchant[i]['email']))
                    lanjutupdate = input ("\nApakah data ini ingin diupdate (Y/N):").upper()
                    if lanjutupdate =='Y':
                        bagianupdate = input('\nMasukkan bagian yang ingin diupdate (nama/telp/alamat/email):')
                        if bagianupdate == 'nama merchant':
                            namaupdate = input('\nMasukkan nama merchant terbaru:').capitalize()
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listmerchant[i][bagianupdate] = namaupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatemerchant()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatemerchant()
                        elif bagianupdate == 'telp':
                            telpupdate = input('\nMasukkan nomor telp merchant terbaru:')
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listmerchant[i][bagianupdate] = telpupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatemerchant()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatemerchant()
                        elif bagianupdate == 'alamat':
                            alamatupdate = input ('\nMasukkan alamat merchant terbaru:').title()
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listmerchant[i][bagianupdate] = alamatupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatemerchant()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatemerchant()
                        elif bagianupdate == 'email':
                            emailupdate = input('Masukkan email terbaru:').lower()
                            cek = input('\nApakah anda ingin menyimpan data di atas (Y/N):').upper()
                            if cek == 'Y':
                                listmerchant[i][bagianupdate] = emailupdate
                                print ("\nData berhasil diupdate")
                                kembali()
                                mengupdatemerchant()
                            else:
                                print("\nData tidak tersimpan")
                                kembali()
                                mengupdatemerchant()
                        else:
                            kembali()
                            mengupdatemerchant()
                    else:
                        kembali()
                        mengupdatemerchant()
            else:
                print ('\nData tidak tersedia')
                kembali()
                mengupdatemerchant()
        elif pilihan == '2':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            mengupdatemerchant()

#Delete Data
def menghapusmerchant():
    lihatmerchant()
    while True:
        print('''
---------------------------------------------------------------------------------
|                                   MENU 4                                      |
|                              MENGHAPUS MERCHANT                               |
---------------------------------------------------------------------------------
1. Menghapus Merchant
2. Kembali ke menu utama
''')
        pilihan = input ("Masukkan pilihan anda: ")
        if pilihan == '1':
            idhapus = input ('\nMasukkan id merchant yang ingin dihapus:').upper()
            for i in range(len(listmerchant)):
                if idhapus == listmerchant[i]['id']:
                    cek = input ("\nApakah anda yakin akan menghapus data (Y/N):").upper()
                    if cek =='Y':
                        del listmerchant[i]
                        print ("\nMerchant berhasil dihapus")
                        kembali()
                        menghapusmerchant()
                    else:
                        print ("\nMerchant tidak dihapus")
                        kembali()
                        menghapusmerchant()
            else:
                print ("\nMerchant tidak tersedia")
                kembali()
                menghapusmerchant()
        elif pilihan == '2':
            mainmenu()
        else:
            print('\nMenu yang anda masukkan salah, silahkan pilih menu yang tersedia')
            kembali()
            menghapusmerchant()

#Exit Program
def keluarprogram():
    print('\nSampai jumpa lagi !')
    exit()

mainmenu()