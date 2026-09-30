import json, subprocess, urllib.request, concurrent.futures as cf
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
BASE = ("flat vector illustration, clean geometric shapes, limited palette of bright blue #009EFF, deep royal blue #0039B8, "
        "warm amber orange #FE9901 and off-white, on a plain very dark navy background #0E121A, subtle glow, modern tech brand style, no text, no letters, no people. ")
P = {
 'starter-cart': "A single street fruit cart filling most of the frame, a large umbrella in amber orange and royal blue, crates of oranges and apples, and a blank wooden sign board hanging proudly on the front of the cart, standing on a corner of off-white sidewalk tiles with a blue curb, large and centered.",
 'team-shop': "A single two-storey shop building filling most of the frame, a wide striped awning in blue and off-white, two big display windows with goods, an open double door, a second floor with lit windows, standing on a corner of off-white sidewalk tiles with a blue curb, large and centered.",
 'ai-edits': "A glowing paper envelope with small motion lines flying toward a small street fruit cart with a striped umbrella, tiny sparkles where it arrives, standing on off-white sidewalk tiles, playful metaphor for emailing a change that gets made automatically, large and centered.",
 'ai-care': "A small friendly rounded robot on a short ladder repainting the sign board above a small shop storefront with a striped awning, a clipboard with a check mark resting at the foot of the ladder, standing on off-white sidewalk tiles, large and centered.",
 'ai-employee': "A small friendly rounded robot sitting at a tidy desk with a laptop, a large round wall clock with visible gears behind it, inside a modern industrial building interior with big windows glowing amber, large and centered.",
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
