from .user_inputs_service import UserInputsService
from .user_inputs_controller import UserInputsController

class UserInputsModule:
    controllers = [UserInputsController]
    services = [UserInputsService]