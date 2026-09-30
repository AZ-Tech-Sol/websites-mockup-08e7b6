import json, subprocess, urllib.request, concurrent.futures as cf
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
BASE = ("flat vector illustration, clean geometric shapes, limited palette of bright blue #009EFF, deep royal blue #0039B8, "
        "warm amber orange #FE9901 and off-white, on a plain very dark navy background #0E121A, subtle glow, modern tech brand style, no text, no letters, no people. ")
P = {
 'fr-hector': "a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, warm and approachable,  waving hello from behind a cozy front desk with a little bell and a neat stack of envelopes, large and centered, on off-white floor tiles.",
 'fr-lena': "a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, warm and approachable,  wearing a tiny beret, holding a paintbrush and happily painting a flower on a small shop's awning, large and centered, on off-white sidewalk tiles.",
 'fr-otto': "a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, warm and approachable,  wearing small round glasses, happily holding up a paper receipt with a check mark next to a little stack of coins, large and centered, on off-white floor tiles.",
 'fr-bjorn': "a cute friendly cartoon robot mascot with a soft rounded body, big round glowing smiling eyes and a happy smile, warm and approachable,  wearing a small helmet, giving a thumbs up while holding a friendly rounded shield with a heart-shaped keyhole, large and centered, on off-white floor tiles.",
 'fr-desk': "Four cute friendly cartoon robot mascots with soft rounded bodies and big smiling eyes, working happily together around one long desk under a big friendly round wall clock with gears, one waving, one painting, one holding a receipt, one holding a shield, warm and welcoming, large and centered.",
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
