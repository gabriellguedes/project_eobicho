from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
	available_permissions = {
		'add_pet': True, 'view_pet': True, 'update_pet': True, 'delete_pet': True,
		'add_user': True, 'view_user': True, 'update_user': True, 'delete_user':True,
		'add_user_cliente': True, 'view_user_cliente': True, 'update_user_cliente': True, 'delete_user_cliente':True,
		'add_ficha': True, 'view_ficha': True, 'update_ficha': True, 'delete_ficha': True,
		'add_peso': True,
		'add_itens_ficha': True, 'view_itens_ficha': True, 'update_itens_ficha': True, 'delete_itens_ficha': True,
		'add_cad_pet': True, 'view_cad_pet': True, 'update_cad_pet': True, 'delete_cad_pet': True,
		'view_funcionario': True,
	}

class Medico(AbstractUserRole):
	available_permissions = {
		'add_pet': True, 'view_pet': True, 'update_pet': True,
		'add_ficha': True, 'view_ficha': True,
		'add_peso': True, 
		'add_user_cliente': True, 'view_user_cliente': True, 'update_user_cliente': True,
		'view_funcionario': True,
	}

class Colaborador(AbstractUserRole):
	available_permissions = {
		'add_pet': True, 'view_pet': True, 'update_pet': True,
		'add_ficha': True, 'view_ficha': True, 
		'add_user_cliente': True, 'view_user_cliente': True, 'update_user_cliente': True, 
		'view_funcionario': True,
	}

class Cliente(AbstractUserRole):
	available_permissions = {
		'add_pet': True,
		'update_pet': True, 
		'view_pet': True,
		'view_user_cliente': True,
		'update_user_cliente': True, 
		'delete_user_cliente': True,
	}