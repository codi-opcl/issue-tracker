#!/usr/bin/env python3
\"\"\"OpenClaw Issue Tracker CLI\"\"\"

import json
import sys
import argparse
import uuid
import datetime

ISSUES_FILE = 'issues.json'

def load_issues():
    try:
        with open(ISSUES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_issues(issues):
    with open(ISSUES_FILE, 'w') as f:
        json.dump(issues, f, indent=2)

def add_issue(title, stakeholder):
    issues = load_issues()
    issue_id = str(uuid.uuid4())[:8]
    issue = {
        'id': issue_id,
        'title': title,
        'status': 'open',
        'history': [{
            'action': 'opened',
            'timestamp': datetime.datetime.now().isoformat(),
            'by': stakeholder
        }],
        'stakeholder': stakeholder
    }
    issues.append(issue)
    save_issues(issues)
    print(f'Added issue {issue_id}: {title}')

def list_issues():
    issues = load_issues()
    if not issues:
        print('No issues.')
        return
    for issue in issues:
        status = issue['status'].upper()
        print(f'{issue[\"id\"]} [{status}] {issue[\"title\"]} - {issue[\"stakeholder\"]}')

def close_issue(issue_id):
    issues = load_issues()
    for issue in issues:
        if issue['id'] == issue_id:
            issue['status'] = 'closed'
            issue['history'].append({
                'action': 'closed',
                'timestamp': datetime.datetime.now().isoformat(),
                'by': 'codi'
            })
            save_issues(issues)
            print(f'Closed {issue_id}')
            return
    print(f'Issue {issue_id} not found.')

def status_issue(issue_id):
    issues = load_issues()
    for issue in issues:
        if issue['id'] == issue_id:
            print(f'ID: {issue[\"id\"]}')
            print(f'Title: {issue[\"title\"]}')
            print(f'Status: {issue[\"status\"]}')
            print('History:')
            for h in issue['history']:
                print(f'  {h[\"action\"]} by {h.get(\"by\", \"system\")} at {h[\"timestamp\"]}')
            return
    print(f'Issue {issue_id} not found.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Issue Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('title')
    add_parser.add_argument('--stakeholder', required=True)

    list_parser = subparsers.add_parser('list')

    close_parser = subparsers.add_parser('close')
    close_parser.add_argument('id')

    status_parser = subparsers.add_parser('status')
    status_parser.add_argument('id')

    args = parser.parse_args()

    if args.command == 'add':
        add_issue(args.title, args.stakeholder)
    elif args.command == 'list':
        list_issues()
    elif args.command == 'close':
        close_issue(args.id)
    elif args.command == 'status':
        status_issue(args.id)
    else:
        parser.print_help()
