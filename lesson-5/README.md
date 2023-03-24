# Lesson 5

- `assert` : Anahtar kelimesi ile bir test yapabiliriz. Eğer test doğru ise programımız çalışmaya devam eder. Eğer test
  yanlış ise programımız hata verir ve durur.
- `setup_method()` : Bu fonksiyon her test fonksiyonu çalışmadan önce çalışır.
- `teardown_method()` : Bu fonksiyon her test fonksiyonu çalıştıktan sonra çalışır.
- `@pytest.mark.skip()` : Bu fonksiyon ile test fonksiyonunu çalıştırmadan geçebiliriz. Bu fonksiyonun içine bir
  neden yazabiliriz. Bu nedeni `pytest` çalıştırdığımızda görebiliriz.
- `@pytest.mark.parametrize(param1,param2,[("param1Value","param1Value2)` : Bu fonksiyon ile bir fonksiyonu birden fazla
  parametre ile çalıştırabiliriz.