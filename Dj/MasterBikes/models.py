from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    nickname = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    activo = models.BooleanField()

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )

class Talla(models.Model):
    id_talla = models.AutoField(primary_key=True, db_column="idTalla")
    talla = models.CharField(max_length=10)
    def __str__(self):
        return (
            str(self.talla)
        )

class TipoBici(models.Model):
    id_tipo_bici = models.AutoField(primary_key=True, db_column="idTipoBici")
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.tipo)
        )

class FormaPago(models.Model):
    id_forma_pago = models.AutoField(primary_key=True, db_column="idFormaPago")
    forma = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.forma)
        )

class Arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True, db_column="idArriendo")
    rut = models.ForeignKey(
        "Usuario", on_delete=models.CASCADE, db_column="rut"
    )
    direccion = models.CharField(max_length=80)
    id_tipo_bici = models.ForeignKey(
        "TipoBici", on_delete=models.CASCADE, db_column="idTipoBici"
    )
    id_talla = models.ForeignKey(
        "Talla", on_delete=models.CASCADE, db_column="idTalla"
    )
    inicio = models.DateField()
    termino = models.DateField()
    id_forma_pago = models.ForeignKey(
        "FormaPago", on_delete=models.CASCADE, db_column="idFormaPago"
    )


    def __str__(self):
        return (
            str(self.id_arriendo)
            + " "
            + str(self.rut)
        )

class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True, db_column="idTipoProducto")
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.tipo)
        )

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column="idProducto")
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30, null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_tipo_producto = models.ForeignKey(
        "TipoProducto", on_delete=models.CASCADE, db_column="idTipoProducto"
    )
    foto = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return (
            str(self.id_producto)
            + " "
            + str(self.nombre)
        )

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, db_column="idEstado")
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.estado)
        )

class Reparacion(models.Model):
    id_reparacion = models.AutoField(primary_key=True, db_column="idReparacion")
    rut = models.ForeignKey(
        "Usuario", on_delete=models.CASCADE, db_column="rut"
    )
    modelo_bicicleta = models.CharField(max_length=80)
    problema = models.CharField(max_length=150)
    id_estado = models.ForeignKey(
        "Estado", on_delete=models.CASCADE, db_column="idEstado"
    )
    fecha = models.DateTimeField()
    def __str__(self):
        return(
            str(self.id_reparacion)
            + " "
            + str(self.modelo_bicicleta)
            + " "
            + str(self.rut)
        )