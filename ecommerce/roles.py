from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
	available_permissions = {}

class MedicoVet(AbstractUserRole):
	available_permissions = {}

class Colaborador(AbstractUserRole):
	available_permissions = {}

class Cliente(AbstractUserRole):
	available_permissions = {
		'add_pet': True,
		'update_pet': True, 
		'update_user_cliente': True, 
		'delete_user_cliente': True,
	}