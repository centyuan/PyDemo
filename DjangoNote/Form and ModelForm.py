from django import forms


# http://c.biancheng.net/view/7985.html

# 1.Form
class TitleForm(forms.Form):
    title = forms.CharField(label='书名', error_messages={'required': '请输入正确的title'})

    # 加上自定义校验规则:在默认验证逻辑执行完成后
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise forms.ValidationError("书名字符长度超出限制")
        return title


# title_form = TitleForm(request.GET)
title_form = TitleForm({'title': 'aaaaaaaaaaa'})
if not title_form.is_valid():
    print(title_form['title'].errors)
    # 字典:{'title': ['书名字符长度超出限制'], 'c': ['确保该值小于或等于10。']}
    print('aaaaa', title_form.errors)

# 2.ModelForm

Book = 'model'


class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        # labels 为字典类型，用于定义表单字段的名称
        # 表单的名称首先默认使用 Model字段设置的 verbose_name，但是若 Model 字段没有设置该字段选项，则就可以使用 lables 设置的字段名；
        labels = {'price': '零售价格'}
        # 指定包含那些
        fields = ()
        # exclude 标识不需要在表单中显示的字段，这和 Model 的 Meta 也一样
        exclude = ('retail_price')


# bookmodel_form = BookModelForm(request.POST)
# if bookmodel_form.is_valid():
#     user=UserInfo.objects.create(username=bookmodel_form.cleaned_data['username'],
#                                  password=bookmodel_form.cleaned_data["password"],
#                                  gender=bookmodel_form.cleaned_data['gender'])
# 还可以实现保存
# f = BookModelFrom(request.POST)
# new_book = f.save()


"""

ModelForm的使用方法与 Form 类似:
is_valid来校验，cleaned_data获取清理后的字段值
ModelForm也会校验模型字段中设置的限制条件:
比如在 Model 模型的字段中添加了 unique 选项，那么 is_valid 则会查询数据库确认是否存在重复数据
"""
