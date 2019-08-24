print("""
Task :
    Hitung Selisih Umur Keluarga!
    - Bapak vs Ibu
    - Bapak vs Abang, dst..
""")

ages = [
    45,
    30,
    20,
    10
]


def hitung(orang_1, orang_2):
    selisih = orang_1 - orang_2
    print(selisih)

for person_1_id in [0, 1, 2]:
    for person_2_id in [0, 1, 2, 3]:
        if person_1_id < person_2_id:
            hitung(ages[person_1_id], ages[person_2_id])
