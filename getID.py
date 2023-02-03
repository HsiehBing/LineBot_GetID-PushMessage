from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#======python的函數庫==========
import tempfile, os
import logging
#======python的函數庫==========

app = Flask(__name__)

if __name__!= '__main__':
  gunicorn_logger = logging.getLogger('gunicorn.error')
  app.logger.handlers = gunicorn_logger.handlers
  app.logger.setLevel(gunicorn_logger.level)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

# Channel Access Token
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')



#監聽所有來自 /callback 的 Post Request
#######
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400, "Invalid signature. Please check your channel access token/channel secret.")
    return "OK" 
#########

@app.route("/")
def hello():
  
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    return "Hello Flask!"


#########
#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '?' in msg[0]:
        message =TextSendMessage("123") 
        line_bot_api.reply_message(event.reply_token, message)
        print(f'{event.source.user_id}')

        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
