from rolepermissions.roles import AbstractUserRole

class Cliente(AbstractUserRole):
	available_permissions = {'add_pet': True, 'update_pet': True}