Django 実践的課題
====
### DockerでMySQLを構築、起動
dockerをインストールして、プロジェクトルートで以下コマンドを実行する。  
dockerのプロセスは常に起動した状態にする必要があるため、dockerコマンド実行後は  
別のターミナルを開いて作業を行う。  
```
cd docker
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

### 各種フォルダの作成
以下のフォルダをプロジェクトルートに作成する。  
static:css/js等の静的ファイルを格納する  
templates:HTMLテンプレートファイルを格納する  
※アプリ毎に作成する方式もあるが、プロジェクトルートに１つ作成する方が管理しやすいのでオススメ。

既定では、アプリ配下のtemplatesを参照するため、templatesの場所を以下のDIRSで指定することで変更している。
※既にsettings.pyは変更済
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
ダウンロードしたファイルのうち、assetsフォルダをstaticフォルダにコピーする

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
CDNは上記で指定しているので、下記を参考に、好みのアイコンを使用する。  
https://fontawesome.com/icons?d=gallery&p=2  



### 課題3:ルーティングの作成
以下を参考にして、app/urls.pyや各アプリのurlsを作成して、ルーティングを定義してください。  
ここでは、以下のルートのurls.pyの作成と、itemアプリのurls.pyを作成してください。  


今回は、アプリは2つ作る想定なので、以下のようにする  
app/urls.py
```
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # 管理画面
    path('', include('django.contrib.auth.urls')), #  ログイン系処理に必要
    path('item/', include("item.urls")),　# Item
    path('users/', include("users.urls")) # Users
]
```

各アプリには既定ではurls.pyが存在しないので、app/urlsをコピーするなどして作成する。  
itemのurls.pyの例で説明する。  
item/urls.py  
```
# 必要な各Viewファイルを全てインポートする
from django.urls import path
from .views.register import *

app_name = 'item' # この名前でアクセスできるようになる 例：{% url 'setting:asin' %}
urlpatterns = [
    # pathはurlに表示されるPATH、Viewクラス、templateからアクセスするための名前の順で指定する
    path('register', ItemRegisterView.as_view(), name="register"),
]
```

### フォルダ構造について
Django既定では、ModelやViewは、models.pyやviews.pyといった１つのファイルを  
１アプリにつき１ファイルずつ用意するようになっていますが  
規模が大きくなると管理するのが困難になります。  
そこで本案件では、modelsやviewsといったフォルダを作成し  
そこに、sample.pyなどの各ファイルを格納していく方式を採用しています。  

そのため、既定のmodels.py等のファイルは削除して、代りにmodelsフォルダを  
アプリ内に作成します。

### 課題4:Formからのデータ登録、編集（CRUD）
商品登録画面を作成して、Formから入力した情報がModels経由でDBに登録されるようにしてください。

1. item/models/item.py を作成して、以下の項目を持ったテーブルを作成してください。
```
テーブル名:item 
カラム：
　id : PrimaryKeyが自動生成
　name :商品名、文字列
  price :価格、数字
  description: 説明、テキスト
  thumbnail_url: サムネイルURL、テキスト
  created_at: 作成日時、Datetime
  updated_at: 更新日時、Datetime
```

参考
```
from django.db import models

from django.http import request
from django.utils import timezone
from common.utility import get_ulid

class ItemModel(models.Model):
    
    id = models.CharField(max_length=32, default=get_ulid, primary_key=True, editable=False)
    # TODO:以下にカラムを定義

    created_at = models.DateTimeField('作成日時',auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)
    
    class Meta():
        db_table=<テーブル名>
```

1. item/forms/item_register.pyを作成しmodelと連動したformを作成してください。
ただし、Formで作成日時、更新日時を直接指定できる必要はないので、表示させないようにしてください。

参考
```
from django import forms
from django.forms.fields import ChoiceField
from django.forms import TextInput
# TODO:models.itemをインポートする

class ItemRegisterForm(forms.ModelForm):

    class Meta():
        model=ItemModel
        # TODO:表示させたいカラム名を以下に記述    
        fields=('name',)
        
        # テキストエリアのサイズ変更
        widgets = {
            'description': forms.Textarea(attrs={'rows':20, 'cols':40})
        }
```

1. item/views/item_register.py および、templates/item/register.htmlを作成して、Formの画面表示ができるようにしてください。

参考：views/item_register.py
```
from django.shortcuts import render
from django.views import generic
from django.contrib import messages 

from ..forms.item_register import *
from ..models.item import *


class ItemRegisterView(generic.TemplateView):
    template_name = <テンプレートのpathを指定>

    def get(self, request, *args, **kwargs):
        form = ItemRegisterForm()
        context = {
            'form': form
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        '''
        登録ボタン押下時
        '''
        params = {'result': '', 'form': None}
        form = ItemRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form
            }
            messages.success(request, "登録に成功しました。")
            return self.render_to_response(context)
        else:
            messages.warning(request, "登録に失敗しました。")
```

参考：templates/item/register.html
register.htmlを作成して、以下のようなイメージで、formタグを記述します。
{{ form.as_p }}の箇所にFormの要素が一式記述されます。
messagesは、view側でメッセージが登録されている場合に表示されるようになっています。
```
<form id="main-form" role="form" method="POST">
    {% csrf_token %}
    {% if messages %}
        <ul class="messages_ul">
            {% for message in messages %}
                <li class="alert{% if message.tags %} alert-{{ message.tags }}{% endif %} alert-dismissible text-dark" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    {{ form.as_p }}
    <div class="mt-2">
        <button id="submit_btn" type="submit" class="btn btn-primary">登録</button>
    </div>
</form>
```

# 課題５：ログイン処理
Midllewareを使用してログイン処理を実装します。

1. 以下を参考にしてログイン用のmiddlewareファイルを作成してください。
app/middleware/auth.py
```
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin 

class authMiddleware(MiddlewareMixin): 
    def process_response(self, request, response): 
        if not request.user.is_authenticated and request.path != '/login/' or request.path == '/': 
            return HttpResponseRedirect('/login/') 
        return response

```

2. settings.pyに以下の記述を追加してください。
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.auth.authMiddleware', # 追加
]

～～（略）～～

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

～～（略）～～

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'
```

3. templatesに以下のフォルダ、ファイルを追加してください。
templates/registrarion/login.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no" name="viewport">
  <title>Login &mdash; </title>

  <!-- General CSS Files -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">

  <!-- CSS Libraries -->
  <link rel="stylesheet" href="../node_modules/bootstrap-social/bootstrap-social.css">


  <!-- Template CSS -->
  <link rel="stylesheet" href="{% static 'assets/css/style.css' %}">
  <link rel="stylesheet" href="{% static 'assets/css/components.css' %}">
  <link rel="icon" type="image/png" href="{% static 'favicon.png' %}">
</head>

<body>
  <div id="app">
    <section class="section">
      <div class="container mt-5">
        <div class="row">
          <div class="col-12 col-sm-8 offset-sm-2 col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-xl-4 offset-xl-4">
            <div class="login-brand">
              <div alt="logo" width="100" class="shadow-light rounded-circle">Django Study</div>
            </div>

            <div class="card card-primary">
              <div class="card-header"><h4>Login</h4></div>

              <div class="card-body">
                <form method="POST" action="#" class="needs-validation" novalidate="">
                    {% csrf_token %}
                    {{ form.non_field_errors }}
                    <div class="form-group">
                      <label>アカウントID</label><input name="username" class="form-control" placeholder="アカウントID"></input>
                      <label>パスワード</label><input name="password" type="password" class="form-control" placeholder="パスワード"></input>
                    </div>
                    <div class="form-group">
                    </br>
                    <button type="submit" class="btn btn-primary btn-lg btn-block" tabindex="4">
                        Login
                    </button>
                    </div>
                </form>
              </div>
            </div>
            <div class="simple-footer">
              Django Study 2021
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- General JS Scripts -->
  <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.nicescroll/3.7.6/jquery.nicescroll.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js"></script>
  <script src="{% static 'assets/js/stisla.js' %}"></script>

  <!-- JS Libraies -->

  <!-- Template JS File -->
  <script src="{% static 'assets/js/scripts.js' %}"></script>
  <script src="{% static 'assets/js/custom.js' %}"></script>


  <!-- Page Specific JS File -->
</body>
</html>

```

4. app/urls.pyに以下のpathを追加してください。
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')), #  追加
    path('item/', include("item.urls")),
    path('users/', include("users.urls")),
    path('index', IndexView.as_view(), name="index")
]
```

5. template.base.html のナビゲーションバー右側部分に以下の記述を追加して、ログインユーザー情報を表示できるようにしてください。
```
<ul class="navbar-nav navbar-right">
          <li class="dropdown dropdown-list-toggle">
            <div class="nav-link nav-link-lg nav-link-user">
              <a href="#" data-toggle="dropdown" class="nav-link dropdown-toggle nav-link-lg nav-link-user">
                <img alt="image" src="{% static 'assets/img/avatar/avatar-1.png' %}" class="rounded-circle mr-1">
                <div class="d-sm-none d-lg-inline-block">{{ user.email }}</div></a> <!-- この行を追加 -->
            </div>
          </li>
```

# 課題６：Table
完成イメージのようにItemテーブルの情報をTable表示できるようにします。
![イメージ](https://i.gyazo.com/2fb8d2ed0d3e4fd76cedef1aaa34f022.png)

1. item/tablesフォルダを作成して、その配下にitem.pyを作成してください。  
item/tables/item.py
```
import django_tables2 as tables

from ..models.item import *


class ItemTable(tables.Table):
    
    class Meta:
        model = ItemModel
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False
        fields = ('name', 'price', 'description')  

```


2. views/table.py を作成してください。
```
from django.views import generic

from ..models.item import *
from ..tables.item import *

class ItemTableView(generic.TemplateView):
    template_name = "item/table.html"

    def get(self, request, *args, **kwargs):
        items = ItemModel.objects.all()
        table = ItemTable(items)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return self.render_to_response({'table': table, 'count': items.count()})

```

3. base.htmlとitem/urls.pyに上記のitemテーブルを表示させるための記述を行い
Web画面から/item/tableのURLで表示できるようにしてください。

4. tables/item.pyにTemplateColumnを追加して、thumbnail_urlを画像として表示できるようにしてください。
```
    thumbnail_url = tables.TemplateColumn(
        """
        <div><img src="{{ record.thumbnail_url }}"></div>        
        """)
```

# 課題７：
以下のスライドに記載の要件を満たすように実装してください。  
具体的な課題もスライドに記載しています。
https://docs.google.com/presentation/d/1Svsjq3aiGWIuJaB8DwWF5fDSHf5Bhy2S8k350AefETk/edit?usp=sharing