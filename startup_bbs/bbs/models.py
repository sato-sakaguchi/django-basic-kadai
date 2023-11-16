from django.db import models

from django.utils import timezone


# Create your models here.
# モデルを作って、データベースの構造を決める。


# モデルクラス。1個分で、データベースのテーブル1個分
class Topic(models.Model):


    # models.Modelを継承した時点で、idフィールドは存在する。


    # カラム(列)ごとに入力するデータ形式を指定する。
    # 左辺のcommentはDBのカラム名、(Djangoのフィールド名)
    # 右辺のmodels.CharField() はカラムに記録するデータの形式、制約
    # この場合、制約は
    # 文字列型、2000文字まで、入力必須(デフォルトの制約)
    # verbose_nameはこのフィールドに対する説明。制約には影響しない。無くても機能はする。
    # max_length は CharField()において、指定必須。

    comment = models.CharField(verbose_name="コメント",max_length=2000)

    # 制約: 日付型、入力必須
    # デフォルト: レコード登録時の日時
    # 投稿日時のフィールドは予めモデル内に含めておいたほうが良い。
    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    # フィールドもしくはモデルの編集(追加・削除)をした場合は、マイグレーションをしてDBに反映させる。
    # python3 manage.py makemigrations  マイグレーションファイルを作る
    # python3 manage.py migrate DBにマイグレーションファイルを元に反映

    # 制約: 文字列型、入力必須、100文字まで
    # デフォルト: なし
    name    = models.CharField(verbose_name="投稿者の名前",max_length=100)