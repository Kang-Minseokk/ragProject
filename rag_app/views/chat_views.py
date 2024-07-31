from flask import Blueprint, render_template, request
from openai import OpenAI
from ..form import UserinputForm

bp = Blueprint('chat', __name__, url_prefix='/chat')


@bp.route('/', methods=('POST', 'GET'))
def chat_home():


    if request.method == 'GET':
        return render_template('chat/chat_home.html')

    if request.method == 'POST':
        # Point to the local server
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

        # 사용자의 입력에 대한 텍스트를 인식하자.


        completion = client.chat.completions.create(
            model="teddylee777/EEVE-Korean-Instruct-10.8B-v1.0-gguf",
            messages=[
                {"role": "system", "content": "Always answer in rhymes."},
                {"role": "user", "content": "안녕하세요! 반가워요"}
            ],
            temperature=0.7,
        )

        return render_template('404_error.html', machine_response=completion.choices[0].message)
    else:
        return render_template('404_error.html')





