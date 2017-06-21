#! C:/Python34
# -*- encoding:utf-8 -*-
import html.parser, cgi, shelve, os, sys


fieldnames =('name', 'age', 'salary', 'job')
form = cgi.FieldStorage()
print('Content-type: text/html\n')
sys.path.insert(0, os.getcwd())



replyhtml = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Reply People Form</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.10/semantic.min.css" />
</head>
<body>
    <main>
        <form action="./cgi02.py"
              method="post"
              class="ui form"
        >
            <div class="fields">
                <div class="ui inverted input"
                    style="display: block;">
                    <label for="key">Key</label>
                    <input name="key" type="text"
                        placeholder="Key" value="%(key)s" />
                </div>
                <br/>
                $FIELDS$
            </div>

            <div class="handlers">
                <button type="submit"
                        class="ui button blue"
                        value="Fetch"
                >Fetch!</button>

                <button type="submit"
                        class="ui button orange"
                        value="Update"
                >Update!</button>

                <button type="submit"
                        class="ui button yellow"
                        value="Remove"
                >Remove!</button>

                <button type="reset"
                        class="ui button purple"
                >Clear fields!</button>
            </div>
        </form> 
        <p>$REPLY$</p>
    </main>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"
            integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
            crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.10/semantic.min.js"
            integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
            crossorigin="anonymous"></script>
</body>
</html>"""

fieldhtml = """
    <div class="ui inverted input"
        style="display: block;">
        <label for="%s">%s</label>
        <input name="%s" type="text"
        placeholder="%s" value="%%(%s)s"/>
    </div>
    <br/>
"""
fieldshtml = ''

for fieldname in fieldnames:
    fieldnameUpperFirstLetter = fieldname[1].upper() + fieldname[1:]
    fieldshtml += fieldhtml % ((fieldname,) * 5)

replyhtml = replyhtml.replace('$FIELDS$', fieldshtml)

def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing a key or just the record doesn\'t exist. You can try an another key.'
    return fields


def updateRecord(db, form):
    # try:
    #     key = form['key']
    #     record = db[key]
    #     for field in record:
    #         record[field] = form[field]
    #     fields = record.__dict__
    #     fields['key'] = key
    # except:
    #     fields = dict.fromkeys(fieldnames, '?')
    #     fields['key'] = 'Missing a key or just the record doesn\'t exist. You can try an another key.'
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input.'
    else:
        key = form['key'].value

    if key in db:
        record = db[key]  # изменить существующую запись
    else:
        #from sys.modules import db  # создать/сохранить новую
        from gui.db.person import Person  # создать/сохранить новую
        record = Person(name='?', age='?')  # eval: строки должны быть
    # заключены в кавычки
    for field in fieldnames:
        setattr(record, field, eval(form[field].value))
    db[key] = record
    fields = record.__dict__
    fields['key'] = key
    return fields


def removeRecord(db, form):
    try:
        key = form['key']
        record = db[key]
        fields = dict.fromkeys(fieldnames, '')
        fields['key'] = 'Record was removed successfully.'
        del record
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing a key or just the record doesn\'t exist. You can try an another key.'
    return fields

def executeAction(action, db, form):
    return {
        'Fetch': fetchRecord(db, form),
        'Update': updateRecord(db, form),
        'Remove':  removeRecord(db, form)
    }[action]


db = shelve.open('people-shelve')
action = form['action'].value if 'action' in form else None
try:
    fields = executeAction(action, db, form)
    if (action):
        # action+='ed'
        state = action + 'ed'
except:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing a key or just the record doesn\'t exist. You can try an another key.'
    state = 'Nothing happen'
db.close()
replyhtml.replace('$REPLY$', state)
print(replyhtml % htmlize(fields))
 #print('<div>action value is=>%s</div><br />' % form['action'].value)


