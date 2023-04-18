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
    {'name' : 'Navy Dunks', 'price' : '35.99', 'img' : '/static/dunks/navy_dunks/navy_dunks.png', 'desc' : 'Nodding to the aged appeal of vintage Nike Dunks, the women\'s Nike Dunk Low Vintage Navy (W) features a white leather upper with navy overlays and Swooshes. At the base, a yellowed midsole gives off an aged, worn-in feel. Woven Nike tongue labels and an embroidered Nike heel patch add the finishing touch to this retro design.'},
    {'name' : 'Why So Sad? Dunks', 'price' : '35.99', 'img' : '/static/dunks/why_so_sad.png', 'desc' : 'The Nike SB Dunk Low Pro Why So Sad features a mixture of colors, with coastal blue and light current blue being the dominant hues. The upper of this Low Nike SB Dunk is made from leather material and there is a white Fat-style SB lacing system. The lateral heel of this shoe features an embroidered chicken that seems to be riding on a skateboard. Additionally, the heels and the tongues of this sneaker have Nike SB branding. '},
    {'name' : 'Coconut Dunks', 'price' : '35.99', 'img' : '/static/dunks/coconut_dunks.png', 'desc' : 'The Nike Dunk Low Coconut Milk features an off-white tumbled leather upper with pale yellow overlays and white Swooshes. Woven tongue labels and heel embroideries nod to the original 1985 design. From there, a matching Air sole at the base completes the design. '},
    {'name' : 'Blueberry Dunks', 'price' : '35.99', 'img' : '/static/dunks/blueberry_dunks.png', 'desc' : 'A part of Nike’s 2022 sneaker releases, this shoe features a leather upper with a crisp white base and light thistle overlays on its forefoot and heels. The upper’s look is completed by darker hits of lapis on the shoe’s Swoosh, laces, and heel tab embroidered with Nike branding. This colorway rests on a rubber cupsole with a foam wedge for cushioning and a rubber outsole, which features a traction pattern for improved grip. '}
    ],
    #jordans list
    [
    {'name' : 'Off-White Chicago Jordan One', 'price' : '35.99', 'img' : '/static/jordans/off_white_chicago.png', 'desc' : 'The Off-White x Air Jordan 1 Retro High OG was one of the most highly anticipated footwear collaborations of 2017. It marked the first time Virgil Abloh, founder of the Milan-based fashion label and Jordan Brand had teamed up. Nicknamed "The 10" edition, this pair comes in the original Chicago-themed white, black and varsity red colorway. Featuring a white, red and black-based deconstructed leather upper with a Swooshless medial side branded with "Off-White for Nike Air Jordan 1, Beaverton, Oregon, USA © 1985." Other details include: floppy ankle collars with hidden "85" written on the inside, an oversized off-centered Swoosh on the lateral sides, "Air" written on the midsole and the word "Shoelaces" on the laces with no branding on the tongue. Their release date is set for 2017 where they retailed for $190 in men\'s sizes only. As if the hype wasn\'t enough, the limited availability made these Off-White x Air Jordan 1 Retro High OG\'s highly sought after, way before their official release. '},
    {'name' : 'Craft SE Inside Out Jordan One Low', 'price' : '35.99', 'img' : '/static/jordans/inside_out_craft.png', 'desc' : ' The Air Jordan 1 Low Inside Out Black, designed by Peter Moore, is a deconstruction of the White/Sail Inside Out Air Jordan 1 Low. This is made of a mix of suede and leather with tonal black and grey hues in the different panels. The sneaker remixes the upper overlays into underlays while bringing out more detail in the leather toebox on top of the suede toecap. They have a retro vibe in the "Sail" and grey-sole piece with forthright single-stitched ‘23’ branding on the Swoosh and the Jordan branding on the shoe heel and tongue. '},
    {'name' : 'Fragment x Travis Scott x Air Jordan 1 High', 'price' : '35.99', 'img' : '/static/jordans/fragment_high.png', 'desc' : 'The Air Jordan 1 High OG SP Fragment Design x Travis Scott fragment draws inspiration from a Jordan 1 Royal press sample from 1985 with its white and blue tumbled leather upper. Similar to previous Travis Scott Jordan 1s, signature reverse Swooshes and hidden stash pockets in the collar add on to the classic design. From there, both Travis Scott\'s Cactus Jack and Fragment logos are debossed in black on the heel wrap. '},
    {'name' : 'Reverse Mocha Jordan 1 Low', 'price' : '35.99', 'img' : '/static/jordans/reverse_mocha.png', 'desc' : 'Nodding to the Air Jordan 1 High Travis Scott Mocha, the Air Jordan 1 Low Travis Scott Reverse Mocha offers a similar Mocha and off-white palette but in a reverse-style color blocking. Its upper is constructed with a Mocha Durabuck base, white leather overlays, and signature reverse Swooshes. Hits of red on the Wings logo heel embroidery and woven tongue label gives a sharp contrast to the design\'s neutral look. From there, a yellowed Air sole adds a vintage feel. '}, 
    {'name' : 'Taxi Jordan One High', 'price' : '35.99', 'img' : '/static/jordans/taxi.png', 'desc' : 'The Air Jordan 1 Retro High OG Yellow Toe brings back the distinct color blocking as well as the sneaker´s high silhouette. This Retro OG Air Jordan 1 comes in an all leather build that combines a white base with a yellow toe box, and some yellow overlays in the heel and ankle area. A contrasting black appears in the toe and lace area, Swoosh, and Wings logo on the lateral side. A classic AJ1 white midsole and a yellow rubber outsole round off the design'}, 
    {'name' : 'Hyperroyal Jordan 1 High', 'price' : '35.99', 'img' : '/static/jordans/hyperroyal.png', 'desc' : 'Jordan Brand added a new colorway to their Jordan 1 catalog in the spring of 2021 with the Air Jordan 1 Hyper Royal. The Hyper Royal utilizes material selection and color blocking to provide a vintage feel, similar to the 2019 Air Jordan 1 High Turbo Green. \nThe upper of the Air Jordan 1 Hyper Royal is constructed with white leather and distressed Hyper Royal suede overlays while the Swoosh and panels around the ankle are made with a Light Smoke Grey Durabuck. Consistent with Jordan 1s of the past, a classic white "Wings" logo appears on the lateral ankle. A blue woven Nike Air label stitched on the tongue, a white midsole, and a Light Smoke Grey outsole add the finishing touches to this retro design.'}, 
    {'name' : 'Off-White Jordan Fours', 'price' : '35.99', 'img' : '/static/jordans/off-white_4s.png', 'desc' : 'Jordan Brand and Virgil Abloh teamed up once again to release the third silhouette in their collaborative history with the women\'s Jordan 4 Retro Off-White Sail (W), now available on StockX. After teasing the release of the Off-White 4 with samples in his MCA exhibit and presenting them in his Off-White FW2020 Women’s Show, Virgil Abloh finally delivered what might be the most anticipated release of 2020. The Air Jordan 4 Sail features full-grain leather uppers with hits of mesh and translucent materials on the toebox and heel of the shoe. From there, hits of light blue on the tongue’s Jumpman and the outsole’s Nike Swoosh provide contrast to the sail colored sneaker. These women\'s sneakers released in July of 2020 and retailed for $200 USD.'}, 
    {'name' : 'Craft Jordan Fours', 'price' : '35.99', 'img' : '/static/jordans/craft_4s.png', 'desc' : 'After releasing previously in Nikes Dunk, Air Max 90 and Air Force One models, Jordan Brand is getting the Photon treatment, with the release of the Air Jordan 4 Retro SE Craft Photon Dust. \nThe Air Jordan 4 SE Phototon Dust is constructed with leather and suede uppers consisting of various shades of grey. Jordan Brand is changing directions with the Air Jordan 4s mesh cage and replacing it with a soft suede and a cracked leather cage wing. '}, 
    {'name' : 'White Oreo Jordan Fours', 'price' : '35.99', 'img' : '/static/jordans/oreo_4s.png', 'desc' : 'The Air Jordan 4 Retro White Oreo features a white leather and mesh upper with hits of Tech Grey on its eyelets and midsole. From there, a red Jumpman logo is embroidered on the tongue, adding a pop of color to the neutral-toned design. '}
    ]
]
           
@app.route('/details/<int:section>/<int:index>')
def details(index, section):
    if section == 0:
        return render_template('details.html', products=products[0][index])
    else:
        return render_template('details.html', products=products[1][index])

if __name__ == "__main__":
    app.run()