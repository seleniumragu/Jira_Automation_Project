from jira import JIRA

jira = JIRA(basic_auth=('ragu.sekaran@iherb.com','LccQZtLATnGgfbrRcTT096FF'), options={'server': 'https://iherbglobal.atlassian.net/'})
issue = jira.issue('PROMO-1468')
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)