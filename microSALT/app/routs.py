import os
import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from microSALT import db
from microSALT.tables.samples import Samples
from microSALT.tables.seq_types import Seq_types
from microSALT import app


samples = Samples.query.all()
for s in samples:
    print dir(s)

@app.route('/microSALT/')
def start_page():
    samples = Samples.query.all()
    return render_template('templates/start_page.html',
        blast  = samples)


#@app.route('/microSALT/<sample>')
#def sample_page(sample):
#    blast = Samples.query.filter_by(CG_ID_sample=sample)
#    #print dir(blast[0])
#    return render_template('sample_page.html',
#        blast  = blast,
#        sample_name = sample,
#        example_sample = blast[0])
