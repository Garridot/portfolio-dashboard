from flaskr import create_app

app = create_app(config_class='flaskr.config.ProductionConfig')

if __name__ == "__main__":
    app.run()
