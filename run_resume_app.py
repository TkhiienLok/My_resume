import app
import os

port = int(os.environ.get("PORT", 5000))
app.create_app().run(debug=True, host='0.0.0.0', port=port)
