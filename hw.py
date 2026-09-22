# 1.masala

# for i in range(1,6):
#     for j in range(1, 11):
#         print(f"{i}x{j}={i*j}")

# 2.masala

# matritsa = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3):
#         print(matritsa[i][j])

# 3.masala

# for i in range(6):
#     for j in range(1):
#         print("*"*i)

# 4.masala

# shaharlar = ["Toshkent", "Samarqand", "Buxoro", "Andijon", "Xiva"]
# for i, shahar in enumerate(shaharlar, start=1):
#     print(f"{i}, {shahar}")


# 5.masala
# mahsulotlar = ["Noutbuk", "Telefon", "Planshet", "Monitor"]
# narxlar = [4500000, 2500000, 1800000, 1200000]

# for nom, narx in zip(mahsulotlar, narxlar):
#     print(f"{nom} — {narx} so'm")

# 6.masala

# ism = ["Aziz", "Nodira", "Bekzod", "Dilshod"]
# yosh = [25, 30, 22, 28]
# shahar = ["Toshkent", "Samarqand", "Buxoro", "Andijon"]

# for ism , yosh, shahar, in zip(ism, yosh, shahar):
#     print(f"{ism}-{yosh}-{shahar}")


# 7.masala

# kublar = []
# for son in range(1, 11):
#     kublar.append(son ** 3)
# print(kublar)

# 8.masala
# Berilgan gap
gap =input("ixtiyoriy gap kiriting")

# So'zlarni ajratamiz
sozlar = gap.split()

uzun_sozlar = []
for soz in sozlar:
    if len(soz) > 5:
        uzun_sozlar.append(soz)

print(uzun_sozlar)


# 9.masala
# kublar = [son ** 3 for son in range(1, 15)]
# print(kublar)


