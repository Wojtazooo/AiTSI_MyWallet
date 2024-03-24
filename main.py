from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def WelcomePage():
    return render_template('welcome-page/welcome.html')

@app.route("/transactions")
def TranactionsPage():
    return render_template('transactions-page/transactions.html')

@app.route("/wallet-details")
def WalletSummaryPage():
    return render_template('wallet-details-page/wallet-details.html')

@app.route("/user-profile")
def UserProfilePage():
    return render_template('user-profile-page/user-profile.html')
