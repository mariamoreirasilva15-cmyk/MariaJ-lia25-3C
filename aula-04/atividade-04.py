class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
    def get_temperatura(self):
        return self.__temperatura
    def set_temperatura(self, nova_temp):
        if nova_temp >= -50 and nova_temp <= 150:
            self.__temperatura = nova_temp
        else:
            print("Erro: Temperatura fora do limite do sensor")
    def status(self):
        if self.__temperatura >= -50 and self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura >= 81 and self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"
s = Sensor(25) 
s.set_temperatura(30)
print(s.status())
s.set_temperatura(95)
print(s.status())
s.set_temperatura(130)
print(s.status())
s.set_temperatura(200) 