Assume that we need to summarize mathematical skills in Latvian. 
The following CSV file snippet shows skills (with their respective subskills) and 1 sentence description. 
We want to make a shorter summary for each line. 

For example, this CSV file:
```
1,0,0,0,0,alg,Izmantot algebriskos apzīmējumus un metodes skaitļu teorijas uzdevumos,,
1,1,0,0,0,alg.expr,"Ieviest mainīgo apzīmējumus, sastādīt ar tiem izteiksmes",,
1,1,1,0,0,alg.expr.prop,"Izteikt kvalitatīvas skaitļu īpašības (dalāmi ar kko, pēc kārtas sekojoši, nepāru, pilni kvadrāti u.c.) ar mainīgo izteiksmēm",,
1,1,2,0,0,alg.expr.selectvar,"Izvēlēties vien nedaudzus nezināmos lielumus, ar ko izteikt citus",,
1,2,0,0,0,alg.tra,Veikt algebriskus pārveidojumus,,
1,2,1,0,0,alg.tra.binom,"Pārveidot reizinājumus un pakāpes, kuros ietilpst binomi",,
1,2,1,1,0,alg.tra.binom.square,Atvērt iekavas izteiksmēs $(a+b)^2$ un $(a-b)^2$ un dalīt reizinātājos,,
1,2,1,2,0,alg.tra.binom.complsquare,Atdalīt pilnos kvadrātus,,
1,2,1,3,0,alg.tra.binom.newton,Atvērt iekavas izteiksmēs $(a+b)^n$ un $(a-b)^n$ (Ņūtona binomi),,
1,2,2,0,0,alg.tra.factor,Dalīt reizinātājos algebriskas izteiksmes,,
```
converts to these skill names:
```
Algebra
Algebriskas izteiksmes
Skaitļu īpašību izteikšana kvantitatīvi
Mainīgo ieviešana
Algebriski pārveidojumi
Binomu izteiksmes
Summas kvadrāta formula
Pilnu kvadrātu atdalīšana
Ņūtona binoma formula
Dalīšana reizinātājos
```

Please provide short (1-4 words) skill names in Latvian for the following 48 CSV lines: 
```
7,2,1,0,0,misc.extr.pigeon,Izmantot Dirihlē principu,,
7,2,1,1,0,misc.extr.pigeon.plain,Izmantot Dirihlē principa tradicionālo formu (n un n+1),,
7,2,1,2,0,misc.extr.pigeon.floor,Izmantot Dirihlē principa vispārinājumu (n un m),,
7,2,1,3,0,misc.extr.pigeon.collection,Izmantot Dirihlē principa vispārinājumu skaitļu komplektam,,
7,2,2,0,0,misc.extr.param,"Sākt risināt vienādojumu, ievietojot ekstrēmu parametra vai potenciālās saknes vērtību",,
7,3,0,0,0,misc.invar,Izmantot invariantus,,
7,3,1,0,0,misc.invar.parity,Lietot paritāti kā invariantu,,
7,3,2,0,0,misc.invar.congr,Lietot atlikumu/kongruenci kā invariantu,,
7,3,3,0,0,misc.invar.expr,Veidot un lietot citu izteiksmi kā invariantu,,
7,3,4,0,0,misc.invar.game,"Izveidot invariantu, kurš izpildās pēc katra uzvarētāja gājiena kombinatoriskā spēlē",,
7,4,0,0,0,misc.ind,Pamatot ar matemātisko indukciju,,
7,4,1,0,0,misc.ind.least,Izmantot naturālo skaitļu sakārtojuma principu: katrā naturālu skaitļu kopā atradīsies vismazākais elements,,
7,4,2,0,0,misc.ind.descent,"Lietot neierobežotā samazinājuma metodi (piemēram, pamatojot veselu skaitļu sakņu iracionalitāti, ja tās nav veseli skaitļi)",,
7,5,0,0,0,misc.symm,Izmantot uzdevumā esošo simetriju,,
7,5,1,0,0,misc.symm.rename,"Izmantot mainīgo pārsaukšanu simetriskā izteiksmē, lai izdarītu papildu pieņēmumus (teiksim, $a$ &lt; $b$)",,
7,5,2,0,0,misc.symm.periodicity,"Izmantot virkņu periodiskumu, lai aplūkotu tikai vienu periodu. ",,
8,0,0,0,0,plan,Izmantot planimetrijas rezultātus un metodes.,,
8,1,0,0,0,plan.constr,Veikt planimetrijas konstrukcijas uzdevumu risināšanā.,,
8,1,1,0,0,plan.constr.triangulate,Veikt daudzstūru triangulāciju,,
8,1,2,0,0,plan.constr.small,"Izdarīt spriedumus, kuros ir ""ļoti mazi"" ģeometriski pārvietojumi",,
8,2,0,0,0,plan.measurements,"Lietot vienkāršus spriedumus par attālumu, leņķu, laukumu mērīšanu",,
8,2,1,0,0,plan.measurements.angles,Izmantot vienkāršas leņķu sakarības,,
8,2,1,1,0,plan.measurements.angles.central,Izmantot centra leņķu un sektoru metriskās sakarības,,
8,2,1,2,0,plan.measurements.angles.linearpair,Izmantot blakusleņķu īpašību,,
8,2,1,3,0,plan.measurements.angles.vertical,Izmantot krustleņķu īpašību,,
8,2,1,4,0,plan.measurements.angles.interior,"Izmantot iekšējo šķērsleņķu un vienpusleņķu īpašības paralēlām taisnēm, ko krusto trešā taisne",,
8,2,1,5,0,plan.measurements.angles.exterior,"Izmantot ārējo leņķu īpašības paralēlām taisnēm, ko krusto trešā taisne",,
8,2,1,6,0,plan.measurements.angles.corresponding,"Izmantot kāpšļu leņķu īpašības paralēlām taisnēm, ko krusto trešā taisne",,
8,3,0,0,0,plan.circle,Izmantot riņķa līnijas ģeometriskās īpašības,,
8,3,1,0,0,plan.circle.angles,Izmantot leņķu īpašības saistībā ar riņķi,,
8,3,2,0,0,plan.circle.inscribed,Izmantot riņķī ievilkta leņķa īpašības,,
8,4,0,0,0,plan.triangle,Izmantot trijstūru ģeometriskās īpašības,,
8,4,1,0,0,plan.triangle.angles,Izmantot trijstūra iekšējo un ārējo leņķu sakarības,,
8,4,1,1,0,plan.triangle.angles.internal,Lietot trijstūra iekšējo leņķu summas formulu,,
8,4,2,0,0,plan.triangle.area,Izmantot trijstūru laukuma formulas,,
8,4,2,1,0,plan.triangle.area.ah2,Izmantot formulu $ah/2$,,
8,4,3,0,0,plan.triangle.congruence,Izmantot trijstūru vienādības pazīmes,,
8,4,4,0,0,plan.triangle.special,Izmantot noteiktu trijstūru apakškopu īpašības,,
8,4,4,1,0,plan.triangle.special.equilateral,Izmantot vienādmalu trijstūru īpašības,,
8,4,4,2,0,plan.triangle.special.isosceles,Izmantot vienādsānu trijstūru īpašības,,
8,5,0,0,0,plan.quandrangle,Izmantot četrstūru ģeometriskās īpašības,,
8,5,1,0,0,plan.quadrangle.rect,Izmantot kvadrātu un taisnstūru ģeometriskās īpašības,,
8,5,2,0,0,plan.quadrangle.para,Izmantot rombu un paralelogramu ģeometriskās īpašības,,
8,5,3,0,0,plan.quadrangle.trapezoid,Izmantot trapeču ģeometriskās īpašības,,
8,5,3,1,0,plan.quadrangle.trapezoid.area,Izmantot trapeču laukuma formulas,,
8,6,0,0,0,plan.polygon,Izmantot daudzstūru īpašības,,
8,6,1,0,0,plan.polygon.angles,Izmantot daudzstūru leņķu īpašības,,
8,6,1,0,0,plan.polygon.angles.internal,Izmantot daudzstūru leņķu summas sakarību 180*(n-2).,,
```

Please return 48 short names in a single column (one name per line).