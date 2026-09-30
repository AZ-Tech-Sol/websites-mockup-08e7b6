import json, subprocess, urllib.request, concurrent.futures as cf
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
BASE = ("flat vector illustration, clean geometric shapes, limited palette of bright blue #009EFF, deep royal blue #0039B8, "
        "warm amber orange #FE9901 and off-white, on a plain very dark navy background #0E121A, subtle glow, modern tech brand style, no text, no letters, no people. ")
P = {
 'bot-hector': "A friendly rounded robot receptionist at a front desk sorting a stack of glowing envelopes into three labeled-by-color trays, a small bell on the desk, large and centered, standing on off-white floor tiles.",
 'bot-lena': "A friendly rounded robot designer holding a paintbrush, repainting the striped awning of a small shop storefront, a color palette in its other hand, large and centered, standing on off-white sidewalk tiles.",
 'bot-otto': "A friendly rounded robot bookkeeper at a small desk with an open ledger book, a stack of coins and a calculator, a paper invoice with a check mark, large and centered, on off-white floor tiles.",
 'bot-bjorn': "A friendly rounded robot security guard holding a large glowing shield with a keyhole, standing in front of a small server rack with blinking lights, large and centered, on off-white floor tiles.",
}
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
