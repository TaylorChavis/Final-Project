from api.routers import customerRouter, menuItemRouter, orderRouter

from . import customerRouter, menuItemRouter, orderRouter


def load_routes(app):
    app.include_router(customerRouter.router)
    app.include_router(menuItemRouter.router)
    app.include_router(orderRouter.router)