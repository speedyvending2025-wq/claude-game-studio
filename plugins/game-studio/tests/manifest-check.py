from pathlib import Path
import json
root=Path(__file__).parents[1]
manifest=json.loads((root/'.claude-plugin/plugin.json').read_text())
assert manifest['name']=='claude-game-studio-universal'
assert len(list((root/'skills').glob('*/SKILL.md'))) >= 79
assert len(list((root/'agents').glob('*.md'))) >= 50
for p in (root/'skills').glob('*/SKILL.md'):
    s=p.read_text()
    assert s.startswith('---\nname: ')
print('PASS: plugin structure and component counts')
