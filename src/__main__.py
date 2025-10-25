from src.settings import Settings

if __name__ == "__main__":
    from uvicorn import run

    from .racanus_api.core.application import Application

    application = Application()

    run(
        application.application,
        host=application.settings.racanus_api_host,
        port=application.settings.racanus_api_port
    )
