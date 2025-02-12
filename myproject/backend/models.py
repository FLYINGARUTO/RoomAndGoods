from django.db import models

class Banner(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    picture_url = models.CharField(max_length=255)  # 图片 URL，最长 255 字符
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间，自动添加当前时间
    deleted = models.BooleanField(default=False)  # 删除标记，默认为 False
    admin_id = models.IntegerField()  # 管理员 ID，整型字段

    class Meta:
        db_table = 'banner'  # 替换为实际的表名
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return f'Banner {self.id} - {self.picture_url}'


class User(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    username = models.CharField(max_length=255, unique=True)  # 用户名，确保唯一
    password = models.CharField(max_length=255)  # 密码字段（建议加密存储）
    role = models.CharField(max_length=255)  # 角色字段，如 admin, user 等
    register_time = models.DateTimeField(auto_now_add=True)  # 注册时间，自动记录创建时间
    level = models.IntegerField()  # 用户等级，默认初级
    avatar = models.URLField(max_length=255, blank=True, null=True)  # 头像链接，可为空

    class Meta:
        db_table = 'user'  # 数据库表名为 user
        verbose_name = 'User'  # Django 后台单数显示为 User
        verbose_name_plural = 'Users'  # Django 后台复数显示为 Users

    def __str__(self):
        return self.username  # 返回用户名作为模型的字符串表示


class Post(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    publisher_id = models.IntegerField()  # 发布者 ID，非空
    title = models.CharField(max_length=255)  # 标题，非空
    details = models.CharField(max_length=255)  # 详细描述，非空
    views = models.IntegerField(default=0)  # 浏览量，默认为 0
    likes = models.IntegerField(default=0)  # 点赞数，默认为 0
    photo_urls = models.CharField(max_length=255)  # 图片链接，非空
    category = models.CharField(max_length=255)  # 分类，非空
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间，自动添加
    delete_time = models.DateTimeField(blank=True, null=True)  # 删除时间，允许为空（软删除）

    class Meta:
        db_table = 'post'  # 数据库表名为 post
        verbose_name = 'Post'  # Django 后台单数显示为 Post
        verbose_name_plural = 'Posts'  # Django 后台复数显示为 Posts

    def __str__(self):
        return self.title if self.title else f'Post {self.id}'



class Comment(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    from_id = models.IntegerField()  # 评论者 ID，非空
    post_id = models.IntegerField()  # 所属帖子 ID，非空
    to_id = models.IntegerField()  # 被回复用户 ID，非空
    comment = models.CharField(max_length=255)  # 评论内容，最大长度 255，非空
    read = models.IntegerField(default=0)  # 是否已读，默认为 0

    class Meta:
        db_table = 'comment'  # 数据库表名为 comment
        verbose_name = 'Comment'  # Django 后台单数显示为 Comment
        verbose_name_plural = 'Comments'  # Django 后台复数显示为 Comments

    def __str__(self):
        return f'Comment by User {self.from_id} on Post {self.post_id}'


class Like(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    from_id = models.IntegerField()  # 点赞用户 ID，非空
    to_id = models.IntegerField()  # 被点赞用户 ID，非空
    post_id = models.IntegerField()  # 被点赞的帖子 ID，非空
    created_time = models.DateTimeField(auto_now_add=True)  # 点赞时间，自动记录

    class Meta:
        db_table = 'like'  # 数据库表名为 like
        verbose_name = 'Like'  # Django 后台单数显示为 Like
        verbose_name_plural = 'Likes'  # Django 后台复数显示为 Likes
        unique_together = ('from_id', 'post_id')  # 防止同一用户对同一帖子重复点赞

    def __str__(self):
        return f'User {self.from_id} liked Post {self.post_id}'


class Collect(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    from_id = models.IntegerField()  # 收藏用户 ID，非空
    to_id = models.IntegerField()  # 被收藏用户 ID，非空
    post_id = models.IntegerField()  # 被收藏的帖子 ID，非空
    created_time = models.DateTimeField(auto_now_add=True)  # 收藏时间，自动记录

    class Meta:
        db_table = 'collect'  # 数据库表名为 collect
        verbose_name = 'Collect'  # Django 后台单数显示为 Collect
        verbose_name_plural = 'Collects'  # Django 后台复数显示为 Collects
        unique_together = ('from_id', 'post_id')  # 防止同一用户对同一帖子重复收藏

    def __str__(self):
        return f'User {self.from_id} collected Post {self.post_id}'


class Message(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    from_id = models.IntegerField()  # 发送者 ID，非空
    to_id = models.IntegerField()  # 接收者 ID，非空
    text = models.CharField(max_length=255)  # 消息内容，最大长度 255，非空
    read = models.IntegerField(default=0)  # 是否已读，默认为未读 (False)
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间，自动记录发送时间

    class Meta:
        db_table = 'message'  # 数据库表名为 message
        verbose_name = 'Message'  # Django 后台单数显示为 Message
        verbose_name_plural = 'Messages'  # Django 后台复数显示为 Messages
        ordering = ['-created_time']  # 默认按消息创建时间倒序排列

    def __str__(self):
        return f'Message from User {self.from_id} to User {self.to_id}'
