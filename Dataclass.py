from dataclasses import dataclass, field, asdict
import Operaciones
from typing import List
@dataclass(frozen=True) 
class Persona:
    nombre: str
    edad: int = field(default=35)

    @property # no necesita poner parentecis al llamar al metodo, solo se usa si no resive parametros 
    def retornarEdadX2(self) -> int:
        return self.edad * 2
    
@dataclass
class Puesto:
    nombre: str
    persona: Persona

@dataclass
class Grupo:
    personas: List[Persona] = field(default_factory=list)

persona1 = Persona("Juan")
persona2 = Persona("Juan", 37)
print(persona2.retornarEdadX2) # metodo
print(persona1, "\n", persona2)
print(Operaciones.suma(persona1.edad, persona2.edad)) #Modulacion


print(asdict(persona1))

puesto1 = Puesto("Desarrollador", persona1)
print(puesto1)

grupo1 = Grupo()
grupo1.personas.append(persona1)
grupo1.personas.append(persona2)
print(grupo1)
if persona2.nombre == persona1.nombre:
    print("Son iguales")
else:
    print("No son iguales")
