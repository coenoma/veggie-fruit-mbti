from app import create_app
from app.config.development import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
