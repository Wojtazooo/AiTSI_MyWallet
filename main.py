from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def IndexPage():
    return render_template('index.html')

@app.route("/home")
def Welcome():
    return render_template('home-page/home.html')

@app.route('/transactions')
def TranactionsPage():
    return render_template('transactions-page/transactions.html')

@app.route("/wallet-details")
def WalletSummaryPage():
    return render_template('wallet-details-page/wallet-details.html')

@app.route("/user-profile")
def UserProfilePage():
    return render_template('user-profile-page/user-profile.html')
