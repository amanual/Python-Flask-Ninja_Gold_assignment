from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "MySecretKey;;;;"

@app.route('/')
def main():  
    if 'count' not in session:
        session['count'] = 0  
    if 'num' not in session:
        session['num'] = []
    print session['num']
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():    
  
    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        print gold
        
        session['num'].append("Earned: {} golds from the farm!".format(gold))
       
    elif request.form['building'] == 'cave':
        gold = random.randrange(5, 10)
        session['num'].append("Earned: {} golds from the cave!".format(gold))
        
    elif request.form['building'] == 'house':
        gold = random.randrange(2, 5)
        session['num'].append("Earned: {} golds from the house!".format(gold))
        
    elif request.form['building'] == 'casino':
        gold = random.randrange(-50, 50)
        session['num'].append("Earned: {} golds from the casino!".format(gold))
    
    session['count'] += gold  
    return redirect('/')
    
    
@app.route('/reset')
def reset():         
    session['count'] = 0
    session['num'] = []
    return redirect('/')
app.run(debug = True)