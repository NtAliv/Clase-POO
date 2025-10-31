import pytest
from TallerJhairoMu_SanetCo import Empresa, Particular, Camion, Moto

def test_vehiculo_se_crea_correctamente():
    p = Particular("ABC123", "Toyota", 10000, "Particular")
    assert p.placa == "ABC123"
    assert p.marca == "Toyota"
    assert p.valor == 10000
    assert p.tipo == "Particular"
    assert p.calcular_impuesto() == 1000

def test_impuesto_camion():
    c = Camion("XYZ789", "Volvo", 20000, "Camion")
    assert c.calcular_impuesto() == 3000

def test_impuesto_moto():
    m = Moto("YMA456", "Yamaha", 5000, "Moto")
    assert m.calcular_impuesto() == 250

def test_agregar_vehiculo_a_empresa(tmp_path):
    archivo = tmp_path / "flota.txt"
    empresa = Empresa("Transportes S.A.", archivo)
    p = Particular("ABC123", "Toyota", 10000, "Particular")
    empresa.añadir_vehiculos(p)
    assert len(empresa.lista_vehiculos) == 1

def test_guardar_y_cargar_vehiculos(tmp_path):
    archivo = tmp_path / "flota.txt"
    empresa = Empresa("Transportes S.A.", archivo)
    p = Particular("ABC123", "Toyota", 10000, "Particular")
    c = Camion("XYZ789", "Volvo", 25000, "Camion")
    empresa.añadir_vehiculos(p)
    empresa.añadir_vehiculos(c)


    # Guardar
    empresa.guardar_en_archivo()
    assert archivo.exists() is True

    # Cargar desde archivo
    empresa2 = Empresa("Otra Empresa", archivo)
    empresa2.cargar_vehiculos()


