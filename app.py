from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *



app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')
#UID or GID
UID=''
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

@app.route("/pum")
def pushmessage():
  try:
    line_bot_api.push_message(UID,TextSendMessage(text='Hello world!!!'))
    return "Hello Flask!"
  except:
    print('error')



        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
