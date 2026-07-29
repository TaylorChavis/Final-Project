from api.routers import customerRouter, menuItemRouter

from . import customerRouter, menuItemRouter


def load_routes(app):
    app.include_router(customerRouter.router)
    app.include_router(menuItemRouter.router)