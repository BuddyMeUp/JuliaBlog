from flask import render_template,url_for,flash,redirect,request,Blueprint
from julia_blog import db
from flask_login import current_user,login_required
from julia_blog.models import budget_group_analysis
from julia_blog.YNAB_files.YNAB_API_GroupReporting import group_analysis,category_analysis
from julia_blog.YNAB_files.YNAB_API_pacing import pacing_report

budgets = Blueprint('budgets',__name__)

@budgets.route('/budget')
@login_required
def budget():
    #page = request.args.get('page',1,type=int)
    #budget_list = Project.query.order_by(Project.project_date.desc()).paginate(page=page,per_page=5)
    return render_template('budget.html')

@budgets.route('/budget/reporting')
@login_required
def reporting():
    return render_template('budget_group_analysis.html',
                           title='Category Group Spending',
                           rows=rows)
#    return render_template('YNAB_API_group_reporting.html')


# Category Grouping Lab
# Pacing
# Income Allocation Lab
# budget ID & Key to be set during login? on the budget screen?

#table per analysis type
#form to enter budget_id

"""

@budgets.route("/reporting")
def reporting():
    form = budget_form()
    conn = db.connect(budget_group_analysis)

    c = conn.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE name='%s' AND type='table' ''' % table_name)

    if (c.fetchone()[0] == 0):

        conn.execute(
            '''CREATE TABLE '%s' (names TEXT,  reviewerLink TEXT, reviewTitles TEXT, reviewBody TEXT, verifiedPurchase TEXT, postDate TEXT, starRating TEXT, helpful TEXT, nextPage TEXT)''' % table_name)

        for x in output_data:
            c.execute(
                '''INSERT INTO '%s' (names, reviewerLink, reviewTitles, reviewBody, verifiedPurchase, postDate, starRating, helpful, nextPage) VALUES (?,?,?,?,?,?,?,?,?)''' % table_name,
                (
                x["names"], x["reviewerLink"], x["reviewTitles"], x["reviewBody"], x["verifiedPurchase"], x["postDate"],
                x["starRating"], x["helpful"], x["nextPage"]))

        conn.commit()
        conn.close()

        print("Table and Records created Successfully!")


    else:  # The code will come here if it doesn't find the URL data in DB
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute(''' SELECT * from '%s' ''' % table_name)

        rows = cur.fetchall()
        output_data = ([dict(i) for i in rows])

        conn.close()

        print("Data Fetched Successfully!")

    return render_template('budget_group_analysis.html',
                           title='Category Group Spending',
                           rows=rows)

"""