from abc import ABC, abstractmethod

class MedioComunicacion(ABC):

    @abstractmethod
    def enviar_mensaje(self, mensaje):
        ...

class CorreoElectronico(MedioComunicacion):
    
    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por Correo:", mensaje)

class SMS(MedioComunicacion):
    
    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por SMS:", mensaje)

class Push(MedioComunicacion):
    
    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por notificacion al celular:", mensaje)

class wasa(MedioComunicacion):
    
    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por notificacion al wasa:", mensaje)


class FactoryMedios:

    @staticmethod
    def crear_medio(tipo):
        if tipo == "correo":
            return CorreoElectronico()
        elif tipo == "sms":
            return SMS()
        elif tipo == "push":
            return Push()
        elif tipo == "wasa":
            return wasa()
        else:
            raise ValueError( "Medio de comunicacion no 4existe")
        
class GestorEnvios:
    def __init__(self, tipos):
        self.tipos = [FactoryMedios.crear_medio(t) for t in tipos]

    def enviar_meansaje(self, mensaje):
        for t in self.tipos:
            t.enviar_mensaje(mensaje)

gestor = GestorEnvios(["correo", "sms", "push", "wasa"])
gestor.enviar_meansaje("hola")