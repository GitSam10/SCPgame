# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template, request, send_file, send_from_directory, session, redirect, url_for
import pandas as pd
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'max_on_top'


@app.route('/', methods=['GET', 'POST'])
def greet_user():
    if request.method == 'POST':
        session['user_name'] = request.form['user_name']
        user_name = session.get('user_name')
        return render_template('index.html', user_name=user_name)
    else:
        return render_template('form.html')


@app.route('/index')
def index():
    user_name = session.get('user_name')
    return render_template('index.html', user_name=user_name)

@app.route('/index_lt')
def index_lt():
    user_name = session.get('user_name')
    session['sust_correct'] = 0
    return render_template('index_lt.html', user_name=user_name)

@app.route('/finance')
def finance():
    return render_template('finance.html')

@app.route('/risk')
def risk():
    return render_template('risk.html')

@app.route('/data')
def data():
    user_name = session.get('user_name')
    return render_template('data.html', user_name=user_name)
@app.route('/data_engineer')
def data_engineer():
    return render_template('data_engineer.html')
@app.route('/data_analyst')
def data_analyst():
    return render_template('data_analyst.html')
@app.route('/data_scientist')
def data_scientist():
    return render_template('data_scientist.html')
@app.route('/submit_data_engineer', methods=['POST'])
def submit_data_engineer():
    solution = request.form.get('solution')
    # You would use the OpenAI API to grade the solution here. For now, let's assume the score is 85.
    score = 85
    session['data_engineer_score'] = score
    return render_template('data_engineer_score.html', score=score)

@app.route('/sustainability')
def sustainability():
    sust_correct = session.get('sust_correct')
    if sust_correct is not None and sust_correct > 3:
        session['sust_correct'] = 3
    return render_template('sustainability.html', sust_correct=sust_correct)

@app.route('/sustainability1')
def sustainability1():
    return render_template('sustainability1.html')

@app.route('/sustainability2')
def sustainability2():
    return render_template('sustainability2.html')

@app.route('/sustainability3')
def sustainability3():
    return render_template('sustainability3.html')

@app.route('/recruitment_problem')
def recruitment_problem():
    return render_template('recruitment_problem.html')

@app.route('/greenfin')
def greenfin():
    return render_template('greenfin.html')

@app.route('/greenfin/<employee>')
def greenfin_test():
    return render_template('greenfin.html')


@app.route('/download_excel/<file>')
def download_excel(file):
    # Logic to determine the file path based on the provided parameter
    file_path = f"data/{file}.xlsx"

    # Return the file for download
    return send_file(file_path, as_attachment=True)

@app.route('/download_docx/<file>')
def download_docx(file):
    # Logic to determine the file path based on the provided parameter
    file_path = f"data/{file}.docx"

    # Return the file for download
    return send_file(file_path, as_attachment=True)

@app.route('/greenfin_ceo')
def greenfin_ceo():
    return render_template('greenfin_ceo.html')

@app.route('/greenfin_legal')
def greenfin_legal():
    return render_template('greenfin_legal.html')

@app.route('/greenfin_risk')
def greenfin_risk():
    return render_template('greenfin_risk.html')

@app.route('/greenfin_invest')
def greenfin_invest():
    return render_template('greenfin_invest.html')

@app.route('/greenfin_operations')
def greenfin_operations():
    return render_template('greenfin_operations.html')

@app.route('/greenfin_hr')
def greenfin_hr():
    return render_template('greenfin_hr.html')

@app.route('/greenfin_marketing')
def greenfin_marketing():
    return render_template('greenfin_marketing.html')

@app.route('/greenfin_crm')
def greenfin_crm():
    return render_template('greenfin_crm.html')

@app.route('/greenfin_external')
def greenfin_external():
    return render_template('greenfin_external.html')


@app.route('/check_input_s1', methods=['POST'])
def check_input_s1():
    session['current_question'] = 's1'
    user_input = request.form.get('user_input')
    answer_correct = (user_input == 'b')
    session['answer_correct'] = answer_correct
    if answer_correct:
        session['sust_correct'] = (session.get('sust_correct') or 0) + 1
        return redirect(url_for('sustain_answer'))
    else:
        answer_correct = False
        return redirect(url_for('sustain_answer'))


@app.route('/check_input_s2', methods=['POST'])
def check_input_s2():
    session['current_question'] = 's2'
    user_input = request.form.get('user_input')
    answer_correct = (user_input == 'a')
    session['answer_correct'] = answer_correct
    if answer_correct:
        session['sust_correct'] = (session.get('sust_correct') or 0) + 1
        return redirect(url_for('sustain_answer'))
    else:
        answer_correct = False
        return redirect(url_for('sustain_answer'))

@app.route('/check_input_s3', methods=['POST'])
def check_input_s3():
    session['current_question'] = 's3'
    user_input = request.form.get('user_input')
    answer_correct = (user_input == 'd')
    session['answer_correct'] = answer_correct
    if answer_correct:
        session['sust_correct'] = (session.get('sust_correct') or 0) + 1
        return redirect(url_for('sustain_answer'))
    else:
        answer_correct = False
        return redirect(url_for('sustain_answer'))


@app.route('/sustain_answer')
def sustain_answer():
    answer_correct = session.get('answer_correct')
    current_question = session.get('current_question')
    return render_template('sustain_answer.html', answer_correct=answer_correct, current_question=current_question)
    
if __name__ == '__main__':
    app.run(debug=True)