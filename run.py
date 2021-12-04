import os
from dotenv import load_dotenv
import os
# load environment variables
load_dotenv()
from library import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()