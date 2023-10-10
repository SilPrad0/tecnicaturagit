# calculadora de impuestos, fx para calcular el total de un pago incluyendo
#iva. Formula: pago_total = pago_sin_iva + pago_sin_iva * (impuesto/100)

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input('digite el pago sin impuesto: '))
impuesto = float(input('digite el impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'el pago con impuesto es: {pago_con_impuesto}')
