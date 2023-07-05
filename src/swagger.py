from flasgger import LazyJSONEncoder, LazyString, Swagger

from flask import Flask, request


def initialize_flasgger(app: Flask):
    app.json_encoder = LazyJSONEncoder

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
    }

    template = dict(
        info={
            "title": LazyString(lambda: "Flask App - Swagger UI"),
            "version": LazyString(lambda: "0.1.0"),
            "uiversion": LazyString(lambda: 3),
            "description": LazyString(lambda: "Flask App - API Documentation"),
            "termsOfService": LazyString(lambda: "/there_is_no_tos"),
        },
        host=LazyString(lambda: request.host),
        schemes=[LazyString(lambda: "https" if request.is_secure else "http")],
    )

    return Swagger(app, config=swagger_config, template=template)
