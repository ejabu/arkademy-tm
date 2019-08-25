print("""
Task :
    Hitung Selisih Umur Keluarga dengan Label!
    - Bapak vs Ibu
    - Bapak vs Abang, dst..
""")

ages = {
    "Bapak" : 45,
    "Ibu": 30,
    "Abang" : 20,
    "Adik": 10,
}

def hitung(id_1, id_2):
    labels = list(ages.keys())
    selisih = ages[labels[id_1]] - ages[labels[id_2]]
    print("'%s vs %s' : %s" % (labels[id_1], labels[id_2], selisih))

for person_1_id in [0, 1, 2]:
    for person_2_id in [0, 1, 2, 3]:
        if person_1_id < person_2_id:
            hitung(person_1_id, person_2_id)
