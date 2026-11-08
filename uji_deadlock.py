# uji_deadlock.py — UTS Sistem Operasi Level 5
# Jalankan:  timeout 10 python3 uji_deadlock.py <NIM> buntu ; echo "exit=$?"
#            timeout 10 python3 uji_deadlock.py <NIM> urut  ; echo "exit=$?"
import sys, socket, threading, time
nim, mode = sys.argv[1], sys.argv[2]
R1, R2 = threading.Lock(), threading.Lock()

def proses(nama, pertama, kedua):
    if mode == "urut":                       # pencegahan: urutan global
        pertama, kedua = sorted([pertama, kedua], key=id)
    with pertama:
        print(f"{nama} memegang sumber daya pertama"); time.sleep(0.5)
        with kedua:
            print(f"{nama} memegang keduanya, selesai")

a = threading.Thread(target=proses, args=(f"P-{nim[-2:]}a", R1, R2))
b = threading.Thread(target=proses, args=(f"P-{nim[-2:]}b", R2, R1))
print(f"{socket.gethostname()} | NIM {nim} | mode={mode}")
a.start(); b.start(); a.join(); b.join()
print("SEMUA PROSES SELESAI")
