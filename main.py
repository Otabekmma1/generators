###-------------------- FOR 1 ----------------------------

# k, n = int(input("Sonni kiriting: ")), int(input("k son nechi marta chiqarilsin? "))
# num = [k for i in range(n)]
# print(num)

##--------------------- FOR 2 -------------------------------

# a, b = int(input("a sonni kiriting: ")), int(input("b sonni kiriting: "))
# if a < b:
#     result = [i for i in range(a, b+1)]
# else:
#     result = "a soni b sonidan kichik bo'lishi kerak!"
# print(result)

##---------------------- FOR 3 -------------------------

# a, b = int(input("a sonni kiriting: ")), int(input("b sonni kiriting: "))
# if a < b:
#     result = [i for i in sorted(range(a+1, b), reverse=True)]
# else:
#     result = "a soni b sonidan kichik bo'lishi kerak!"
# print(result)

##------------------ FOR 4 -----------------------

# kg = int(input("Konfet narxini kiriting: "))
# num = [f"{i}kg = {i * kg}$" for i in range(1, 11)]
# print(num)

##---------------- FOR 5 ----------------------

# word = "hello world"
# letters = [i.upper() for i in word]
# print(letters)

##------------- FOR 6 -------------------------

# word = 'HeLlo wORlD'
# big_letters = []
# smal_letters = []
# letters = [big_letters.append(i) if i.isupper() else smal_letters.append(i) for i in word]
# print(f"{word} so'zidagi \n"
#       f"Kichkina harflar: {smal_letters}\n"
#       f"Katta harflar: {big_letters}")

##------------ FOR 7 ------------------------

# number = [i ** 3 for i in range(1, 21)]
# print(number)

## --------- FOR 8 --------------

# number = [i // 2 for i in range(1, 21) if i % 2 == 0]
# print(number)

##-------------- FOR 9 ----------------------

# num = [(i, i**2) for i in range(1, 11)]
# print(dict(num))

##------------ FOR 10 ---------------------

# word = 'salom dunyo'
# letters = [(i, i.upper()) for i in word.replace(' ', '')]
# print(dict(letters))
