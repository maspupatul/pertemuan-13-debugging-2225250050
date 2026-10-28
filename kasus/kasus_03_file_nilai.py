
def baca_nilai(nama_file):
    with open(nama_file, "r") as file:
        nilai = []

        for baris in file:
            nilai.append(int(baris.strip()))

    return nilai


data = baca_nilai("data_nilai.txt")
print("Data nilai:", data)
print("Rata-rata:", sum(data) / len(data))
