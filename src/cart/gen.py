import json, subprocess, urllib.request, concurrent.futures as cf
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
BASE = ("flat vector illustration, clean geometric shapes, limited palette of bright blue #009EFF, deep royal blue #0039B8, "
        "warm amber orange #FE9901 and off-white, on a plain very dark navy background #0E121A, subtle glow, modern tech brand style, no text, no letters, no people. ")
P = {'dz-hector': 'Portrait from the chest up, centered, on a plain solid very dark navy background with nothing else behind. A formidable, capable futuristic android crew member with sleek dark navy armor plating and bright blue edge lighting, a smooth dark glass faceplate showing only two calm glowing blue eyes, no mouth and no human features, broad confident shoulders, standing relaxed and ready, one hand resting on a glowing holographic navigation panel, a small glowing blue collar band, a small round mission patch on the shoulder. Serious, trustworthy and on your side, like a veteran starship pilot. Flat vector illustration, clean geometric shapes.'}

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
