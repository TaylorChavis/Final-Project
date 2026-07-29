from api.routers import customerRouter, menuItemRouter, orderRouter, orderDetailRouter, inventoryRouter, paymentRouter, reviewRouter

from . import customerRouter, menuItemRouter, orderRouter, orderDetailRouter, inventoryRouter, paymentRouter, reviewRouter


def load_routes(app):
    app.include_router(customerRouter.router)
    app.include_router(menuItemRouter.router)
    app.include_router(orderRouter.router)
    app.include_router(orderDetailRouter.router)
    app.include_router(inventoryRouter.router)
    app.include_router(paymentRouter.router)
    app.include_router(reviewRouter.router)