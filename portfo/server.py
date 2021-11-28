from types import new_class
from flask import Flask, render_template, url_for, request, redirect
import csv  # builting module ..csv stand for comma seperated value
app = Flask(__name__)

# print(app)
print(__name__)

# urls parameters or also called end_points


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # create csv object that we can use
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            # grab data
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong!!try again.'


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')
