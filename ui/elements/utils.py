"""  aclu/ui/elements/utils.py 
simple dataclasses for props used by templates in ui/templates/utils.html
I realize I'm duplicating the definition of StrOrDict here (see acluutils.py
I want to keep ui a self contained package and maybe break it out from aclu some day )
"""

from datetime import datetime as dt 
from markupsafe import escape 
from typing import TypeVar, Dict, Any
StrOrDict = TypeVar('StrOrDict', str, Dict) 

from .baseElements import BaseElement 

class Heading(BaseElement):
    def __init__(self, level: int, contents: Any, **kwArgs):
        self.level = level
        ## self.contents = contents 
        super().__init__(tag=f'h{level}', contents=contents, **kwArgs)


class Anchor(BaseElement):
    def __init__(self, href: str, contents: Any, **kwArgs):
        self.href = str(escape(href))
        ## self.contents = contents 
        super().__init__(tag='a', contents=contents, href=self.href, **kwArgs)


## end of file 