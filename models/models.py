#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class ModuloActividad(models.Model):
    _name = 'gym.actividad'
    _description = 'gym.actividad'

    name = fields.Char(string="Nombre", required=True)
    fecha_alta = fields.Date(string='Fecha de alta', default=lambda self: fields.Date.today())
    fecha_actividad = fields.Date(string="Fecha de actividad")
    precio = fields.Selection([
        ('1', 'Prueba Gratis'),
        ('2', 'Básica'),
        ('3', 'Premium'),
        ('4', 'Gold'),
    ], string="Precio", default='2')
    foto = fields.Image(max_width=100, max_height=100)
    responsable = fields.Char(string="Responsable")
    # El campo monitores se marcará como verdadero si el precio = 15
    monitores = fields.Boolean(string="Monitores", compute='_compute_monitores')
    ids_alumnos = fields.Many2many(
        comodel_name='gym.alumno',
        string="Alumnos",
        ondelete='cascade'
    )

    trainings = fields.Integer(string='Trainings', compute='_compute_trainings')

    @api.depends('precio')
    def _compute_monitores(self):
        for record in self:
            if record.precio == '4':
                record.monitores = True
            else:
                record.monitores = False

    @api.depends('precio')
    def _compute_trainings(self):
        for record in self:
            if record.precio == '1':
                record.trainings = 0
            elif record.precio == '2':
                record.trainings = 5
            elif record.precio == '3':
                record.trainings = 10
            else:
                record.trainings = 15


class ModuloProfesor(models.Model):
    _name = 'gym.profesor'
    _description = 'gym.profesor'

    name = fields.Char(string="Nombre", required=True)
    apellido1 = fields.Char(string="Primer apellido", required=True)
    apellido2 = fields.Char(string="Segundo apellido", required=True)
    foto = fields.Image(max_width=100, max_height=100)
    # Relaciones
    ids_actividades = fields.One2many(
        comodel_name='gym.actividad',
        inverse_name='responsable',
        string="Actividades",
        ondelete='set null'
    )


class ModuloAlumno(models.Model):
    _name = 'gym.alumno'
    _description = 'gym.alumno'

    nre = fields.Char(string="NRE", required=True)
    name = fields.Char(string="Nombre", required=True)
    apellido1 = fields.Char(string="Primer apellido")
    apellido2 = fields.Char(string="Segundo apellido")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    grupo = fields.Selection([
        ('1', 'Grupo 1'),
        ('2', 'Grupo 2'),
        ('3', 'Grupo 3'),
        ('4', 'Grupo 4'),
    ], string="Grupo", default='1')
    # Relaciones a una actividad pueden apuntarse varios alumnos
    ids_actividades = fields.Many2many(
        comodel_name='gym.actividad',
        string="Actividades",
        ondelete='cascade'
    )
