print("""
Task :
    Hitung Selisih Umur Keluarga dengan Label!
    - Bapak vs Ibu
    - Bapak vs Abang, dst..
""")

ages = [
    45,
    30,
    20,
    10
]

label = [
    "Bapak",
    "Ibu",
    "Abang",
    "Adik"
]

def hitung(id_1, id_2):
    selisih = ages[id_1] - ages[id_2]
    "'Bapak vs Ibu' :"
    print("'%s vs %s' : %s" % (label[id_1], label[id_2], selisih))


for person_1_id in [0, 1, 2]:
    for person_2_id in [0, 1, 2, 3]:
        if person_1_id < person_2_id:
            hitung(person_1_id, person_2_id)
