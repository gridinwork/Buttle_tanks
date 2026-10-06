"""Client for the co-op API.  python ai_client.py state | act <dir> [fire] [secs] | speed <0..1>"""
import json, socket, sys

def call(c, port=8765):
    with socket.create_connection(('127.0.0.1', port), timeout=3) as s:
        s.sendall((json.dumps(c) + '\n').encode()); return json.loads(s.makefile().readline())

def show(st):
    g = [list(r) for r in st['map']]
    def mark(x, y, ch):
        for dy in (0, 1):
            for dx in (0, 1):
                cx, cy = int(x) // 8 + dx, int(y) // 8 + dy
                if 0 <= cx < 26 and 0 <= cy < 26: g[cy][cx] = ch
    for e in st['enemies']: mark(e['x'], e['y'], 'A' if e['kind'] == 3 else 'E')
    for i, p in enumerate(st['players']):
        if p['alive']: mark(p['x'], p['y'], str(i + 1))
    for b in st['bullets']:
        cx, cy = int(b['x']) // 8, int(b['y']) // 8
        if 0 <= cx < 26 and 0 <= cy < 26: g[cy][cx] = '*'
    print('   ' + ''.join(str(i % 10) for i in range(26)))
    for i, r in enumerate(g): print('%2d ' % i + ''.join(r))
    print('stage', st['stage'], 'score', st['score'], 'enemies_left', st['enemies_left'], 'base_dead', st['base_dead'], 'gameover', st['gameover'], 'intro', st['intro'])
    for i, p in enumerate(st['players']): print('P%d' % (i + 1), p)
    for e in st['enemies']: print('enemy', e)
    print('bullets', st['bullets'])

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'state': show(call({'cmd': 'state'}))
    elif a[0] == 'mini': print(json.dumps(call({'cmd': 'mini'}), separators=(',', ':')))
    elif a[0] == 'act': print(call({'cmd': 'act', 'dir': a[1], 'fire': 'fire' in a, 'secs': float(next((x for x in a[2:] if x != 'fire'), .4))}))
    elif a[0] == 'speed': print(call({'cmd': 'speed', 'value': float(a[1])}))
