import os
import csv
import json
import datetime as dt

csvPemesanan = 'daftarPesanan.csv'
csvBarang = 'daftarBarang.csv'
csvHapus = 'daftarHapus.csv'
authAdmin = 'loginAdmin.json'
    
           
# MAIN MENU
def show_menu():

    os.system('cls')
    print(f'{"SELAMAT DATANG DI":^40}')
    print(f'{"APLIKASI RESTORAN DEN BEI":^40}')
    print('='*40)
    print("[1] Buat Pesanan")
    print("[2] Lihat Pesanan")
    print("[3] Admin")
    print("[4] Exit")

    menu = input("PILIH MENU> ")
    print("\n")

    if menu == '1':
        buatPesanan()
    elif menu == '2':
        lihatData()
    elif menu == '3':
        admin()
    elif menu == '4':
        print('Keluar dari program')
        exit()
    else:
        print("Pilihan menu tidak tersedia!")
        input("Tekan enter untuk memilih kembali...")


# MENU [1] BUAT PESANAN
def buatPesanan():

    while True:
        os.system('cls')
        print(f'{"MENU BUAT PESANAN":^{40}}')
        print('='*40)
        print("[1] Pilih Barang sendiri")
        print("[2] Menggunakan Saran System")

        print("\n[0] Kembali")
        menu = input("PILIH MENU> ")
        print("\n")

        if menu == '1':
            pilihManual()
        elif menu == '2':
            saranSystem()
        elif menu == '0':
            break
        else:
            print("Pilihan menu tidak tersedia!")
            input("Tekan enter untuk memilih kembali...")


# SUBMENU [1] PILIH SECARA MANUAL
def pilihManual():

    with open(csvBarang, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        show = list(reader)

        maksItems, maksWeight, maksPrice = 0, 0, 0

        for i in range(len(show)):
            if len(show[i]['barang']) > maksItems:
                maksItems = len(show[i]['barang'])
            if len(show[i]['berat']) > maksWeight:
                maksWeight = len(show[i]['berat'])
            if len(show[i]['harga']) > maksPrice:
                maksPrice = len(show[i]['harga'])

        leng = maksItems+maksWeight+maksPrice+41

        barang = []
        listBerat = []
        listHarga = []
        berat = 0
        harga = 0

        while True:
            os.system("cls")
            print("BUAT PESANAN BARU".center(leng))
            print("PILIH BARANG YANG ANDA INGINKAN".center(leng))
            print('='*leng)

            print()
            print('-'*leng)
            print(
                f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+5}}| {"HARGA":^{maksPrice+5}}')
            print('-'*leng)

            if len(show) <= 0:
                print("BELUM ADA BARANG")
                input("Tekan Enter untuk Kembali")
            else:
                no = 1
                for row in show:
                    print(
                        f'{no:<3}| {row["barang"]:<{maksItems+5}}| {row["berat"]:<{maksWeight+5}}| {row["harga"]:<{maksPrice+5}}')
                    no += 1
                print('-'*leng)
                print("Inputkan No Barang        [0] Kembali")

                try:
                    pick = int(input("Pilih > "))

                    if pick == 0:
                        break

                    # Pilih barang yang diinginkan
                    elif 0 <= pick <= len(show):
                        os.system('cls')
                        pick -= 1

                        print('-'*leng)
                        print(
                            f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+5}}| {"HARGA":^{maksPrice+5}}')
                        print('-'*leng)
                        print(
                            f'{"1":<3}| {show[pick]["barang"]:<{maksItems+5}}| {show[pick]["berat"]:<{maksWeight+5}}|{show[pick]["harga"]:<{maksPrice+5}}')
                        print('-'*leng)
                        print(f"Pilihan Anda : {show[pick]['barang']}, berat {show[pick]['berat']}gr dan Harga {show[pick]['harga']}")
                        
                        command = input("Yakin akan memilih barang tersebut [y/t]? ")

                        if command == "y":

                            barang.append(show[pick]['barang']) # Menambahkan nama barang yang dipilih ke list barang
                            listBerat.append(int(show[pick]['berat'])) # Menambahkan berat barang yang dipilih ke list berat
                            listHarga.append(int(show[pick]['harga'])) # Menambahkan harga barang yang dipilih ke list harga
                            berat += int(show[pick]['berat']) # Menambah berat barang untuk setiap perulangan
                            harga += int(show[pick]['harga']) # Menambah harga barang untuk setiap perulanagan

                            os.system('cls')
                            print('-'*leng)
                            print(
                                f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+5}}| {"HARGA":^{maksPrice+5}}')
                            print('-'*leng)
                            print(
                                f'{"1":<3}| {show[pick]["barang"]:<{maksItems+5}}| {show[pick]["berat"]:<{maksWeight+5}}|{show[pick]["harga"]:<{maksPrice+5}}')
                            print('-'*leng)

                            print("Pesanan Berhasil ditambahkan...")
                            
                            inputUser = input("\nPilih lagi [y/t] ? ")

                            if inputUser == "y":
                                continue
                            elif inputUser == "t":
                                
                                os.system('cls')
                                print("PESANAN ANDA".center(leng))
                                print('-'*leng)
                                print(
                                    f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+15}}| {"HARGA":^{maksPrice+15}}')
                                print('-'*leng)
                                no = 1
                                
                                for i in range(len(barang)):
                                    print(
                                        f'{no:<3}| {str(barang[i]):<{maksItems+5}}| {str(listBerat[i]):<{maksWeight+15}}| {str(listHarga[i]):<{maksPrice+15}}')
                                    no += 1
                                print('-'*leng)
                                print(
                                    f'{"":<3} {"TOTAL PESANAN  ":>{maksItems+6}}| {str(berat):<{maksWeight+15}}| {str(harga):<{maksPrice+15}}')
                                
                                date = dt.datetime.now().strftime('%d/%m/%Y/%H:%M:%S')
                                name = str(input("\nPesanan atas Nama : "))

                                # Menambahakan seluruh data pesanaan ke file csv (daftarPesanan.csv)
                                with open(csvPemesanan, 'a', newline='') as csv_file:
                                    fieldnames = ['tanggal','nama', 'pesanan', 'harga','kapasitas','status']
                                    write = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
                                    write.writerow({'tanggal': date,'nama': name,'pesanan': barang, 'harga': int(harga),'kapasitas': int(berat), 'status': "Dikemas"})
                                print("\nPesanan Berhasil di Buat..")
                                input("Tekan Enter untuk Kembali...")
                                break

                            else:
                                print("Input yang Anda masukkan salah")
                                input("Tekan Enter untuk input Kembali...")
                        elif command == "t":
                            input("\nTekan Enter untuk memilih barang lain...")

                        else:
                            print("Input yang Anda masukkan salah")
                            input("Tekan Enter untuk input Kembali...")
                    else:
                        print("Input yang Anda masukkan salah")
                        input("Tekan Enter untuk input Kembali...")
                except:
                    print("Input yang Anda masukkan salah")
                    input("Tekan Enter untuk input Kembali...")


# SUBMENU [2] MENGGUNAKAN SARAN SYSTEM 
def saranSystem():

    with open(csvBarang, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        show = list(reader)

        maksItems, maksWeight, maksPrice = 0, 0, 0

        for i in range(len(show)):
            if len(show[i]['barang']) > maksItems:
                maksItems = len(show[i]['barang'])
            if len(show[i]['berat']) > maksWeight:
                maksWeight = len(show[i]['berat'])
            if len(show[i]['harga']) > maksPrice:
                maksPrice = len(show[i]['harga'])

        leng = maksItems+maksWeight+maksPrice+41

        while True:
            os.system("cls")
            print("BUAT PESANAN BARU".center(leng))
            print("MENGGUNAKAN SARAN DARI SYSTEM".center(leng))
            print('='*leng)

            print()
            print('-'*leng)
            print(
                f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+5}}| {"HARGA":^{maksPrice+5}}')
            print('-'*leng)

            if len(show) <= 0:
                print("BELUM ADA BARANG")
                input("Tekan Enter untuk Kembali")
            else:
                no = 1
                for row in show:
                    print(
                        f'{no:<3}| {row["barang"]:<{maksItems+5}}| {row["berat"]:<{maksWeight+5}}| {row["harga"]:<{maksPrice+5}}')
                    no += 1
                print('-'*leng)
                print("[1] Small Pack (800gr)   [2] Medium Pack (1,5kg)")
                print("[3] Large Pack (3kg)     [0] Kembali")


            items = []
            weight = []
            price = []
            
            # Mengambil data dari file csv (datarBarang.csv)
            for row in range(len(show)):
                items.append(show[row]["barang"])
                weight.append(int(show[row]["berat"]))
                price.append(int(show[row]["harga"]))

            try:
                # Pilih Kapasitas
                kapasitas = input("\nPilih kapasitas > ")

                if kapasitas == "0":
                    break

                elif kapasitas == "1" or kapasitas == "2" or kapasitas == "3":
                    
                    if kapasitas == "1":
                        capacity = 800
                        txt = "SMALL"
                    elif kapasitas == "2":
                        capacity = 1500
                        txt = "MEDIUM"
                    elif kapasitas == "3":
                        capacity = 3000
                        txt = "LARGE"

                    # Table untuk Dynamic Programming
                    table = [[-1 for i in range (capacity+1)] for j in range(len(price)+1)]
                    
                    # Function Knapsack menggunakan Dynamic Programming
                    def knapsack(weight, price, capacity, n):
                        
                        if n == 0 or capacity == 0:
                            return 0

                        if table[n][capacity] != -1:
                            return table[n][capacity]

                        if weight[n-1] <= capacity:
                            table[n][capacity] = max(price[n - 1] + knapsack(weight, price, capacity - weight[n-1], n - 1),
                            knapsack(weight, price, capacity, n - 1))
                            return table[n][capacity]

                        elif weight[n-1] > capacity:
                            table[n][capacity] = knapsack(weight, price, capacity, n - 1)
                            return table[n][capacity]

                    value = knapsack(weight, price, capacity, n=len(price))
                    harga = value
                    thingsItems = []
                    thingsWeight = []
                    thingsPrice = []
                    idx = capacity

                    # Mengambil data barang yang diambil
                    for i in range(len(price), 0, -1):
                        if value <= 0:
                            break
                        if value == table[i - 1][idx]:
                            continue
                        else:
                            pickItems = items[i - 1]
                            pickWeight = weight[i - 1]
                            pickPrice = price[i - 1]
                            thingsItems.append(pickItems)
                            thingsWeight.append(pickWeight)
                            thingsPrice.append(pickPrice)

                            value = value - price[i - 1]
                            idx = idx - weight[i - 1]

                    date = dt.datetime.now().strftime('%d/%m/%Y/%H:%M:%S')
                    while True:
                        os.system('cls')
                        print(f'DENGAN {txt} PACK'.center(leng))
                        print("ANDA AKAN MENDAPATKAN BARANG".center(leng))
                        print('_'*leng)

                        print()
                        print('-'*leng)
                        print(
                            f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+15}}| {"HARGA":^{maksPrice+15}}')
                        print('-'*leng)
                        no = 1
                        
                        for i in range(len(thingsItems)):
                            print(
                                f'{no:<3}| {str(thingsItems[i]):<{maksItems+5}}| {str(thingsWeight[i]):<{maksWeight+15}}| {str(thingsPrice[i]):<{maksPrice+15}}')
                            no += 1
                        print('-'*leng)
                        print(
                            f'{"":<3} {"TOTAL PESANAN  ":>{maksItems+6}}| {str(sum(thingsWeight)):<{maksWeight+15}}| {str(harga):<{maksPrice+15}}')
                                    
                        inputUser = input("\nBuat Pesanan[y/t] ? ")

                        if inputUser == "y":
                            # Menambahkan data barang ke file csv (daftarPesanan.csv)
                            name = str(input("\nPesanan atas Nama : "))
                            with open(csvPemesanan, 'a', newline='') as csv_file:
                                fieldnames = ['tanggal','nama', 'pesanan', 'harga','kapasitas','status']
                                write = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
                                write.writerow({'tanggal': date,'nama': name,'pesanan': list(thingsItems), 'harga': harga,'kapasitas': int(capacity), 'status': "Dikemas"})
                            
                            os.system('cls')
                            print(f'DENGAN {txt} PACK'.center(leng))
                            print("ANDA AKAN MENDAPATKAN BARANG".center(leng))
                            print('_'*leng)

                            print()
                            print('-'*leng)
                            print(
                                f'{"NO":^3}| {"BARANG":^{maksItems+5}}| {"BERAT":^{maksWeight+15}}| {"HARGA":^{maksPrice+15}}')
                            print('-'*leng)
                            no = 1
                            
                            for i in range(len(thingsItems)):
                                print(
                                    f'{no:<3}| {str(thingsItems[i]):<{maksItems+5}}| {str(thingsWeight[i]):<{maksWeight+15}}| {str(thingsPrice[i]):<{maksPrice+15}}')
                                no += 1
                            print('-'*leng)
                            print(
                                f'{"":<3} {"TOTAL PESANAN  ":>{maksItems+6}}| {str(sum(thingsWeight)):<{maksWeight+15}}| {str(harga):<{maksPrice+15}}')
                            
                            print("\nPesanan berhasil di simpan!!")
                            input("Tekan Enter untuk Kembali...")
                            break

                        elif inputUser == "t":
                            break

                        else:
                            print('input yang anda masukkan salah!')
                            input('Tekan enter untuk input kembali..')
            except:
                print('input yang anda masukkan salah!')
                input('Tekan enter untuk input kembali..')


# MENU [2] LIHAT DATA PESANAN
def lihatData():
    
    with open(csvPemesanan, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        show = list(reader)

        maksDate, maksName, maksOrder, maksPrice, maksCapacity, maksStatus = 0, 0, 0, 0, 0, 0

        for i in range(len(show)):
            if len(show[i]['tanggal']) > maksDate:
                maksDate = len(show[i]['tanggal'])
            if len(show[i]['nama']) > maksName:
                maksName = len(show[i]['nama'])
            if len(show[i]['pesanan']) > maksOrder:
                maksOrder = len(show[i]['pesanan'])
            if len(show[i]['harga']) > maksPrice:
                maksPrice = len(show[i]['harga'])
            if len(show[i]['kapasitas']) > maksCapacity:
                maksCapacity = len(show[i]['kapasitas'])
            if len(show[i]['status']) > maksStatus:
                maksStatus = len(show[i]['status'])
        leng = maksDate+maksName+maksOrder+maksPrice+maksCapacity+maksStatus+41

        os.system("cls")
        print("DAFTAR PESANAN".center(leng))
        print("TERAKHIR YANG ANDA BUAT".center(leng))
        print('_'*leng)

        print()
        print('-'*leng)
        print(
            f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
        print('-'*leng)
        
        while True:
            if len(show) <= 0:
                print("BELUM ADA PESANAN")
                input("Tekan Enter untuk Kembali...")
            
            else:
                no = 1
                for row in show:
                    print(
                        f'{no:<3}| {row["tanggal"]:<{maksDate+5}}| {row["nama"]:<{maksName+5}}| {row["pesanan"]:<{maksOrder+2}}| {row["harga"]:<{maksPrice+5}}| {row["kapasitas"]:<{maksCapacity+5}}| {row["status"]:<{maksStatus+5}}')
                    no += 1
                print('-'*leng)
                input("\nTekan Enter Untuk Kembali...")
            break


# MENU [3] MENU ADMIN
def admin():

    os.system('cls')
    with open(authAdmin, 'r') as json_file:
        data = json.load(json_file)

        x = True
        while x:
            os.system('cls')
            print(f'{"Login Admin":^{40}}')
            print('='*40, '\n')
            print('Input 0 untuk kembali..\n')
            username = input('Username : ')
            password = input('Password : ')

            # Masuk menggunakan data admin yang ada di file json (loginAdmin.json)
            for row in data:
                if username == row['username'] and password == row['password']:
                    os.system('cls')
                    print(f'{"MENU ADMIN":^{40}}')
                    print(f'{"APLIKASI PICK PACK":^{40}}')
                    print('='*40)
                    input(f"\n\n{'Hello, '+row['username']+'!':^40}")

                    while x:
                        os.system('cls')
                        print(f'{"MENU ADMIN":^{40}}')
                        print(f'{"APLIKASI PICK PACK":^{40}}')
                        print('='*40)
                        print("[1] Tampilkan Data")
                        print("[2] Hapus Data")
                        print("[3] Ubah Data")
                        print("[4] Login")

                        print("\n[0] Logout")
                        menu = input("PILIH MENU> ")
                        print("\n")

                        if menu == '1':
                            menuShowData()
                        elif menu == '2':
                            menuDeleteData()
                        elif menu == '3':
                            menuUpdateData()
                        elif menu == '4':
                            menuLoginAdmin()
                        elif menu == '0':
                            input('Logout sebagai admin..')
                            x = False
                            break
                        else:
                            print("Pilihan menu tidak tersedia!")
                            input(
                                'Tekan Enter untuk memilih menu kembali..')
                elif username == "0" and password == "0":
                    x = False            
                    break


# SUBMENU [1] Tampilkan Data Pesanan
def menuShowData():

    while True:
        os.system('cls')
        print("MENU TAMPILKAN".center(40))
        print("DATA PEMESANAN BARANG".center(40))
        print('='*40)
        print("[1] Lihat data Pemesanan")
        print("[2] Pesananan Dibatalkan")

        print("\n[0] Kembali")
        menu = input("PILIH MENU> ")
        print("\n")

        if menu == '1':
            lihatData() # Menggunakan Function yang digunakan pada menu [2] Lihat Data

        elif menu == '2':
            showDataDel() # Menggunakan Function showDataDel

        elif menu == '0':
            break
        else:
            print("Pilihan menu tidak tersedia!")
            input('Tekan enter untuk memilih menu kembali..')


# Menampilkan Data Pesanan yang Dibatalkan dari file csv (daftarHapus.csv)
def showDataDel():

    os.system('cls')
    with open(csvHapus) as csv_file:

        reader = csv.DictReader(csv_file, delimiter=";")
        show = list(reader)
        maksDate, maksName, maksOrder, maksPrice, maksCapacity, maksStatus = 0, 0, 0, 0, 0, 0

        for i in range(len(show)):
            if len(show[i]['tanggal']) > maksDate:
                maksDate = len(show[i]['tanggal'])
            if len(show[i]['nama']) > maksName:
                maksName = len(show[i]['nama'])
            if len(show[i]['pesanan']) > maksOrder:
                maksOrder = len(show[i]['pesanan'])
            if len(show[i]['harga']) > maksPrice:
                maksPrice = len(show[i]['harga'])
            if len(show[i]['kapasitas']) > maksCapacity:
                maksCapacity = len(show[i]['kapasitas'])
            if len(show[i]['status']) > maksStatus:
                maksStatus = len(show[i]['status'])
        leng = maksDate+maksName+maksOrder+maksPrice+maksCapacity+maksStatus+41
        
        print("DAFTAR PESANAN".center(leng))
        print("PELANGGAN YANG DIBATALKAN".center(leng))
        print('_'*leng)

        print()
        print('-'*leng)
        print(
            f'{"NO":^3}| {"TANGGAL":^{maksDate+2}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
        print('-'*leng)
        
        while True:
            if len(show) <= 0:
                print("BELUM ADA PESANAN")
                input("Tekan Enter untuk Kembali...")
            
            else:
                no = 1
                for row in show:
                    print(
                        f'{no:<3}| {row["tanggal"]:<{maksDate+2}}| {row["nama"]:<{maksName+5}}| {row["pesanan"]:<{maksOrder+2}}| {row["harga"]:<{maksPrice+5}}| {row["kapasitas"]:<{maksCapacity+5}}| {row["status"]:<{maksStatus+5}}')
                    no += 1
                print('-'*leng)
                input("\nTekan Enter Untuk Kembali...")
            break


# SUBMENU [2] HAPUS DATA PESANAN
def menuDeleteData():

    data = []
    out = []
    x = True

    with open(csvPemesanan) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        show = list(csv_reader)

        for row in show:
            data.append(row)

        maksDate, maksName, maksOrder, maksPrice, maksCapacity, maksStatus = 0, 0, 0, 0, 0, 0

        for i in range(len(show)):
            if len(show[i]['tanggal']) > maksDate:
                maksDate = len(show[i]['tanggal'])
            if len(show[i]['nama']) > maksName:
                maksName = len(show[i]['nama'])
            if len(show[i]['pesanan']) > maksOrder:
                maksOrder = len(show[i]['pesanan'])
            if len(show[i]['harga']) > maksPrice:
                maksPrice = len(show[i]['harga'])
            if len(show[i]['kapasitas']) > maksCapacity:
                maksCapacity = len(show[i]['kapasitas'])
            if len(show[i]['status']) > maksStatus:
                maksStatus = len(show[i]['status'])
        leng = maksDate+maksName+maksOrder+maksPrice+maksCapacity+maksStatus+41

        while x:
            os.system("cls")
            print("MENU DELETE".center(leng))
            print("PESANAN PELANGGAN".center(leng))
            print('_'*leng)

            print()
            print('-'*leng)
            print(
                f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
            print('-'*leng)

            if len(data) <= 0:
                print('BELUM ADA DATA')
                input('\nTekan Enter untuk kembali..')
                break

            elif len(data) > 0:
                with open(csvPemesanan) as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=';')
                    show = list(csv_reader)
                    no = 1
                    for row in show:
                        print(
                            f'{no:<3}| {row["tanggal"]:<{maksDate+5}}| {row["nama"]:<{maksName+5}}| {row["pesanan"]:<{maksOrder+2}}| {row["harga"]:<{maksPrice+5}}| {row["kapasitas"]:<{maksCapacity+5}}| {row["status"]:<{maksStatus+5}}')
                        no += 1
                    print('-'*leng)

                try:
                    while x:
                        print('\n0 > Kembali ke menu')
                        index = int(input("Hapus no data > "))

                        if index == 0:
                            x = False
                        elif 0 < index <= len(data):
                            index -= 1
                            while True:
                                os.system('cls')
                                print()
                                print('-'*leng)
                                print(
                                    f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
                                print('-'*leng)
                                print(
                                    f'{"1":<3}| {show[index]["tanggal"]:<{maksDate+5}}| {show[index]["nama"]:<{maksName+5}}| {show[index]["pesanan"]:<{maksOrder+2}}| {show[index]["harga"]:<{maksPrice+5}}| {show[index]["kapasitas"]:<{maksCapacity+5}}| {show[index]["status"]:<{maksStatus+5}}')
                                print('-'*leng)
                                command = input(f'Apakah anda yakin ingin menghapus pesanan atas Nama "{data[index]["nama"]}"? [y/t] : ')
                                
                                if command == 'y':
                                    os.system('cls')
                                    print()
                                    print('-'*leng)
                                    print(
                                        f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
                                    print('-'*leng)
                                    print(
                                        f'{"1":<3}| {show[index]["tanggal"]:<{maksDate+5}}| {show[index]["nama"]:<{maksName+5}}| {show[index]["pesanan"]:<{maksOrder+2}}| {show[index]["harga"]:<{maksPrice+5}}| {show[index]["kapasitas"]:<{maksCapacity+5}}| {show[index]["status"]:<{maksStatus+5}}')
                                    print('-'*leng)
                                    print('\n')

                                    out.append(data.pop(index)) # Menghapus Data yang dipilih
                                    print("\nData diatas sudah terhapus")
                                    input('Tekan enter untuk kembali..')
                                    
                                    # Menulis Kembali File csv (daftarPesanan.csv)
                                    with open(csvPemesanan, 'w', newline='') as csv_file:
                                        fieldnames = ['tanggal', 'nama', 'pesanan', 'harga','kapasitas', 'status']
                                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
                                        writer.writeheader()
                                        for newData in data:
                                            writer.writerow(
                                                {'tanggal': newData['tanggal'],
                                                'nama': newData['nama'],
                                                'pesanan': newData['pesanan'],
                                                'harga': newData['harga'],
                                                'kapasitas': newData['kapasitas'],
                                                'status': newData['status']})

                                    # Menambahkan File yang dihapus ke file csv (daftarHapus.csv)
                                    with open(csvHapus, 'a', newline='') as csv_file:
                                        fieldnames = ['tanggal', 'nama', 'pesanan', 'harga', 'kapasitas', 'status']
                                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
                                        date = dt.datetime.now().strftime('%d/%m/%Y/%H:%M:%S')
                                        for newData in out:
                                            writer.writerow(
                                                {'tanggal': date,
                                                'nama': newData['nama'],
                                                'pesanan': newData['pesanan'],
                                                'harga': newData['harga'],
                                                'kapasitas': newData['kapasitas'],
                                                'status': "Dibatalkan"})
                                    break
                                elif command == 't':
                                    break
                                else:
                                    print('Input yang anda masukkan salah')
                                    input('Tekan enter untuk input kembali..')
                            break
                        elif index > len(data) or index < 0:
                            print('No data tidak tersedia, silahkan input kembali')
                            input('Tekan enter untuk input kembali...')
                            break
                        else:
                            print('Input yang anda masukkan salah')
                            input('Tekan enter untuk input kembali...')
                except:
                    print('Input yang anda masukkan salah')
                    input('Tekan enter untuk input kembali...')


# SUBMENU [3] UBAH DATA PESANAN
def menuUpdateData():

    while True:
        os.system('cls')
        with open(csvPemesanan) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            show = list(reader)

            maksDate, maksName, maksOrder, maksPrice, maksCapacity, maksStatus = 0, 0, 0, 0, 0, 0

            for i in range(len(show)):
                if len(show[i]['tanggal']) > maksDate:
                    maksDate = len(show[i]['tanggal'])
                if len(show[i]['nama']) > maksName:
                    maksName = len(show[i]['nama'])
                if len(show[i]['pesanan']) > maksOrder:
                    maksOrder = len(show[i]['pesanan'])
                if len(show[i]['harga']) > maksPrice:
                    maksPrice = len(show[i]['harga'])
                if len(show[i]['kapasitas']) > maksCapacity:
                    maksCapacity = len(show[i]['kapasitas'])
                if len(show[i]['status']) > maksStatus:
                    maksStatus = len(show[i]['status'])
            leng = maksDate+maksName+maksOrder+maksPrice+maksCapacity+maksStatus+41

            os.system("cls")
            print("MENU UPDATE".center(leng))
            print("PESANAN PELANGGAN".center(leng))
            print('_'*leng)

            print()
            print('-'*leng)
            print(
                f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
            print('-'*leng)

            if len(show) <= 0:
                print(f'\n{"BELUM ADA DATA":^{leng}}')
                input('\n\nTekan enter untuk kembali..')
                break

            elif len(show) > 0:
                try:
                    with open(csvPemesanan) as csv_file:
                        csv_reader = csv.DictReader(csv_file, delimiter=';')
                        show = list(csv_reader)
                        no = 1
                        for row in show:
                            print(
                                f'{no:<3}| {row["tanggal"]:<{maksDate+5}}| {row["nama"]:<{maksName+5}}| {row["pesanan"]:<{maksOrder+2}}| {row["harga"]:<{maksPrice+5}}| {row["kapasitas"]:<{maksCapacity+5}}| {row["status"]:<{maksStatus+5}}')
                            no += 1
                        print('-'*leng)

                    print('\n0 > Kembali ke menu')
                    index = int(input("Update no data > "))

                    if index == 0:
                        break
                    elif 0 <= index <= len(show):
                        index -= 1
                        x = True
                        while x:
                            os.system('cls')
                            print()
                            print('-'*leng)
                            print(
                                f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
                            print('-'*leng)
                            print(
                                f'{"1":<3}| {show[index]["tanggal"]:<{maksDate+5}}| {show[index]["nama"]:<{maksName+2}}| {show[index]["pesanan"]:<{maksOrder+5}}| {show[index]["harga"]:<{maksPrice+5}}| {show[index]["kapasitas"]:<{maksCapacity+5}}| {show[index]["status"]:<{maksStatus+5}}')
                            print('-'*leng)
                            command = input(f'\nApakah anda yakin ingin mengupdate "{show[index]["nama"]}"? [y/n] : ')

                            if command == 'y':
                                while True:
                                    os.system("cls")
                                    print("MENU UPDATE".center(leng))
                                    print("PESANAN PELANGGAN".center(leng))
                                    print('_'*leng)

                                    print()
                                    print('-'*leng)
                                    print(
                                        f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
                                    print('-'*leng)
                                    print(
                                        f'{"1":<3}| {show[index]["tanggal"]:<{maksDate+5}}| {show[index]["nama"]:<{maksName+5}}| {show[index]["pesanan"]:<{maksOrder+2}}| {show[index]["harga"]:<{maksPrice+5}}| {show[index]["kapasitas"]:<{maksCapacity+5}}| {show[index]["status"]:<{maksStatus+5}}')
                                    print('-'*leng)

                                    print('[1] Nama')
                                    print('[2] Status')
                                    print('\n[0] Kembali')
                                    noUpdate = input('Pilih yang ingin di update : ')

                                    if noUpdate == '0':
                                        break

                                    # Update Nama
                                    elif noUpdate == '1':

                                        while True:
                                            command = input('Apakah anda yakin ingin mengupdate "Nama" ? [y/n] : ')
                                            if command == 'y':
                                                os.system('cls')
                                                print("MENU UPDATE".center(leng))
                                                print("PESANAN PELANGGAN".center(leng))
                                                print('_'*leng)

                                                print()
                                                print('-'*leng)
                                                print(
                                                    f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
                                                print('-'*leng)
                                                print(
                                                    f'{"1":<3}| {show[index]["tanggal"]:<{maksDate+5}}| {show[index]["nama"]:<{maksName+5}}| {show[index]["pesanan"]:<{maksOrder+2}}| {show[index]["harga"]:<{maksPrice+5}}| {show[index]["kapasitas"]:<{maksCapacity+5}}| {show[index]["status"]:<{maksStatus+5}}')
                                                print('-'*leng)

                                                show[index]['nama'] = input('Nama Pelanggan : ')
                                                print("\nData sudah terupdate")
                                                input('\nTekan enter untuk kembali..')
                                                break
                                            elif command == 'n':
                                                break
                                            else:
                                                print('Input yang anda masukkan salah')
                                                input('Tekan enter untuk input kembali..')
                                                break
                                    
                                    # Update Status Pesanan
                                    elif noUpdate == '2':

                                        while True:
                                            command = input('Apakah anda yakin ingin mengupdate "Status" ? [y/n] : ')
                                            if command == 'y':
                                                os.system('cls')
                                                print("MENU UPDATE".center(leng))
                                                print("PESANAN PELANGGAN".center(leng))
                                                print('_'*leng)

                                                print()
                                                print('-'*leng)
                                                print(
                                                    f'{"NO":^3}| {"TANGGAL":^{maksDate+5}}| {"NAMA":^{maksName+5}}| {"PESANAN":^{maksOrder+2}}| {"HARGA":^{maksPrice+5}}| {"KAPASITAS":^{maksCapacity+5}}| {"STATUS":^{maksStatus+5}}')
                                                print('-'*leng)
                                                print(
                                                    f'{"1":<3}| {show[index]["tanggal"]:<{maksDate+5}}| {show[index]["nama"]:<{maksName+5}}| {show[index]["pesanan"]:<{maksOrder+2}}| {show[index]["harga"]:<{maksPrice+5}}| {show[index]["kapasitas"]:<{maksCapacity+5}}| {show[index]["status"]:<{maksStatus+5}}')
                                                print('-'*leng)

                                                show[index]['status'] = input('Status : ')
                                                print("\nData sudah terupdate")
                                                input('\nTekan enter untuk kembali..')
                                                break
                                            elif command == 'n':
                                                break
                                            else:
                                                print('Input yang anda masukkan salah')
                                                input('Tekan enter untuk input kembali..')
                                                break
                                    else:
                                        print('Input yang anda masukkan salah')
                                        input('Tekan enter untuk input kembali..')

                                    # Menuliskan data terbaru ke file csv (daftarPesanan.csv)
                                    with open(csvPemesanan, 'w', newline='') as csv_file:
                                        fieldnames = ['tanggal', 'nama', 'pesanan', 'harga','kapasitas', 'status']
                                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
                                        writer.writeheader()
                                        for newData in show:
                                            writer.writerow(
                                                {'tanggal': newData['tanggal'],
                                                'nama': newData['nama'],
                                                'pesanan': newData['pesanan'],
                                                'harga': newData['harga'],
                                                'kapasitas': newData['kapasitas'],
                                                'status': newData['status']})
                                break
                            elif command == 'n':
                                x = False

                            else:
                                print('Input yang anda masukkan salah')
                                input('Tekan enter untuk input kembali..')

                    elif index > len(show) or index < 0:
                        print(
                            'No data tidak tersedia, silahkan input kembali\n')
                    else:
                        print('Input yang anda masukkan salah')
                        input('Tekan enter untuk input kembali..')

                except:
                    print('Input yang anda masukkan salah')
                    input('Tekan enter untuk input kembali..')


# SUBMENU [4] LOGIN ADMIN
def menuLoginAdmin():

    while True:
        os.system('cls')
        print(f'{"MENU":^40}')
        print(f'{"LOGIN ADMIN":^40}')
        print('='*40)
        print("[1] Tampilkan Data Admin")
        print("[2] Tambah Data Admin")
        print("[3] Hapus Data Admin")
        print("[4] Ubah Data Admin")

        print("\n[0] Kembali")
        menu = input("PILIH MENU> ")
        print("\n")

        if menu == '1':
            showDataAdmin()
        elif menu == '2':
            insertDataAdmin()
        elif menu == '3':
            deleteDataAdmin()
        elif menu == '4':
            updateDataAdmin()
        elif menu == '0':
            break
        else:
            print("Pilihan menu tidak tersedia!")


# Menampikan Data Username dan Password admin dari file json (loginAdmin.json)
def showDataAdmin():

    os.system('cls')
    with open(authAdmin, 'r') as json_file:
        data = json.load(json_file)

        username, password = 15, 15
        leng = username+password+24
        print('Data Admin'.center(leng))
        print('_'*leng)
        print('\n')

        no = 1
        if len(data) <= 0:

            print('BELUM ADA DATA')
            input('\nTekan Enter untuk kembali..')

        elif len(data) > 0:
            print('-'*leng)
            print(
                f'{"NO":^3}| {"USERNAME":^{username+5}}| {"PASSWORD":^{password+12}}')
            print('-'*leng)
            for row in data:
                print(
                    f'{no:^3}| {row["username"]:<{username+5}}| {row["password"]:<{password+5}}')
                no += 1
            print('-'*leng)

            input('\nTekan Enter untuk kembali..')


# Menambahkan data Admin baru 
def insertDataAdmin():

    os.system('cls')
    data = []
    with open(authAdmin, 'r') as json_file:
        data = json.load(json_file)
        titleMK1 = "ADD ADMIN"
        print(titleMK1.center(40))
        print('_'*40)
        print('\n')
        dw = {'username': input("username : "),
              'password': input("password : ")}
        data.append(dw)

    # Menambahkan Username dan Password ke file json (loginAdmin.json)
    with open(authAdmin, 'w') as json_file:
        json.dump(data, json_file,indent=2)
        print("\nBerhasil disimpan!")
        input('Tekan enter untuk kembali..')


# Menghapus data Admin dari file json (loginAdmin.json)
def deleteDataAdmin():

    os.system('cls')
    data = []
    with open(authAdmin, 'r') as json_file:
        data = json.load(json_file)

        username, password = 0, 0
        for i in range(len(data)):
            if len(data[i]['username']) > username:
                username = len(data[i]['username'])
            if len(data[i]["password"]) > password:
                password = len(data[i]["password"])
        leng = username+password+25

        while True:
            os.system('cls')
            print(f'{"DELETE ADMIN":^{leng}}')
            print('_'*leng, '\n')
            print(f'{"NO":^3}| {"USERNAME":^{username+5}}| {"PASSWORD":^{password}}')
            print('-'*leng)
            no = 1
            if len(data) <= 0:

                print('BELUM ADA DATA')
                input('\nTekan Enter untuk kembali..')

            elif len(data) > 0:
                for row in data:
                    print(
                        f'{no:<3}| {row["username"]:<{username+5}}| {row["password"]:<{password+5}}')
                    no += 1
                print('-'*leng)

                try:
                    print('\n0 > Kembali ke menu')
                    index = int(input("Hapus no data > "))
                    if index == 0:
                        break
                    elif 0 < index <= len(data):
                        index -= 1
                        while True:
                            os.system('cls')
                            print(f'{"DELETE ADMIN":^{leng}}')
                            print('_'*leng, '\n')
                            print(f'{"NO":^3}| {"USERNAME":^{username+5}}| {"PASSWORD":^{password}}')
                            print('-'*leng)
                            no = 1
                            for row in data:
                                print(f'{no:<3}| {row["username"]:<{username+5}}| {row["password"]:<{password+5}}')
                                no += 1
                            print('-'*leng, '\n')
                            answer = input(f'Apakah anda yakin ingin menghapus "{data[index]["username"]}" ? [y/n] : ')
                            if answer == 'y':

                                data.remove(data[index]) # Meghapus data yang dipilih
                                print("\nData sudah terhapus")
                                input('Tekan enter untuk kembali..')

                                # Menulis ulang file json (loginAdmin.json)
                                with open(authAdmin, 'w') as json_file:
                                    json.dump(data, json_file)

                                break
                            elif answer == 'n':
                                break
                            else:
                                print('Input yang anda masukkan salah')
                                input('Tekan enter untuk input kembali..')

                    elif index > len(data) or index < 0:
                        print('No data tidak tersedia, silahkan input kembali\n')
                except:
                    print('Input yang anda masukkan salah')
                    input('Tekan enter untuk input kembali..')


# Mengubah data Username/Password Admin
def updateDataAdmin():

    os.system('cls')
    with open(authAdmin, 'r') as json_file:
        data = json.load(json_file)

        username, password = 0, 0
        for i in range(len(data)):
            if len(data[i]['username']) > 0:
                username = len(data[i]['username'])
            if len(data[i]['password']) > 0:
                password = len(data[i]['password'])

        pluss = 25
        leng = username+password+pluss
        x = True
        while x:
            os.system('cls')
            print(f'{"UPDATE ADMIN":^{leng}}')
            print('_'*leng, '\n')
            print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
            print('-'*leng)

            if len(data) <= 0:
                print('BELUM ADA DATA')
                input('\nTekan Enter untuk kembali..')

            elif len(data) > 0:
                no = 1
                for row in data:
                    print(
                        f'{no:<3}| {row["username"]:<{username+7}}| {row["password"]:<{password+5}}')
                    no += 1
                print('-'*leng)
                try:
                    print('\n0 > Kembali ke menu')
                    index = int(input("Update no data > "))
                    if index == 0:
                        break
                    elif 0 <= index <= len(data):
                        index -= 1
                        y = True
                        while y:
                            os.system('cls')
                            print(f'{"UPDATE ADMIN":^{leng}}')
                            print('_'*leng, '\n')
                            print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
                            print('-'*leng)
                            print(f'{"1":<3}| {data[index]["username"]:<{username+7}}| {data[index]["password"]:<{password+5}}')
                            print('-'*leng)
                            command = input(f'\nApakah anda yakin ingin mengupdate data diatas? [y/n] : ')
                            
                            try:
                                if command == 'y':
                                    while y:
                                        os.system('cls')
                                        print(f'{"UPDATE ADMIN":^{leng}}')
                                        print('_'*leng, '\n')
                                        print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
                                        print('-'*leng)
                                        print(f'{"1":<3}| {data[index]["username"]:<{username+7}}| {data[index]["password"]:<{password+5}}')
                                        print('-'*leng)
                                        print('\n[1] Username')
                                        print('[2] Password')
                                        print('\n[0] Kembali')
                                        noUpdate = input('Pilih yang ingin di update : ')

                                        if noUpdate == '0':
                                            y = False
                                            x = True

                                        elif noUpdate == '1':
                                            while True:
                                                os.system('cls')
                                                print(f'{"UPDATE ADMIN":^{leng}}')
                                                print('_'*leng, '\n')
                                                print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
                                                print('-'*leng)
                                                print(f'{"1":<3}| {data[index]["username"]:<{username+7}}| {data[index]["password"]:<{password+5}}')
                                                print('-'*leng)
                                                print('\n[1] Username')
                                                print('[2] Password')
                                                print('\n[0] Kembali')

                                                command = input('Apakah anda yakin ingin mengupdate "Username" ? [y/n] : ')
                                                    
                                                if command == 'y':
                                                    os.system('cls')
                                                    print(f'{"UPDATE ADMIN":^{leng}}')
                                                    print('_'*leng, '\n')
                                                    print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
                                                    print('-'*leng)
                                                    print(f'{"1":<3}| {data[index]["username"]:<{username+7}}| {data[index]["password"]:<{password+5}}')
                                                    print('-'*leng)
                                                    print('\n')

                                                    data[index]['username'] = input('New Username : ')

                                                    # Menuliskan kembali Username Baru ke file json (loginAdmin.json)
                                                    with open(authAdmin, 'w') as json_file:
                                                        json.dump(data, json_file)
                                                        print("\nData sudah terupdate")
                                                        input('\nTekan enter untuk kembali..')
                                                    x = False
                                                    y = True
                                                    break

                                                elif command == 'n':
                                                    break

                                                else:
                                                    print('Input yang anda masukkan salah')
                                                    input('Tekan enter untuk input kembali..')

                                        elif noUpdate == '2':
                                            while True:
                                                os.system('cls')
                                                print(f'{"UPDATE ADMIN":^{leng}}')
                                                print('_'*leng, '\n')
                                                print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
                                                print('-'*leng)
                                                print(f'{"1":<3}| {data[index]["username"]:<{username+7}}| {data[index]["password"]:<{password+5}}')
                                                print('-'*leng)
                                                print('\n[1] Username')
                                                print('[2] Password')
                                                print('\n[0] Kembali')
                                                command = input('Apakah anda yakin ingin mengupdate "Password" ? [y/n] : ')

                                                if command == 'y':
                                                    os.system('cls')
                                                    print(f'{"UPDATE ADMIN":^{leng}}')
                                                    print('_'*leng, '\n')
                                                    print(f'{"NO":^3}| {"USERNAME":^{username+7}}| {"PASSWORD":^{password}}')
                                                    print('-'*leng)
                                                    print(f'{"1":<3}| {data[index]["username"]:<{username+7}}| {data[index]["password"]:<{password+5}}')
                                                    print('-'*leng)
                                                    print('\n')

                                                    data[index]['password'] = input('New Password : ')

                                                    # Menuliskan Kembali Password Baru ke file json (loginAdmin.json)
                                                    with open(authAdmin, 'w') as json_file:
                                                        json.dump(data, json_file)
                                                        print("\nData sudah terupdate")
                                                        input('\nTekan enter untuk kembali..')
                                                    x = False
                                                    y = True
                                                    break
                                                elif command == 'n':
                                                    break
                                                else:
                                                    print('Input yang anda masukkan salah')
                                                    input('Tekan enter untuk input kembali..')
                                        else:
                                            print('Input yang anda masukkan salah')
                                            input('Tekan enter untuk input kembali..')

                                elif command == 'n':
                                    break
                                else:
                                    print('Input yang anda masukkan salah')
                                    input('Tekan enter untuk input kembali..')
                            except:
                                pass

                    elif index > len(data) or index < 0:
                        print('No data tidak tersedia, silahkan input kembali')
                        input('Tekan enter untuk input kembali..')
                    else:
                        print('Input yang anda masukkan salahh')
                        input('Tekan enter untuk input kembali..')
                except:
                    print('Input yang anda masukkan salah')
                    input('Tekan enter untuk input kembali..')


# Perulangan Untuk Menu Utama
while True:
    show_menu()