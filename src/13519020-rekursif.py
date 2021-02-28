# Nama  : Muhammad Azhar Faturahman
# NIM   : 13519020
# Kelas : K1

# TUGAS KECIL 1
# IF2211 STRATEGI ALGORITMA

# --- TOPOPGRAPICAL SORT --- #
# Implementasi graph menggunakan adjacent list

## LIBRARY


## KAMUS GLOBAL
graphMatkul = {}
urutanMatkul = []
daftarSemester = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV"]  # Hardcode it's de way, lebih dari ini DO!

## FUNGSI DAN MODUL

# Membaca input berupa file, mengembalikan waktu dimulainya program
def bacaFile(namaFile) :
    global graphMatkul
    
    try:
        alamatFile = "../test/" + namaFile
        f = open(alamatFile,'r')
        
        lines = f.readlines()
        # print(lines)
        
        i = 0
        while (i < len(lines)):
            clearLine = lines[i].replace("\n","")
            clearLine = clearLine.replace(".","")
            clearLine = clearLine.replace(", ",",")
            splitLine = clearLine.split(",")
            
            # Isi dictionary dengan keys splitLine[0] dan value splitLine[1:]
            if (len(splitLine) > 1):
                graphMatkul.update({splitLine[0]: splitLine[1:]})
            else:
                graphMatkul.update({splitLine[0]: []})
            
            i += 1
        
        f.close()
    except FileNotFoundError:
        print("\nError: File tidak ditemukan")


# Mengurutkan graph berdasarkan topograpical sort
def topSort(olahMatkul):
    global graphMatkul, urutanMatkul
    
    if len(olahMatkul) == 0:    # BASIS
        return 0    # DO NOTHING
    else:                       # REKURENS
        found = False

        # Cari matkul yang sudah tidak punya prerequisite
        for namaMatkul in olahMatkul:
            if len(olahMatkul[namaMatkul]) == 0:    # Jika matkul ini sudah tidak punya prerequisite
                found = True
                break                  
        
        if found:  
            urutanMatkul.append(namaMatkul)     # Tambah ke list matkul terurut
            olahMatkul.pop(namaMatkul)          # Hapus dari graph
            
            # Iterasi untuk hapus namaMatkul tersebut dari matkulLain
            for matkulLain in olahMatkul:
                    if namaMatkul in olahMatkul[matkulLain]:
                        # Note : olahMatkul[matkulLain] akan menghasilkan list prerequisite maktulLain tersebut
                        olahMatkul[matkulLain].remove(namaMatkul)
            
            topSort(olahMatkul)                 # Rekursi, ulang lagi dari awal untuk graph yang telah dikurangi (Decrease and Conquare)
        else:
            raise Exception("GraphError: Contains a cycle")
        
        
# Menampilkan hasil urutan pada layar               
def outputHasil():                                                             # Something I found : Sebenernya ini juga udah bisa toposort wkwkw, tinggal ubah metode looping matkul
    global graphMatkul, urutanMatkul, daftarSemester
                   
    # listMatkul = list(graphMatkul.keys()).copy()
    listMatkul = urutanMatkul.copy()
    pastSemester = []
    semester = 1
    
    while (len(pastSemester) != len(graphMatkul)):
        currSemester = []
        i = 0       # Iterator setiap matkul
        i = 0       # Iterator setiap matkul
        j = 0       # Penanda matkul terakhir yang dicek
        
        while(i < len(listMatkul)):             # Iterasi semua matkul yang masih tersedia
            matkul = listMatkul[i]
            prerequisite = graphMatkul[matkul].copy()
            
            valid = True    
            for preMatkul in prerequisite:      # Iterasi matkul prerequisite
                # Cek apakah sudah diambil di semester sebelumnya
                if preMatkul not in pastSemester:
                    valid = False
                    break
                # Cek apakah ada prerequisite diambil bersamaan
                elif preMatkul in currSemester:
                    valid = False
                    break
                
            if valid:   # Tambah ke semester sekarang dan hapus dari matkul tersedia
                currSemester.append(matkul)
                listMatkul.remove(matkul)
                i = j   # listMatkul sudah dimodifikasi, harus diulang dari cek terakhir
            else:
                i += 1  
                j = i      # Biar ga ngulang lagi loopnya dari awal
                
        if (semester-1 < len(daftarSemester)):    
            print(("Semester "+daftarSemester[semester-1]).ljust(13),end=": ")
            for i in range(len(currSemester)):
                if (i != len(currSemester) - 1):    # Bukan matkul terakhir disuatu semester
                    print(currSemester[i], end=", ")
                else:
                    print(currSemester[i])
            
            pastSemester = pastSemester + currSemester
            semester = semester + 1
        else:
            print("-- DO --")
            break
    
            
# MAIN PROGRAM            
        
def main():
    global graphMatkul, urutanMatkul
    
    print()
    print("--------------------------------------------")
    print("         --- TOPOPGRAPICAL SORT ---")
    print("--------------------------------------------")
    print("Created by : M Azhar Faturahman (13519020)")
    print()
    namaFile = input("Masukkan nama file: ")
    
    bacaFile(namaFile)
    olahMatkul = {key: value[:] for key, value in graphMatkul.items()}      # Dicopy dulu biar ga ngeubah yang global bray
    topSort(olahMatkul)
    
    print()
    print("--------------------------------------------")
    print("           --- HASIL SORTING ---")
    print("--------------------------------------------")
    # print(urutanMatkul)
    outputHasil()
    input("\nPress Enter to Continue...")
    
main()