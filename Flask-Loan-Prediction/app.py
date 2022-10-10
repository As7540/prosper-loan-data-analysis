from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)
Filename = 'model/model.pkl'
file=open(Filename, 'rb')  
model = pickle.load(file)

@app.route('/')
def index_page():
    print(model)
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_logic():
    
    if request.method == 'POST':
        CreditGrade = float(request.form.get('CreditGrade'))
        AvailableBankcardCredit = float(request.form.get('AvailableBankcardCredit'))
        StatedMonthlyIncome = float(request.form.get('StatedMonthlyIncome'))
        DebtToIncomeRatio = float(request.form.get('DebtToIncomeRatio'))
        LoanOriginalAmount = float(request.form.get('LoanOriginalAmount'))
        MonthlyLoanPayment = float(request.form.get('MonthlyLoanPayment'))
        LP_InterestandFees = float(request.form.get('LP_InterestandFees'))
        LP_CollectionFees = float(request.form.get('LP_CollectionFees'))
        LP_CustomerPayments = float(request.form.get('LP_CustomerPayments'))
    pred_name = model.predict([[CreditGrade,MonthlyLoanPayment,AvailableBankcardCredit,LP_InterestandFees,DebtToIncomeRatio,StatedMonthlyIncome,LoanOriginalAmount,LP_CustomerPayments,LP_CollectionFees]]).tolist()[0]
    yes = "Congrats!! Your loan is accepted"
    no = "Sorry !! Your loan is rejected"
    result = ''
    if  pred_name == '1':
        result = yes
    else:
        result = no
    return render_template('index.html', pred_name=pred_name, result=result)

if __name__ == "__main__":
    app.run(debug=True)