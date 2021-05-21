from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import datetime
from os import chdir
import os
import re
import sys
import traceback

env = Environment(loader = FileSystemLoader('.'))
template = env.get_template('btemp.html')
root = os.path.dirname(os.path.realpath(__file__))
tresults = Path(str(root + '/results'))

trans_matrix = {
	'tests/test_card_archetypes_endpoint.py' : 'Test Card Archetypes Endpoint',
	'tests/test_card_database_version_endpoint.py' : 'Test Card Database Version Endpoint',
	'tests/test_card_set_information_endpoint.py' : 'Test Card Set Information Endpoint',
	'tests/test_card_set_list_endpoint.py' : 'Test Card Set List Endpoint',
	'tests/test_random_card_endpoint.py' : 'Test Random Card Endpoint',
}

def count_testpass(aggtestpass):
	try:
		count = 0
		reg = re.compile("\d+ passed")
		matches = reg.findall(aggtestpass)
		for match in matches:
			count += int(match.split(' ')[0])
		return str(count)
	except Exception as exception:
		traceback.print_exc()
		return str('Err')

def count_testfail(aggtestpass):
	try:
		count = 0
		reg = re.compile("\d+ failed")
		matches = reg.findall(aggtestpass)
		for match in matches:
			count += int(match.split(' ')[0])
		return str(count)
	except Exception as exception:
		traceback.print_exc()
		return str('Err')

def get_tresults(tdir):
	tres = ''
	tlist = os.listdir(tdir)
	for log in tlist:
		logloc = Path(str(str(tdir) + '/' + log))
		with open(logloc) as f:
			content = f.readlines()
		for line in content:
			tres = str(tres + line)

	return tres

def get_short_test_results(aggtestpass):
	shorthand = ''
	tnames = []
	tpasses = []
	tfails = []
	try:
		reg = re.compile('.+test_.+\.py ')
		matches = reg.findall(aggtestpass)
		for match in matches:
			cleaned_match = str(match).split(' ')[0]
			tnames.append(trans_matrix[cleaned_match])

		reg = re.compile('FAILED .+test_.+\.py')
		matches = reg.findall(aggtestpass)
		for match in matches:
			cleaned_match = str(match).replace('=', '').split(' ')[1]
			tfails.append(trans_matrix[cleaned_match])

		reg = re.compile('\d+ passed')
		matches = reg.findall(aggtestpass)
		for match in matches:
			tpasses.append(str(match).replace('=', ''))

		for i in range(len(tnames)):
			shorthand += str(tnames[i] + '\n')
			if tnames[i] in tfails:
				count = 0
				for j in range(len(tfails)):
					if tnames[i] in tfails[j]:
						count += 1
				shorthand += str('\t' + str(count) + ' failed, ' + tpasses[i] + '\n')
			else:
				shorthand += str('\t' + tpasses[i] + '\n')
	except Exception as exception:
		traceback.print_exc()
		return 'Err'

	return shorthand

if __name__ == '__main__':
	# print(str('Current Working Directory: ' + str(Path.cwd())))
	if len(sys.argv) > 1:
		bday = sys.argv[1]
		bday = bday.replace('.', '-')
	else:
		bday = datetime.date.today().strftime('%Y-%m-%d')

	template_vars = {
	    'date' : str(datetime.datetime.now()).split('.')[0],
	    'numofpasses' : count_testpass(get_tresults(tresults)),
		'numoffails' : count_testfail(get_tresults(tresults)),
		'numoftests' : str(int(count_testpass(get_tresults(tresults))) + int(count_testfail(get_tresults(tresults)))),
	    'testresults': get_short_test_results(get_tresults(tresults)),
		'testoutput': get_tresults(tresults),
	}

	try:
		html_out = template.render(template_vars)
		hfile = open("report.html", "w")
		hfile.write(html_out)
		hfile.close()
		print(str('Report written to: ' + str(Path.cwd()) + '/report.html'))
	except Exception as exception:
		traceback.print_exc()

	print('END OF LINE.')
