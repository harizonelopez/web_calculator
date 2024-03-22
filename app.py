from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.secret_key = 'aladinh00-01montext'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/rectangle', methods=['GET', 'POST'])
def rectangle():
    area = 0.0
    perimeter = 0.0
    if request.method == 'POST':
        length = float(request.form['length'])
        width = float(request.form['width'])

        area1 = length * width
        area = round(area1, 2)

        perimeter1 = 2 * (length + width)
        perimeter = round(perimeter1, 2)
            
    return render_template("rectangle.html", area=area, perimeter=perimeter)

@app.route('/cylinder', methods=['GET', 'POST'])
def cylinder():
    area = 0.0
    volume = 0.0
    pi = 3.142
    if request.method == 'POST':
        radius = float(request.form['radius'])
        height = float(request.form['height'])

        area1 = (2*pi*radius*height) + (2*pi*radius)
        area = round(area1, 2)

        volume1 = pi*(radius*radius)*height
        volume = round(volume1, 2)

    return render_template("cylinder.html", area=area, volume=volume)

@app.route('/cuboid', methods=['GET', 'POST'])
def cuboid():
    area = 0.0
    volume = 0.0
    if request.method == 'POST':
        length = float(request.form['length'])
        width = float(request.form['width'])
        height = float(request.form['height'])

        volume1 = length * width * height
        volume = round(volume1, 2)

        area1= (2*(length*width)) + (2*(length*height)) + (2*(width*height))
        area = round(area1, 2)

    return render_template("cuboid.html", area=area, volume=volume)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = 0.0
    circumfference = 0.0
    pi = 3.147
    if request.method == 'POST':
        radius = float(request.form['radius'])

        area1 = pi * radius * radius
        area = round(area1, 2)

        circumfference1 = 2 * pi * radius 
        circumfference = round(circumfference1, 2)

    return render_template("circle.html", area=area, circumfference=circumfference)

if __name__ == "__main__":
    app.run(debug=True)

