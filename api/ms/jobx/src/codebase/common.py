from gettext import gettext as _


MARKUP_CHOICES = (
    ("text", _("Txt")),
    ("html", _("HTML")),
    ("markdown", _("Markdown")),
)

MARKUP_CHOICES_VALUE = {
    "text": 0,
    "html": 1,
    "markdown": 2,
}
