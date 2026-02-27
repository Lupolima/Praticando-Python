tempo_assistido=6
tempo_total=7

assistido_minutos=tempo_assistido*60
total_minutos=tempo_total*60

if assistido_minutos >= (total_minutos-60):
    print ("receba")
else:
    print("nao receba email")