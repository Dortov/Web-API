from flask import Flask, jsonify, request
from calculation import Calc

app = Flask(__name__)


@app.route('/get_time', methods=['POST'])

def give_res():
    do = Calc()
    answer_dict = {}
    n = 1  # переменная для нумерации ответов в словаре answer_dict

    for i, test in enumerate(request.json):      # нумеруем и итерируем данные из нужной нам части запроса
        test_answer = do.appearance(test['data'])   # за расчетами обращаемся к классу в отдельном файле (calculate.py)
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
        answer_dict.setdefault(n, test_answer)
        n += 1
#    print(answer_dict)

    return jsonify(answer_dict)


if __name__ == '__main__':
    app.run()
