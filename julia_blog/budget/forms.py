# add user input to a new category

class budget_form(FlaskForm):
    budget_id = StringField('Budget_id',[validators.DataRequired()])
    submit = SubmitField("Let's Analyse!")

# add new category grouping