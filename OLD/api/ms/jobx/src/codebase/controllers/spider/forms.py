from gettext import gettext as _

from wtforms import Form, validators
from wtforms.fields import (
    FieldList,
    StringField,
    TextField,
    SelectField,
    IntegerField
)

from codebase.common import MARKUP_CHOICES


class JobNewForm(Form):

    platform = StringField("Platform", [validators.Length(min=2, max=64)])

    title = StringField("Title", [validators.Length(min=2, max=256)])
    body = TextField("Body", [validators.Length(min=2)])
    body_markup = SelectField(
        "Body Markup",
        choices=MARKUP_CHOICES,
        validators=[validators.optional()],
        default="text"
    )

    url = StringField("URL", [validators.Length(min=6)])
    sid = StringField("Source ID", [validators.Length(min=2, max=128)])

    price = IntegerField("Price")
    status = StringField("Status", [validators.Length(max=64)])

    city = FieldList(StringField("City List"))
    category = FieldList(StringField(
        "Category List",
        [validators.Length(max=128)]
    ))
    role = FieldList(StringField(
        "Role List",
        [validators.Length(max=128)]
    ))
    skill = FieldList(StringField(
        "Skill List",
        [validators.Length(max=128)]
    ))

    # TODO: 校验 UTC string
    release_date = StringField(_("Release Date"), [validators.Required()])
    expire_date = StringField(_("Expire Date"))


class JobEditForm(JobNewForm):
    '''更新Job

    TODO: 设置必要属性检查
    '''
