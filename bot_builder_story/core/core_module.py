from fastapi import FastAPI, APIRouter


class CoreModule(FastAPI):
    def __init__(self, modules: list, **kwargs):
        super().__init__(**kwargs)
        self.modules = modules
        self._register_controllers()

    def _register_controllers(self):
        for module in self.modules:
            module_instance = module()
            for controller in module_instance.controllers:
                router: APIRouter = controller.get_router()
                self.include_router(router)
