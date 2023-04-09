from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="./static", static_url_path='/static')


products = [
    {'name': "Philly Dunks", "price": "35.99", "img":"static/images/philly_dunks.png", "desc":"Paying homage to the Philadelphia Phillies, the Nike SB Dunk Low Philadelphia Phillies, boasts a Valor blue Durabuck and suede upper, Team Maroon Swooshes, and woven tongue labels with graphics depicting two Philly staples: the Liberty Bell and a Philly cheese steak sandwich. From there, a white and gum brown Nike Zoom sole completes the design. "}, 
    {'name': '', 'price': '', 'img': '', 'desc': ''}
]

@app.route('/')
def index():
    return render_template('index.html', css_file=url_for('static', filename='css/styles.css'))

@app.route('/dunks')
def dunks():
    return render_template('dunks.html', css_file=url_for('static', filename='css/styles.css'))

@app.route('/jordans')
def jordans():
    return render_template('jordans.html', css_file=url_for('static', filename='css/styles.css'))

@app.route('/apparel')
def apparel():
    return render_template('apparel.html', css_file=url_for('static', filename='css/styles.css'))
           
@app.route('/details-page')
def details_page():
    return render_template('html/details.html', products=products)

if __name__ == "__main__":
    app.run()