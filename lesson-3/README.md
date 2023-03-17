# Lesson 3

## Classes (Sınıflar)

Bir sınıf tanımlamak için `class` anahtar kelimesi kullanılır. Sınıfın adı PascalCase kullanılarak yazılır.

`instance` : Sınıfın örneği (instance) olarak da adlandırılır.

`self` : Sınıfın örneğini temsil eder. Bir class içerisindeki herhangi bir methodun ilk parametresi `self`
olmalıdır. `Self` anahtar kelimesi zorunlu değildir istediğiniz değeri verebilirsiniz.

`__init__` : Sınıfın örneği oluşturulduğunda çalışan methoddur. Bir nevi `constructor` olarak düşünebilirsiniz.

`__str__` : Sınıfın örneği `print` edildiğinde string olarak döndürülmesini sağlayan methoddur.

## Modules (Modüller)

`import module_name` : Bir modülü projeye dahil etmek için kullanılır.

`import module_name as alias` : Bir modülü projeye dahil etmek için kullanılır. Modülün adını alias olarak değiştirmek
için kullanılır.

`from module_name import class_name` : Bir modül içerisindeki sınıfı projeye dahil etmek için kullanılır.

## Packages (Paketler)

[Python Packaging User Guide](https://pypi.org/project/pip/) addresinden geliştiriciler tarafından hazırlanan paketleri
indirebilirsiniz.

`pip install package_name` : Bir paketi projeye dahil etmek için kullanılır.

`import package_name` : Bir paketi projeye dahil etmek için kullanılır.

`from package_name import module_name` : Bir paket içerisindeki modülü projeye dahil etmek için kullanılır.