1\. Aprēķini trijstūra laukumu, ja trijstūra malu garumi ir

> a\) 13 cm, 14 cm, 15 cm;
>
> b\) 6 cm, 25 cm, 29 cm;
>
> c\) 5 cm, 6 cm, 9 cm!

2\. Aprēķini trijstūra īsāko augstumu, ja trijstūra malu garumi ir 25
cm, 29 cm un 36 cm!

3\. Aprēķini trijstūra garāko augstumu, ja trijstūra malu garumi ir 3
cm, 25 cm un 26 cm!

4.\* Pierādi, ka trijstūra, kura malu garumi ir
$\sqrt{40}\ $cm,$\ \sqrt{53}\ $cm un$\ \sqrt{145}\ $cm, laukums ir 19
cm^2^!

**I veids.** Ievēro, ka $40 = 2^{2} + 6^{2}$, $53 = 2^{2} + 7^{2}$ un
$145 = 8^{2} + 9^{2}$. Līdz ar to doto trijstūri var iezīmēt taisnstūrī
ar izmēriem $8 \times 9$. Tad dotā trijstūra laukums ir

$$S_{\mathrm{\Delta}} = \frac{1}{2} \bullet 8 \bullet 9 - \frac{1}{2} \bullet 2 \bullet 7 - \frac{1}{2} \bullet 2 \bullet 6 - 2 \bullet 2 = 36 - 7 - 6 - 4 = 19,$$

kas ir naturāls skaitlis.

![Attēls, kurā ir rinda, diagramma, skice Mākslīgā intelekta ģenerēts
saturs var būt nepareizs.](media/image1.png){width="2.131859142607174in"
height="2.0078740157480315in"}

**\**

**II veids.** Izmantosim Hērona formulu
$S_{\mathrm{\Delta}} = \sqrt{p(p - a)(p - b)(p - c)}$.

Aprēķina trijstūra laukuma kvadrātu, tas ir, $S_{\mathrm{\Delta}}^{2}$:

$$\frac{\sqrt{40} + \sqrt{53} + \sqrt{145}}{2} \bullet \left( \frac{\sqrt{40} + \sqrt{53} + \sqrt{145}}{2} - \sqrt{40} \right) \cdot$$

$$\cdot \left( \frac{\sqrt{40} + \sqrt{53} + \sqrt{145}}{2} - \sqrt{53} \right)\left( \frac{\sqrt{40} + \sqrt{53} + \sqrt{145}}{2} - \sqrt{145} \right) =$$

$$= \frac{1}{16}\left( \sqrt{40} + \sqrt{53} + \sqrt{145} \right)\left( - \sqrt{40} + \sqrt{53} + \sqrt{145} \right)\left( \sqrt{40} - \sqrt{53} + \sqrt{145} \right)\left( \sqrt{40} + \sqrt{53} - \sqrt{145} \right) =$$

$$= \frac{1}{16}\left( - \left( \sqrt{40} \right)^{2} + \left( \sqrt{53} + \sqrt{145} \right)^{2} \right)\left( \left( \sqrt{40} \right)^{2} - \left( \sqrt{53} - \sqrt{145} \right)^{2} \right) =$$

$$= \frac{1}{16}\left( - 40 + 53 + 145 + 2\sqrt{53 \bullet 145}\  \right)\left( 40 - 53 - 145 + 2\sqrt{53 \bullet 145} \right) =$$

$$= \frac{1}{16}\left( 2\sqrt{53 \bullet 145} + 158 \right)\left( 2\sqrt{53 \bullet 145} - 158 \right) = \frac{1}{16}\left( 4 \bullet 53 \bullet 145 - 158^{2} \right) =$$

$$= \frac{1}{16} \bullet 4\left( 53 \bullet 145 - 79^{2} \right) = \frac{1}{4}(7685 - 6241) = \frac{1}{4} \bullet 1444 = \left( \frac{1}{2} \bullet 38 \right)^{2} = 19^{2}$$

Tātad dotā trijstūra laukums 19, kas ir naturāls skaitlis.

**III veids.** Apskata trijstūri $ABC$ ar malu garumiem
$AB = \sqrt{40}$, $BC = \sqrt{53}$ un $AC = \sqrt{145}$. Novelk augstumu
$BD$ un apzīmē $AD = x$ un $CD = \sqrt{145} - x$. Izmantojot Pitagora
teorēmu, iegūst:

- $BD^{2} = AB^{2} - AD^{2} = 40 - x^{2}$ (no $\mathrm{\Delta}ADB$);

- $BD^{2} = BC^{2} - CD^{2} = 53 - \left( \sqrt{145} - x \right)^{2} = 2x\sqrt{145} - x^{2} - 92$
  (no $\mathrm{\Delta}BDC$).

![Attēls, kurā ir skečs, diagramma, rinda, zīmējums Mākslīgā intelekta
ģenerēts saturs var būt
nepareizs.](media/image2.png){width="2.7559055118110236in"
height="1.3779527559055118in"}

Līdz ar to iegūst $40 - x^{2} = 2x\sqrt{145} - x^{2} - 92$ jeb
$x = \frac{66}{\sqrt{145}}$.

Aprēķina
$BD = \sqrt{40 - \left( \frac{66}{\sqrt{145}} \right)^{2}} = \sqrt{\frac{40 \bullet 145 - 66^{2}}{145}} = \sqrt{\frac{4(1450 - 33^{2})}{145}} = \sqrt{\frac{4 \bullet 361}{145}} = \frac{38}{\sqrt{145}}$.

Tātad
$S_{ABC} = \frac{1}{2}AC \bullet BD = \frac{1}{2}\sqrt{145} \bullet \frac{38}{\sqrt{145}} = 19$,
kas ir naturāls skaitlis.
