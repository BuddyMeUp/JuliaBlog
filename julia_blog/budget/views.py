from flask import render_template,url_for,flash,redirect,request,Blueprint
from julia_blog import db,engine
from flask_login import current_user,login_required
import os
from julia_blog.models import budget_group_analysis,budget_category_analysis
from julia_blog.YNAB_files.YNAB_API_GroupReporting import group_analysis,category_analysis
from julia_blog.YNAB_files.YNAB_API_pacing import pacing_report,emoji_pattern
from sqlalchemy import create_engine, Integer, String

def html_change(html_string):
    html_string = emoji_pattern.sub(r'', html_string)
    html_string = html_string.replace(u'\U0001F3A2', '')
    html_string = html_string.replace(u'\U0001f7e1', '')
    html_string = html_string.replace(u'\U0001f9f7', '')
    html_string = html_string.replace(u'\U0001f9af', '')
    html_string = html_string.replace(u'\u26ea', '')
    html_string = html_string.replace(u'\u2016', '')
    html_string = html_string.replace(u'\U0001f7e2', '')
    html_string = html_string.replace(u'\U0001f3a2', '')


# group_analysis_sql = group_analysis.to_sql(
#     'group_analysis',
#     engine,if_exists='replace',index=False,chunksize=500,
#     dtype={
#         "user_id": Integer,
#         "category_group_name": String(50),
#         "spending_this_month": Integer,
#         "spending_this_month_perc": Integer,
#         "spending_last_month":  Integer,
#         "spending_last_month_perc": Integer,
#         "budgeting_this_month": Integer,
#         "budgeting_this_month_perc": Integer,
#         "budgeting_last_month": Integer,
#         "budgeting_last_month_perc": Integer,
#         "spending_diff_mom": Integer,
#         "budgeting_diff_mom": Integer,
#         "ideal_contribution": Integer,
#         "ideal_contribution_perc": Integer,
#         "budgeting_diff_mom": Integer,
#         "spending_3m_diff": Integer,
#         "budgeting_3m_diff": Integer })


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
    return render_template('budget_reporting.html')

@budgets.route('/budget/reporting/CategoryGroupReporting')
@login_required
def groupreporting():
    html_string = """{% extends "base.html" %} {% block content %} <div class="container">  <div class="jumbotron">
    <div align='center'>      <h1 >Budget Overview by Category Groups</h1>
    </div>  </div><table border="1" class="table table-striped table-hover>  <thead>
    <tr style="text-align: right;">            <th>category_group_name</th>
      <th>spending_this_month</th>      <th>spending_this_month%</th>      <th>spending_last_month</th>      <th>spending_last_month%</th>
      <th>budgeting_this_month</th>      <th>budgeting_this_month%</th>      <th>budgeting_last_month</th>      <th>budgeting_last_month%</th>      <th>spending_diff_mom</th>
      <th>budgeting_diff_mom</th>      <th>ideal_contribution</th>      <th>ideal_contribution%</th>      <th>spending_3m_diff</th>      <th>budgeting_3m_diff</th>    </tr>
  </thead>  <tbody>    <div class="container">"""
    for x in range(len(group_analysis['category_group_name'])):
        html_string += "<tr>"
        for y in group_analysis.columns:
            html_string += "<td>"
            html_string += str(group_analysis[y][x])
            html_string += "</td>"

        html_string += "</tr>"
    html_string += "  </tbody></table></div></div>{% endblock content %}"
    html_string = emoji_pattern.sub(r'', html_string)
    html_change(html_string)
    html_string = html_string.replace('class="dataframe"','class="table table-striped table-hover')
    html_string = str(html_string.encode('utf-8').strip())
    path_parent = os.path.dirname(os.getcwd())
    with open(path_parent+"/JuliaBlog/julia_blog/templates/budget_group_analysis.html", "w") as file_object:
        file_object.write( html_string)
    return render_template('budget_group_analysis.html',
                           title='Category Group Spending')

@budgets.route('/budget/reporting/CategoryReporting')
@login_required
def categoryreporting():
    html_string = """{% extends "base.html" %} {% block content %} <div class="container">  <div class="jumbotron">
      <div align='center'>      <h1 >Budget Overview by Category Groups</h1>
      </div>  </div><table border="1" class="table table-striped table-hover>  <thead>
      <tr style="text-align: right;">            <th>category_group_name</th>
        <th>spending_this_month</th>      <th>spending_this_month%</th>      <th>spending_last_month</th>      <th>spending_last_month%</th>
        <th>budgeting_this_month</th>      <th>budgeting_this_month%</th>      <th>budgeting_last_month</th>      <th>budgeting_last_month%</th>      <th>spending_diff_mom</th>
        <th>budgeting_diff_mom</th>      <th>ideal_contribution</th>      <th>ideal_contribution%</th>      <th>spending_3m_diff</th>      <th>budgeting_3m_diff</th>    </tr>
    </thead>  <tbody>    <div class="container">"""
    for x in range(len(category_analysis['category_name'])):
        html_string += "<tr>"
        for y in category_analysis.columns:
            html_string += "<td>"
            html_string += str(category_analysis[y][x])
            html_string += "</td>"

        html_string += "</tr>"
    html_string += "  </tbody></table></div></div>{% endblock content %}"
    html_string = emoji_pattern.sub(r'', html_string)
    html_change(html_string)
    html_string = html_string.replace('class="dataframe"', 'class="table table-striped table-hover')
    html_string = str(html_string.encode('utf-8').strip())
    path_parent = os.path.dirname(os.getcwd())
    with open(path_parent + "/JuliaBlog/julia_blog/templates/budget_category_analysis.html", "w") as file_object:
        file_object.write(html_string)

    return render_template('budget_category_analysis.html',
                           title='Category Spending')


@budgets.route('/budget/reporting/Pacing')
@login_required
def pacing():
    return render_template('YNAB_API_pacing.html')

@budgets.route('/budget/reporting/SpendingTimeSeries')
@login_required
def spending_time_series():
    return render_template('YNAB_API_lines_S.html')

@budgets.route('/budget/reporting/BudgetingTimeSeries')
@login_required
def budgeting_time_series():
    return render_template('YNAB_API_lines_B.html')

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