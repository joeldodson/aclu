"""  aclu/ui/elements/baseElements.py
classes in here are meant to be used to build HTML elements
"""

from datetime import datetime as dt 
from typing import Dict, Any

from markupsafe import escape 


class BaseElement:
    """
    BaseElement holds the tag value and a dict of attrivutes      
    """
    def __init__(self, tag: str, contents: Any = None, **kwArgs):
        self.tag = tag
        self.contents = contents
        self.attrs = dict(kwArgs)

    def getAttributesString(self, inAttrs: Dict = None) -> str:
        """
        in general, this will return the string of the attributes currently set on the element
        alternatively, if a derived element has a dict of attributes not in the base attrs dict,
        that dict can be passed in and used instead.
        """
        lattrs = inAttrs if inAttrs else  self.attrs 
        attrString = ''
        if not lattrs or len(lattrs) == 0: 
            return attrString
        for k,v in lattrs.items():
            attrString += f' {k}="{v}"'
        return attrString 


    def addAttributes(self, **kwArgs) -> None:
        self.attrs.update(kwArgs)


    def openingTag(self) -> str:
        """
        returns a string representing the opening tag  and any attributes 
        """
        return f'<{self.tag} {self.getAttributesString()}>'
        
    def closingTag(self) -> str:
        return f'</{self.tag}>'


    def __repr__(self):
        return f'{self.openingTag()} {self.contents} {self.closingTag()}'



## end of file 