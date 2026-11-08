# buat_zombie.py — UTS Sistem Operasi Level 2
# Jalankan:  python3 buat_zombie.py <NIM> &
import os, sys, time, socket, threading
nim = sys.argv[1]
A, B = int(nim[-2]), int(nim[-1])
pid = os.fork()
if pid == 0:
    os._exit(0)                       # anak langsung selesai
for _ in range(2 + (10 * A + B) % 5): # thread pekerja induk
    threading.Thread(target=time.sleep, args=(900,), daemon=True).start()
print(f"[{socket.gethostname()}] NIM {nim}: induk PID {os.getpid()}, anak PID {pid}", flush=True)
# os.waitpid(pid, 0)                  # <-- baris perbaikan (Level 2c)
time.sleep(900)                       # induk tidak memanggil wait()
