# Lesson 2

## Tür Dönüşümleri

`int()` fonksiyonu ile bir değişkenin türünü integer'a çevirebiliriz.

`str()` fonksiyonu ile bir değişkenin türünü string'e çevirebiliriz.

`float()` fonksiyonu ile bir değişkenin türünü float'a çevirebiliriz.

`bool()` fonksiyonu ile bir değişkenin türünü boolean'a çevirebiliriz.

`type()` fonksiyonu ile bir değişkenin türünü öğrenebiliriz.

## String Interpolation

`.format()` ile string içerisinde verilen değişkene sırayla erişebiliriz.

`f-string` ile string içerisinde değişken kullanabiliriz.

## Listeler

- `[...]` ile listeler oluşturulabilir.
- `len()` fonksiyonu ile listenin uzunluğunu öğrenebiliriz.
- `.append()` ile listenin sonuna eleman ekleyebiliriz.
- `.pop()` ile listenin sonundan eleman çıkarabiliriz.
- `.pop(index)` ile listenin istediğimiz index'indeki elemanı çıkarabiliriz.
- `.remove("element")` ile listenin istediğimiz elemanını çıkarabiliriz.
- `.extend[...]` ile listenin sonuna başka bir liste ekleyebiliriz.

## Döngüler

### For

```python
for item in list:
    print(item)
```

### While

```python
while True:
    print("Hello")
    break
```

## Fonksiyonlar

```python
def function_name():
    # Do something
    print("Hello")


# Parametreli fonksiyonlar
def function_name(parameter1, parameter2):
    # Do something
    print(parameter1, parameter2)


# Geriye değer döndüren fonksiyonlar
def function_name(parameter1, parameter2):
    # Do something
    return parameter1 + parameter2
```
