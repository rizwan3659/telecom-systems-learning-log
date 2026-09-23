"""Validate self-reported progress and render public Markdown; does not run the lab."""
import argparse
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
LABELS = {'not_started': 'Not started', 'in_progress': 'In progress', 'blocked': 'Blocked', 'done': 'Done'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Validate and reject stale generated files')
    args = parser.parse_args()
    data = json.loads((ROOT / 'progress.json').read_text(encoding='utf-8'))
    tasks = data['deliverables']
    seen = set()
    for task in tasks:
        if task['id'] in seen or task['status'] not in LABELS:
            raise ValueError('Duplicate ID or invalid status: ' + task['id'])
        seen.add(task['id'])
        if task['day'] not in range(1, 6):
            raise ValueError('Invalid day: ' + task['id'])
        paths = [task['template']] + task['evidence']
        for link in paths:
            if link.startswith('https://'):
                continue
            path = (ROOT / link).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                raise ValueError('Missing/unsafe local evidence path: ' + link)
        if task['updated']:
            date.fromisoformat(task['updated'])
        if task['status'] != 'not_started' and not task['updated']:
            raise ValueError('Active work needs an update date: ' + task['id'])
        if task['status'] == 'blocked' and not task['notes'].strip():
            raise ValueError('Blocked work needs a reason: ' + task['id'])
        if task['status'] == 'done':
            if not (task['evidence_ready'] is True and task['evidence'] and task['result'].strip() and task['limitations'].strip()):
                raise ValueError('Done needs evidence, result and limitations: ' + task['id'])
            if 'TEMPLATE — not evidence yet' in (ROOT / task['template']).read_text(encoding='utf-8'):
                raise ValueError('Replace the unfinished template: ' + task['id'])
    completed = sum(t['status'] == 'done' for t in tasks)
    header = f'# Progress dashboard\n\n**Week 1: {completed}/{len(tasks)} deliverables complete ({completed / len(tasks):.0%}).**\n\n'
    header += 'Planning materials are published. Technical completion requires evidence; all statuses are self-reported. These are equal-weight deliverable counts, not an estimate of hours or mastery. CI validates the learning record, not the lab.\n\n'
    header += '| Day | Completed | Status | Guide |\n|---|---|---|---|\n'
    for day in range(1, 6):
        group = [t for t in tasks if t['day'] == day]
        done = sum(t['status'] == 'done' for t in group)
        status = 'Done' if done == len(group) else 'Blocked' if any(t['status'] == 'blocked' for t in group) else 'In progress' if any(t['status'] != 'not_started' for t in group) else 'Not started'
        header += f'| {day} | {done}/{len(group)} | {status} | [Day {day}](weeks/week-01/days/day-{day:02d}.md) |\n'
    header += '\n## Deliverables\n\n'
    showcase = '# Week 1 deliverable showcase\n\nThis page lists the evidence visitors can inspect. A template is not a completed result.\n\n'
    for t in tasks:
        state = LABELS[t['status']]
        header += f"### {t['id']} — {t['title']}\n\n**{state}** · Day {t['day']} · Updated: {t['updated'] or 'not recorded'}\n\n{t['acceptance']}\n\n[Work record]({t['template']})\n\n"
        if t['notes']:
            header += t['notes'] + '\n\n'
        rel = str(Path(t['template']).relative_to('weeks/week-01')).replace('\\', '/')
        showcase += f"## {t['id']} — {t['title']}\n\n**{state}.** [Work record]({rel})\n\n"
        if t['status'] == 'done':
            for link in t['evidence']:
                showlink = link if link.startswith('https://') else '../../' + link
                header += f'- [Evidence]({link})\n'
                showcase += f'- [Evidence]({showlink})\n'
            header += f"\nResult: {t['result']}\n\nLimitations: {t['limitations']}\n\n"
            showcase += f"\nResult: {t['result']}\n\nLimitations: {t['limitations']}\n\n"
        else:
            showcase += 'Evidence pending. No successful experiment is claimed.\n\n'
    header += '## Updating this dashboard\n\nEdit progress.json, then run `python scripts/update_progress.py`. See [the update guide](CONTRIBUTING.md).\n'
    outputs = {'PROGRESS.md': header, 'weeks/week-01/SHOWCASE.md': showcase}
    for filename, text in outputs.items():
        text = text.rstrip() + '\n'
        path = ROOT / filename
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                raise ValueError('Generated page is stale: ' + filename)
        else:
            path.write_text(text, encoding='utf-8')
    print(f'Valid: {completed}/{len(tasks)} deliverables complete. Lab not executed by this checker.')

if __name__ == '__main__':
    main()
