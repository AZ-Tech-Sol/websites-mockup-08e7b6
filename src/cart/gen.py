import json, subprocess, urllib.request, concurrent.futures as cf
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
BASE = ("flat vector illustration, clean geometric shapes, limited palette of bright blue #009EFF, deep royal blue #0039B8, "
        "warm amber orange #FE9901 and off-white, on a plain very dark navy background #0E121A, subtle glow, modern tech brand style, no text, no letters, no people. ")
P = {'hx-mecha': 'Portrait from the chest up, centered, on a plain solid very dark navy background with nothing else behind. A heroic anime-style mecha hero, a friendly giant-robot ally: sleek angular armor in royal blue and white with bright electric blue accents and gold trim, a sculpted helmet with a crest and a sharp visor showing two determined glowing eyes under angled brow plates, a confident slight smile on a small silver faceplate, shoulders squared, one fist raised in a thumbs-up, radiating courage and warmth. The heroic team leader who has your back. Flat vector illustration, clean bold shapes, dynamic lighting.', 'hx-ranger': 'Portrait from the chest up, centered, on a plain solid very dark navy background with nothing else behind. A heroic color-coded team hero in sleek futuristic power armor, royal blue with white panels and a bright electric blue chest emblem shaped like a gear, a streamlined helmet with a wide dark visor showing two bright determined eyes and expressive angled brow lights, standing in a confident heroic pose, one hand raised in a salute, energetic and warm, the dependable leader of the squad. Flat vector illustration, clean bold shapes, dynamic lighting.'}

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
