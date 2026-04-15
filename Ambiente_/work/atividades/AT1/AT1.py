def calcular_financiamento(preco, entrada, parcelas):
    taxa = 0.015
    valor_financiado = preco - entrada
    valor_total = valor_financiado * (1 + taxa * parcelas)
    parcela = valor_total / parcelas
    return parcela