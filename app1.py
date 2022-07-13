from flask import Flask, render_template
from views import my_view

app = Flask(__name__)
@app.route('/index')
def index():
    return render_template("index.html")
app.register_blueprint(my_view)

# @app.errorhandler(404)
# def page_not_found_dude_dudette(e):
#     return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True, port=3002) 
