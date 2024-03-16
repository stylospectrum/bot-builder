from fastapi import APIRouter

from .helpers import class_based_view as ClassBasedView


def Controller(tag: str = None, prefix: str = None):
    if prefix is None:
        prefix = tag

    if not prefix.startswith("/"):
        prefix = "/" + prefix

    if prefix.endswith("/"):
        prefix = prefix[:-1]

    def wrapper(cls) -> ClassBasedView:
        router = APIRouter(tags=[tag] if tag else None)

        http_method_names = ("GET", "POST", "PUT", "DELETE", "PATCH")

        for name, method in cls.__dict__.items():
            if callable(method) and hasattr(method, "method"):
                assert (
                    hasattr(method, "__path__") and method.__path__
                ), f"Missing path for method {name}"

                http_method = method.method
                assert http_method in http_method_names, f"Invalid method {http_method}"

                if prefix:
                    method.__path__ = prefix + method.__path__

                if not method.__path__.startswith("/"):
                    method.__path__ = "/" + method.__path__

                router.add_api_route(
                    method.__path__, method, methods=[http_method], **method.__kwargs__
                )

        def get_router() -> APIRouter:
            return router

        cls.get_router = get_router

        return ClassBasedView(router=router, cls=cls)

    return wrapper


def Get(path: str = None, **kwargs):
    if path is None:
        path = "/"

    def decorator(func):
        func.method = "GET"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Post(path: str = None, **kwargs):
    if path is None:
        path = "/"

    def decorator(func):
        func.method = "POST"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Delete(path: str, **kwargs):
    def decorator(func):
        func.method = "DELETE"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Put(path: str, **kwargs):
    def decorator(func):
        func.method = "PUT"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Patch(path: str, **kwargs):
    def decorator(func):
        func.method = "PATCH"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator
