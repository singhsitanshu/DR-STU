from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="./static", static_url_path='/static')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/apparel')
def apparel():
    return render_template("apparel.html")

@app.route('/dunks')
def dunks():
    return render_template("dunks.html")

@app.route('/jordans')
def jordans():
    return render_template("jordans.html")

products = [
    # {'name' : '', 'price' : '', 'img' : '', 'desc' : ''} 
    #dunks list
    [
    {'name': 'Grey Fog Dunks', 'price': '35.99', 'img': '/static/dunks/grey_fog.png', 'desc': 'The Nike Dunk Low Grey Fog features a white leather upper with Grey Fog leather overlays and Swooshes. From there, a matching woven tongue label, heel tab, and sole completes the design. '},
    {'name': "Philly Dunks", "price": "35.99", "img":"/static/dunks/philly_dunks.png", "desc":"Paying homage to the Philadelphia Phillies, the Nike SB Dunk Low Philadelphia Phillies, boasts a Valor blue Durabuck and suede upper, Team Maroon Swooshes, and woven tongue labels with graphics depicting two Philly staples: the Liberty Bell and a Philly cheese steak sandwich. From there, a white and gum brown Nike Zoom sole completes the design. "},
    {'name' : 'Navy Dunks', 'price' : '35.99', 'img' : '/static/dunks/navy_dunks.png', 'desc' : 'Nodding to the aged appeal of vintage Nike Dunks, the women\'s Nike Dunk Low Vintage Navy (W) features a white leather upper with navy overlays and Swooshes. At the base, a yellowed midsole gives off an aged, worn-in feel. Woven Nike tongue labels and an embroidered Nike heel patch add the finishing touch to this retro design.'},
    {'name' : 'Why So Sad? Dunks', 'price' : '35.99', 'img' : '/static/dunks/why_so_sad.png', 'desc' : 'The Nike SB Dunk Low Pro Why So Sad features a mixture of colors, with coastal blue and light current blue being the dominant hues. The upper of this Low Nike SB Dunk is made from leather material and there is a white Fat-style SB lacing system. The lateral heel of this shoe features an embroidered chicken that seems to be riding on a skateboard. Additionally, the heels and the tongues of this sneaker have Nike SB branding. '},
    {'name' : 'Coconut Dunks', 'price' : '35.99', 'img' : '/static/dunks/coconut_dunks.png', 'desc' : 'The Nike Dunk Low Coconut Milk features an off-white tumbled leather upper with pale yellow overlays and white Swooshes. Woven tongue labels and heel embroideries nod to the original 1985 design. From there, a matching Air sole at the base completes the design. '},
    {'name' : 'Blueberry Dunks', 'price' : '35.99', 'img' : '/static/dunks/blueberry_dunks.png', 'desc' : 'A part of Nike’s 2022 sneaker releases, this shoe features a leather upper with a crisp white base and light thistle overlays on its forefoot and heels. The upper’s look is completed by darker hits of lapis on the shoe’s Swoosh, laces, and heel tab embroidered with Nike branding. This colorway rests on a rubber cupsole with a foam wedge for cushioning and a rubber outsole, which features a traction pattern for improved grip. '}
    ]
    #jordans list
  {'name' : 'Off-White Chicago Jordan One', 'price' : '', 'img' : '', 'desc' : ''} 
  {'name' : 'Craft SE Inside Out Jordan One Low', 'price' : '', 'img' : '', 'desc' : ' The Air Jordan 1 Low Inside Out Black, designed by Peter Moore, is a deconstruction of the White/Sail Inside Out Air Jordan 1 Low. This is made of a mix of suede and leather with tonal black and grey hues in the different panels. The sneaker remixes the upper overlays into underlays while bringing out more detail in the leather toebox on top of the suede toecap. They have a retro vibe in the "Sail" and grey-sole piece with forthright single-stitched ‘23’ branding on the Swoosh and the Jordan branding on the shoe heel and tongue. '} 
  {'name' : 'Fragment x Travis Scott x Air Jordan 1 High', 'price' : '35.99', 'img' : '', 'desc' : ''} 
  {'name' : 'Reverse Mocha Jordan 1 Low', 'price' : '35.99', 'img' : '', 'desc' : ''} 
  {'name' : 'Taxi Jordan One High', 'price' : '35.99', 'img' : '', 'desc' : ''} 
  {'name' : 'Hyperroyal Jordan 1 High', 'price' : '35.99', 'img' : '', 'desc' : ''} 
  {'name' : 'Off-White Jordan Fours<', 'price' : '35.99', 'img' : '', 'desc' : ''} 
  {'name' : 'Craft Jordan Fours', 'price' : '35.99', 'img' : '', 'desc' : ''} 
  {'name' : 'White Oreo Jordan Fours', 'price' : '35.99', 'img' : '', 'desc' : ''} 
 ]
           
@app.route('/details/<int:section>/<int:index>')
def details(index, section):
    if section == 0:
        return render_template('details.html', products=products[0][index])
    else:
        return render_template('details.html', products=products[1][index])

if __name__ == "__main__":
    app.run()