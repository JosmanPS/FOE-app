# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Modelos para registro
class Comite(models.Model):
    CARGO_CHOICES = [
        ('presidente', 'Presidente'),
        ('secretario', 'Secretario'),
        ('tesorero', 'Tesorero'),
        ('colaborador', 'Colaborador')
    ]
    CARRERA_CHOICES = [
        ('actuaria', 'Actuaría'),
        ('administracion', 'Administración'),
        ('cpol', 'Ciencia Política'),
        ('contabilidad', 'Contabilidad'),
        ('derecho', 'Derecho'),
        ('finanzas', 'Dirección Financiera'),
        ('economia', 'Economía'),
        ('matematicas', 'Matemáticas Aplicadas'),
        ('rrii', 'Relaciones Internacionales'),
        ('computacion', 'Ingeniería en Computación'),
        ('industrial', 'Ingeniería Industrial'),
        ('mecatronica', 'Ingeniería Mecatrónica'),
        ('negocios', 'Ingeniería en Negocios'),
        ('telecomunicaciones', 'Telecomunicaciones')
    ]

    # TODO: Ligar a un usuario especifico de tipo comite
    usuario = models.OneToOneField(User, verbose_name='Usuario')
    nombre = models.CharField(max_length=200, verbose_name='Nombre completo')
    foto = models.ImageField(verbose_name='Foto de perfil', blank=True,
                             null=True)
    cargo = models.CharField(max_length=32, default='colaborador',
                             choices=CARGO_CHOICES, verbose_name='Cargo')
    carrera = models.CharField(max_length=100, default='actuaria',
                               choices=CARRERA_CHOICES,
                               verbose_name='Carrera')
    segunda_carrera = models.CharField(max_length=100,
                                       choices=CARRERA_CHOICES,
                                       verbose_name='Segunda Carrera',
                                       blank=True, null=True)
    clave = models.IntegerField(verbose_name='Clave única',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(999999)])
    semestre = models.SmallIntegerField(verbose_name='Semestre',
                                        validators=[MinValueValidator(1),
                                                    MaxValueValidator(20)])
    correo = models.EmailField(verbose_name='Correo electrónico')
    telefono = models.IntegerField(verbose_name='Teléfono')
    aportacion = models.FloatField(verbose_name='Aportación al fondo')

    def __unicode__(self):
        return u'%s, (Comité Técnico)' % self.nombre


class OrganizacionEstudiantil(models.Model):
    REG_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('renovacion', 'Renovación'),
    ]
    CLAS_CHOICES = [
        ('deportivo', 'Deportivo'),
        ('cultural', 'Cultural'),
        ('academico', 'Académico'),
        ('publicacion', 'Publicación'),
        ('recreacion', 'Recreación'),
    ]
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('prospecto', 'Prospecto'),
    ]

    # TODO: Ligar a un usuario en la db de tipo OE

    # Formato único de registro
    usuario = models.OneToOneField(User, verbose_name='Usuario')
    fiscalizador = models.ForeignKey(Comite, verbose_name='Fiscalizador',
                                     blank=True, null=True)
    nombre = models.CharField(max_length=50, unique=True,
                              verbose_name='Nombre de la OE')
    slug = models.SlugField(blank=True, null=True)
    logo = models.ImageField(verbose_name='Logo')
    estado = models.CharField(max_length=10, verbose_name='Estado',
                              default='prospecto', choices=ESTADO_CHOICES)
    tipo_registro = models.CharField(max_length=10,
                                     verbose_name='Tipo de registro',
                                     default='nuevo',
                                     choices=REG_CHOICES)
    registro_desde = models.DateField(verbose_name='Registrado desde')
    correo = models.EmailField(verbose_name='Correo electrónico de la OE')
    facebook = models.URLField(verbose_name='Cuenta de Facebook',
                               help_text='Pon el URL completo a tu perfil de \
                                          Facebook para crear los links en tu \
                                          perfil.', blank=True, null=True)
    twitter = models.URLField(verbose_name='Cuenta de Twitter',
                              help_text='Pon el URL completo a tu perfil de \
                                         Twitter para crear los links en tu \
                                         perfil.', blank=True, null=True)
    clasificacion = models.CharField(max_length=32,
                                     verbose_name='Clasificación',
                                     default='deportivo',
                                     choices=CLAS_CHOICES)
    descripcion = models.TextField(verbose_name='Descripción')
    beneficio = models.TextField(verbose_name='Beneficio a alumnos del ITAM',
                                 help_text='Exposición de motivos por los \
                                 cuales el club beneficiaría a los \
                                 alumnos del ITAM.')
    plan_trabajo = models.FileField(verbose_name='Plan de trabajo')
    presupuesto = models.FileField(verbose_name='Presupuesto')

    def __unicode__(self):
        return self.nombre


class Miembro(models.Model):
    CARGO_CHOICES = [
        ('presidente', 'Presidente'),
        ('secretario', 'Secretario'),
        ('tesorero', 'Tesorero'),
        ('redes', 'Redes Sociales'),
        ('colaborador', 'Colaborador')
    ]
    CARRERA_CHOICES = [
        ('actuaria', 'Actuaría'),
        ('administracion', 'Administración'),
        ('cpol', 'Ciencia Política'),
        ('contabilidad', 'Contabilidad'),
        ('derecho', 'Derecho'),
        ('finanzas', 'Dirección Financiera'),
        ('economia', 'Economía'),
        ('matematicas', 'Matemáticas Aplicadas'),
        ('rrii', 'Relaciones Internacionales'),
        ('computacion', 'Ingeniería en Computación'),
        ('industrial', 'Ingeniería Industrial'),
        ('mecatronica', 'Ingeniería Mecatrónica'),
        ('negocios', 'Ingeniería en Negocios'),
        ('telecomunicaciones', 'Ingeniería en Telecomunicaciones')
    ]

    organizacion_estudiantil = models.ForeignKey(OrganizacionEstudiantil,
                                                 verbose_name='Organización \
                                                 Estudiantil')
    nombre = models.CharField(max_length=200, verbose_name='Nombre completo')
    foto = models.ImageField(verbose_name='Foto de perfil', blank=True,
                             null=True)
    cargo = models.CharField(max_length=32, default='colaborador',
                             choices=CARGO_CHOICES, verbose_name='Cargo')
    carrera = models.CharField(max_length=100, default='actuaria',
                               choices=CARRERA_CHOICES,
                               verbose_name='Carrera')
    segunda_carrera = models.CharField(max_length=100,
                                       choices=CARRERA_CHOICES,
                                       verbose_name='Segunda Carrera',
                                       blank=True, null=True)
    clave = models.IntegerField(verbose_name='Clave única',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(999999)])
    semestre = models.SmallIntegerField(verbose_name='Semestre',
                                        validators=[MinValueValidator(1),
                                                    MaxValueValidator(20)])
    correo = models.EmailField(verbose_name='Correo electrónico')
    telefono = models.IntegerField(verbose_name='Teléfono',
                                   blank=True, null=True)

    def __unicode__(self):
        return u'%s, (%s)' % (self.nombre,
                              self.organizacion_estudiantil.nombre)


class DatosBancarios(models.Model):
    BANCOS_CHOICES = [
        ('banamex', 'Banamex'),
        ('bancomer', 'Bancomer'),
        ('banorte', 'Banorte'),
        ('hsbc', 'HSBC'),
        ('scotiabank', 'Scotiabank'),
        ('santander', 'Santander'),
        ('ixe', 'IXE'),
        ('inbursa', 'Inbursa'),
    ]

    organizacion_estudiantil = models.OneToOneField(OrganizacionEstudiantil,
                                                    verbose_name='Organización \
                                                    Estudiantil')
    banco = models.CharField(max_length=64, default='bancomer',
                             choices=BANCOS_CHOICES, verbose_name='Banco')
    cuenta = models.IntegerField(verbose_name='Número de Cuenta')
    CLABE = models.IntegerField(verbose_name='CLABE')
    tarjeta = models.IntegerField(verbose_name='Número de tarjeta',
                                  blank=True, null=True)

    def __unicode__(self):
        return self.organizacion_estudiantil.nombre

