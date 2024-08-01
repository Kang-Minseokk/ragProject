from flask import Blueprint, render_template, request, redirect, session
from openai import OpenAI
from rag_app.form import UserMsgForm

bp = Blueprint('chat', __name__, url_prefix='/chat')


@bp.route('/', methods=('POST', 'GET'))
def chat_home():
    form = UserMsgForm()
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        # Point to the local server
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        # 사용자의 입력에 대한 텍스트를 인식하자.
        user_msg = form.user_msg.data

        completion = client.chat.completions.create(
            model="teddylee777/EEVE-Korean-Instruct-10.8B-v1.0-gguf",
            messages=[
                {"role": "system", "content": "당신은 친절한 AI Assistant입니다. 답변을 할 때는 간결하게 답변을 하며, 신중하게 답변합니다."},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.7,
        )
        machine_response = completion.choices[0].message.content
        session['chat_history'].append({"role": "user", "content": user_msg})
        session['chat_history'].append({"role": "machine", "content": machine_response})

        session.modified = True

        return render_template('chat/chat_home.html', machine_response=machine_response,
                               form=form, chat_history=session['chat_history'])

    return render_template('chat/chat_home.html', form=form, machine_response='',
                           chat_history=session['chat_history'])




