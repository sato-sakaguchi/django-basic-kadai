from django.shortcuts import render, redirect

from django.views import View

import datetime

from .models import Topic
from .forms import TopicForm

# Create your views here.
# Viewを継承してビュークラスを作る。
class IndexView(View):
    # このgetメソッドはGETメソッドのリクエストが送られたときに発動する。
    def get(self, request):
        
        context = {}
        context["comment"]  = "Hello!!"
        context["numbers"]  = [ 1,2,3,4,5,6,7,8,9 ]

        context["score"]    = 70
        context["status"]   = True

        # Topicテーブルの全データになるので、topics
        context["topics"]   = Topic.objects.all()

        # 辞書型のリスト
        """
        context["topics"]   = [ { "id":1 , "comment":"Hello" },
                                { "id":2 , "comment":"Hey" },
                                { "id":3 , "comment":"aaaaaa" },
                                { "id":4 , "comment":"Hello" },
        ]
        """

        context["now"]      = datetime.datetime.now()

        """
        context = { "comment":"Hello!!" }
        """

        # 指定したテンプレートをレンダリングする。
        return render(request, "bbs/index.html", context)

    def post(self, request):
        
        print(request.POST)
        print(request.POST["comment"])

        # Topicのオブジェクトを作る
        # バリデーションされていない。モデルの制約に則っていないデータまで投稿されてしまう。
        # DBの整合性が保てない。検索・計算処理が正常に機能しなくなる。
        """
        topic   = Topic(comment=request.POST["comment"])
        topic.save()
        """

        # 送られたデータを引数にして、バリデーション(検証)する。
        form    = TopicForm(request.POST)

        # バリデーションチェックの結果を出力する .is_valid() が有る。
        # ルールに則っていれば True、そうでなければ False
        if form.is_valid():
            # DBに書き込み
            form.save()
        else:
            # エラーの理由を表示させる。
            print(form.errors)

        

        # DBへデータの書き込み処理
        #return render(request, "bbs/index.html")

        # urls.pyのapp_nameとnameを組み合わせてリダイレクト先を指定する。
        return redirect("bbs:index")

# urls.pyから呼び出せるようにする。.as_view()を使う。
index   = IndexView.as_view()