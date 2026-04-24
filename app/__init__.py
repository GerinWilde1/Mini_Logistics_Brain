from flask import Flask

def create_app():
    app = Flask(__name__)

    # 🔥 Global error handler lives here
    @app.errorhandler(Exception)
    def handle_error(e):
        return {
            "success": False,
            "error": str(e)}, 500

    class NotFoundError(Exception):
        pass

    # 📦 Register blueprints
    from app.routes.package_routes import bp as package_bp
    app.register_blueprint(package_bp)

    return app