from datetime import datetime
from pytz import country_timezones
from paises import paises
import pytz

timezone_country = {}

for countrycode in country_timezones:
    timezones = country_timezones[countrycode]
    # Iterating over the timezones of the country.
    for timezone in timezones:
        timezone_country[timezone] = countrycode
zonas = []
for i in timezone_country.keys():
    zonas.append(i)

zone_selecionada = pytz.timezone(zonas[5])
country_time = datetime.now(zone_selecionada)


#obtendo o nome do pais da zona selecionada ---------------------------------------
numero = int(input("digite o numero do pais:"))
#variavel que tera o simbolo do pais
simbol_do_pais = [timezone_country[zonas[numero]]]

for i in paises.keys():
    simbol_do_pais.append(i.lower())

#usando formatpara obter o caminho da imagem (bandeira do pais)
imagem = "png250px/{}.{}".format(simbol_do_pais[0],'png')

#obrtendo o key do pais em letras maiusculas
key = simbol_do_pais[0].upper()

#obtendo o nome do pais
nome_do_pais = paises[key]

print(f"A data da {2} eh {country_time.strftime('%d-%m-%y')} e o pais eh {nome_do_pais} e la sao {country_time.strftime('%H:%M:%S')}")