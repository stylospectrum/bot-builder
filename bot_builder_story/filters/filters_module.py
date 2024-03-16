from .filters_service import FiltersService
from .filters_controller import FiltersController


class FiltersModule:
    controllers = [FiltersController]
    services = [FiltersService]
