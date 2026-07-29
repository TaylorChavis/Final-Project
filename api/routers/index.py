from api.routers import customerRouter

from . import customerRouter


def load_routes(app):
    app.include_router(customerRouter.router)