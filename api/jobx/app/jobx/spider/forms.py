from wtforms import Form, validators
from wtforms.fields import (
    FieldList,
    StringField,
    TextField,
    SelectField,
    IntegerField
)

from eva.utils.translation import ugettext_lazy as _
from app.jobx.settings import MARKUP_CHOICES


class JobNewForm(Form):

    platform = StringField("Platform", [validators.Length(min=2, max=128)])

    title = StringField("Title")
    body = TextField("Body")
    body_markup = SelectField(
        "Body Markup",
        coerce=int,
        choices=MARKUP_CHOICES,
        validators=[validators.optional()],
        default=1
    )

    url = StringField("URL")
    checksum = StringField("Checksum")

    price = IntegerField("Price")
    city = StringField("City")

    categories = FieldList(StringField(
        "Category List",
        [validators.Length(max=128)]
    ))
    roles = FieldList(StringField(
        "Role List",
        [validators.Length(max=128)]
    ))
    skills = FieldList(StringField(
        "Skill List",
        [validators.Length(max=128)]
    ))

    # TODO: 校验 UTC string
    release_date = StringField(_("Release Date"))
    expire_date = StringField(_("Expire Date"))


class JobEditForm(JobNewForm):
    '''更新Job

    TODO: 设置必要属性检查
    '''
