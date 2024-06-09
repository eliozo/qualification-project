import sys
import os
import pytest

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we can import webmd_utils
from webmd_utils import fix_image_links


def test_image_with_alt():
    STR1 = """<p>Parādi, kā no 1. att. dotās rūtiņu lapas var izgriezt desmit figūras, 
kādas dotas 2. att. (iezīmē, kur jāiet griezuma līnijām)! 
Figūras var būt arī pagrieztas.<br />
<img alt="1.att., 2.att." src="LV.AMO.2022B.6.2.png" /></p>"""
    STR2 = """<p>Parādi, kā no 1. att. dotās rūtiņu lapas var izgriezt desmit figūras, 
kādas dotas 2. att. (iezīmē, kur jāiet griezuma līnijām)! 
Figūras var būt arī pagrieztas.<br />
<img alt="1.att., 2.att." src="https://www.dudajevagatve.lv/static/eliozo/images/LV.AMO.2022B.6.2.png"/></p>"""

    result = fix_image_links(STR1)
    assert result == STR2


def test_image_no_alt():
    STR1 = """<p>No četrām tādām figūrām, kāda dota 9. att., uzzīmē figūru, kurai ir tieši: <strong>(A)</strong> $2$ simetrijas asis;
<strong>(B)</strong> $4$ simetrijas asis!</p>
<p><img alt="" src="LV.AMO.2023.6.3.png" /></p>
<p><em>Piezīme.</em> Figūru, kas dota 9. att., drīkst pagriezt un apmest otrādi. Uzzīmētajai figūrai var būt arī
caurumi. Figūrai jābūt saistītai, tas ir, no figūras katras rūtiņas jābūt iespējai aiziet uz jebkuru citu šīs
figūras rūtiņu, ejot tikai pa šīs figūras rūtiņām, katru reizi pārejot no attiecīgās rūtiņas uz blakus rūtiņu,
ar ko tai ir kopīga mala.</p>"""

    STR2 = """<p>No četrām tādām figūrām, kāda dota 9. att., uzzīmē figūru, kurai ir tieši: <strong>(A)</strong> $2$ simetrijas asis;
<strong>(B)</strong> $4$ simetrijas asis!</p>
<p><img alt="" src="https://www.dudajevagatve.lv/static/eliozo/images/LV.AMO.2023.6.3.png"/></p>
<p><em>Piezīme.</em> Figūru, kas dota 9. att., drīkst pagriezt un apmest otrādi. Uzzīmētajai figūrai var būt arī
caurumi. Figūrai jābūt saistītai, tas ir, no figūras katras rūtiņas jābūt iespējai aiziet uz jebkuru citu šīs
figūras rūtiņu, ejot tikai pa šīs figūras rūtiņām, katru reizi pārejot no attiecīgās rūtiņas uz blakus rūtiņu,
ar ko tai ir kopīga mala.</p>"""

    result = fix_image_links(STR1)
    assert result == STR2


def test_image_with_width_no_alt():
    STR1 = """<h2>Atrisinājums</h2>
<p>Taisnstūrī pretējās malas ir paralēlas, tāpēc 
iekšējo vienpusleņķu summa $60^{\\circ} + \\alpha = 180^{\\circ}$.<br />
Iegūstam, ka $\\alpha = 120^{\\circ}$. </p>
<p><img alt="" src="EE.PKTEST.2012.7.8A.png" />{ width=200px }</p>"""

    STR2 = """<h2>Atrisinājums</h2>
<p>Taisnstūrī pretējās malas ir paralēlas, tāpēc 
iekšējo vienpusleņķu summa $60^{\\circ} + \\alpha = 180^{\\circ}$.<br />
Iegūstam, ka $\\alpha = 120^{\\circ}$. </p>
<p><img alt="" style="width:200px" src="https://www.dudajevagatve.lv/static/eliozo/images/EE.PKTEST.2012.7.8A.png"/></p>"""

    result = fix_image_links(STR1)
    assert result == STR2

def test_image_with_width_but_with_alt():
    STR1 = """<h2>Atrisinājums</h2>
<p>Taisnstūrī pretējās malas ir paralēlas, tāpēc 
iekšējo vienpusleņķu summa $60^{\\circ} + \\alpha = 180^{\\circ}$.<br />
Iegūstam, ka $\\alpha = 120^{\\circ}$. </p>
<p><img alt="Some 'comment'" src="EE.PKTEST.2012.7.8A.png" />{ width=200px }</p>"""

    STR2 = """<h2>Atrisinājums</h2>
<p>Taisnstūrī pretējās malas ir paralēlas, tāpēc 
iekšējo vienpusleņķu summa $60^{\\circ} + \\alpha = 180^{\\circ}$.<br />
Iegūstam, ka $\\alpha = 120^{\\circ}$. </p>
<p><img alt="Some 'comment'" style="width:200px" src="https://www.dudajevagatve.lv/static/eliozo/images/EE.PKTEST.2012.7.8A.png"/></p>"""

    result = fix_image_links(STR1)
    assert result == STR2