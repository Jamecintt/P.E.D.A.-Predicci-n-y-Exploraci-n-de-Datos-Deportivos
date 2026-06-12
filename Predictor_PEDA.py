print("===== PREDICTOR FUTBOL V1 =====\n")

equipo_local = input("Equipo local: ")
equipo_visitante = input("Equipo visitante: ")

print("\n--- ESTADISTICAS ---")

goles_local = float(input("Promedio goles anotados local: "))
goles_visitante = float(input("Promedio goles anotados visitante: "))

goles_recibidos_local = float(input("Promedio goles recibidos local: "))
goles_recibidos_visitante = float(input("Promedio goles recibidos visitante: "))

racha_local = int(input("Puntos ultimos 5 partidos local: "))
racha_visitante = int(input("Puntos ultimos 5 partidos visitante: "))

# VENTAJA DE LOCALIA
localia = 0.30

# FUERZA DE ATAQUE
ataque_local = goles_local
ataque_visitante = goles_visitante

# FUERZA DEFENSIVA
defensa_local = goles_recibidos_local
defensa_visitante = goles_recibidos_visitante

# GOLES ESPERADOS

goles_esperados_local = (
    ataque_local +
    defensa_visitante
) / 2 + localia

goles_esperados_visitante = (
    ataque_visitante +
    defensa_local
) / 2

# TOTAL DE GOLES

total_goles = (
    goles_esperados_local +
    goles_esperados_visitante
)

# SCORE GENERAL

score_local = (
    goles_esperados_local * 2
    + (racha_local / 5)
)

score_visitante = (
    goles_esperados_visitante * 2
    + (racha_visitante / 5)
)

# DIFERENCIA

diferencia = abs(
    score_local - score_visitante
)

print("\n==========================")
print("RESULTADO")
print("==========================")

print(
    "Goles esperados local:",
    round(goles_esperados_local,2)
)

print(
    "Goles esperados visitante:",
    round(goles_esperados_visitante,2)
)

print(
    "Total goles esperados:",
    round(total_goles,2)
)

# FAVORITO

if diferencia < 0.50:
    print("\nFavorito: PARTIDO MUY PAREJO")

elif score_local > score_visitante:
    print("\nFavorito:", equipo_local)

else:
    print("\nFavorito:", equipo_visitante)

# OVER UNDER

if total_goles >= 2.5:
    print("Mercado sugerido: OVER 2.5")

else:
    print("Mercado sugerido: UNDER 2.5")

# CONFIANZA

if diferencia >= 2:
    print("Confianza: ALTA")

elif diferencia >= 1:
    print("Confianza: MEDIA")

else:
    print("Confianza: BAJA")
