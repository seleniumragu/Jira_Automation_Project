from jira import JIRA

user = 'ragu.sekaran@iherb.com'
apikey = 'LccQZtLATnGgfbrRcTT096FF'
server = 'https://iherbglobal.atlassian.net'

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )

ticket = 'PROMO-12345'
issue = jira.issue(ticket)
summary = issue.fields.summary

description = issue.fields.description
status = issue.fields.status
comment = issue.fields.comment
jira.create_issue(ticket)
print('ticket: ', ticket, summary)
print(description)
print(status)
print(comment)

