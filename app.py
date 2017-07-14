from flask import Response, Flask, render_template, request, redirect, url_for, json
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'techsitution4'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

@app.route('/audits', methods=['GET', 'POST'])
def audits():
	if request.method == 'GET':
		# Query to retrieve data from DB
		audits = mongo.db.audit.find()
		return render_template('audits.html', audits=audits)
		
	elif request.method == 'POST':
		data = request.form
		select = data['select1'] # Getting audit name value
		select2 = data['select2'] # Getting audit ref num
		accident = data['Accident']
	#	incident = data['Incident']
	#	procedural = data['Procedural']
	#	failure = data['Failure']
	#	hazard = data['Hazard']

	#	location = data['location']
	#	date = data['date']
	#	time = data['time']
	#	duration = data ['Duration']
	#	ATS = data ['ATS']
	#	ATS1 = data ['ATS1']
	#	ATS2 = data ['ATS2']
	#	ATS3 = data ['ATS3']
	#	ATS4 = data ['ATS4']
	#	service = data ['Service']
	#	eqman = data ['eqman']
	#	frequency = data ['frequency']
	#	callsign = data ['Callsign']
	#	eqlocation = data ['eqlocation']
	#	atsfac = data ['ATSfac']
	#	atsfac1 = data ['ATSfac1']
	#	atsfac2 = data ['ATSfac2']
	#	atsfac3 = data ['ATSfac3']
	#	atsfac4 = data ['ATSfac4']
	#	atsfac5 = data ['ATSfac5']
	#	atsfac6 = data ['ATSfac6']
	#	atsfac7 = data ['ATSfac7']
	#	atsfac8 = data ['ATSfac8']
	#	eqs = data ['eqs']
	#	select3 = data ['select3']
	#	eqs1 = data ['eqs1']
	#	select4 = data ['select4']
	#	eqs2 = data ['eqs2']
	#	select5 = data ['select5']
	#	eqs3 = data ['eqs3']
	#	select6 = data ['select6']
	#	select7 = data ['select7']
	#	ats5 = data ['ATS5']
	#	ats6 = data ['ATS6']
	#	ats7 = data ['ATS7']
	#	ats8 = data ['ATS8']
	#	eqman1 = data ['eqman1']
	#	ats9 = data ['ATS9']
	#	ats10 = data ['ATS10']
	#	ats11 = data ['ATS11']
	#	select8 = data ['select8']
	#	select9 = data ['select9']
	#	ats12 = data ['ATS12']
	#	ats13 = data ['ATS13']
	#	ats14 = data ['ATS14']
	#	ats15 = data ['ATS15']
	#	name = data ['name']
	#	company = data ['company']
	#	number = data ['number']
	#	location1 = data ['location1']
	#	stime = data ['stime']
	#	date1 = data ['date1']
	#	company1 = data ['company1']
	#	email = data ['email']
		#Query for inserting into DB
		mongo.db.audit.insert({
	 	"select": select,
	 	"select2": select2,
	 	"Accident": accident
		#"Incident": incident,
		#"Procedural": procedural,
		#"Failure": failure
	#		"Hazard": hazard,
	#		"location": location,
	#		"date": date
	#		"time": time
	#		"Duration": duration,
	#		"ATS": ATS,
	#		"ATS1": ATS1,
	#		"ATS2": ATS2,
	#		"ATS3": ATS3,
	#		"ATS4": ATS4,
	#		"Service": service,
	#		"eqman": eqman,
	#		"frequency": frequency,
	#		"Callsign": callsign,
	#		"eqlocation": eqlocation,
	#		"ATSfac": atsfac,
	#		"ATSfac1": atsfac1,
	#		"ATSfac2": atsfac2,
	#		"ATSfac3": atsfac3,
	#		"ATSfac4": atsfac4,
	#		"ATSfac5": atsfac5,
	#		"ATSfac6": atsfac6,
	#		"ATSfac7": atsfac7,
	#		"ATSfac8": atsfac8,
	#		"eqs": eqs,
	#		"select3": select3,
	#		"eqs1": eqs1,
	#		"select4": select4,
	#		"eqs2": eqs2,
	#		"select5": select5,
	#		"eqs3": eqs3,
	#		"select6": select6,
	#		"select7": select7,
	#		"ATS5": ats5,
	#		"ATS6": ats6,
	#		"ATS7": ats7,
	#		"ATS8": ats8,
	#		"eqman1": eqman1,
	#		"ATS9": ats9,
	#		"ATS10": ats10,
	#		"ATS11": ats11,
	#		"select8": select8,
	#		"select9": select9,
	#		"ATS12": ats12,
	#		"ATS13": ats13,
	#		"ATS14": ats15,
	#		"name": name,
	#		"company": company,
	#		"number": number,
	#		"location1": location1,
	#		"stime": stime,
	#		"date1": date1,
	#		"company1": company1,
	#		"email": email
			 })
		return redirect(url_for('audits'))

# @app.route('/audits', methods=['GET', 'POST'])
# def audits():
# 	if request.method == 'GET':
# 		audits = mongo.db.audit.find()
# 		return render_template("audits.html", audits=audits)


# Showing specific audit
@app.route('/audits/<string:audit_id>', methods=['GET', 'POST'])
def show(audit_id):
	if request.method == 'GET':
		# Query to get specific audit
		audit = mongo.db.audit.find_one({"_id": ObjectId(audit_id)})

        return render_template('show.html', audit=audit)

# Editing audit
@app.route('/audits/<string:audit_id>/edit', methods=['GET', 'POST'])
def edit(audit_id):
	if request.method == 'GET':
		audit = mongo.db.audit.find_one({"_id": ObjectId(audit_id)})
		return render_template('edit.html', audit=audit)
	elif request.method == 'POST':
		edit_data = request.form
		mongo.db.audit.update({"_id": ObjectId(audit_id)}, {"$set":{
			"select": edit_data['select'],
	 		"select2": edit_data['select2']
		}})
		return redirect(url_for("show", audit_id=audit_id))
# Delete the specific audit

@app.route('/audits/delete', methods=['POST'])
def delete():
	if request.method == 'POST':
		audit_id = request.form["audit_id"]
		# Query to sepecific audit
		mongo.db.audit.remove({"_id": ObjectId(audit_id)})
		#return redirect(url_for('audits'))
		return Response(response=json.dumps(
			{"STATUS": "SUCCESS"}),
			status=200,
			mimetype="application/json")

if __name__ == '__main__':
	app.run(port=5015,host='0.0.0.0', debug=True)
