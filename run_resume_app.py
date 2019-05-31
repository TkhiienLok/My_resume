import app
import os

# running application on heroku
port = int(os.environ.get("PORT", 5000))
app.create_app().run(debug=True, host='0.0.0.0', port=port)

# running application locally
# app.create_app().run()
