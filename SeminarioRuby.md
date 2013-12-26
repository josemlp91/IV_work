#Una introducción ligera al lenguaje Ruby
================================================


###Ejercicio 1:
_Instalar Ruby y usar ```ruby --version``` para comprobar la versión instalada.
A la vez, conviene instalar también irb, rubygems y rdoc._


~~~
sudo apt-get install ruby1.9.3
~~~

###Ejercicio 2:
_Crear un programa en Ruby que imprima los números desde el 1 hasta otro contenido en una variable._

~~~
#!/usr/bin/env ruby

$i = 0
$num = 5
begin
   puts("Valor de la variable #$i" )
   $i +=1;
end until $i > $num
~~~

###Ejercicio 3:
_¿Se pueden crear estructuras de datos mixtas en Ruby? Crear un array de hashes de arrays e imprimirlo._

~~~

#!/usr/bin/ruby

    vectorHashMix = { :vehiculos=> {"coche" => 'Volwagen', "moto" => 'Yamaha', "avion" => 'Airbus'}, :Nbingo => {"Galan" => 1, "Sol" => 2, "Cama" => 4, "Espina" => 5 }, :math => {"e" => 2.7182, "pi" => 3.1415}, :mix => {"pi" => 3.14, "Galan" =>4, "coche" =>"fiat" }}

    puts vectorHashMix.inspect

    vectorHashMix.keys().each do |valor|
        puts vectorHashMix[valor]

    end

~~~

###Ejercicio 4:
_Crear una serie de funciones instanciadas con un URL que devuelvan algún tipo de información sobre el mismo: fecha de última modificación, por ejemplo. Pista: esa información está en la cabecera HTTP que devuelve._


~~~

#!/usr/bin/ruby

    require 'net/http'

    def fecha(url)
        response = Net::HTTP.get_response(url,'/')
        return response['date'].to_s
    end

    def conexion(url)
        response = Net::HTTP.get_response(url,'/')
        return response['content-type'].to_s
    end

    def servidor(url)
        response = Net::HTTP.get_response(url,'/')
        return response['server'].to_s
    end


    url = ARGV[0]

    puts "URL del servidor: " << url
    puts "fecha: "<<fecha(url)
    puts "tipo del contenido" <<conexion(url)
    puts "informacion del servidor: "<< servidor(url)

~~~

###Ejercicio 5:
_Ver si está disponible Vagrant como una gema de Ruby e instalarla._

No existe como gema local:

~~~
gem search vagrant
~~~

Pero si como una gema remota:

~~~
gem search --remote vagrant
~~~

Como vemos al ejecurar directamente ```sudo gem install vagrant``` no da el siguiente error.

Como nos indica los apuntes es interesante istallar ```rubygems``` y  ```ruby1.9.1-dev```.

~~~
sudo apt-get install rubygems ruby1.9.1-dev
~~~

Ahora el ejecutar ```sudo gem install vagrant``` se completa la instalación satisfactoriamente.






