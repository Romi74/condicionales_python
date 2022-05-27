# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if str(texto_1) >= str(texto_2):
    print("texto_1 = a {} es mayor o igual a texto_2 = a {}. ".format(texto_1, texto_2))
else:
    print("texto_1 = a {}) es menor a texto_2 = a ({}).".format(texto_1, texto_2))
# 2-Transforma esas variables tipo texto en variables numéricas con (int)
texto_3 = int(texto_1)
texto_4 = int(texto_2)
# y almacénalas en nuevas variables.

# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
if texto_3 >texto_4:
    print("texto_3 igual a {} es mayor a texto_4 igual a {}. ".format(texto_3, texto_4))
else:
    print("texto_4 = a {} es mayor a texto_3 = a {}. ".format(texto_3, texto_4))

print("termine!!")  
# Para pensar!a
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
