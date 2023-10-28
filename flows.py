#!/usr/bin/env python3

from PIL import Image
import io, time, gzip
import brotli

def response(flow):
  if "content-type" in flow.response.headers and "content-length" in flow.response.headers:
    ru = str(flow.request.url)
    ae = str(flow.request.headers["accept-encoding"])
    ct = str(flow.response.headers["content-type"])
    cl = int(flow.response.headers["content-length"])
    s = io.BytesIO(flow.response.content)
    s2 = io.BytesIO()
    if (cl) > 10000:

     # jpeg を quality 10/100 に変換する
     if (ct) [0:10] == ("image/jpeg"):
         print("*** start %s ***" % (ru))
         start = time.time()
         img = Image.open(s)
         # img.save(s2, "jpeg", quality=10, optimize=True, progressive=True)
         img.save(s2, "webp", quality=0)
         flow.response.content = s2.getvalue()
         ct2 = str(flow.response.headers["content-type"])
         cl2  = int(flow.response.headers["content-length"])
         i = int(cl2 /cl * 100)
         elapsed_time = time.time() - start
         print("*** compressed %s percent, size = %s/%s bytes, %s to %s, %s is processed, %s sec ***" % (i, cl2, cl, ct, ct2, ru, elapsed_time))
         #return

     # png を compress_level=9, 8bit に変換する
     if (ct) [0:9] == ("image/png"):
         print("*** start %s ***" % (ru))
         start = time.time()
         # img = Image.open(s).convert(mode='P', palette=Image.ADAPTIVE, colors=8)
         # img.save(s2, "png", compress_level=9, bits=8)
         img = Image.open(s).convert(mode='P', palette=Image.ADAPTIVE)
         img.save(s2, "webp", quality=0)
         flow.response.content = s2.getvalue()
         ct2 = str(flow.response.headers["content-type"])
         cl2  = int(flow.response.headers["content-length"])
         i = int(cl2 /cl * 100)
         elapsed_time = time.time() - start
         print("*** compressed %s percent, size = %s/%s bytes, %s to %s, %s is processed, %s sec ***" % (i, cl2, cl, ct, ct2, ru, elapsed_time))
         return

     # webp を quality 10/100 に変換する
     if (ct) [0:10] == ("image/webp"):
         print("*** start %s ***" % (ru))
         start = time.time()
         img = Image.open(s)
         img.save(s2, "webp", quality=0)
         flow.response.content = s2.getvalue()
         ct2 = str(flow.response.headers["content-type"])
         cl2  = int(flow.response.headers["content-length"])
         i = int(cl2 /cl * 100)
         elapsed_time = time.time() - start
         print("*** compressed %s percent, size = %s/%s bytes, %s to %s, %s is processed, %s sec ***" % (i, cl2, cl, ct, ct2, ru, elapsed_time))
         return

     if (ct) [0:9] == ("image/gif"):
         print("*** start %s ***" % (ru))
         start = time.time()
         img = Image.open(s)
         img.save(s2, "webp", quality=0)
         flow.response.content = s2.getvalue()
         ct2 = str(flow.response.headers["content-type"])
         cl2  = int(flow.response.headers["content-length"])
         i = int(cl2 /cl * 100)
         elapsed_time = time.time() - start
         print("*** compressed %s percent, size = %s/%s bytes, %s to %s, %s is processed, %s sec ***" % (i, cl2, cl, ct, ct2, ru, elapsed_time))
         return
