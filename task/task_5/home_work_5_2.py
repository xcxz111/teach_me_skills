# Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку.
# В качестве функции map использовать lambda.

spisok = [12, 24, 14, 544, 234]
var = list(map(lambda x: str(x), spisok))
print(var)