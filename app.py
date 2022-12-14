import streamlit as slt
import pickle5 as pickle
from sklearn.preprocessing import StandardScaler
def isfloat(x):
  try:
    float(x)
    return True
  except ValueError:
    return False
#PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
#slt.beta_set_page_config(**PAGE_CONFIG)
logistic_regression = pickle.load(open('/app/colab-notebook/Completed_llogistic_regression_model.joblib', 'rb'))
tree = pickle.load(open('/app/colab-notebook/Completed_Bayesian_model.joblib', 'rb'))
GNB = pickle.load(open('/app/colab-notebook/Completed_tree_model.joblib', 'rb'))
def main():
  slt.title('compare between three models in case of accept or refuse give a loan')

  #input vabs
  Gender = slt.selectbox('Select your gender',
            ('Male', 'Female'))
  #slt.write('You selected:', Gender)
  if Gender == 'Male' :
    Gender = 1
  else:
    Gender = -1

  Married = slt.radio(
    "Your Marital Status is:",
    ('Married', 'not Married'))
  #slt.write('you selected:', Married)

  if Married == 'Married' :
    Married = 1
  else:
    Married = -1

  Dependents = slt.text_input("Enter the value of Dependents")
  if Dependents.isdigit() == True:
    Dependents = int(Dependents)
    slt.write('Valid Number')  
  #elif len(Dependents) !=0 :
   #   slt.warning('please enter a valid number(enter an postive integer one)' ,icon="⚠️"('.'))
  else:
      slt.write('Please enter a valid number(Number must be postive & integer)')
  Education = slt.radio(
    "Your Academic Status is:",
    ('Graduate', 'not Graduate'))
  #slt.write('you selected:', Education)

  if Education == 'Graduate' :
    Education = 1
  else:
    Education = -1


  Self_Employed = slt.selectbox('Are you self employed',('Yes', 'No'))
  #slt.write('You selected:', Self_Employed)
  if Self_Employed == 'Yes' :
    Self_Employed = 1
  else:
    Self_Employed = -1

  ApplicantIncome = slt.text_input("Applicant Income")
  if  isfloat(ApplicantIncome):
      if float(ApplicantIncome)>=100:
        ApplicantIncome = float(ApplicantIncome)
        slt.write('Good you inserted a valid number which is {}'.format(ApplicantIncome))
      else:
        slt.write('please enter a valid number(enter an number equals or bigger than 100$)')
  else:
    slt.write('please enter a valid number(enter an number equals or bigger than 100$)')
    
  CoapplicantIncome = slt.text_input("Co-applicant Income")
  if  isfloat(CoapplicantIncome):
      if float(CoapplicantIncome)>=0:
        CoapplicantIncome = float(CoapplicantIncome)
        slt.write('Number Entered : {}'.format(CoapplicantIncome))
      else:
      	slt.write('please enter a valid number(number must be equal to or bigger than 0$ )')
  else:
    slt.write('please enter a valid number(number must be equal to or bigger than 0$ )')

  Loan_Amount = slt.slider("What's the Loan-Amount you're applying for?", min_value=10,max_value=500000,step=10)
  slt.write("the loan amount is: ",Loan_Amount, '$')
  
  Loan_Amount_Term = slt.selectbox('Loan Term (in Months)',
            (12,24,36,48,60,72,84,96,108,120,132,144,156,168,180,192,204,216,228,240,252,264,276,288,300,312,324,336,348,360))
  slt.write('You selected:', Loan_Amount_Term)
  
  Credit_History = slt.radio(
    "Have you Applied for/Received a loan before?",
    ('YES', "NO"))
  #slt.write('you selected:', Credit_History)

  if Credit_History == 'YES' :
    Credit_History = 1
  else:
    Credit_History = 0
  result=["can get a loan","can not get a loan"]
  record=[[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_Amount,Loan_Amount_Term,Credit_History]]
 
  
  if slt.button('logistic_regression'):
    y_pred = logistic_regression.predict(record)
    output = y_pred[0]
    if output ==1:
      slt.success("the person with the former data  : {}".format(result[0]))
    else:
      slt.success("the person with the former data  : {}".format(result[1]))
  if slt.button('GNB'):
    y_pred = logistic_regression.predict(record)
    output = y_pred[0]
    if output ==1:
      slt.success("the person with the former data  : {}".format(result[0]))
    else:
      slt.success("the person with the former data  : {}".format(result[1])) 
  if slt.button('tree'):
    y_pred = logistic_regression.predict(record) 
    output = y_pred[0]
    if output ==1:
      slt.success("the person with the former data  : {}".format(result[0]))
    else:
      slt.success("the person with the former data  : {}".format(result[1]))
if __name__ == '__main__':
	main()
