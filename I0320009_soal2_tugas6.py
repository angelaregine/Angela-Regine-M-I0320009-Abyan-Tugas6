n = int(input("Banyaknya data: "))
jumlah = 0

for i in range(0, n):
    nilai = float(input("Nilai ujian ke-%d: " % (i + 1)))
    jumlah += nilai

rata_rata = jumlah / n
print("Nilai rata-rata = %0.2f" % rata_rata)