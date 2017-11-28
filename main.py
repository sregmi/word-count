from flask import Flask, render_template
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from collections import Counter
import re
import operator
import enchant

app = Flask(__name__)
app.config['SECRET_KEY'] = 's3cr3tk3y'

class MyForm(Form):
	input_text = TextAreaField('Insert your text here', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
	form = MyForm()
	if form.validate_on_submit():
		results = count_letters(form.input_text.data)
		return render_template(
			'main.html',
			total=results[0],
			words=results[1],
			valid_words=results[2],
			valid_word_count=len(results[2])
			)
	return render_template('index.html', form=form)

def count_letters(input_string):
	'''
	this function will count the number of words in any given text.
	words are categorized into two pools. one is any alphanumeric string and
	the other is just a valid dictionary word. please read readme for more
	information
	'''

	list_words = input_string.split()

	#removing all the non alphabet words from the string using regex
	alphabet_filter = re.compile('.*[A-Za-z].*')
	alpha_string = [word for word in list_words if alphabet_filter.match(word)]

	#removing all non alpha-numeric characters at the beginning and end of string and saving as lowercase
	alpha_num = [re.sub("^[^a-zA-Z0-9\\s]+|[^a-zA-Z0-9\\s]+$", "", s.lower()) for s in alpha_string]

	dictionary = enchant.Dict("en_US")
	dic_words = [word for word in alpha_num if dictionary.check(word)]

	total_word_count = str(len(alpha_num))
	alpha_num_count = Counter(alpha_num)
	dic_word_count = Counter(dic_words)

	word_count = sorted(
		alpha_num_count.items(),
		key=operator.itemgetter(1),
		reverse=True
		)

	valid_word_count = sorted(
		dic_word_count.items(),
		key=operator.itemgetter(1),
		reverse=True
		)

	return [total_word_count, word_count, valid_word_count]

if __name__ == '__main__':
	app.run(debug=True)
