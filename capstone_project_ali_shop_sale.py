## Capstone Project 1 - Purwadhika Digital School Surabaya
## Moh. Ali Fauzi
## Data Science

########################## Perancangan Program ############################
judul_kolom = ['Kode Barang', 'Nama Barang', 'Kategori', 'Stok Barang', 'Harga Satuan', 'Nama Sales']
barang = [['PP01', 'Sabuk Maritop', 'Sabuk', 15, 50000, 'Sales A'],
          ['PP02', 'Topi Nevada', 'Topi', 20, 30000, 'Sales B'], 
          ['PP03', 'Kaos Alphine', 'Baju', 25, 250000, 'Sales C'], 
          ['PP04', 'Celana Nariso', 'Celana', 12, 225000, 'Sales D'], 
          ['PP05', 'Sepatu Aidas', 'Sepatu', 25, 300000, 'Sales E']]
format_spasi = '{:^24}' * len(judul_kolom)
######################## Rancangan Tampilan Barang ########################
def tampilan_daftar_barang():
    print('================================================================ Daftar Barang ==========================================================')
    print(format_spasi.format(*judul_kolom))
    print('=========================================================================================================================================')
    for i in range(len(barang)) :
        print(format_spasi.format(*barang[i]))
    print('_________________________________________________________________________________________________________________________________________')
    print()
    if len(barang) == 0:
        print()
        print('!!! Maaf, Tidak ada data barang penjualan !!!')
        print()
################### Rancangan Konfirmasi Perubahan ########################
def konfirm(x):
    if x == 'Y':
        print()
    elif x == 'T':
        print()
        print('!!! Aktifitas dibatalkan !!!')
        print()
    else:
        print()
        print('!!! Masukan keyword yang benar !!!')
        print()
######################## 1. Rancangan Tampilan Penjual ####################
def penjual() :
    while True:
        print('''==========================================================
          SELAMAT DATANG DI TOKO CAK ALI
                User: Penjual
==========================================================
        Menu 1 : Menampilkan Data Barang
        Menu 2 : Menambah Data Barang
        Menu 3 : Mengubah Data Barang
        Menu 4 : Menghapus Data Barang
        Menu 5 : Kembali ke Menu Utama Toko
__________________________________________________________''')
        pilih_menu = input('Masukan angka menu yang diinginkan (1 / 2 / 3 / 4 / 5) : ')
        print()

        if pilih_menu == '1':
            print('!!! Anda telah memilih menu 1 (menampilkan data barang) !!!')
            print()
            print()
            menu_1()
        elif pilih_menu == '2':
            print('!!! Anda telah memilih menu 2 (menambah data barang) !!!')
            print()
            print()
            menu_2()
        elif pilih_menu == '3':
            print('!!! Anda telah memilih menu 3 (mengubah data barang) !!!')
            print()
            print()
            menu_3()
        elif pilih_menu == '4':
            print('!!! Anda telah memilih menu 4 (menghapus data barang) !!!')
            print()
            print()
            menu_4()
        elif pilih_menu == '5':
            print('!!! Anda Kembali ke menu utama toko !!!')
            print()
            print()
            break
        else:
            print()
            print('!!! Maaf anda tidak memilih dari no. 1 sampai 5. Mohon masukan angka menu yang benar !!!')
            print()
            continue
############################# Menampilkan Data ############################
def menu_1():
    while True:
        print('======== PILIH MENU YANG DIINGINKAN ========')
        print('1. Menampilkan semua data barang')
        print('2. Menampilkan kode barang yang diinginkan')
        print('3. Kembali ke menu utama penjual')
        print('4. Keluar dari aplikasi')
        print('__________________________________________')
        input_menu1 = input('Masukan angka yang diinginkan (1 / 2 / 3 / 4) : ')
        print()
        if input_menu1 == '1':
            print()
            tampilan_daftar_barang()

        elif input_menu1 == '2':
            kode_barang = input('Masukan kode barang yang diinginkan: ').upper()
            print()
            var_tem = 1
            while var_tem <= len(barang):
                if kode_barang == barang[var_tem - 1][0]:
                    print('================================================= Daftar Barang ======================================================')
                    print(format_spasi.format(*judul_kolom))
                    print('====================================================================================================================')
                    print(format_spasi.format(*barang[var_tem-1]))
                    print('____________________________________________________________________________________________________________________')
                    print()
                    break
                else:
                    var_tem += 1
            else:
                print()
                print('!!! Kode barang yang di input tidak tersedia !!!')
                print()
        elif input_menu1 == '3':
            print()
            print('!!! Anda kembali ke menu utama penjual !!!')
            print()
            break
        elif input_menu1 == '4':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            exit()
        else :
            print()
            print ('!!! Mohon masukan menu angka yang benar !!!')
            print()
            continue
############################## Menambah Data ##############################
def menu_2():
    while True:
        print('======== PILIH MENU YANG DIINGINKAN ========')
        print('1. Menambahkan barang baru')
        print('2. Kembali ke menu utama penjual')
        print('3. Keluar dari aplikasi')
        print('__________________________________________')
        input_menu2 = input('Masukan menu angka yang diinginkan (1 / 2 ) : ')
        print()

        if input_menu2 == '1':
            input_kode_barang = input('Masukan kode barang: ').upper()
            var_tem = 1
            while var_tem <= len(barang):
                if input_kode_barang == barang[var_tem-1][0]:
                    print()
                    print('!!! Kode barang yang anda masukan sudah tersedia !!!')
                    print()
                    break
                else:
                    var_tem += 1
            else:
                nama_barang = input('Masukan nama barang: ').title()
                kategori = input('Masukan kategori barang: ').title()          
                stok_barang = input('Masukan stok barang: ') 
                if stok_barang.isdigit() == True:
                    stok_barang = int(stok_barang)
                else:
                    print()
                    print('!!! Masukan stok barang berupa angka (tanpa huruf dan karakter) !!!')
                    print()
                    continue
                harga_satuan = input('Masukan harga satuan barang: ')
                if harga_satuan.isdigit() == True:
                    harga_satuan = int(harga_satuan)
                else:
                    print()
                    print('!!! Masukan harga berupa angka (tanpa huruf dan karakter) !!!')
                    print()
                    continue
                nama_sales = input('Masukan nama sales barang: ').title()
                list_baru_barang = [input_kode_barang, nama_barang, kategori, stok_barang, harga_satuan, nama_sales]
                simpan_data_1 = input('Apakah Anda ingin menyimpan data barang baru ini? (Y/T):').upper()
                konfirm(simpan_data_1) 
                if simpan_data_1 == 'Y':
                    barang.append(list_baru_barang)
                    print('Berikut adalah daftar barang terbaru')
                    barang.sort()
                    print()
                    tampilan_daftar_barang()
        elif input_menu2 == '2':
            print()
            print('!!! Anda Kembali ke menu utama penjual !!!')
            print()
            break
        elif input_menu2 == '3':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            exit()
        else:
            print()
            print('!!! Mohon masukan menu angka yang benar !!!')
            print()
            continue
############################## Mengubah Data ##############################
def menu_3():
    while True:
        print('========PILIH MENU YANG DIINGINKAN========')
        print('1. Mengubah data barang')
        print('2. Kembali ke menu utama penjual')
        print('3. Keluar dari aplikasi')
        print('__________________________________________')
        input_menu3 = input('Masukan angka yang diinginkan (1 / 2 / 3) : ')
        print()

        if input_menu3 == '1':
            tampilan_daftar_barang()
            input_kode_barang = input('Masukan kode barang: ').upper()
            #masukkan kode barang sebagai referensi mana yang mau diubah
            print()
            var_tem = 1
            while var_tem <= len(barang) :
                if input_kode_barang == barang[var_tem-1][0] :
                    print('============================================================= Daftar Barang ======================================================')
                    print(format_spasi.format(*judul_kolom))
                    print('==================================================================================================================================')
                    print(format_spasi.format(*barang[var_tem-1]))
                    print('__________________________________________________________________________________________________________________________________')
                    print()
                    simpan_data_2 = input(f'Apakah Anda ingin mengubah barang {input_kode_barang} ini? (Y/T):').upper()
                    konfirm(simpan_data_2) 
                    if simpan_data_2 == 'Y':
                        update_nama_kolom = input('Masukan nama kolom yang ingin diubah (nama barang / kategori / stok barang / harga satuan / nama sales) : ').title()
                        #ketikan input harus persis sesuai panjangnya dengan nama kolom
                        if update_nama_kolom == judul_kolom[0]: 
                            print('Maaf, anda tidak bisa mengubah kode barang. Kecuali anda menghapus dan membuat ulang data yang baru.')
                            print()
                            continue #kalau break nanti kembali ke menu mengubah data
                            #padahal yang diminta itu data seleksi & kembali ke apa ingin mengubah Y/T
                        elif update_nama_kolom == judul_kolom[1]:
                            nama_baru = input('Masukan nama barang baru: ').title()
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah nama barang {barang[var_tem-1][1]} menjadi {nama_baru}? (Y/T):').upper()
                            konfirm(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_tem-1][1] = nama_baru
                                tampilan_daftar_barang()
                                print()
                                var_tem += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[2]:
                            kategori_baru = input('Masukan nama kategori baru: ').title()
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah {barang[var_tem-1][2]} menjadi {kategori_baru}? (Y/T):').upper()
                            konfirm(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_tem-1][2] = kategori_baru
                                tampilan_daftar_barang()
                                print()
                                var_tem += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[3]:
                            stok_baru = input('Masukan stok barang baru: ')
                            if stok_baru.isdigit() == True:
                                stok_baru = int(stok_baru)
                            else:
                                print()
                                print('!!! Masukan stok barang berupa angka (tanpa huruf dan karakter) !!!')
                                print()
                                break
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah stok barang {barang[var_tem-1][3]} menjadi {stok_baru}? (Y/T):').upper()
                            konfirm(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_tem-1][3] = stok_baru
                                tampilan_daftar_barang()
                                var_tem += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[4]: 
                            harga_baru = input('Masukan harga satuan barang baru: ')
                            if harga_baru.isdigit() == True:
                                harga_baru = int(harga_baru)
                            else:
                                print()
                                print('!!! Masukan harga berupa angka (tanpa huruf dan karakter) !!!')
                                print()
                                break
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah {barang[var_tem-1][4]} menjadi {harga_baru}? (Y/T):').upper()
                            konfirm(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_tem-1][4] = harga_baru
                                tampilan_daftar_barang()
                                print()
                                var_tem += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[5]:
                            sales_baru = input('Masukan nama sales baru: ').title()
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah {barang[var_tem-1][5]} menjadi {sales_baru}? (Y/T):').upper()
                            konfirm(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_tem-1][5] = sales_baru
                                tampilan_daftar_barang()
                                print()
                                var_tem += 1
                                break
                            else:
                                break
                        else:
                            print()
                            print('!!! Nama kolom yang dimasukan tidak tersedia !!!')
                            print()
                            break
                    else:
                        break
     
                else:
                    var_tem += 1
            else:
                print()
                print('!!! Kode barang tidak tersedia !!!')
                print()
                continue
        elif input_menu3 == '2':
            print()
            print('!!! Anda kembali ke menu utama penjual !!!')
            print()
            break
        elif input_menu3 == '3':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            exit()
        else:
            print()
            print('!!! Masukan menu angka yang benar !!!')
            print()
            continue
############################## Menghapus Data #############################
def menu_4():
    while True:
        print('======== PILIH MENU YANG DIINGINKAN ========')
        print('1. Menghapus data barang')
        print('2. Kembali ke menu utama penjual')
        print('3. Keluar dari aplikasi')
        print('__________________________________________')
        input_menu4 = input('Masukan angka yang diinginkan: ')
        print()
        if input_menu4 == '1':
            tampilan_daftar_barang()
            hapus_barang = input('Masukan kode barang: ').upper()
            if len(barang) == 0:
                    print()
                    print('!!! Tidak ada data barang penjualan, silahkan tambah barang baru pada menu 3 !!!')
                    print()
                    break
            var_tem = 1
            while var_tem <= len(barang) :
                if hapus_barang == barang[var_tem-1][0] :
                    print('======================================= Daftar Barang ======================================================')
                    print(format_spasi.format(*judul_kolom))
                    print('==========================================================================================================')
                    print(format_spasi.format(*barang[var_tem-1]))
                    print('__________________________________________________________________________________________________________')
                    print()
                    simpan_data_3 = input(f'Apakah Anda ingin menghapus barang {barang[var_tem-1][1]} ini? (Y/T):').upper()
                    konfirm(simpan_data_3)
                    if simpan_data_3 == 'Y':
                        barang.pop(var_tem-1)
                        tampilan_daftar_barang()
                        print()
                        break
                    else:
                        break
                else:
                    var_tem +=1
            else:
                print()
                print('!!! Kode barang yang di input tidak tersedia !!!')
                print()       
        elif input_menu4 == '2':
            print()
            print('!!! Anda kembali ke menu utama penjual !!!')
            print()
            break
        elif input_menu4 == '3':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            exit()
        else:
            print()
            print('!!! Masukan menu angka yang benar !!!')
            print()
            continue
######################## 2. Rancangan Tampilan Pembeli ####################
def pembeli():
    user_pembeli = input('Masukkan nama anda : ')
    while True:
        print()
        print(f'''==================================================
          SELAMAT DATANG DI TOKO CAK ALI
                User: {user_pembeli}
==================================================
        Menu 1 : Menampilkan data barang
        Menu 2 : Membeli barang
        Menu 3 : Kembali ke menu utama toko
        Menu 4 : Keluar dari aplikasi
__________________________________________________''')
        pilih_menu_pembeli = input('Masukan angka menu yang diinginkan (1 / 2 / 3) : ')
        print()

        if pilih_menu_pembeli == '1':
            tampilan_daftar_barang()
            print()
        elif pilih_menu_pembeli == '2':
            print()
            tampilan_daftar_barang()
            input_kode_barang = input('Masukan Kode Barang yang ingin dibeli (pp01 / pp02 / pp03 / pp04 / pp05): ').upper()
            print()
            var_tem = 1
            while var_tem <= len(barang):
                if input_kode_barang == barang[var_tem - 1][0]:
                    input_jumlah_beli = input('Masukan jumlah pembelian: ') 
                    print()
                    if input_jumlah_beli.isdigit() == True:
                        input_jumlah_beli = int(input_jumlah_beli)
                        if input_jumlah_beli <= int(barang[var_tem-1][3]): 
                            total_harga_beli = input_jumlah_beli*(barang[var_tem-1][4]) 
                            print(f'Anda akan membeli {barang[var_tem-1][1]} sebanyak {input_jumlah_beli} Pcs dengan total seharga Rp{total_harga_beli}.')
                            simpan_data_beli = input('Apakah Anda ingin melanjutkan pembayaran? (Y/T):').upper()
                            konfirm(simpan_data_beli) 
                            if simpan_data_beli == 'Y':
                                input_uang = input('Masukan jumlah uang anda: ')
                                print()
                                if input_uang.isdigit() == True:
                                    input_uang = int(input_uang)
                                    print()
                                else:
                                    print()
                                    print('!!! Masukan jumlah uang berupa angka (tanpa huruf dan karakter) !!!')
                                    continue
                                if input_uang == total_harga_beli:
                                    print()
                                    print('### Transaksi berhasil ###')
                                    print()
                                    barang[var_tem-1][3] -= input_jumlah_beli 
                                    tampilan_daftar_barang()
                                    print()
                                    var_tem += 1
                                    break
                                elif input_uang > total_harga_beli:
                                    print()
                                    print('### Transaksi berhasil ###')
                                    print(f'### Uang anda kembali Rp{input_uang-total_harga_beli} ###')
                                    print()
                                    barang[var_tem-1][3] -= input_jumlah_beli 
                                    tampilan_daftar_barang()
                                    print()
                                    var_tem += 1
                                    break
                                else:
                                    print()
                                    print('!!! Transaksi dibatalkan !!!')
                                    print(f'!!! Maaf, uang yang anda masukan kurang Rp{total_harga_beli-input_uang} !!!')
                                    print()
                                    break  
                            else:
                                print()
                                break
                        else:
                            print()
                            print('!!! Stok barang tidak mencukupi dengan jumlah yang ingin anda beli !!!')
                            print() 
                            break 
                    else:
                        print()
                        print('!!! Masukan jumlah beli berupa angka (tanpa huruf dan karakter) !!!')
                        print()
                        continue
                else:
                    var_tem += 1
            else:
                print()
                print('!!! Kode yang anda masukan tidak tersedia !!!')
                print()
                continue
        elif pilih_menu_pembeli == '3':
            print()
            print('!!! Anda kembali ke menu utama toko !!!')
            print()
            break
        elif pilih_menu_pembeli == '4':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            exit()
        else:
            print()
            print('!!! Masukan angka menu yang benar !!!')
            print() 
            continue
####################### Perancangan Program Aplikasi ######################
def program_start():
     while True:
        print('''===============================================
        SELAMAT DATANG DI MENU UTAMA
                TOKO CAK ALI
===============================================
            Pilih User Sebagai:
            1 : Sebagai Penjual
            2 : Sebagai Pembeli
            3 : Hentikan Aplikasi
_______________________________________________''')
        pilih_user = input('Masukan menu yang diinginkan (1 / 2 / 3) : ')
        print()

        if pilih_user == '1':
            penjual()
        elif pilih_user == '2':
            pembeli()
        elif pilih_user == '3':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            break
        else:
            print('!!! Angka menu yang anda masukan tidak tersedia !!!')
            print()
            continue
############################ Program Selesai ##############################
######################### Menjalankan Program #############################
program_start()
