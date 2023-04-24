class Registro: 
    __temperatura = ''
    __humedad = ''
    __presion = ''
    
    def __init__(self, temperatura="", humedad="", presion=""):

        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
        
    def retornaTemperatura(self):
        return self.__temperatura
    
    def retornaHumedad(self):
        return self.__humedad
    
    def retornaPresion(self):
        return self.__presion
