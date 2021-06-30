﻿実案件課題　メルカリ、ラクマ、Amazon物販業務効率化ツール
====
本タスクは、実際の案件の内容をタスク化した応用的なものです。  
Djangoの課題１～４およびその前提知識を習得していることを前提しておりますので、細かな機能の説明は省略しております。

この講座で扱うWebサイトの完成形は下記の動画を参照してください。  
https://youtu.be/7jiWb7vzoNE

## Django側の構築
### DockerでMySQLを構築、起動
dockerをインストールして、プロジェクトルートで以下コマンドを実行する。  
dockerのプロセスは常に起動した状態にする必要があるため、dockerコマンド実行後は  
別のターミナルを開いて作業を行う。  
```
docker-compose up --buld
```

### Python仮想環境の作成、ライブラリインストール、開発サーバー起動確認
venvを作成して有効化後、requirements.txtをinstall  
```
python -m venv venv
venv/Scripts/activate ※windows
. venv/bin/activate ※MacOS/Linux
pip install -r requirements.txt
```

開発用環境設定ファイル.env.devを.envにリネーム  
.env.dev →　.env  
※.envファイルを読み込むことで、開発環境と本番環境の差異を吸収する  
今回は、開発環境用の.envファイルのみを用意している。

初回migrationを実施して、superuserを作成、runserver起動確認
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 課題0:Djangoプロジェクト作成、アプリの作成
Djangoプロジェクトを任意の名称で作成し、以下の４つのアプリを作成します。  
settings.pyにもアプリ名を追記してください。  
```
mypage:マイページ関連
users:パスワード変更  
setting:設定関連（ASIN登録や除外設定など）  
syuppin:出品関連（商品一覧やExcel出力）  
```

### 各種フォルダの作成
以下のフォルダをプロジェクトルートに作成する。  
static:css/js等の静的ファイルを格納する  
templates:HTMLテンプレートファイルを格納する  
※アプリ毎に作成する方式もあるが、プロジェクトルートに１つ作成する方が管理しやすいのでオススメ。

既定では、アプリ配下のtemplatesを参照するため、templatesの場所を以下のDIRSで指定することで変更する。  
settings.py
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # templateをプロジェクト直下に配置するための設定
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Bootstrapテンプレートを適用
案件では、顧客の要望に合わせて適切なテンプレートを使用します。  
特に要望がない場合は、常に共通で使うテンプレートを決めておくと、工数が削減できます。  
※最近のモダン開発では、BootstrapよりもTailwind等の方が自由度が高く好まれる傾向にありますが  
多少難易度が高いため、本講座ではBootstrapを使用します。

本講座では、以下のテンプレートを使用します。  
https://coliss.com/articles/build-websites/operation/work/free-admin-template-stisla.html

その他のテンプレートの一例）Bootstrap5  
Volt公式  
https://github.com/themesberg/volt-bootstrap-5-dashboard  
Dango用にカスタマイズした版  
https://github.com/marutoraman/django-bootrap-template


#### 課題1:base.htmlへのテンプレート組み込み
以下を参照して、１からbase.htmlにテンプレートを組み込んでください。  
案件では、基本的には過去案件のコピペが可能ですが、新規のテンプレートを適用する場合は  
以下の作業を行う必要があります。

- 以下からテンプレート一式ダウンロードする  
https://github.com/stisla/stisla

- モジュールのコピー  
assetsフォルダをtemplatesフォルダにコピーする

- base.htmlの作成  
ダウンロードしたファイルのpages/layout-default.htmlをtemplatesにコピーして、base.htmlにリネームする。

```
<section class="section">
```
の配下の要素を全て削除する。  
section内は具体的なページ毎のコンテンツに相当するため、baseに記述は不要。  
（sectionタグ自体は削除しない。sectionの中身(下層)の要素を削除するが、footer等を削除するわけでない）  

必要な外部リンクを記述する  
以下のように使用するCSSのCDNをbase.htmlのheadタグ内に記載する。  
（バージョンはその時期に合わせて適切に選択する）  
※本テンプレートのBootstrapバージョンは4である前提。  
簡単にするために公式で公開されているものは全てCDNで指定しているが  
ローカルにダウンロードした方が初期のパフォーマンスは早くなるの可能性があるので  
ローカルにダウンロードしても良い。  

css系(bootstrapとfontawesome)
```
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
```

javascript系(jquery、ajax、bootstrap)
```
  <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.nicescroll/3.7.6/jquery.nicescroll.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js"></script>
```

公式がCDNで公開していないライブラリについては、ローカルにダウンロードして、staticでアクセスする。  
プロジェクト内にリンクしている箇所をstaticのタグで置き換える。  
これにより、staticが実際のPATHに置き換わるので、環境に関わらず動作する。  

base.htmlの一番上に以下を記載することで、staticという名前でstaticフォルダのpathが参照可能になる。
```
{% load static %}
```

base.htmlのheadに以下のassetsの情報を追記する。
```
  <link rel="stylesheet" href="{% static 'assets/css/style.css' %}">
  <link rel="stylesheet" href="{% static 'assets/css/components.css' %}">
```

base.htmlのbodyの下部に以下のassetsの情報を追記する。
```
   <script src="{% static 'assets/js/scripts.js' %}"></script>
   <script src="{% static 'assets/js/custom.js' %}"></script>
```


### 課題2:Templateのカスタマイズ
- base.htmlに対して以下のように、全画面共通のNavバー(画面右上)、サイドバーやコンテンツエリア(機能ページ)を作成します。

![template](https://i.gyazo.com/4ce6468143c9740a2ca87566557de494.png)

サイトバー、Navバーについては、案件に合わせて必要なメニューへのリンクを記述する。  
fontsomeaweを使用すると、キレイなアイコンをクラス指定だけで使うことができるのでおすすめ  
CDNは上記で指定しているので、下記を参考に、このみのアイコンを使用する。  
https://fontawesome.com/icons?d=gallery&p=2  



### 課題3:ルーティングの作成
以下を参考にして、app/urls.pyや各アプリのurlsを作成して、ルーティングを定義してください。  
最終的には、作成したページ全てのルーティングを行う必要がありますが、  
ここでは、以下のルートのurls.pyの作成と、settingアプリのurls.pyを作成してください。  
以下で示しているsetting/urls.pyに対して、今回使用するsampleページへのルーティングを追記してください。

今回は、アプリは4つ作る想定なので、以下のようにする  
app/urls.py
```
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # 管理画面（案件ではセキュリティ上、PATHを既知のadmin以外にする方が良い）
    path('', include('django.contrib.auth.urls')), #  ログイン系処理に必要なので追加
    path('syuppin/', include("syuppin.urls")),
    path('setting/', include("setting.urls")),
    path('mypage/', include("mypage.urls")),
    path('users/', include("users.urls"))
]
```

各アプリには既定ではurls.pyが存在しないので、app/urlsをコピーするなどして作成する。  
一例として、settingsのurls.pyの例で説明する。  
setting/urls.py  
```
# 必要な各Viewファイルを全てインポートする
from django.urls import path
from .views.asin import *
from .views.asin_group import *
from .views.price_setting import *
from .views.exclude_asin import *
from .views.exclude_word import *
from .views.common_setting import *
from .views.eval_setting import *
from .views.search_word import *
from .views.blacklist_word import *
from .views.blacklist_seller import *
from .views.fetch_url import *
from .views.profit import *
from .views.replace_word import *
from .views.sample_form import *

app_name = 'setting' # この名前でアクセスできるようになる 例：{% url 'setting:asin' %}
urlpatterns = [
    # pathはurlに表示されるPATH、Viewクラス、templateからアクセスするための名前の順で指定する
    path('replace-word', ReplaceWordView.as_view(), name="replace-word"),
    path('common-setting',SyuppinCommonSettingView.as_view(), name="common-setting"),
    path('search-word',SearchWordView.as_view(), name="search-word"),
    path('search-word-rakuma',SearchWordView.as_view(), name="search-word-rakuma"),
    path('blacklist-word',BlacklistWordView.as_view(), name="blacklist-word"),
    path('blacklist-seller',BlacklistSellerView.as_view(), name="blacklist-seller"),
    path('fetch-url',FetchUrlView.as_view(), name="fetch-url"),
    path('profit', ProfitView.as_view(), name="profit"),
]
```

### 課題4:Formからのデータ登録、編集（CRUD）
本案件においては、応用的なフォームしか使用しておらず、はじめの学習には不向きなため  
別案件で使用した基礎的かつ一般的なフォームによるCRUDの練習を行います。  
（最終的なWebサイトでは使わないページだが練習用として作成する）

以下のファイルに完成形が記載してありますので適宜参照してください。
```
views/sample_form.py
forms/sample_form.py
models/saple_form.py
tamplates/setting/sample.html
```

### フォルダ構造について
Django既定では、ModelやViewは、models.pyやviews.pyといった１つのファイルを  
１アプリにつき１ファイルずつ用意するようになっていますが  
規模が大きくなると管理するのが困難になります。  
そこで本案件では、modelsやviewsといったフォルダを作成し  
そこに、sample.pyなどの各ファイルを格納していく方式を採用しています。  

そのため、既定のmodels.py等のファイルは削除して、代りにmodelsフォルダを  
アプリ内に作成します。

#### 実装したい要件
フォーム画面からDBに情報を登録、変更、表示を行いたい。  
フォームの項目はinput入力の他、選択肢、複数行のinputを可能としたい。  
完成形では実際の案件のため、カラム項目数がかなり多いため  
練習が目的であれば、いくつか選択して実装する形でも構いません。  

#### Task
上記の要件を満たすフォーム画面を実装してください。  
1. settingアプリにmodels、forms、viewsフォルダを作成してください。  
2. sample_formモデルを作成してMigrateしてください(カラムの項目は完成品を参照)  
※なお、選択肢の項目はchoicesにで指定します。   
参考:https://qiita.com/ryu22e/items/37bf4f5f6b60ccccebe2
2. FormをModelFormクラスを使用して作成して先程作成したModelと紐付けてください  
参考:https://noumenon-th.net/programming/2019/11/07/django-modelform/
1. Viewを作成して、GETでフォームが表示できるようにしてください（要urlsへの追加）  
参考:https://django.kurodigi.com/form/
1. Htmlを作成して、GETで返したformのobjectを表示できるようにしてください  
参考:https://qiita.com/frosty/items/e340365684f679b9e5ca
1. Viewを修正して、POSTでフォームの内容を更新できるようにしてください  
参考:https://yuki.world/django-modelform-update-pitfall/

#### 実装例
setting/views/sample_form.py に実装例をアップしています。  
TemplateViewを使用しており、Form、TableやCreate、Updateに関わらず  
汎用的に対応できる実装となっております。  


### Tableへのデータ表示
#### 実装したい要件
メルカリ、ラクマらか商品データを収集しDBに登録された場合に  
DBに登録されている商品データをTable形式で表示させたい。  
テーブルは各行にチェックボックスを追加し選択できるようにし  
選択した行に対する削除をできるようにしたい。  
カラムには、画像やinput、buttonを設置できるようにしたい。  

#### Task
上記の要件を満たすTableを実装してください。  
1. 各アプリ内にtablesフォルダを作成して、この中に各tableの定義を行えるようにpyファイルを作成してください。
2. django-tables2をinstallして、settingsのINSTALLED_APPSに「django_tables2」と追記してください
3. メルカリやラクマから取得した商品のの情報を管理するためのテーブル(model)を作成してください。  
必須項目：ツールのアカウント名、商品名、価格、商品の個別ID、画像×４、メルカリかラクマかの判別  
4. tablesフォルダ内に以下のようにpyファイルを作成してください  
tablesフォルダ内に作成したpyファイル  
```
import django_tables2 as tables
from django_tables2.utils import Accessor

class ItemTable(tables.Table):
    
    class Meta:
        model = <modelクラス>
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False
        
        fields = (<modelで定義したカラム名を羅列>) 
```
5. viewに新しいpyファイルを作成し、Tableを表示するためのクラスを作成してください
SigleTableViewクラスもしくはTemplateViewクラスを継承したクラスを使用するとtableを簡単に表示させることができます。  
GET処理の流れ(TemplateViewクラスの場合)  
- Modelからデータを取得
- 作成したTableクラスのインスタンスにmodelをクエリした結果をセット
- table等のkeyで辞書を作成して上記のTableクラスのインスタンスをセット

1. templatesに新しいhtmlファイルを作成し、tableを表示するためのタグを記述し、WebページにTableが表示されることを確認してください
```
<!-- 個別ページhtml上部に記述 -->
{% load render_table from django_tables2 %}

<!-- 個別ページhtmlのテーブルを表示させたい場所に記述 -->
{% render_table table %}
```
7. DBに直接色々なデータを登録して、Tableに表示されることを確認してください。

### スクレイピングによるデータ取得
#### 実装したい要件
requestsライブラリを使用して、メルカリ、ラクマからスクレイピングして  
商品データをDBに格納します。  
スクレイピング処理側はDjangoとは別プロセスで通常のPythonとして実行する。  
DBとの連携はSQLAlchemyを使用して効率的に実装する。  

#### Task
1. SQLAlchemyをinstallしてください
```
pip install SQLAlchemy pymysql
```
※requirements.txtでインストール済の場合はスキップされます。  

2. データベース設定ファイルを以下のpyファイルのように作成してください。
この設定のカスタマイズは難しいので、一旦は定型文として使用してください。  
SQLALCHEMY_DATABASE_URLの設定は環境によって変更できます。    
database.py
```
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session,Session
import os
import ulid

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://docker:docker@localhost:43306/docker"
SQLALCHEMY_DATABASE_URL += '?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=360,pool_size=100)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(bind=engine)
session = scoped_session(SessionLocal)


# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close() # pylint: disable=no-member

def get_db_instance():
  return SessionLocal()

def get_ulid():
  return ulid.new().str

```

3. modelsファイルを作成してください。
Djangoと同様にテーブルを定義するためのファイルですが
記述方法がだいぶ異なります。

```
from datetime import datetime as dt
from datetime import timedelta as delta
from sqlalchemy import Column, String,Text ,DateTime, Float, Integer, ForeignKey, Boolean, func, update
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.sql.type_api import STRINGTYPE
from sqlalchemy_utils import UUIDType
from pytz import timezone
import ulid


class SyuppinItem(Base):
    __tablename__ = 't_syuppin_item'
    mysql_charset = 'utf8mb4',
    mysql_collate = 'utf8mb4_unicode_ci'

    # Djangoで定義したテーブルに接続するため、全く同様の定義をSQLAlchemyの文法で記述する
    # 以下は案件時の例のため、今回自身で実装するテーブルの定義に合わせて適宜編集する
    id = Column('id', Integer, primary_key=True)
    account_id = Column('account_id', String(100), nullable=False)
    item_sku = Column('item_sku', String(32), nullable=False,default=ulid.new().str)
    item_name = Column('item_name', String(256), nullable=False)
    item_id = Column('item_id', String(64), nullable=False)
    description = Column('description', String(4096), default="")
    price = Column('price', Integer, default=0)
    amazon_price = Column('amazon_price', Integer, default=0)
    category = Column('category', String(50), nullable=True)
    brand = Column('brand', String(50), nullable=True)
    thumbnail_url = Column('thumbnail_url', String(256), nullable=True)
    image_url1 = Column('image_url1', Text, nullable=True)
    image_url2 = Column('image_url2', Text, nullable=True)
    image_url3 = Column('image_url3', Text, nullable=True)
    image_url4 = Column('image_url4', Text, nullable=True)
    image_url5 = Column('image_url5', Text, nullable=True)
    image_url6 = Column('image_url6', Text, nullable=True)
    image_url7 = Column('image_url7', Text, nullable=True)
    image_url8 = Column('image_url8', Text, nullable=True)
    image_url9 = Column('image_url9', Text, nullable=True)
    is_image1_selected = Column('is_image1_selected', String(10), default="checked")
    is_image2_selected = Column('is_image2_selected', String(10), default="")
    is_image3_selected = Column('is_image3_selected', String(10), default="")
    is_image4_selected = Column('is_image4_selected', String(10), default="")
    is_image5_selected = Column('is_image5_selected', String(10), default="")
    is_image6_selected = Column('is_image6_selected', String(10), default="")
    is_image7_selected = Column('is_image7_selected', String(10), default="")
    is_image8_selected = Column('is_image8_selected', String(10), default="")
    is_image9_selected = Column('is_image9_selected', String(10), default="")
    is_image10_selected = Column('is_image10_selected', String(10), default="")
    condition = Column('condition', String(20), nullable=True)
    shipping_payment = Column('shipping_payment', String(20), nullable=True)
    shipping_method = Column('shipping_method', String(20), nullable=True)
    shipping_prefecture = Column('shipping_prefecture', String(20), nullable=True)
    shipping_leadtime = Column('shipping_leadtime', String(20), nullable=True)
    seller_name = Column('seller_name', String(50), nullable=True)
    is_export_completed = Column('is_export_completed', Boolean, default=False)
    is_alert = Column('is_alert', Boolean, default=False)
    site = Column('site', String(20), nullable=False)
    url = Column('url', Text)
    created_at = Column('created_at', DateTime, nullable=False,
                        default=current_timestamp())
    updated_at = Column('updated_at', DateTime, nullable=False,
                        default=current_timestamp(), onupdate=func.utc_timestamp())


```

4. メルカリからのスクレイピング
requestsとBeautifulsoupを使用してスクレイピングします。  
引数としてURLを与えた時に、requestsでメルカリの個別商品ページにアクセスしてBeautifulSoupで解析して、以下の情報を取得してください  
必須：タイトル、価格、セラー名、画像URL、URL、item_id（urlに記載されている商品固有のID）、サイト名  
任意：説明、発送方法、発送期間、発送元、発送負担元、カテゴリー、ブランド、商品状態

なお、取得した商品情報は以下のような検索結果格納用のクラスを準備して格納しておくと、後々便利です。
```python:agent/models/searched_item.py
class SearchedItem():
    
    def __init__(self, 
                 item_name:str, description:str, item_id:str, image_urls:list, thumbnail_url:str, category:str, 
                 brand:str, condition:str, shipping_payment:str, shipping_method:str,
                 shipping_prefecture:str, shipping_leadtime:str, seller_name:str, site:str, url:str, price:int):
        self.item_name = item_name
        self.description = description
        self.item_id = item_id
        self.image_urls = image_urls
        self.thumbnail_url = thumbnail_url
        self.category = category
        self.brand = brand
        self.condition = condition
        self.shipping_payment = shipping_payment
        self.shipping_method = shipping_method
        self.shipping_prefecture = shipping_prefecture
        self.shipping_leadtime = shipping_leadtime
        self.seller_name = seller_name
        self.is_remove = False
        self.site = site
        self.url = url
        self.price = price
        self.amazon_price = 0
        
```

5. 複数のURLをLISTで与えた時に、全ての商品情報をスクレイピングできるようにしてください
6. 取得した商品情報をDBに格納してください。
１つの商品情報をInsertする場合の例
```
from agent.common.database import SessionLocal
db:SessionLocal() # DBセッションをオープン
item = SyuppinItem(<SearchedItemの値を入れる>) # 格納する商品レコードを作成
db.add(item) # DBに追加 
db.commit() # 変更を確定
db.close() # DBをクローズ
```

7. 取得した商品情報が前の課題で作成したTableに表示されること確認してください。
8. 取得する商品のURL一覧をフォーム画面から登録できるようにする
- URL設定用のフォーム、モデルを作成して、TextAreaタグで複数行入力可能な入力欄を作成してください。
- 複数行入力されたURLをPOSTした際に、入力文字列を\nでsplitして、各URLに分解して、それぞれを１レコードしてテーブルに格納してください。（なお、この方法ではPOSTする毎に古いURL設定は一旦全て削除して、改めてInsertしてください）
9. スクレピング機能側でURL一覧を読み込んでスクレイピングできるようにしてください。
なお、URL設定用のテーブル情報はDjango側だけでなく、SQLAlchemy用にも作成する必要があります。
例）FetchURLテーブルを対象とし、アカウントIDを指定した、Select文の発行
```
# 末尾にall()をつけると、Select結果をListとして取得、Listの各要素にはFetchURLのレコードにアクセス可能なオブジェクトが格納されている。
url_objects = db.query(FetchUrl).filter_by(account_id=<アカウントID>).all()
for url_obj in url_objects:
  print(url.obj.url) # URLを取得
```

10. テーブル表示のカスタマイズ
tablesで定義したファイルを使って任意のHTMLを埋め込むことができます。
１つの列に複数の項目を入れる、画像を見やすく表示するなど、自由にカスタマイズしてみましょう。

例）商品情報を１つの列に複数入れる(サイト名、URLリンク、商品名、状態、出品者、ItemID)
tables/syuppin.py
```
    # templateと同様の記述が可能。record.<modelsの項目名>で各項目にアクセスできる。
    item_info_container = tables.TemplateColumn(
         '{% if record.is_alert == 1 %}\
            <i class="fas fa-exclamation-triangle fa-2x alert-icon mb-2"></i>\
          {% endif %}\
          {% if record.site == "mercari" %}\
            <a href="{{record.url}}" target="_blank"><div class="mercari-icon">　</div></a>\
          {% elif record.site == "rakuma" %}\
            <a href="{{record.url}}" target="_blank"><div class="rakuma-icon">　</div></a>\
          {% endif %}\
          <a href="{{record.url}}" target="_blank">商品ページへ</a>\
          <div><input class="form-control item-field" name="item_name" type="text" value="{{record.item_name}}" /></div>\
          <div><span>【出品者】{{record.seller_name}}</span><span class="ml-2">【状態】{{record.condition}}</span></div>\
          <div>(id: {{record.item_id}})</div>',
          verbose_name="商品情報"
    )

    (～～略～～)

    # 以下のように作成した新たな列名をfieldsに記述する
      fields = ('checkbox', 'row_no', 'image_container', 'item_info_container', 
            'price_container') 
```

### Excel出力
#### 実装したい要件
DBに格納されているItemデータをExcelに出力する。
Excelのレイアウトは予め用意したAmazon出品用のテンプレートを使用する。
商品一覧ページで、Tableに表示されている１ページ分のデータをExcelに出力する。

#### Task
1. Excelのテンプレートをopenpyxlを使用して開いてください。
2. 開いたExcelのテンプレートシートに対して、商品一覧テーブルから取得した商品データを当てはめてください。
3. 固定値については、共通設定テーブルから取得して当てはめてください。
4. Excelをダウンロードできるようにしてください。
Excelをダウンロードするためのヘッダの設定は以下の例を参考にしてください。
```
 response = HttpResponse(content_type="application/vnd.ms-excel")
 response['Content-Disposition'] = f'attachment; filename={<ファイル名>}'
``` 
5. 商品一覧ページにExcelダウンロードボタンを作成し、クリック時にExcelをダウンロードするようにしてください。
6. Excel出力済の商品を削除するボタンを作成し、クリック時に出力済の商品は削除されるようにしてください。
====================================================  
★★★★★★★★　　以降は作成中。　★★★★★★★★　　

