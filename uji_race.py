# uji_race.py — UTS Sistem Operasi Level 4
# Jalankan:  python3 uji_race.py <NIM> bahaya   lalu   python3 uji_race.py <NIM> aman
import sys, socket, threading, time, datetime
nim, mode = sys.argv[1], sys.argv[2]
A, B = int(nim[-2]), int(nim[-1])
T = 3 + A % 3                 # jumlah thread
ULANG = 2000                  # tiap thread mengurangi data sebanyak ini
data = {"X": T * ULANG + int(nim[-2:])}
kunci = threading.Lock()

def kerja():
    for _ in range(ULANG):
        if mode == "aman":
            with kunci:
                lama = data["X"]; time.sleep(0); data["X"] = lama - 1
        else:
            lama = data["X"]; time.sleep(0); data["X"] = lama - 1

ts = [threading.Thread(target=kerja) for _ in range(T)]
[t.start() for t in ts]; [t.join() for t in ts]
print(f"{socket.gethostname()} | NIM {nim} | {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
print(f"mode={mode} thread={T} nilai akhir X = {data['X']}")
