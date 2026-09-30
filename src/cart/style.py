import json, subprocess, urllib.request, concurrent.futures as cf, uuid
K = subprocess.run(['op','item','get','Recraft AI','--vault','Cortana','--fields','API Key','--reveal'],capture_output=True,text=True).stdout.strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'
# create a style from the cart
b = uuid.uuid4().hex
data = open('ref-cart.png','rb').read()
body = (f'--{b}\r\nContent-Disposition: form-data; name="style"\r\n\r\nvector_illustration\r\n'
        f'--{b}\r\nContent-Disposition: form-data; name="file1"; filename="ref.png"\r\nContent-Type: image/png\r\n\r\n').encode()+data+f'\r\n--{b}--\r\n'.encode()
req = urllib.request.Request('https://external.api.recraft.ai/v1/styles', data=body, headers={'Content-Type':'multipart/form-data; boundary='+b,'Authorization':'Bearer '+K,'User-Agent':UA})
sid = json.loads(urllib.request.urlopen(req, timeout=120).read())['id']; print('style', sid, flush=True)
open('style_id.txt','w').write(sid)
P = {
 'storefront': "a single small shop storefront on a city street corner, big display window with goods, a striped awning, an open door, a potted plant by the door, sidewalk tiles in front, on a plain very dark navy background, no text, no people",
 'industrial': "a single modern industrial building, a small factory or warehouse with a sawtooth roof, big loading doors, a few lit windows, a delivery truck at the dock, on a plain very dark navy background, no text, no people",
}
def gen(item):
    name, p = item
    body = json.dumps({"prompt": p, "style_id": sid, "size": "1024x1024"}).encode()
    r = urllib.request.Request('https://external.api.recraft.ai/v1/images/generations', data=body, headers={'Content-Type':'application/json','Authorization':'Bearer '+K,'User-Agent':UA})
    try: d = json.loads(urllib.request.urlopen(r, timeout=200).read() or b'{}')
    except urllib.error.HTTPError as e: return name, 'ERR '+e.read().decode()[:200]
    if 'data' not in d: return name, 'ERR '+json.dumps(d)[:200]
    svg = urllib.request.urlopen(urllib.request.Request(d['data'][0]['url'], headers={'User-Agent':UA}), timeout=120).read()
    open(name+'.svg','wb').write(svg); return name, f'ok {len(svg)//1024}KB'
with cf.ThreadPoolExecutor(2) as ex:
    for n, r in ex.map(gen, P.items()): print(n, r, flush=True)
