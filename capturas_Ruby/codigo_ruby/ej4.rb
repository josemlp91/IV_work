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