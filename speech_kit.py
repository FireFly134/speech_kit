import requests


def synthesize(folder_id, api_key, text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Api-Key ' + api_key,
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        #'voice': 'ermil',#'filipp',
        'folderId': folder_id
    }

    ### По ссылке ниже есть "Параметры в теле запроса" где исходя из того что забиваешь и выбираешь в форме выдает  то что записываем в переменную "data"
    ### https://cloud.yandex.ru/services/speechkit#demo
    ### https://cloud.yandex.ru/docs/speechkit/quickstart
    ### https://www.youtube.com/watch?v=Px1YyTj1h9M
#============================= ТУТ ЗАВИСАЕТ НА СЕРВЕРЕ LINUX ===============================#
    with requests.post(url, headers=headers, data=data, stream=True) as resp:
#============================= Все что дальше не обрабатывается ===============================#
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk


if __name__ == "__main__":
    output = "speech.ogg"
    folder_id = "Your folder_id"
    token = "Your token"
    text = "Синтез речи который без параметра voice"#"добрый вечер. Я научился синтезировать текст в речь. что будем делать дальше?"
    with open(output, "wb") as f:
        for audio_content in synthesize(folder_id, token, text):
            f.write(audio_content)
