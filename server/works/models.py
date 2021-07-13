from django.core.validators import URLValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from colorfield.fields import ColorField
from colour import Color
from django.core.exceptions import ValidationError

DEFAULT_DESCRIPTION = """
<details>
  <summary class="Subject">作品紹介</summary>
  <p class="Paragraph">
    <b>作品説明：</b><br>
     このゲームは、探索型2dアクションゲームです。<br>
    マップを探索して鍵を集めて先に進み、ボスを倒せばゲームクリアです。
  </p>
  <p class="Paragraph">
    <b>使用ツール：</b><br>
    Unity 2019.3.14f1
  </p>
</details>
<details>
  <summary class="Subject">操作方法</summary>
  <ul class="Paragraph">
    <li>矢印← ... 左に移動</li>
    <li>矢印→ ... 右に移動</li>
    <li>矢印↑ ... ジャンプ</li>
    <li>矢印↓ ... (すり抜け床の上にいるとき)床をすり抜ける</li>
  </ul>
  <p class="Paragraph">
    敵は踏みつけたら倒せます。(マリオの踏みつけと同じ)<br>
    敵に当たると体力が減ります。<br>
    体力が無くなると、セーブポイントに戻されます。<br>
    フルーツを取ると体力が回復します。<br>
    <br>
    鍵を取ると進める場所が増えます。<br>
    マップ上には、アクションを増やすアイテムが存在します。<br>
    もし先に進めなくなったら、アイテムを探してみましょう。
  </p>
</details>
<details>
  <summary class="Subject">制作者からひとこと</summary>
  <p class="Paragraph">
    <b>Kuroki：</b><br>
    プレイヤー･敵キャラを作りました。<br>
    このゲームで使ったUnityアセット「Pixel Adventure」は、<br>
    無料かつ素材が豊富なのでぜひ使ってみてください。<br>
    <b>Crucio：</b><br>
    ステージ･ギミックを作りました。
  </p>
</details>
"""

# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    color = ColorField(null=False, blank=False, default='#ff0000')

    def __str__(self):
        return self.name

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, default="Genre")
    description = models.TextField(null=False, blank=False, default="No description...")
    bg_color = ColorField(default="#ff0000")

    def __str__(self):
        return self.title

    def bg_color_lighten(self):
        delta = 0.1
        c = Color(self.bg_color)
        if(c.luminance + delta > 1):
            c.luminance = 1
        else:
            c.luminance += delta
        return c.hex_l

    def card_color(self):
        delta = 0.3
        c = Color(self.bg_color)
        if(c.luminance + delta > 1):
            c.luminance = 1
        else:
            c.luminance += delta
        return c.hex_l

    def text_color(self):
        bg_c = Color(self.bg_color)
        txt_c = Color()
        if bg_c.luminance < 0.5:
            txt_c.luminance = 1
        else:
            txt_c.luminance = 0
        return txt_c

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    genre = models.ForeignKey(Genre, related_name='works', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=False, upload_to='images/system/')
    goods = models.IntegerField(null=False, default=0)
    download_link = models.CharField(null=True, blank=True, max_length=255, validators=[URLValidator()])
    
    # model3d = models.ForeignKey(Model3D, on_delete=models.SET_NULL, null=True, blank=True)
    # video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "%s - %s (%s)" % (self.team.name, self.title, self.genre.title)

    def get_absolute_url(self):
        return reverse("work", args=[str(self.id)])

class MediaAsset(models.Model):
    id = models.AutoField(primary_key=True)
    work = models.ForeignKey(Work, related_name='media_assets', on_delete=models.CASCADE)
    youtube_video_id = models.CharField(null=True, blank=True, max_length=16)
    image = models.ImageField(null=True, blank=True, upload_to='images/system')
    sketchfab_embed_html = models.TextField(null=True, blank=True)
    soundcloud_embed_html = models.TextField(null=True, blank=True)

    def clean(v):
        # media_assets_must_have_least_an_asset 
        # どれか一つのアセットタイプを指定する必要がある
        error_message = 'アセットタイプは少なくともどれか一つだけ指定してください。'
        contain_asset = False
        if v.youtube_video_id:
            if contain_asset:
                raise ValidationError(error_message)
            contain_asset = True

        if v.image:
            if contain_asset:
                raise ValidationError(error_message)
            contain_asset = True

        if v.sketchfab_embed_html:
            if contain_asset:
                raise ValidationError(error_message)
            contain_asset = True

        if v.soundcloud_embed_html:
            if contain_asset:
                raise ValidationError(error_message)
            contain_asset = True
        
        if not contain_asset:
            raise ValidationError(error_message)
            

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    work = models.ForeignKey(Work, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    
    def __str__(self):
        return "[{}] {}".format(self.name, self.text)


    def ja_created_at_str(self):
        return self.created_at.strftime("%Y/%m/%d %H:%M")