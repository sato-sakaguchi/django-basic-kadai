from django.urls import path

# 別のPythonファイルを読む。
from . import views

app_name    = "bbs"
urlpatterns = [
    # トップページにアクセスしてきた時、views.pyの中に有るindexという処理を呼び出す。
    path("", views.index, name="index"),
]