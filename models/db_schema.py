import os 

# ---------------------------------------------------------------------------
# localization
# ---------------------------------------------------------------------------
T.set_current_languages('en')

# if language is not set, default is japanese
if request.url and [i for i in request.url.split('/') if i in ['en']]!=[]:
    T.force('{0}'.format(request.uri_language))
elif request.url and [i for i in request.url.split('/') if i in ['jp']]!=[]:
    T.force('jp')
else:
    T.force('jp') #please don't change this and commit 


db.define_table('company',
    Field('company_name','string',length=20, requires=IS_NOT_EMPTY(), required=True, label=T('Company Name')),
    Field('company_description', 'string', length=128, required=False, label=T('Company Description'))
)

db.define_table('department',
    Field('department_name','string',length=20, requires=IS_NOT_EMPTY(), required=True, label=T('Deparment Name')),
    Field('department_description', 'string', length=128, required=False, label=T('Deparment Description')),
    Field('company_id', 'references company', requires=IS_IN_DB(db, 'company.id', '%(company_name)s'), required=True, label=T('Company '))
)
db.define_table('employee',
    Field('employee_fname','string',length=20, requires=IS_NOT_EMPTY(), required=True, label=T('Employee First Name')),
    Field('employee_mname','string',length=20, required=False, label=T('Employee Middle Name')),
    Field('employee_last','string',length=20, requires=IS_NOT_EMPTY(), required=True, label=T('Employee Last Name')),
    Field('employee_position', 'string', length=20, requires=IS_NOT_EMPTY(), required=True, label=T('Deparment Position')),
    Field('department_id', 'references department', requires=IS_IN_DB(db, 'department.id', '%(department_name)s'), required=True, label=T('Department '))
)

