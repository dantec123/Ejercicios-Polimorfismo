class pago:
    def procesar_pago(self):
        pass  


class tarjeta_credito(pago):
    def procesar_pago(self):
        print("Procesando pago con tarjeta de crédito")


class PayPal(pago):
    def procesar_pago(self):
        print("Procesando pago en PayPal")


if __name__ == "__main__":
    pagos = [tarjeta_credito(), PayPal(), 
    tarjeta_credito(), PayPal()]

    for pago in pagos:
        pago.procesar_pago()