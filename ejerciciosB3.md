###Ejercicio 9

Comprobar si el procesador o procesadores instalados lo tienen. 
¿Qué modelo de procesador es? ¿Qué aparece como salida de esa orden?

~~~
grep 'vendor_id' /proc/cpuinfo ; grep 'model name' /proc/cpuinfo ; grep 'cpu MHz' /proc/cpuinfo

uname -m

grep -i vmx /proc/cpuinfo
~~~

[Consola](http://showterm.io/4f1ff54e3b101ddb9025b#fast)
