from flask import Flask, request, redirect, render_template, session, flash

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect("/Home")

@app.route("/Home")
def landing():
    return render_template("Featured.html", title1= "Welcome Runners!!!", 
    welcome1= "this is a message to tell you about the site", title2= "Featured Training Plans", 
    welcome2="a list of recommended plans for you to check out", 
    title3= "Featured Running Events", welcome3= "a list of recommended events for you to check out" )
    
if __name__ == '__main__':
    app.run()