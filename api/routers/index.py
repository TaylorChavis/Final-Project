from api.routers import customerRouter, menuItemRouter, orderRouter, orderDetailRouter

from . import customerRouter, menuItemRouter, orderRouter, orderDetailRouter


def load_routes(app):
    app.include_router(customerRouter.router)
    app.include_router(menuItemRouter.router)
    app.include_router(orderRouter.router)
    app.include_router(orderDetailRouter.router)