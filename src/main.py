import os
from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template

class app:
	def __init__(self):
		self = Flask(__name__)
		_dir = os.path.dirname(os.path.abspath(__file__))
		self.template_folder = os.path.join(_dir, "templates")
		self.static_folder = os.path.join(_dir, "static")
		self.debug = True

		@self.errorhandler(404)
		def page_not_found(e):
			return render_template("page_not_found.html")

		@self.before_request
		def before_request():
			pass

		@self.before_first_request
		def before_first_request():
			pass

		@self.after_request
		def after_request(response):
			response.headers.add("Access-Control-Allow-Origin", "*")
			response.headers.add("Cache-control", "no-cache, no-store, must-revalidate")
			return response

		@self.route("/", methods = ["GET"])
		def slash():
			return redirect(url_for("index"))

		@self.route("/index.html", methods = ["GET"])
		def index():
			return render_template("index.html")

		self.run(host="0.0.0.0", port=5000, threaded=True)

if __name__ == "__main__":
	app()
