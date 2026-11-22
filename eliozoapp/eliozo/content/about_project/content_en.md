# About the Project

Latvia has held national olympiads since 1951 (including the school/preparatory and
district/municipal rounds) and Open olympiads since 1974 (LU NMS, n.d.-c, n.d.-a).
The problems and solutions are available in the NMS olympiad problem archive
(LU NMS, n.d.-b), ordered by the type of olympiad, the year and the grade. These
problems are often needed in other cross-sections as well — that is what Eliozo
provides.

## Goals of the problem base

* **Alignment with the curriculum:** Latvian basic education and the secondary
  school courses Mathematics I and Mathematics II follow the
  Skola2030 and 2026 programmes (VISC, n.d.). When offering
  problems to today's students, one cannot rely on older education standards or on
  the grades given in the archive. Linking a problem to a standard and a programme
  must be verifiable, but the existing olympiad archives say nothing about the
  school knowledge a problem needs.
* **Preprocessing of metadata:** Efficient search and ranking of problems need a
  classification. Problems are best sorted into large groups before it is known what
  users will look for: consistent indexing is hard to achieve by labelling a few
  problems on demand.
* **Step-by-step help:** The experience of teaching olympiad problems can be
  collected as *hint ladders* that lead to *key ideas*. AI tools would easily generate
  hints, but they must be reviewed and tested: hints given at the wrong moment and
  poorly structured help improve nothing. Teaching also yields *pedagogical
  observations* about frequent misunderstandings and common mistakes.
* **Empirical difficulty:** The results table of each olympiad gives the factual
  grounding for judging the difficulty of a problem. Empirical difficulty, when it can
  be obtained, is far more accurate than any "speculative" difficulty score (based,
  for example, on the length of the solution, the number of key ideas used or the
  amount of prerequisite knowledge). Olympiads also produce *grading criteria*, which
  show which partial scores were common.
* **Related problems:** Variants of a problem, the same key idea in a different
  setting and similar fragments in solutions reveal chains of related problems,
  which gradually become clear while working with the problem corpus.
* **Clean text in several languages:** Reviewing archive problems after the
  olympiads allows fixing shortcomings in the problem and solution texts and
  translating them.

## Who the site is for

The primary audience of Eliozo is students, teachers and others who prepare them for
olympiads, as well as the authors of new olympiad problem sets. We also try to make
the data visible to AI tools, so that the information collected here can be used in
new ways that the web interface does not foresee.

* **Cheap metadata** that AI agents can assign and verify (classification by topic,
  concepts, question type) we try to create for as many problems on the site as
  possible — several thousand of them.
* **Expensive metadata** that requires testing a problem with students or using it
  in an olympiad (*ground truth*) we create for a smaller number of pedagogically
  interesting problems — we hope to do it for a few hundred problems, covering the
  topics usually taught to olympiad participants.

How this metadata is organized is explained in the
[Introduction to the Ontology](/ontology).

## Problem sources and other collections

The primary sources of the Eliozo problems are the olympiad archives of Latvia
(LU NMS, n.d.-b), of its neighbouring countries (Tartu Ülikool, n.d.-b; Vilniaus
universitetas, n.d.; Olimpiada Matematyczna Juniorów, n.d.; Stowarzyszenie na rzecz
Edukacji Matematycznej, n.d.; Всеукраїнська олімпіада, n.d.; Математичні олімпіади,
n.d.) and the archives of international olympiads (International Mathematical
Olympiad, n.d.; European Girls' Mathematical Olympiad, n.d.; Tartu Ülikool, n.d.-a).

Larger olympiad problem collections include a forum with user-tagged problems (Art of
Problem Solving, n.d.-a, n.d.-b, n.d.-c), a Russian-language problem base with topics,
grades and difficulty estimates (МЦНМО, n.d.) and datasets for training and testing AI
models (MIT CSAIL, n.d.; Gao et al., 2024; Sun et al., 2025).

## Contact

The site was created by Elizabete Ozoliņa and Kalvis Apsītis. Your feedback and
suggestions are welcome at `liliyang146@gmail.com`.

## Sources and links

Art of Problem Solving. (n.d.-a). *Contests* [Forum]. A forum for publishing and
solving problems, with about 80 thousand olympiad problems that can be tagged with
hashtags.
[https://artofproblemsolving.com/community/c13_contests](https://artofproblemsolving.com/community/c13_contests)

Art of Problem Solving. (n.d.-b). *International contests* [Forum]. IMO, Baltic Way
and EGMO problems and solutions.
[https://artofproblemsolving.com/community/c14_international_contests](https://artofproblemsolving.com/community/c14_international_contests)

Art of Problem Solving. (n.d.-c). *National and regional contests* [Forum]. National
mathematical contests.
[https://artofproblemsolving.com/community/c16_national_and_regional_contests](https://artofproblemsolving.com/community/c16_national_and_regional_contests)

European Girls' Mathematical Olympiad. (n.d.). *EGMO* [Website]. The official website
of the European Girls' Mathematical Olympiad.
[https://www.egmo.org/](https://www.egmo.org/)

Gao, B., et al. (2024). *Omni-MATH: A universal Olympiad level mathematic benchmark
for large language models* [Dataset]. About 5 thousand problems for training models.
[https://omni-math.github.io/](https://omni-math.github.io/)

International Mathematical Olympiad. (n.d.). *Problems* [Archive]. The problems and
the jury materials (shortlists) of the IMO.
[https://www.imo-official.org/problems.aspx](https://www.imo-official.org/problems.aspx)

LU NMS. (n.d.-a). *Atklātā olimpiāde* [Open olympiad; Website]. Correspondence
Mathematics School of the University of Latvia.
[https://www.nms.lu.lv/olimpiades/atklata-olimpiade/](https://www.nms.lu.lv/olimpiades/atklata-olimpiade/)

LU NMS. (n.d.-b). *Olimpiāžu uzdevumu arhīvs* [Olympiad problem archive]. Problems and
solutions of the preparatory, regional, national and open olympiads.
[https://www.nms.lu.lv/arhivs-un-materali/uzdevumu-arhivs/olimpiazu-uzdevumu-arhivs/](https://www.nms.lu.lv/arhivs-un-materali/uzdevumu-arhivs/olimpiazu-uzdevumu-arhivs/)

LU NMS. (n.d.-c). *Valsts olimpiāde* [National olympiad; Website]. Correspondence
Mathematics School of the University of Latvia.
[https://www.nms.lu.lv/olimpiades/valsts-olimpiade/](https://www.nms.lu.lv/olimpiades/valsts-olimpiade/)

MIT CSAIL. (n.d.). *MathNet* [Dataset]. About 30 thousand problems from international
competitions of various levels, sorted by subfield and topic; the project aims to
advance the ability of AI tools to solve olympiad problems.
[https://mathnet.mit.edu/](https://mathnet.mit.edu/)

Olimpiada Matematyczna Juniorów. (n.d.). *OMJ* [Archive]. Problems and official
solutions of stages 1–3 of the Polish Junior Mathematical Olympiad.
[https://omj.edu.pl/](https://omj.edu.pl/)

Stowarzyszenie na rzecz Edukacji Matematycznej. (n.d.). *Olimpiada Matematyczna:
zadania* [Archive]. Problems and official solutions of stages 1–3 of the Polish
Mathematical Olympiad.
[https://om.sem.edu.pl/problems/](https://om.sem.edu.pl/problems/)

Sun, H., et al. (2025). *Challenging the boundaries of reasoning: An Olympiad-level
math benchmark for large language models* (OlymMATH) [Dataset]. Problems in Chinese
and English, well annotated and solved in Lean4; suitable for testing AI tools.
[https://arxiv.org/html/2503.21380v3](https://arxiv.org/html/2503.21380v3)

Tartu Ülikool. (n.d.-a). *Baltic Way* [Archive]. Problems and results of the team
olympiad "Baltic Way".
[https://www.math.olympiaadid.ut.ee/eng/html/?id=bw](https://www.math.olympiaadid.ut.ee/eng/html/?id=bw)

Tartu Ülikool. (n.d.-b). *Eesti matemaatikaolümpiaadid* [Archive]. Problems in
Estonian and Russian: regional round (piirkonnavoorud), national round (lõppvoorud),
open contests in autumn and winter (lahtised võistlused), team selection tests
(valikvõistlused).
[https://www.math.olympiaadid.ut.ee/html/index.php](https://www.math.olympiaadid.ut.ee/html/index.php)

Valsts izglītības satura centrs [VISC]. (n.d.). *Mācību programmu paraugi* [Model
curricula; Website]. The Skola2030 and 2026 programmes.
[https://mape.gov.lv/page/programms](https://mape.gov.lv/page/programms)

Vilniaus universitetas. (n.d.). *Matematikos olimpiados* [Archive]. The Lithuanian
olympiad archive; problems in Lithuanian.
[https://mif.vu.lt/matematikos-olimpiados/](https://mif.vu.lt/matematikos-olimpiados/)

Всеукраїнська олімпіада. (n.d.). *УМО* [Archive]. The All-Ukrainian Mathematical
Olympiad (stage 4).
[https://data.uoi.ua/contest/umo](https://data.uoi.ua/contest/umo)

Математичні олімпіади. (n.d.). *Всеукраїнський цикл* [Website]. News of the All-
Ukrainian olympiad cycle.
[https://matholymp.com.ua/vseukrayinskii-cikl](https://matholymp.com.ua/vseukrayinskii-cikl)

МЦНМО. (n.d.). *Задачи* [Problem base]. Olympiad mathematics from sources of the
former USSR; every problem shows its theory topics, grades and a difficulty estimate.
[https://problems.ru/](https://problems.ru/)
