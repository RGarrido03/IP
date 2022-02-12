# Ler o tempo do teclado
tempo_s = int(input("Qual o tempo em segundos? "))

# Converter em h, m e s
horas = tempo_s // 3600
minutos = tempo_s % 3600
segundos = (tempo_s % 3600) % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
