from jira.client import JIRA

jira_options={'server': 'https://iherbglobal.atlassian.net'}
jira=JIRA(options=jira_options,basic_auth=('ragu.sekaran@iherb.com','LccQZtLATnGgfbrRcTT096FF'))

#Creating an issue:

new_issue = jira.create_issue(project={'key': "PROMO"}, summary='New issue Demo',   description='Look into this one', issuetype={'name': 'Bug'})

# or creating issues using dict:

issue_dict = {
    'project': {'key': "PROMO"},
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Task'},
}
new_issue = jira.create_issue(fields=issue_dict)
summary = new_issue.fields.summary
issue_type = new_issue.fields.issuetype.name
description = new_issue.fields.description
reporter = new_issue.fields.reporter.displayName
status = new_issue.fields.status
comment = new_issue.fields.comment
print('ticket: ', new_issue, summary)
print(new_issue)
print(description)
print(status)
print(reporter)
print(comment)