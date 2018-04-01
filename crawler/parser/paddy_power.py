from crawler.parser import BaseParser


class PaddyPowerParser(BaseParser):
    def parse(self, html):
        import pdb; pdb.set_trace()
        return html



"""
<avb-item.

<ui-scoreboard-coupon

ui-scoreboard-runner -> span #first team
ui-scoreboard-runner -> span #second team


x3 ->
<div class="avb-item__box grid grid__cell-2-12" 
-> home
-> draw
-> away
"""
