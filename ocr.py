from paddleocr import PaddleOCR
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = 'localhost'
serverPort = 9999

class OCRServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    img_path = './Snipaste_2022-04-19_18-37-19.png'
    result = ocr.ocr(img_path, cls=True)

    self.wfile.write(json.dumps({'result': str(result)}).encode())

  def do_POST(self):
    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    print("xxx!")

    print(self.rfile.read(int(self.headers['Content-Length'])))
    
    self.wfile.write(json.dumps({'result': 'haha'}).encode())
    # self.send_header('Content-Type', 'application/json')
    # self.end_headers()
    # ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    # img_path = './Snipaste_2022-04-19_18-37-19.png'
    # result = ocr.ocr(img_path, cls=True)

    # self.wfile.write(json.dumps({'result': str(result)}).encode())


if __name__ == "__main__":
  webServer = HTTPServer((hostName, serverPort), OCRServer)
  print("server started http://%s:%s" % (hostName, serverPort))

  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print('server stopped')


# ocr = PaddleOCR(use_angle_cls=True, lang='ch')
# img_path = './Snipaste_2022-04-19_18-37-19.png'
# result = ocr.ocr(img_path, cls=True)
# for line in result:
#   print(line)