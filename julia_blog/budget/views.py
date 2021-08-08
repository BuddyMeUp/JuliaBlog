from flask import render_template,url_for,flash,redirect,request,Blueprint
from julia_blog import db,engine
from flask_login import current_user,login_required
from sqlalchemy import and_
from julia_blog.models import budget_group_analysis
from julia_blog.YNAB_files.YNAB_API_GroupReporting import group_analysis,category_analysis
from julia_blog.YNAB_files.YNAB_API_pacing import pacing_report
from sqlalchemy import create_engine, Integer, String

group_analysis_sql = group_analysis.to_sql(
    'group_analysis',
    engine,if_exists='replace',index=False,chunksize=500,
    dtype={
        "user_id": Integer,
        "category_group_name": String(50),
        "spending_this_month": Integer,
        "spending_this_month_perc": Integer,
        "spending_last_month":  Integer,
        "spending_last_month_perc": Integer,
        "budgeting_this_month": Integer,
        "budgeting_this_month_perc": Integer,
        "budgeting_last_month": Integer,
        "budgeting_last_month_perc": Integer,
        "spending_diff_mom": Integer,
        "budgeting_diff_mom": Integer,
        "ideal_contribution": Integer,
        "ideal_contribution_perc": Integer,
        "budgeting_diff_mom": Integer,
        "spending_3m_diff": Integer,
        "budgeting_3m_diff": Integer })


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
    #rows = group_analysis_sql.query.all()
    #return render_template('budget_group_analysis.html',
    #                       title='Category Group Spending',
    #                       rows=rows)

    return render_template('budget_reporting.html')

@budgets.route('/budget/reporting/CategoryGroupReporting')
@login_required
def groupreporting():
    return render_template('YNAB_API_group_reporting.html')

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