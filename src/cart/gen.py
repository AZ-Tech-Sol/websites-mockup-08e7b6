import json, subprocess, urllib.request, concurrent.futures as cf
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
BASE = ("flat vector illustration, clean geometric shapes, limited palette of bright blue #009EFF, deep royal blue #0039B8, "
        "warm amber orange #FE9901 and off-white, on a plain very dark navy background #0E121A, subtle glow, modern tech brand style, no text, no letters, no people. ")
P = {'ftl-hector': "a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, standing at the ship's helm with a round steering control and a star map screen, inside a small square spaceship room with a visible square-grid floor, rounded door frames on the walls, and a small console showing a row of glowing skill pips, large and centered.", 'ftl-lena': 'a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, holding a wrench in one hand and a paintbrush in the other, happily repairing a glowing wall panel, inside a small square spaceship room with a visible square-grid floor, rounded door frames on the walls, and a small console showing a row of glowing skill pips, large and centered.', 'ftl-otto': 'a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, happily counting a small pile of shiny scrap metal pieces into a crate while holding a little receipt, inside a small square spaceship room with a visible square-grid floor, rounded door frames on the walls, and a small console showing a row of glowing skill pips, large and centered.', 'ftl-bjorn': 'a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, standing at a shield station giving a thumbs up, a glowing bubble shield dome around a small console, inside a small square spaceship room with a visible square-grid floor, rounded door frames on the walls, and a small console showing a row of glowing skill pips, large and centered.', 'ftl-desk': 'Four cute friendly cartoon robot mascots with soft rounded bodies and big smiling eyes, each in its own small square room of a cutaway spaceship with square-grid floors and doors between the rooms: one at the helm, one repairing a panel with a wrench, one counting scrap into a crate, one at a glowing shield station; a big friendly round clock with gears on the central wall, warm and welcoming, large and centered.'}

def gen(item):
    name, p = item
    body = json.dumps({"prompt": BASE + p, "model": "recraftv4_1_vector", "size": "1024x1024"}).encode()
    req = urllib.request.Request('https://external.api.recraft.ai/v1/images/generations', data=body, headers={'Content-Type':'application/json','Authorization':'Bearer '+K,'User-Agent':UA})
    try: d = json.loads(urllib.request.urlopen(req, timeout=200).read() or b'{}')
    except Exception as e: return name, 'ERR '+str(e)[:160]
    if 'data' not in d: return name, 'ERR '+json.dumps(d)[:200]
    svg = urllib.request.urlopen(urllib.request.Request(d['data'][0]['url'], headers={'User-Agent':UA}), timeout=120).read()
    open(name+'.svg','wb').write(svg); return name, f'ok {len(svg)//1024}KB'
with cf.ThreadPoolExecutor(3) as ex:
    for n, r in ex.map(gen, P.items()): print(n, r, flush=True)
