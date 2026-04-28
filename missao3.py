LIMITE_MAXIMO = 80
LIMITE_MINIMO = 0


def alerta_sistema(sensor: str, valor: float, tipo: str) -> None:
    print(f"[ALERTA] Sensor '{sensor}': valor crítico detectado ({valor}°C) — tipo: {tipo}.")


def enviar_notificacao(canal: str, motivo: str) -> None:
    print(f"[NOTIFICACAO] Enviando alerta via {canal}. Motivo: {motivo}.")


def monitorar_temperatura(atual: float) -> None:
    print(f"[MONITORAMENTO] Temperatura atual: {atual}°C")

    if atual > LIMITE_MAXIMO:
        alerta_sistema("Temperatura", atual, "MAXIMA")
        enviar_notificacao("E-mail", f"Temperatura acima do limite maximo ({LIMITE_MAXIMO}°C)")

    elif atual < LIMITE_MINIMO:
        alerta_sistema("Temperatura", atual, "MINIMA")
        enviar_notificacao("E-mail", f"Temperatura abaixo do limite minimo ({LIMITE_MINIMO}°C)")

    else:
        print(f"[OK] Temperatura dentro dos parametros normais ({LIMITE_MINIMO}°C a {LIMITE_MAXIMO}°C).")


if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA DE MONITORAMENTO DE TEMPERATURA")
    print("=" * 50)

    monitorar_temperatura(85)
    print()
    monitorar_temperatura(-5)
    print()
    monitorar_temperatura(42)
