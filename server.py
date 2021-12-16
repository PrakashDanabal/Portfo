from flask import Flask,render_template,request,redirect


#app=Flask(__name__,template_folder='templates')
app=Flask(__name__)
@app.route('/')
def homePage():
    return render_template('index.html')



def write_to_file(data):
    dname=data['name']
    dmessage=data['message']
    demail=data['email']
    with open ('data.txt','a') as database:
        database.write(f'\n{dname},{dmessage},{demail}')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_file(data)
        name= data['name']
    return render_template('/thankyou.html',username=name)


@app.route('/<string:page_name>')
def web_pages(page_name):
    return render_template(page_name)




