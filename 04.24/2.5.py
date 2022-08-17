gor1 = (input())
ver1 = int(input())
gor2 = (input())
ver2 = int(input())
gors= "abcdefgh"
print("Нет" if (
                gors.find(gor1) + (ver1)
                +
                gors.find(gor2) + (ver2)
                ) % 2 else "Да")