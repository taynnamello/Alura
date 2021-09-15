##Classe

class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        print("Construindo Objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ##self.__codigo_banco = "001" - Código torna-se dispensável devido ao @staticmethod criado abaixo

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __permite_saque(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_saque

    def saca(self, valor):
        if(self.__permite_saque(valor)):
            self.__saldo -= valor
        else:
            print("Saque ultrapassou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
        
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod ##pertence a classe e não precisa do objeto 
    def codigo_banco():
        return "001"

    @staticmethod 
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
        

