#!/usr/bin/ruby

    vectorHashMix = { :vehiculos=> {"coche" => 'Volkswagen', "moto" => 'Yamaha', "avion" => 'Airbus'}, :Nbingo => {"Galan" => 1, "Sol" => 2, "Cama" => 4, "Espina" => 5 }, :math => {"e" => 2.7182, "pi" => 3.1415}, :mix => {"pi" => 3.14, "Galan" =>4, "coche" =>"fiat" }}

    puts vectorHashMix.inspect

    vectorHashMix.keys().each do |valor|
        puts vectorHashMix[valor]

    end