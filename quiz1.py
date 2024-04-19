n=9
if (n%2==0):
    print ("the num is even")
else:
    print ("the num is odd")



    import os

folder_path = "Lab4"


if os.path.exists(folder_path):
    print(f"Содержимое папки {folder_path}:")
    
    contents = os.listdir(folder_path)
    for item in contents:
        print(item)
else:
    print(f"Папка {folder_path} не существует.")




    # Генератор для всех двухзначных чисел, у которых первая цифра больше второй
def two_digit_numbers():
    for i in range(1, 10):  
        for j in range(0, i):  
            yield int(str(i) + str(j))  


for number in two_digit_numbers():
    print(number)
