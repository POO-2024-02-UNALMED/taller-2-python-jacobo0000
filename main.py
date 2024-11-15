class Auto:
  cantidadCreados = 0
  def __init__(self,modelo,precio,asientos,marca,motor,registro):
    self.modelo = modelo
    self.precio =precio
    self.asientos = asientos
    self.marca = marca
    self.motor = motor
    self.registro = registro
    
  def cantidadAsientos(self):
    cantidadAsientos = 0
    for asiento in self.asientos:
      if isinstance(asiento, Asiento):
        cantidadAsientos += 1
    return cantidadAsientos

  
  def verificarIntegridad(self):
    if (self.registro != self.motor.registro ):
      return "Las piezas no son originales"

    for asiento in self.asientos:
      if (asiento != None):
        if(asiento.registro != self.registro):
          return("Las piezas no son originales")
      else:
        continue
              
    return("Auto original")

class Asiento:
  def __init__(self,color,precio,registro):
    self.color = color
    self.precio = precio
    self.registro = registro

  def cambiarColor(self,colorNuevo):
    colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
    if (colorNuevo in colores):
      self.color = colorNuevo

class Motor:
  def __init__(self, numeroCilindros, tipo, registro):
    self.numeroCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro

  def cambiarRegistro(self,registroNuevo):
    self.registro = registroNuevo
  
  def asignarTipo(self,tipoNuevo):
    tipos = ["gasolina", "electrico"]
    if(tipoNuevo in tipos):
      self.tipo = tipoNuevo 


